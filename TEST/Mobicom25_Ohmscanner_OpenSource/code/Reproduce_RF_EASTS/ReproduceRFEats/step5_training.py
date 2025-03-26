import os
import argparse

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import confusion_matrix

from models import Classifier
from utils.logger import create_logger
from utils.dataloader import create_dataloader
from utils.utils import seed_everything, AverageMeter


def train(args, logger):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    # 不使用 args.use_generator，改为手动遍历两种情况
    for use_generator in [False, True]:
        version = "With Generator" if use_generator else "Without Generator"
        model_path = 'logs_vae/classifier.pt' if use_generator else 'logs/classifier.pt'

        logger.info(f"\n=== Evaluating model {version} ===")

        # 构造带 use_generator 的 args，供 dataloader 使用
        class ArgsWrapper:
            def __init__(self, base_args, use_gen):
                self.__dict__.update(vars(base_args))
                self.use_generator = use_gen

        current_args = ArgsWrapper(args, use_generator)
        data_dict = create_dataloader(current_args, mode='cls')
        test_loader = data_dict['test_loader']
        logger.info(f"Test dataset size: {len(data_dict['test_dataset'])}")

        # 加载模型
        model = Classifier(input_dim=52, hidden_dim=64, num_classes=args.num_classes)
        model.load_state_dict(torch.load(model_path))
        model = model.to(device)

        # 测试
        results = test(model, test_loader, device)
        acc = results['accuracy']
        cm = results['confusion_matrix']

        logger.info(f"Final Accuracy: {acc:.4f}")
        logger.info(f"Confusion Matrix:\n{cm}")

        # 每类准确率
        per_class_acc = []
        for i in range(len(cm)):
            tp = cm[i, i]
            total = cm[i, :].sum()
            acc_i = tp / total if total > 0 else 0.0
            per_class_acc.append(round(float(acc_i), 4))

        logger.info(f"Per-class accuracy (Material 1 to {len(cm)}): {per_class_acc}")



def test(model, test_loader, device):
    model.eval()
    acc = AverageMeter('Accuracy')
    all_preds = []
    all_labels = []
    with torch.no_grad():
        for batch_idx, (input_, label) in enumerate(test_loader):
            input_ = input_.to(device)
            label = label.to(device)

            outputs = model(input_)
            _, pred = torch.max(outputs, 1)

            correct = (pred == label).sum().item()
            total = label.size(0)
            acc.update(correct / total, total)

            all_preds.extend(pred.cpu().numpy())
            all_labels.extend(label.cpu().numpy())

    return {
        'accuracy': acc.avg,
        'confusion_matrix': confusion_matrix(np.array(all_labels), np.array(all_preds)),
    }


def parse_args():
    parser = argparse.ArgumentParser(description='Train a VAE')
    # parser.add_argument('--config', type=str, default='configs/vae.yaml', help='Path to the config file.')
    parser.add_argument('--seed', type=int, default=0, help='Random seed.')
    parser.add_argument('--gpus', type=str, default='0', help='GPU to use.')
    parser.add_argument('--data_dir', type=str, default='data/', help='Path to the data directory.')
    parser.add_argument('--epochs', type=int, default=50, help='Number of epochs to train.')
    parser.add_argument('--batch_size', type=int, default=16, help='Batch size.')
    parser.add_argument('--num_workers', type=int, default=4, help='Number of workers for dataloader.')
    parser.add_argument('--num_classes', type=int, default=10, help='Number of data classes.')
    parser.add_argument('--use-generator', action='store_true', help='Use generated data.')
    return parser.parse_args()


def main():
    args = parse_args()
    logger = create_logger(f"logs/train_classifier{'_generate' if args.use_generator else ''}.log")
    logger.info(args)
    os.environ['CUDA_VISIBLE_DEVICES'] = args.gpus
    seed_everything(args.seed)
    train(args, logger)


if __name__ == '__main__':
    main()