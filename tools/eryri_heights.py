import sys, math, os, subprocess
import numpy as np
from PIL import Image
out=sys.argv[1]; Z=13
def xy(lat,lon):
    n=2**Z; x=(lon+180)/360*n; y=(1-math.asinh(math.tan(math.radians(lat)))/math.pi)/2*n; return x,y
x0,y0=xy(53.135,-4.155); x1,y1=xy(53.005,-3.955)
tx0,ty0,tx1,ty1=int(x0),int(y0),int(x1),int(y1)
big=np.zeros(((ty1-ty0+1)*256,(tx1-tx0+1)*256),np.float32)
for ty in range(ty0,ty1+1):
    for tx in range(tx0,tx1+1):
        f=f'{out}/{Z}_{tx}_{ty}.png'
        if not os.path.exists(f): subprocess.run(['curl','-s','-o',f,f'https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{Z}/{tx}/{ty}.png'],check=True)
        a=np.asarray(Image.open(f).convert('RGB')).astype(np.float32)
        big[(ty-ty0)*256:(ty-ty0+1)*256,(tx-tx0)*256:(tx-tx0+1)*256]=a[:,:,0]*256+a[:,:,1]+a[:,:,2]/256-32768
px0,py0,px1,py1=[int(round(v)) for v in ((x0-tx0)*256,(y0-ty0)*256,(x1-tx0)*256,(y1-ty0)*256)]
h=big[py0:py1,px0:px1]; np.save(out+'/h.npy',h)
mpp=156543.03*math.cos(math.radians(53.07))/2**Z
print(h.shape,h.min(),h.max(),'m/px',mpp,'km',h.shape[1]*mpp/1000,h.shape[0]*mpp/1000)
i=np.unravel_index(h.argmax(),h.shape); print('summit px',i)
for nm,(la,lo) in {'summit':(53.0685,-4.0763),'llydawE':(53.0705,-4.0330),'penypass':(53.0805,-4.0210)}.items():
    x,y=xy(la,lo); X=int((x-tx0)*256-px0); Y=int((y-ty0)*256-py0); print(nm,X,Y,h[Y,X])
g=(np.clip(h/1100,0,1)*255).astype(np.uint8); Image.fromarray(g).save(out+'/h.png')
