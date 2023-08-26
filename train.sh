CONFIG='/mnt/disk1/mbbank/OCR/CODE/VietOcr/config/config_V2.yml'
EXPERIMENT='V2'
SAVE_PERIOD=10000
CUDA_VISIBLE_DEVICES=0,1,2,3 python3 train.py \
--config $CONFIG \
--experiment $EXPERIMENT \
--pretrain \
--save_period $SAVE_PERIOD 
