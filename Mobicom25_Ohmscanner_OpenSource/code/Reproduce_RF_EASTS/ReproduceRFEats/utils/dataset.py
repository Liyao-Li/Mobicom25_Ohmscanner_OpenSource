import os
import glob
from functools import partial

import torch
from torch.utils.data import Dataset
    

class RFIDDataset(Dataset):

    class_to_index = {
        'coke': 0,
        'milk': 1,
        'sesameoil': 2,
        'soybeanoil': 3,
        'redbull': 4,
        'salt': 5,
        'sprite': 6,
        'vinegar': 7,
        'water': 8,
        'wine': 9
    }

    def __init__(self, 
                 data_dir: str='data/',
                 is_train: bool=True,
                 mode: str = 'gen',
                 use_generator: bool=True):
        self.data_dir = data_dir
        self.is_train = is_train
        self.mode = mode
        self.use_generator = use_generator
        assert mode in ['gen', 'cls']

        # load default data
        if mode == 'gen':
            file_paths = glob.glob(data_dir + r'p[2-9]*/*.txt')
            file_paths = sorted(file_paths)
            self.data = [data for data in map(partial(self.parse_file, load_label=False), file_paths) if len(data) > 0]
        else:
            all_data = sorted(glob.glob(os.path.join(data_dir, r'[0-9]*')), key=lambda x: int(os.path.basename(x)))
            split_ratio = 0.8
            split_index = round(len(all_data) * split_ratio)
            if is_train:
                split_data = all_data[:split_index]
            else:
                split_data = all_data[split_index:]
            file_paths = [file_ for dir_ in split_data for file_ in glob.glob(os.path.join(dir_, r'*.txt'))]
            file_paths = sorted(file_paths)
            self.data = [(data, label) for data, label in map(self.parse_file, file_paths) if len(data) > 0]
        # print(file_paths)
        
        # load generated data
        if mode == 'cls' and use_generator:
            generated_paths = glob.glob(os.path.join(data_dir, 'generate', r'*.txt'))
            generated_paths = sorted(generated_paths)
            self.env_data = [data for data in map(partial(self.parse_file, load_label=False), generated_paths) if len(data) > 0]
            self.add_generate_data()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        if self.mode == 'gen':
            sample = self.data[idx]
        else:
            sample, label = self.data[idx]
        amplitude = torch.Tensor([float(item[1]) for item in sample])
        phase = torch.Tensor([float(item[2]) for item in sample])
        if self.mode == 'gen':
            return torch.cat([amplitude, phase], dim=0)
        else:
            return torch.cat([amplitude, phase], dim=0), label
    
    def parse_file(self, file_path: str, load_label: bool = True):
        with open(file_path, 'r') as f:
            lines = f.readlines()
        data = []
        for line in lines:
            data.append([float(item) for item in line.strip().split(',')])
        
        if load_label:
            label = os.path.basename(file_path).split('_')[0]
            label = self.class_to_index[label]
            return data, label
        else:
            return data
    
    def add_generate_data(self):
        generated_data_all = []
        for data, label in self.data:
            for data_gen in self.env_data:
                generated_data_for_one = []
                for line, line_gen in zip(data, data_gen):
                    freq, amplitude, phase = line
                    freq_gen, amplitude_gen, phase_gen = line_gen
                    generated_data_for_one.append([freq, amplitude * amplitude_gen, phase * phase_gen])
                generated_data_all.append((generated_data_for_one, label))
        self.data += generated_data_all

if __name__ == '__main__':
    RFIDDataset(is_train=True, mode='gen')
    RFIDDataset(is_train=False, mode='gen')
    RFIDDataset(is_train=True, mode='cls')
    RFIDDataset(is_train=False, mode='cls')