import os
import argparse
import numpy as np
import torch
from sklearn.metrics import confusion_matrix

from models import Classifier
from utils.logger import create_logger
from utils.dataloader import create_dataloader
from utils.utils import seed_everything, AverageMeter


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
        'confusion_matrix': confusion_matrix(np.array(all_labels), np.array(all_preds))
    }

def main():
    parser = argparse.ArgumentParser(description='Classify with a pre-trained model')
    parser.add_argument('--seed', type=int, default=0, help='Random seed.')
    parser.add_argument('--gpus', type=str, default='0', help='GPU to use.')
    parser.add_argument('--data_dir', type=str, default='data/', help='Path to the data directory.')
    parser.add_argument('--batch_size', type=int, default=16, help='Batch size.')
    parser.add_argument('--num_workers', type=int, default=4, help='Number of workers for dataloader.')
    parser.add_argument('--num_classes', type=int, default=10, help='Number of data classes.')
    args = parser.parse_args()

    logger = create_logger("logs/classify_compare.log")
    logger.info(args)

    os.environ['CUDA_VISIBLE_DEVICES'] = args.gpus
    seed_everything(args.seed)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'


    class ArgsWrapper:
        def __init__(self, args, use_generator):
            self.__dict__.update(vars(args))
            self.use_generator = use_generator

    for use_generator in [False, True]:
        tag = "With Generator" if use_generator else "Without Generator"
        model_path = 'logs_vae/classifier.pt' if use_generator else 'logs/classifier.pt'

        logger.info(f"\n=== Evaluating Model {tag} ===")

        current_args = ArgsWrapper(args, use_generator)
        data_dict = create_dataloader(current_args, mode='cls')
        test_loader = data_dict['test_loader']

        model = Classifier(input_dim=52, hidden_dim=64, num_classes=args.num_classes)
        model.load_state_dict(torch.load(model_path))
        model = model.to(device)


        results = test(model, test_loader, device)
        cm = results['confusion_matrix']
        acc = results['accuracy']

        logger.info(f"Overall Accuracy: {acc:.4f}")
        logger.info(f"Confusion Matrix:\n{cm}")


        per_class_acc_list = []
        for i in range(len(cm)):
            true_positives = cm[i, i]
            total_samples = cm[i, :].sum()
            acc_i = true_positives / total_samples if total_samples > 0 else 0.0
            per_class_acc_list.append(round(float(acc_i), 4))

        print("Per-class accuracy (Material 1 to 10):")
        print(per_class_acc_list)
        logger.info(f"Per-class accuracy: {per_class_acc_list}")


if __name__ == '__main__':
    main()
