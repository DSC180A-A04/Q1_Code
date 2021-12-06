import torch


def quantile_loss(y_pred, y_true):
    quantiles = [0.025, 0.5, 0.975]
    losses = []
    for i, q in enumerate(quantiles):
        errors = y_true - torch.unbind(y_pred, 3)[i]
        errors[errors != errors] = 0
        losses.append(torch.max((q - 1) * errors, q * errors).unsqueeze(0))
    loss = torch.mean(torch.sum(torch.cat(losses, dim=0), dim=0))
    return loss
