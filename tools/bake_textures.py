import sys, numpy as np
from PIL import Image, ImageFilter
src,out=sys.argv[1],sys.argv[2]
def nrm(im,strength):
    g=np.asarray(im.convert('L').filter(ImageFilter.GaussianBlur(0.8))).astype(np.float64)/255
    gx=(np.roll(g,-1,1)-np.roll(g,1,1))*strength; gy=(np.roll(g,-1,0)-np.roll(g,1,0))*strength
    l=1/np.sqrt(gx*gx+gy*gy+1); n=np.stack([-gx*l*.5+.5,gy*l*.5+.5,l*.5+.5],-1)
    return Image.fromarray((n*255).astype(np.uint8))
for name,f,size,st in (('stone','castle_wall_slates_diff.jpg',1024,5.0),('rock','aerial_rocks_02_diff.jpg',512,4.0)):
    im=Image.open(f'{src}/{f}').convert('RGB').resize((size,size),Image.LANCZOS)
    im.save(f'{out}/{name}.webp',quality=82); nrm(im,st).save(f'{out}/{name}-n.webp',quality=82)
# fine grain for the mountain slopes: the rock photograph in grey, evened out so that its average is mid-grey
g=np.asarray(Image.open(f'{src}/aerial_rocks_02_diff.jpg').convert('L').resize((512,512),Image.LANCZOS)).astype(np.float64)
g=np.clip(127.5+(g-g.mean())/g.std()*46,0,255).astype(np.uint8); Image.fromarray(np.stack([g,g,g],-1)).save(f'{out}/detail.webp',quality=80)
