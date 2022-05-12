# Only 3 lines have changed, signified by ##CHANGED
# If you want to increase the speed of training the network (recommended if you use CPU)
# set the self.dims to 64 or 32 (the lower, the faster)

class NucleiData(Dataset):
        def __init__(self,path):
            self.path = path
            self.folders = [f for f in os.listdir(path) if 'stage' not in f]
            self.transforms = get_transforms(0.5, 0.5)
            self.dims = 64,64 ##CHANGED
        
        def __len__(self):
            return len(self.folders)
            
        def __getitem__(self,idx):
            image_folder = os.path.join(self.path,self.folders[idx],'images/')
            mask_folder = os.path.join(self.path,self.folders[idx],'masks/')
            image_path = os.path.join(image_folder,os.listdir(image_folder)[0])
            
            img = io.imread(image_path)[:,:,:3].astype('float32')
            img = transform.resize(img,(self.dims)) ##CHANGED
            mask = self.get_mask(mask_folder, *self.dims).astype('float32') ##CHANGED
    
            augmented = self.transforms(image=img, mask=mask) 
            img = augmented['image']
            mask = augmented['mask']
            mask = mask.permute(2, 0, 1)
            return (img,mask) 

        def get_mask(self,mask_folder,IMG_HEIGHT, IMG_WIDTH):
            mask = np.zeros((IMG_HEIGHT, IMG_WIDTH, 1), dtype=bool)
            for mask_ in os.listdir(mask_folder):
                    mask_ = io.imread(os.path.join(mask_folder,mask_))
                    mask_ = transform.resize(mask_, (IMG_HEIGHT, IMG_WIDTH)) ##CHANGED
                    mask_ = np.expand_dims(mask_,axis=-1)
                    mask = np.maximum(mask, mask_)
            return mask
        
data = NucleiData(DATA)

for i in range(10):
    print(data.__getitem__(i)[0].size())