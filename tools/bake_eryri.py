import sys, numpy as np
from PIL import Image
dem,out=sys.argv[1],sys.argv[2]
T=1024; N=900; KM=N*11.4816; cell=KM/T  # a square 10.3 km across, summit left of centre
h=np.load(dem+'/h.npy'); c=h[190:190+N,150:150+N]
base=np.asarray(Image.fromarray(c.astype(np.float32),mode='F').resize((T,T),Image.BICUBIC)).astype(np.float64)
def blur(a,s):
    fy=np.fft.fftfreq(a.shape[0])[:,None]; fx=np.fft.fftfreq(a.shape[1])[None,:]
    pad=64; b=np.pad(a,pad,mode='reflect'); fy=np.fft.fftfreq(b.shape[0])[:,None]; fx=np.fft.fftfreq(b.shape[1])[None,:]
    return np.real(np.fft.ifft2(np.fft.fft2(b)*np.exp(-2*(np.pi*s)**2*(fx**2+fy**2))))[pad:-pad,pad:-pad]
rng=np.random.default_rng(5)
FY=np.fft.fftfreq(T)[:,None]*T; FX=np.fft.fftfreq(T)[None,:]*T; FR=np.hypot(FX,FY); FR[0,0]=1
def spec(lo,hi,beta=1.0):  # tiling noise with features between T/hi and T/lo pixels, 0..1
    w=rng.normal(size=(T,T)); F=np.fft.fft2(w)*np.where((FR>=lo)&(FR<=hi),FR**-beta,0)
    a=np.real(np.fft.ifft2(F)); a=(a-a.mean())/a.std(); return np.clip(a*0.22+0.5,0,1)
def fbm(n0,oct,ridged=False,gain=0.5):
    a=np.zeros((T,T)); amp=1; tot=0
    for o in range(oct):
        v=spec(n0*2**o*0.7,n0*2**o*1.5,0)
        if ridged: v=1-np.abs(2*v-1); v=v*v
        a+=v*amp; tot+=amp; amp*=gain
    return a/tot
base=blur(base,1.6)
water=((np.abs(base-432.2)<1.0)|(np.abs(base-604.3)<1.0))
gy,gx=np.gradient(base,cell); water&=(np.hypot(gx,gy)<0.01)
# bring back the sharpness the survey smoothed away, then add crag detail on steep, high ground
sharp=base+0.9*(base-blur(base,7))+0.5*(base-blur(base,20))
gy,gx=np.gradient(blur(base,3),cell); slope=np.hypot(gx,gy)
st=np.clip((slope-0.25)/0.5,0,1); hi=np.clip((base-450)/350,0,1)
rid=fbm(10,6,True,0.55); soft=fbm(6,5)
det=sharp+(rid-0.3)*(22+150*st*(0.35+0.65*hi))+(soft-0.5)*20
det=np.where(water,base,det)
VE=float(sys.argv[3]) if len(sys.argv)>3 else 1.0
gy,gx=np.gradient(det*VE,cell); l=1/np.sqrt(gx*gx+gy*gy+1); nx,ny,nz=-gx*l,l,-gy*l
N=np.stack([nx*.5+.5,ny*.5+.5,nz*.5+.5],-1); Image.fromarray((N*255).clip(0,255).astype(np.uint8)).save(out+'/eryri-n.webp',quality=90)
sl=1-ny
f=fbm(48,4); f2=fbm(5,4); f3=fbm(160,2)
def lerp(a,b,k): return a+(b-a)*k[...,None]
col=lerp(np.array([0.085,0.125,0.055]),np.array([0.19,0.15,0.075]),np.clip(f2*1.8-0.4,0,1))
col=lerp(col,np.array([0.21,0.205,0.2]),np.clip((base-500+f*200)/280,0,1))
strata=fbm(90,2)
rc=(0.085+0.11*f+0.05*strata)[...,None]*np.array([1.03,1.0,1.02])
rk=np.clip((sl-0.16)/0.14,0,1); col=col*(1-rk[...,None])+rc*rk[...,None]
sn=np.clip((base-590+(f2-0.5)*240+(f-0.5)*90)/110,0,1)*np.clip((0.46-sl)/0.2,0,1)
sn=np.clip(sn+np.clip((base-820)/120,0,1)*np.clip((0.66-sl)/0.2,0,1)*0.8,0,1)
col=lerp(col,np.array([0.82,0.87,0.95]),sn)
ao=np.clip(1-(blur(det,6)-det)/40,0.45,1.15); col*=ao[...,None]*(0.82+0.36*f3[...,None])
col=np.where(water[...,None],np.array([0.01,0.018,0.035]),col)
Image.fromarray((np.clip(col,0,1)**(1/2.2)*255).astype(np.uint8)).save(out+'/eryri-c.webp',quality=86)
rough=np.where(water,0.12,0.96-0.3*sn)
M=384; hm=np.asarray(Image.fromarray(blur(det,1.2).astype(np.float32),mode='F').resize((M,M),Image.BILINEAR))
v=np.clip(hm*56,0,65535).astype(np.uint16); rgb=np.zeros((M,M,3),np.uint8); rgb[:,:,0]=v>>8; rgb[:,:,1]=v&255
rgb[:,:,2]=np.asarray(Image.fromarray((rough*255).astype(np.uint8)).resize((M,M),Image.BILINEAR))
Image.fromarray(rgb).save(out+'/eryri-h.png',optimize=True)
print('max',det.max(),'water px',water.sum())
