import os
import torch
import torch.nn as nn

MODEL_PATH = os.path.join(os.path.dirname(__file__), "lstm_stock_model.pth")


class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super().__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.output_size = output_size
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out


class StockLSTM:
    def __init__(self):
        self.input_size = 1
        self.hidden_size = 64
        self.num_layers = 3
        self.output_size = 1

    def get_model(self):
        model = LSTM(
            input_size=self.input_size,
            hidden_size=self.hidden_size,
            num_layers=self.num_layers,
            output_size=self.output_size)
        model.load_state_dict(torch.load(MODEL_PATH))
        model.eval()
        return model
