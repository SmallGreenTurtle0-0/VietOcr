import argparse

import sys,os
sys.path.append(os.getcwd())
from vietocr.model.trainer import Trainer
from vietocr.tool.config import Cfg

def main():
    parser = argparse.ArgumentParser()
    # true false argument
    parser.add_argument('--use_checkpoint', action='store_true', required=False, help='use checkpoint or not')
    parser.add_argument('--pretrained', action='store_true', required=False, help='use pretrained model or not')
    parser.add_argument('--config', required=True, help='see example at ')
    parser.add_argument('--experiment', required=False, default='exp', help='your experiment name')
    parser.add_argument('--save_period', required=False, default=100, help='save model every x iteration')
    args = parser.parse_args()
    config = Cfg.load_config_from_file(args.config)

    trainer = Trainer(config, pretrained=args.pretrained, experiment=args.experiment,
                      use_checkpoint=args.use_checkpoint, save_period=int(args.save_period))

            
    trainer.train()

if __name__ == '__main__':
    main()
