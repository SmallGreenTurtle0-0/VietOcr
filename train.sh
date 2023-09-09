CONFIG='/mnt/disk1/mbbank/OCR/CODE/VietOcr/config/config_V5.yml'
EXPERIMENT='V5'
SAVE_PERIOD=10000
CUDA_VISIBLE_DEVICES=2 python train.py \
--config $CONFIG \
--experiment $EXPERIMENT \
--save_period $SAVE_PERIOD 
