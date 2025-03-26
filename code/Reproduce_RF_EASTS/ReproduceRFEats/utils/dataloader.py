from torch.utils.data import DataLoader

from utils.dataset import RFIDDataset


def create_dataloader(args, mode: str = 'gen'):

    train_dataset = RFIDDataset(data_dir=args.data_dir, is_train=True, mode=mode, use_generator=args.use_generator if mode == 'cls' else False)
    test_dataset = RFIDDataset(data_dir=args.data_dir, is_train=False, mode=mode)

    train_loader = DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True, pin_memory=True, drop_last=True, num_workers=args.num_workers)
    test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False, pin_memory=True, drop_last=False, num_workers=args.num_workers)

    return {
        'train_dataset': train_dataset,
        'test_dataset': test_dataset,
        'train_loader': train_loader,
        'test_loader': test_loader
    }