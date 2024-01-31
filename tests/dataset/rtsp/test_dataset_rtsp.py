from xeye import Dataset

data = Dataset(source='rtsp://admin:hik12345@192.168.10.6/ISAPI/Streaming/channels/101', img_types=2, label=['a', 'b'], num=10, height=100, width=100, stand_by_time=0)
data.preview()
data.gray()
data.compress_train_test(perc=0.2)
data.compress_all()
data.just_compress(name="batch_test")