var Sf=0,th=1,bf=2;var Du=1,hc=2,Ei=3,Yi=0,Sn=1,mn=2;var Gi=0,$s=1,js=2,eh=3,nh=4,Ef=5,cs=100,wf=101,Tf=102,ih=103,sh=104,Af=200,Rf=201,Cf=202,Pf=203,vl=204,yl=205,If=206,Lf=207,Uf=208,Df=209,Nf=210,Ff=211,Of=212,Bf=213,zf=214,Hf=0,kf=1,Vf=2,Oo=3,Gf=4,Wf=5,Xf=6,Yf=7,Nu=0,qf=1,Zf=2,Wi=0,$f=1,Jf=2,Kf=3,uc=4,jf=5,Qf=6;var Fu=300,Qs=301,tr=302,Ml=303,Sl=304,ga=306,ps=1e3,Rn=1001,bl=1002,An=1003,rh=1004;var za=1005;var kn=1006,td=1007;var Cr=1008;var Xi=1009,ed=1010,nd=1011,fc=1012,Ou=1013,ki=1014,Vi=1015,Pr=1016,Bu=1017,zu=1018,us=1020,id=1021,Qn=1023,sd=1024,rd=1025,fs=1026,er=1027,od=1028,Hu=1029,ad=1030,ku=1031,Vu=1033,Ha=33776,ka=33777,Va=33778,Ga=33779,oh=35840,ah=35841,lh=35842,ch=35843,Gu=36196,hh=37492,uh=37496,fh=37808,dh=37809,ph=37810,mh=37811,gh=37812,_h=37813,xh=37814,vh=37815,yh=37816,Mh=37817,Sh=37818,bh=37819,Eh=37820,wh=37821,Wa=36492,Th=36494,Ah=36495,ld=36283,Rh=36284,Ch=36285,Ph=36286;var Bo=2300,zo=2301,Xa=2302,Ih=2400,Lh=2401,Uh=2402;var Wu=3e3,ds=3001,cd=3200,hd=3201,Xu=0,dc=1,Vn="",Je="srgb",Ai="srgb-linear",pc="display-p3",_a="display-p3-linear",Ho="linear",ke="srgb",ko="rec709",Vo="p3";var Ts=7680;var Dh=519,ud=512,fd=513,dd=514,Yu=515,pd=516,md=517,gd=518,_d=519,Nh=35044;var Fh="300 es",El=1035,Ti=2e3,Go=2001,qi=class{addEventListener(t,e){this._listeners===void 0&&(this._listeners={});let n=this._listeners;n[t]===void 0&&(n[t]=[]),n[t].indexOf(e)===-1&&n[t].push(e)}hasEventListener(t,e){if(this._listeners===void 0)return!1;let n=this._listeners;return n[t]!==void 0&&n[t].indexOf(e)!==-1}removeEventListener(t,e){if(this._listeners===void 0)return;let s=this._listeners[t];if(s!==void 0){let r=s.indexOf(e);r!==-1&&s.splice(r,1)}}dispatchEvent(t){if(this._listeners===void 0)return;let n=this._listeners[t.type];if(n!==void 0){t.target=this;let s=n.slice(0);for(let r=0,a=s.length;r<a;r++)s[r].call(this,t);t.target=null}}},vn=["00","01","02","03","04","05","06","07","08","09","0a","0b","0c","0d","0e","0f","10","11","12","13","14","15","16","17","18","19","1a","1b","1c","1d","1e","1f","20","21","22","23","24","25","26","27","28","29","2a","2b","2c","2d","2e","2f","30","31","32","33","34","35","36","37","38","39","3a","3b","3c","3d","3e","3f","40","41","42","43","44","45","46","47","48","49","4a","4b","4c","4d","4e","4f","50","51","52","53","54","55","56","57","58","59","5a","5b","5c","5d","5e","5f","60","61","62","63","64","65","66","67","68","69","6a","6b","6c","6d","6e","6f","70","71","72","73","74","75","76","77","78","79","7a","7b","7c","7d","7e","7f","80","81","82","83","84","85","86","87","88","89","8a","8b","8c","8d","8e","8f","90","91","92","93","94","95","96","97","98","99","9a","9b","9c","9d","9e","9f","a0","a1","a2","a3","a4","a5","a6","a7","a8","a9","aa","ab","ac","ad","ae","af","b0","b1","b2","b3","b4","b5","b6","b7","b8","b9","ba","bb","bc","bd","be","bf","c0","c1","c2","c3","c4","c5","c6","c7","c8","c9","ca","cb","cc","cd","ce","cf","d0","d1","d2","d3","d4","d5","d6","d7","d8","d9","da","db","dc","dd","de","df","e0","e1","e2","e3","e4","e5","e6","e7","e8","e9","ea","eb","ec","ed","ee","ef","f0","f1","f2","f3","f4","f5","f6","f7","f8","f9","fa","fb","fc","fd","fe","ff"],Oh=1234567,Sr=Math.PI/180,Ir=180/Math.PI;function ys(){let i=Math.random()*4294967295|0,t=Math.random()*4294967295|0,e=Math.random()*4294967295|0,n=Math.random()*4294967295|0;return(vn[i&255]+vn[i>>8&255]+vn[i>>16&255]+vn[i>>24&255]+"-"+vn[t&255]+vn[t>>8&255]+"-"+vn[t>>16&15|64]+vn[t>>24&255]+"-"+vn[e&63|128]+vn[e>>8&255]+"-"+vn[e>>16&255]+vn[e>>24&255]+vn[n&255]+vn[n>>8&255]+vn[n>>16&255]+vn[n>>24&255]).toLowerCase()}function cn(i,t,e){return Math.max(t,Math.min(e,i))}function mc(i,t){return(i%t+t)%t}function xd(i,t,e,n,s){return n+(i-t)*(s-n)/(e-t)}function vd(i,t,e){return i!==t?(e-i)/(t-i):0}function br(i,t,e){return(1-e)*i+e*t}function yd(i,t,e,n){return br(i,t,1-Math.exp(-e*n))}function Md(i,t=1){return t-Math.abs(mc(i,t*2)-t)}function Sd(i,t,e){return i<=t?0:i>=e?1:(i=(i-t)/(e-t),i*i*(3-2*i))}function bd(i,t,e){return i<=t?0:i>=e?1:(i=(i-t)/(e-t),i*i*i*(i*(i*6-15)+10))}function Ed(i,t){return i+Math.floor(Math.random()*(t-i+1))}function wd(i,t){return i+Math.random()*(t-i)}function Td(i){return i*(.5-Math.random())}function Ad(i){i!==void 0&&(Oh=i);let t=Oh+=1831565813;return t=Math.imul(t^t>>>15,t|1),t^=t+Math.imul(t^t>>>7,t|61),((t^t>>>14)>>>0)/4294967296}function Rd(i){return i*Sr}function Cd(i){return i*Ir}function wl(i){return(i&i-1)===0&&i!==0}function Pd(i){return Math.pow(2,Math.ceil(Math.log(i)/Math.LN2))}function Wo(i){return Math.pow(2,Math.floor(Math.log(i)/Math.LN2))}function Id(i,t,e,n,s){let r=Math.cos,a=Math.sin,o=r(e/2),l=a(e/2),c=r((t+n)/2),h=a((t+n)/2),u=r((t-n)/2),d=a((t-n)/2),p=r((n-t)/2),x=a((n-t)/2);switch(s){case"XYX":i.set(o*h,l*u,l*d,o*c);break;case"YZY":i.set(l*d,o*h,l*u,o*c);break;case"ZXZ":i.set(l*u,l*d,o*h,o*c);break;case"XZX":i.set(o*h,l*x,l*p,o*c);break;case"YXY":i.set(l*p,o*h,l*x,o*c);break;case"ZYZ":i.set(l*x,l*p,o*h,o*c);break;default:console.warn("THREE.MathUtils: .setQuaternionFromProperEuler() encountered an unknown order: "+s)}}function Gs(i,t){switch(t.constructor){case Float32Array:return i;case Uint32Array:return i/4294967295;case Uint16Array:return i/65535;case Uint8Array:return i/255;case Int32Array:return Math.max(i/2147483647,-1);case Int16Array:return Math.max(i/32767,-1);case Int8Array:return Math.max(i/127,-1);default:throw new Error("Invalid component type.")}}function wn(i,t){switch(t.constructor){case Float32Array:return i;case Uint32Array:return Math.round(i*4294967295);case Uint16Array:return Math.round(i*65535);case Uint8Array:return Math.round(i*255);case Int32Array:return Math.round(i*2147483647);case Int16Array:return Math.round(i*32767);case Int8Array:return Math.round(i*127);default:throw new Error("Invalid component type.")}}var Ui={DEG2RAD:Sr,RAD2DEG:Ir,generateUUID:ys,clamp:cn,euclideanModulo:mc,mapLinear:xd,inverseLerp:vd,lerp:br,damp:yd,pingpong:Md,smoothstep:Sd,smootherstep:bd,randInt:Ed,randFloat:wd,randFloatSpread:Td,seededRandom:Ad,degToRad:Rd,radToDeg:Cd,isPowerOfTwo:wl,ceilPowerOfTwo:Pd,floorPowerOfTwo:Wo,setQuaternionFromProperEuler:Id,normalize:wn,denormalize:Gs},xt=class i{constructor(t=0,e=0){i.prototype.isVector2=!0,this.x=t,this.y=e}get width(){return this.x}set width(t){this.x=t}get height(){return this.y}set height(t){this.y=t}set(t,e){return this.x=t,this.y=e,this}setScalar(t){return this.x=t,this.y=t,this}setX(t){return this.x=t,this}setY(t){return this.y=t,this}setComponent(t,e){switch(t){case 0:this.x=e;break;case 1:this.y=e;break;default:throw new Error("index is out of range: "+t)}return this}getComponent(t){switch(t){case 0:return this.x;case 1:return this.y;default:throw new Error("index is out of range: "+t)}}clone(){return new this.constructor(this.x,this.y)}copy(t){return this.x=t.x,this.y=t.y,this}add(t){return this.x+=t.x,this.y+=t.y,this}addScalar(t){return this.x+=t,this.y+=t,this}addVectors(t,e){return this.x=t.x+e.x,this.y=t.y+e.y,this}addScaledVector(t,e){return this.x+=t.x*e,this.y+=t.y*e,this}sub(t){return this.x-=t.x,this.y-=t.y,this}subScalar(t){return this.x-=t,this.y-=t,this}subVectors(t,e){return this.x=t.x-e.x,this.y=t.y-e.y,this}multiply(t){return this.x*=t.x,this.y*=t.y,this}multiplyScalar(t){return this.x*=t,this.y*=t,this}divide(t){return this.x/=t.x,this.y/=t.y,this}divideScalar(t){return this.multiplyScalar(1/t)}applyMatrix3(t){let e=this.x,n=this.y,s=t.elements;return this.x=s[0]*e+s[3]*n+s[6],this.y=s[1]*e+s[4]*n+s[7],this}min(t){return this.x=Math.min(this.x,t.x),this.y=Math.min(this.y,t.y),this}max(t){return this.x=Math.max(this.x,t.x),this.y=Math.max(this.y,t.y),this}clamp(t,e){return this.x=Math.max(t.x,Math.min(e.x,this.x)),this.y=Math.max(t.y,Math.min(e.y,this.y)),this}clampScalar(t,e){return this.x=Math.max(t,Math.min(e,this.x)),this.y=Math.max(t,Math.min(e,this.y)),this}clampLength(t,e){let n=this.length();return this.divideScalar(n||1).multiplyScalar(Math.max(t,Math.min(e,n)))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this}negate(){return this.x=-this.x,this.y=-this.y,this}dot(t){return this.x*t.x+this.y*t.y}cross(t){return this.x*t.y-this.y*t.x}lengthSq(){return this.x*this.x+this.y*this.y}length(){return Math.sqrt(this.x*this.x+this.y*this.y)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)}normalize(){return this.divideScalar(this.length()||1)}angle(){return Math.atan2(-this.y,-this.x)+Math.PI}angleTo(t){let e=Math.sqrt(this.lengthSq()*t.lengthSq());if(e===0)return Math.PI/2;let n=this.dot(t)/e;return Math.acos(cn(n,-1,1))}distanceTo(t){return Math.sqrt(this.distanceToSquared(t))}distanceToSquared(t){let e=this.x-t.x,n=this.y-t.y;return e*e+n*n}manhattanDistanceTo(t){return Math.abs(this.x-t.x)+Math.abs(this.y-t.y)}setLength(t){return this.normalize().multiplyScalar(t)}lerp(t,e){return this.x+=(t.x-this.x)*e,this.y+=(t.y-this.y)*e,this}lerpVectors(t,e,n){return this.x=t.x+(e.x-t.x)*n,this.y=t.y+(e.y-t.y)*n,this}equals(t){return t.x===this.x&&t.y===this.y}fromArray(t,e=0){return this.x=t[e],this.y=t[e+1],this}toArray(t=[],e=0){return t[e]=this.x,t[e+1]=this.y,t}fromBufferAttribute(t,e){return this.x=t.getX(e),this.y=t.getY(e),this}rotateAround(t,e){let n=Math.cos(e),s=Math.sin(e),r=this.x-t.x,a=this.y-t.y;return this.x=r*n-a*s+t.x,this.y=r*s+a*n+t.y,this}random(){return this.x=Math.random(),this.y=Math.random(),this}*[Symbol.iterator](){yield this.x,yield this.y}},ve=class i{constructor(t,e,n,s,r,a,o,l,c){i.prototype.isMatrix3=!0,this.elements=[1,0,0,0,1,0,0,0,1],t!==void 0&&this.set(t,e,n,s,r,a,o,l,c)}set(t,e,n,s,r,a,o,l,c){let h=this.elements;return h[0]=t,h[1]=s,h[2]=o,h[3]=e,h[4]=r,h[5]=l,h[6]=n,h[7]=a,h[8]=c,this}identity(){return this.set(1,0,0,0,1,0,0,0,1),this}copy(t){let e=this.elements,n=t.elements;return e[0]=n[0],e[1]=n[1],e[2]=n[2],e[3]=n[3],e[4]=n[4],e[5]=n[5],e[6]=n[6],e[7]=n[7],e[8]=n[8],this}extractBasis(t,e,n){return t.setFromMatrix3Column(this,0),e.setFromMatrix3Column(this,1),n.setFromMatrix3Column(this,2),this}setFromMatrix4(t){let e=t.elements;return this.set(e[0],e[4],e[8],e[1],e[5],e[9],e[2],e[6],e[10]),this}multiply(t){return this.multiplyMatrices(this,t)}premultiply(t){return this.multiplyMatrices(t,this)}multiplyMatrices(t,e){let n=t.elements,s=e.elements,r=this.elements,a=n[0],o=n[3],l=n[6],c=n[1],h=n[4],u=n[7],d=n[2],p=n[5],x=n[8],y=s[0],g=s[3],m=s[6],w=s[1],v=s[4],I=s[7],H=s[2],U=s[5],N=s[8];return r[0]=a*y+o*w+l*H,r[3]=a*g+o*v+l*U,r[6]=a*m+o*I+l*N,r[1]=c*y+h*w+u*H,r[4]=c*g+h*v+u*U,r[7]=c*m+h*I+u*N,r[2]=d*y+p*w+x*H,r[5]=d*g+p*v+x*U,r[8]=d*m+p*I+x*N,this}multiplyScalar(t){let e=this.elements;return e[0]*=t,e[3]*=t,e[6]*=t,e[1]*=t,e[4]*=t,e[7]*=t,e[2]*=t,e[5]*=t,e[8]*=t,this}determinant(){let t=this.elements,e=t[0],n=t[1],s=t[2],r=t[3],a=t[4],o=t[5],l=t[6],c=t[7],h=t[8];return e*a*h-e*o*c-n*r*h+n*o*l+s*r*c-s*a*l}invert(){let t=this.elements,e=t[0],n=t[1],s=t[2],r=t[3],a=t[4],o=t[5],l=t[6],c=t[7],h=t[8],u=h*a-o*c,d=o*l-h*r,p=c*r-a*l,x=e*u+n*d+s*p;if(x===0)return this.set(0,0,0,0,0,0,0,0,0);let y=1/x;return t[0]=u*y,t[1]=(s*c-h*n)*y,t[2]=(o*n-s*a)*y,t[3]=d*y,t[4]=(h*e-s*l)*y,t[5]=(s*r-o*e)*y,t[6]=p*y,t[7]=(n*l-c*e)*y,t[8]=(a*e-n*r)*y,this}transpose(){let t,e=this.elements;return t=e[1],e[1]=e[3],e[3]=t,t=e[2],e[2]=e[6],e[6]=t,t=e[5],e[5]=e[7],e[7]=t,this}getNormalMatrix(t){return this.setFromMatrix4(t).invert().transpose()}transposeIntoArray(t){let e=this.elements;return t[0]=e[0],t[1]=e[3],t[2]=e[6],t[3]=e[1],t[4]=e[4],t[5]=e[7],t[6]=e[2],t[7]=e[5],t[8]=e[8],this}setUvTransform(t,e,n,s,r,a,o){let l=Math.cos(r),c=Math.sin(r);return this.set(n*l,n*c,-n*(l*a+c*o)+a+t,-s*c,s*l,-s*(-c*a+l*o)+o+e,0,0,1),this}scale(t,e){return this.premultiply(Ya.makeScale(t,e)),this}rotate(t){return this.premultiply(Ya.makeRotation(-t)),this}translate(t,e){return this.premultiply(Ya.makeTranslation(t,e)),this}makeTranslation(t,e){return t.isVector2?this.set(1,0,t.x,0,1,t.y,0,0,1):this.set(1,0,t,0,1,e,0,0,1),this}makeRotation(t){let e=Math.cos(t),n=Math.sin(t);return this.set(e,-n,0,n,e,0,0,0,1),this}makeScale(t,e){return this.set(t,0,0,0,e,0,0,0,1),this}equals(t){let e=this.elements,n=t.elements;for(let s=0;s<9;s++)if(e[s]!==n[s])return!1;return!0}fromArray(t,e=0){for(let n=0;n<9;n++)this.elements[n]=t[n+e];return this}toArray(t=[],e=0){let n=this.elements;return t[e]=n[0],t[e+1]=n[1],t[e+2]=n[2],t[e+3]=n[3],t[e+4]=n[4],t[e+5]=n[5],t[e+6]=n[6],t[e+7]=n[7],t[e+8]=n[8],t}clone(){return new this.constructor().fromArray(this.elements)}},Ya=new ve;function qu(i){for(let t=i.length-1;t>=0;--t)if(i[t]>=65535)return!0;return!1}function Lr(i){return document.createElementNS("http://www.w3.org/1999/xhtml",i)}function Ld(){let i=Lr("canvas");return i.style.display="block",i}var Bh={};function Er(i){i in Bh||(Bh[i]=!0,console.warn(i))}var zh=new ve().set(.8224621,.177538,0,.0331941,.9668058,0,.0170827,.0723974,.9105199),Hh=new ve().set(1.2249401,-.2249404,0,-.0420569,1.0420571,0,-.0196376,-.0786361,1.0982735),ao={[Ai]:{transfer:Ho,primaries:ko,toReference:i=>i,fromReference:i=>i},[Je]:{transfer:ke,primaries:ko,toReference:i=>i.convertSRGBToLinear(),fromReference:i=>i.convertLinearToSRGB()},[_a]:{transfer:Ho,primaries:Vo,toReference:i=>i.applyMatrix3(Hh),fromReference:i=>i.applyMatrix3(zh)},[pc]:{transfer:ke,primaries:Vo,toReference:i=>i.convertSRGBToLinear().applyMatrix3(Hh),fromReference:i=>i.applyMatrix3(zh).convertLinearToSRGB()}},Ud=new Set([Ai,_a]),Ue={enabled:!0,_workingColorSpace:Ai,get workingColorSpace(){return this._workingColorSpace},set workingColorSpace(i){if(!Ud.has(i))throw new Error(`Unsupported working color space, "${i}".`);this._workingColorSpace=i},convert:function(i,t,e){if(this.enabled===!1||t===e||!t||!e)return i;let n=ao[t].toReference,s=ao[e].fromReference;return s(n(i))},fromWorkingColorSpace:function(i,t){return this.convert(i,this._workingColorSpace,t)},toWorkingColorSpace:function(i,t){return this.convert(i,t,this._workingColorSpace)},getPrimaries:function(i){return ao[i].primaries},getTransfer:function(i){return i===Vn?Ho:ao[i].transfer}};function Js(i){return i<.04045?i*.0773993808:Math.pow(i*.9478672986+.0521327014,2.4)}function qa(i){return i<.0031308?i*12.92:1.055*Math.pow(i,.41666)-.055}var As,Xo=class{static getDataURL(t){if(/^data:/i.test(t.src)||typeof HTMLCanvasElement=="undefined")return t.src;let e;if(t instanceof HTMLCanvasElement)e=t;else{As===void 0&&(As=Lr("canvas")),As.width=t.width,As.height=t.height;let n=As.getContext("2d");t instanceof ImageData?n.putImageData(t,0,0):n.drawImage(t,0,0,t.width,t.height),e=As}return e.width>2048||e.height>2048?(console.warn("THREE.ImageUtils.getDataURL: Image converted to jpg for performance reasons",t),e.toDataURL("image/jpeg",.6)):e.toDataURL("image/png")}static sRGBToLinear(t){if(typeof HTMLImageElement!="undefined"&&t instanceof HTMLImageElement||typeof HTMLCanvasElement!="undefined"&&t instanceof HTMLCanvasElement||typeof ImageBitmap!="undefined"&&t instanceof ImageBitmap){let e=Lr("canvas");e.width=t.width,e.height=t.height;let n=e.getContext("2d");n.drawImage(t,0,0,t.width,t.height);let s=n.getImageData(0,0,t.width,t.height),r=s.data;for(let a=0;a<r.length;a++)r[a]=Js(r[a]/255)*255;return n.putImageData(s,0,0),e}else if(t.data){let e=t.data.slice(0);for(let n=0;n<e.length;n++)e instanceof Uint8Array||e instanceof Uint8ClampedArray?e[n]=Math.floor(Js(e[n]/255)*255):e[n]=Js(e[n]);return{data:e,width:t.width,height:t.height}}else return console.warn("THREE.ImageUtils.sRGBToLinear(): Unsupported image type. No color space conversion applied."),t}},Dd=0,Yo=class{constructor(t=null){this.isSource=!0,Object.defineProperty(this,"id",{value:Dd++}),this.uuid=ys(),this.data=t,this.version=0}set needsUpdate(t){t===!0&&this.version++}toJSON(t){let e=t===void 0||typeof t=="string";if(!e&&t.images[this.uuid]!==void 0)return t.images[this.uuid];let n={uuid:this.uuid,url:""},s=this.data;if(s!==null){let r;if(Array.isArray(s)){r=[];for(let a=0,o=s.length;a<o;a++)s[a].isDataTexture?r.push(Za(s[a].image)):r.push(Za(s[a]))}else r=Za(s);n.url=r}return e||(t.images[this.uuid]=n),n}};function Za(i){return typeof HTMLImageElement!="undefined"&&i instanceof HTMLImageElement||typeof HTMLCanvasElement!="undefined"&&i instanceof HTMLCanvasElement||typeof ImageBitmap!="undefined"&&i instanceof ImageBitmap?Xo.getDataURL(i):i.data?{data:Array.from(i.data),width:i.width,height:i.height,type:i.data.constructor.name}:(console.warn("THREE.Texture: Unable to serialize Texture."),{})}var Nd=0,Dn=class i extends qi{constructor(t=i.DEFAULT_IMAGE,e=i.DEFAULT_MAPPING,n=Rn,s=Rn,r=kn,a=Cr,o=Qn,l=Xi,c=i.DEFAULT_ANISOTROPY,h=Vn){super(),this.isTexture=!0,Object.defineProperty(this,"id",{value:Nd++}),this.uuid=ys(),this.name="",this.source=new Yo(t),this.mipmaps=[],this.mapping=e,this.channel=0,this.wrapS=n,this.wrapT=s,this.magFilter=r,this.minFilter=a,this.anisotropy=c,this.format=o,this.internalFormat=null,this.type=l,this.offset=new xt(0,0),this.repeat=new xt(1,1),this.center=new xt(0,0),this.rotation=0,this.matrixAutoUpdate=!0,this.matrix=new ve,this.generateMipmaps=!0,this.premultiplyAlpha=!1,this.flipY=!0,this.unpackAlignment=4,typeof h=="string"?this.colorSpace=h:(Er("THREE.Texture: Property .encoding has been replaced by .colorSpace."),this.colorSpace=h===ds?Je:Vn),this.userData={},this.version=0,this.onUpdate=null,this.isRenderTargetTexture=!1,this.needsPMREMUpdate=!1}get image(){return this.source.data}set image(t=null){this.source.data=t}updateMatrix(){this.matrix.setUvTransform(this.offset.x,this.offset.y,this.repeat.x,this.repeat.y,this.rotation,this.center.x,this.center.y)}clone(){return new this.constructor().copy(this)}copy(t){return this.name=t.name,this.source=t.source,this.mipmaps=t.mipmaps.slice(0),this.mapping=t.mapping,this.channel=t.channel,this.wrapS=t.wrapS,this.wrapT=t.wrapT,this.magFilter=t.magFilter,this.minFilter=t.minFilter,this.anisotropy=t.anisotropy,this.format=t.format,this.internalFormat=t.internalFormat,this.type=t.type,this.offset.copy(t.offset),this.repeat.copy(t.repeat),this.center.copy(t.center),this.rotation=t.rotation,this.matrixAutoUpdate=t.matrixAutoUpdate,this.matrix.copy(t.matrix),this.generateMipmaps=t.generateMipmaps,this.premultiplyAlpha=t.premultiplyAlpha,this.flipY=t.flipY,this.unpackAlignment=t.unpackAlignment,this.colorSpace=t.colorSpace,this.userData=JSON.parse(JSON.stringify(t.userData)),this.needsUpdate=!0,this}toJSON(t){let e=t===void 0||typeof t=="string";if(!e&&t.textures[this.uuid]!==void 0)return t.textures[this.uuid];let n={metadata:{version:4.6,type:"Texture",generator:"Texture.toJSON"},uuid:this.uuid,name:this.name,image:this.source.toJSON(t).uuid,mapping:this.mapping,channel:this.channel,repeat:[this.repeat.x,this.repeat.y],offset:[this.offset.x,this.offset.y],center:[this.center.x,this.center.y],rotation:this.rotation,wrap:[this.wrapS,this.wrapT],format:this.format,internalFormat:this.internalFormat,type:this.type,colorSpace:this.colorSpace,minFilter:this.minFilter,magFilter:this.magFilter,anisotropy:this.anisotropy,flipY:this.flipY,generateMipmaps:this.generateMipmaps,premultiplyAlpha:this.premultiplyAlpha,unpackAlignment:this.unpackAlignment};return Object.keys(this.userData).length>0&&(n.userData=this.userData),e||(t.textures[this.uuid]=n),n}dispose(){this.dispatchEvent({type:"dispose"})}transformUv(t){if(this.mapping!==Fu)return t;if(t.applyMatrix3(this.matrix),t.x<0||t.x>1)switch(this.wrapS){case ps:t.x=t.x-Math.floor(t.x);break;case Rn:t.x=t.x<0?0:1;break;case bl:Math.abs(Math.floor(t.x)%2)===1?t.x=Math.ceil(t.x)-t.x:t.x=t.x-Math.floor(t.x);break}if(t.y<0||t.y>1)switch(this.wrapT){case ps:t.y=t.y-Math.floor(t.y);break;case Rn:t.y=t.y<0?0:1;break;case bl:Math.abs(Math.floor(t.y)%2)===1?t.y=Math.ceil(t.y)-t.y:t.y=t.y-Math.floor(t.y);break}return this.flipY&&(t.y=1-t.y),t}set needsUpdate(t){t===!0&&(this.version++,this.source.needsUpdate=!0)}get encoding(){return Er("THREE.Texture: Property .encoding has been replaced by .colorSpace."),this.colorSpace===Je?ds:Wu}set encoding(t){Er("THREE.Texture: Property .encoding has been replaced by .colorSpace."),this.colorSpace=t===ds?Je:Vn}};Dn.DEFAULT_IMAGE=null;Dn.DEFAULT_MAPPING=Fu;Dn.DEFAULT_ANISOTROPY=1;var Xe=class i{constructor(t=0,e=0,n=0,s=1){i.prototype.isVector4=!0,this.x=t,this.y=e,this.z=n,this.w=s}get width(){return this.z}set width(t){this.z=t}get height(){return this.w}set height(t){this.w=t}set(t,e,n,s){return this.x=t,this.y=e,this.z=n,this.w=s,this}setScalar(t){return this.x=t,this.y=t,this.z=t,this.w=t,this}setX(t){return this.x=t,this}setY(t){return this.y=t,this}setZ(t){return this.z=t,this}setW(t){return this.w=t,this}setComponent(t,e){switch(t){case 0:this.x=e;break;case 1:this.y=e;break;case 2:this.z=e;break;case 3:this.w=e;break;default:throw new Error("index is out of range: "+t)}return this}getComponent(t){switch(t){case 0:return this.x;case 1:return this.y;case 2:return this.z;case 3:return this.w;default:throw new Error("index is out of range: "+t)}}clone(){return new this.constructor(this.x,this.y,this.z,this.w)}copy(t){return this.x=t.x,this.y=t.y,this.z=t.z,this.w=t.w!==void 0?t.w:1,this}add(t){return this.x+=t.x,this.y+=t.y,this.z+=t.z,this.w+=t.w,this}addScalar(t){return this.x+=t,this.y+=t,this.z+=t,this.w+=t,this}addVectors(t,e){return this.x=t.x+e.x,this.y=t.y+e.y,this.z=t.z+e.z,this.w=t.w+e.w,this}addScaledVector(t,e){return this.x+=t.x*e,this.y+=t.y*e,this.z+=t.z*e,this.w+=t.w*e,this}sub(t){return this.x-=t.x,this.y-=t.y,this.z-=t.z,this.w-=t.w,this}subScalar(t){return this.x-=t,this.y-=t,this.z-=t,this.w-=t,this}subVectors(t,e){return this.x=t.x-e.x,this.y=t.y-e.y,this.z=t.z-e.z,this.w=t.w-e.w,this}multiply(t){return this.x*=t.x,this.y*=t.y,this.z*=t.z,this.w*=t.w,this}multiplyScalar(t){return this.x*=t,this.y*=t,this.z*=t,this.w*=t,this}applyMatrix4(t){let e=this.x,n=this.y,s=this.z,r=this.w,a=t.elements;return this.x=a[0]*e+a[4]*n+a[8]*s+a[12]*r,this.y=a[1]*e+a[5]*n+a[9]*s+a[13]*r,this.z=a[2]*e+a[6]*n+a[10]*s+a[14]*r,this.w=a[3]*e+a[7]*n+a[11]*s+a[15]*r,this}divideScalar(t){return this.multiplyScalar(1/t)}setAxisAngleFromQuaternion(t){this.w=2*Math.acos(t.w);let e=Math.sqrt(1-t.w*t.w);return e<1e-4?(this.x=1,this.y=0,this.z=0):(this.x=t.x/e,this.y=t.y/e,this.z=t.z/e),this}setAxisAngleFromRotationMatrix(t){let e,n,s,r,l=t.elements,c=l[0],h=l[4],u=l[8],d=l[1],p=l[5],x=l[9],y=l[2],g=l[6],m=l[10];if(Math.abs(h-d)<.01&&Math.abs(u-y)<.01&&Math.abs(x-g)<.01){if(Math.abs(h+d)<.1&&Math.abs(u+y)<.1&&Math.abs(x+g)<.1&&Math.abs(c+p+m-3)<.1)return this.set(1,0,0,0),this;e=Math.PI;let v=(c+1)/2,I=(p+1)/2,H=(m+1)/2,U=(h+d)/4,N=(u+y)/4,Y=(x+g)/4;return v>I&&v>H?v<.01?(n=0,s=.707106781,r=.707106781):(n=Math.sqrt(v),s=U/n,r=N/n):I>H?I<.01?(n=.707106781,s=0,r=.707106781):(s=Math.sqrt(I),n=U/s,r=Y/s):H<.01?(n=.707106781,s=.707106781,r=0):(r=Math.sqrt(H),n=N/r,s=Y/r),this.set(n,s,r,e),this}let w=Math.sqrt((g-x)*(g-x)+(u-y)*(u-y)+(d-h)*(d-h));return Math.abs(w)<.001&&(w=1),this.x=(g-x)/w,this.y=(u-y)/w,this.z=(d-h)/w,this.w=Math.acos((c+p+m-1)/2),this}min(t){return this.x=Math.min(this.x,t.x),this.y=Math.min(this.y,t.y),this.z=Math.min(this.z,t.z),this.w=Math.min(this.w,t.w),this}max(t){return this.x=Math.max(this.x,t.x),this.y=Math.max(this.y,t.y),this.z=Math.max(this.z,t.z),this.w=Math.max(this.w,t.w),this}clamp(t,e){return this.x=Math.max(t.x,Math.min(e.x,this.x)),this.y=Math.max(t.y,Math.min(e.y,this.y)),this.z=Math.max(t.z,Math.min(e.z,this.z)),this.w=Math.max(t.w,Math.min(e.w,this.w)),this}clampScalar(t,e){return this.x=Math.max(t,Math.min(e,this.x)),this.y=Math.max(t,Math.min(e,this.y)),this.z=Math.max(t,Math.min(e,this.z)),this.w=Math.max(t,Math.min(e,this.w)),this}clampLength(t,e){let n=this.length();return this.divideScalar(n||1).multiplyScalar(Math.max(t,Math.min(e,n)))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this.z=Math.floor(this.z),this.w=Math.floor(this.w),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this.z=Math.ceil(this.z),this.w=Math.ceil(this.w),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this.z=Math.round(this.z),this.w=Math.round(this.w),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this.z=Math.trunc(this.z),this.w=Math.trunc(this.w),this}negate(){return this.x=-this.x,this.y=-this.y,this.z=-this.z,this.w=-this.w,this}dot(t){return this.x*t.x+this.y*t.y+this.z*t.z+this.w*t.w}lengthSq(){return this.x*this.x+this.y*this.y+this.z*this.z+this.w*this.w}length(){return Math.sqrt(this.x*this.x+this.y*this.y+this.z*this.z+this.w*this.w)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)+Math.abs(this.z)+Math.abs(this.w)}normalize(){return this.divideScalar(this.length()||1)}setLength(t){return this.normalize().multiplyScalar(t)}lerp(t,e){return this.x+=(t.x-this.x)*e,this.y+=(t.y-this.y)*e,this.z+=(t.z-this.z)*e,this.w+=(t.w-this.w)*e,this}lerpVectors(t,e,n){return this.x=t.x+(e.x-t.x)*n,this.y=t.y+(e.y-t.y)*n,this.z=t.z+(e.z-t.z)*n,this.w=t.w+(e.w-t.w)*n,this}equals(t){return t.x===this.x&&t.y===this.y&&t.z===this.z&&t.w===this.w}fromArray(t,e=0){return this.x=t[e],this.y=t[e+1],this.z=t[e+2],this.w=t[e+3],this}toArray(t=[],e=0){return t[e]=this.x,t[e+1]=this.y,t[e+2]=this.z,t[e+3]=this.w,t}fromBufferAttribute(t,e){return this.x=t.getX(e),this.y=t.getY(e),this.z=t.getZ(e),this.w=t.getW(e),this}random(){return this.x=Math.random(),this.y=Math.random(),this.z=Math.random(),this.w=Math.random(),this}*[Symbol.iterator](){yield this.x,yield this.y,yield this.z,yield this.w}},Tl=class extends qi{constructor(t=1,e=1,n={}){super(),this.isRenderTarget=!0,this.width=t,this.height=e,this.depth=1,this.scissor=new Xe(0,0,t,e),this.scissorTest=!1,this.viewport=new Xe(0,0,t,e);let s={width:t,height:e,depth:1};n.encoding!==void 0&&(Er("THREE.WebGLRenderTarget: option.encoding has been replaced by option.colorSpace."),n.colorSpace=n.encoding===ds?Je:Vn),n=Object.assign({generateMipmaps:!1,internalFormat:null,minFilter:kn,depthBuffer:!0,stencilBuffer:!1,depthTexture:null,samples:0},n),this.texture=new Dn(s,n.mapping,n.wrapS,n.wrapT,n.magFilter,n.minFilter,n.format,n.type,n.anisotropy,n.colorSpace),this.texture.isRenderTargetTexture=!0,this.texture.flipY=!1,this.texture.generateMipmaps=n.generateMipmaps,this.texture.internalFormat=n.internalFormat,this.depthBuffer=n.depthBuffer,this.stencilBuffer=n.stencilBuffer,this.depthTexture=n.depthTexture,this.samples=n.samples}setSize(t,e,n=1){(this.width!==t||this.height!==e||this.depth!==n)&&(this.width=t,this.height=e,this.depth=n,this.texture.image.width=t,this.texture.image.height=e,this.texture.image.depth=n,this.dispose()),this.viewport.set(0,0,t,e),this.scissor.set(0,0,t,e)}clone(){return new this.constructor().copy(this)}copy(t){this.width=t.width,this.height=t.height,this.depth=t.depth,this.scissor.copy(t.scissor),this.scissorTest=t.scissorTest,this.viewport.copy(t.viewport),this.texture=t.texture.clone(),this.texture.isRenderTargetTexture=!0;let e=Object.assign({},t.texture.image);return this.texture.source=new Yo(e),this.depthBuffer=t.depthBuffer,this.stencilBuffer=t.stencilBuffer,t.depthTexture!==null&&(this.depthTexture=t.depthTexture.clone()),this.samples=t.samples,this}dispose(){this.dispatchEvent({type:"dispose"})}},Ri=class extends Tl{constructor(t=1,e=1,n={}){super(t,e,n),this.isWebGLRenderTarget=!0}},qo=class extends Dn{constructor(t=null,e=1,n=1,s=1){super(null),this.isDataArrayTexture=!0,this.image={data:t,width:e,height:n,depth:s},this.magFilter=An,this.minFilter=An,this.wrapR=Rn,this.generateMipmaps=!1,this.flipY=!1,this.unpackAlignment=1}};var Al=class extends Dn{constructor(t=null,e=1,n=1,s=1){super(null),this.isData3DTexture=!0,this.image={data:t,width:e,height:n,depth:s},this.magFilter=An,this.minFilter=An,this.wrapR=Rn,this.generateMipmaps=!1,this.flipY=!1,this.unpackAlignment=1}};var ti=class{constructor(t=0,e=0,n=0,s=1){this.isQuaternion=!0,this._x=t,this._y=e,this._z=n,this._w=s}static slerpFlat(t,e,n,s,r,a,o){let l=n[s+0],c=n[s+1],h=n[s+2],u=n[s+3],d=r[a+0],p=r[a+1],x=r[a+2],y=r[a+3];if(o===0){t[e+0]=l,t[e+1]=c,t[e+2]=h,t[e+3]=u;return}if(o===1){t[e+0]=d,t[e+1]=p,t[e+2]=x,t[e+3]=y;return}if(u!==y||l!==d||c!==p||h!==x){let g=1-o,m=l*d+c*p+h*x+u*y,w=m>=0?1:-1,v=1-m*m;if(v>Number.EPSILON){let H=Math.sqrt(v),U=Math.atan2(H,m*w);g=Math.sin(g*U)/H,o=Math.sin(o*U)/H}let I=o*w;if(l=l*g+d*I,c=c*g+p*I,h=h*g+x*I,u=u*g+y*I,g===1-o){let H=1/Math.sqrt(l*l+c*c+h*h+u*u);l*=H,c*=H,h*=H,u*=H}}t[e]=l,t[e+1]=c,t[e+2]=h,t[e+3]=u}static multiplyQuaternionsFlat(t,e,n,s,r,a){let o=n[s],l=n[s+1],c=n[s+2],h=n[s+3],u=r[a],d=r[a+1],p=r[a+2],x=r[a+3];return t[e]=o*x+h*u+l*p-c*d,t[e+1]=l*x+h*d+c*u-o*p,t[e+2]=c*x+h*p+o*d-l*u,t[e+3]=h*x-o*u-l*d-c*p,t}get x(){return this._x}set x(t){this._x=t,this._onChangeCallback()}get y(){return this._y}set y(t){this._y=t,this._onChangeCallback()}get z(){return this._z}set z(t){this._z=t,this._onChangeCallback()}get w(){return this._w}set w(t){this._w=t,this._onChangeCallback()}set(t,e,n,s){return this._x=t,this._y=e,this._z=n,this._w=s,this._onChangeCallback(),this}clone(){return new this.constructor(this._x,this._y,this._z,this._w)}copy(t){return this._x=t.x,this._y=t.y,this._z=t.z,this._w=t.w,this._onChangeCallback(),this}setFromEuler(t,e=!0){let n=t._x,s=t._y,r=t._z,a=t._order,o=Math.cos,l=Math.sin,c=o(n/2),h=o(s/2),u=o(r/2),d=l(n/2),p=l(s/2),x=l(r/2);switch(a){case"XYZ":this._x=d*h*u+c*p*x,this._y=c*p*u-d*h*x,this._z=c*h*x+d*p*u,this._w=c*h*u-d*p*x;break;case"YXZ":this._x=d*h*u+c*p*x,this._y=c*p*u-d*h*x,this._z=c*h*x-d*p*u,this._w=c*h*u+d*p*x;break;case"ZXY":this._x=d*h*u-c*p*x,this._y=c*p*u+d*h*x,this._z=c*h*x+d*p*u,this._w=c*h*u-d*p*x;break;case"ZYX":this._x=d*h*u-c*p*x,this._y=c*p*u+d*h*x,this._z=c*h*x-d*p*u,this._w=c*h*u+d*p*x;break;case"YZX":this._x=d*h*u+c*p*x,this._y=c*p*u+d*h*x,this._z=c*h*x-d*p*u,this._w=c*h*u-d*p*x;break;case"XZY":this._x=d*h*u-c*p*x,this._y=c*p*u-d*h*x,this._z=c*h*x+d*p*u,this._w=c*h*u+d*p*x;break;default:console.warn("THREE.Quaternion: .setFromEuler() encountered an unknown order: "+a)}return e===!0&&this._onChangeCallback(),this}setFromAxisAngle(t,e){let n=e/2,s=Math.sin(n);return this._x=t.x*s,this._y=t.y*s,this._z=t.z*s,this._w=Math.cos(n),this._onChangeCallback(),this}setFromRotationMatrix(t){let e=t.elements,n=e[0],s=e[4],r=e[8],a=e[1],o=e[5],l=e[9],c=e[2],h=e[6],u=e[10],d=n+o+u;if(d>0){let p=.5/Math.sqrt(d+1);this._w=.25/p,this._x=(h-l)*p,this._y=(r-c)*p,this._z=(a-s)*p}else if(n>o&&n>u){let p=2*Math.sqrt(1+n-o-u);this._w=(h-l)/p,this._x=.25*p,this._y=(s+a)/p,this._z=(r+c)/p}else if(o>u){let p=2*Math.sqrt(1+o-n-u);this._w=(r-c)/p,this._x=(s+a)/p,this._y=.25*p,this._z=(l+h)/p}else{let p=2*Math.sqrt(1+u-n-o);this._w=(a-s)/p,this._x=(r+c)/p,this._y=(l+h)/p,this._z=.25*p}return this._onChangeCallback(),this}setFromUnitVectors(t,e){let n=t.dot(e)+1;return n<Number.EPSILON?(n=0,Math.abs(t.x)>Math.abs(t.z)?(this._x=-t.y,this._y=t.x,this._z=0,this._w=n):(this._x=0,this._y=-t.z,this._z=t.y,this._w=n)):(this._x=t.y*e.z-t.z*e.y,this._y=t.z*e.x-t.x*e.z,this._z=t.x*e.y-t.y*e.x,this._w=n),this.normalize()}angleTo(t){return 2*Math.acos(Math.abs(cn(this.dot(t),-1,1)))}rotateTowards(t,e){let n=this.angleTo(t);if(n===0)return this;let s=Math.min(1,e/n);return this.slerp(t,s),this}identity(){return this.set(0,0,0,1)}invert(){return this.conjugate()}conjugate(){return this._x*=-1,this._y*=-1,this._z*=-1,this._onChangeCallback(),this}dot(t){return this._x*t._x+this._y*t._y+this._z*t._z+this._w*t._w}lengthSq(){return this._x*this._x+this._y*this._y+this._z*this._z+this._w*this._w}length(){return Math.sqrt(this._x*this._x+this._y*this._y+this._z*this._z+this._w*this._w)}normalize(){let t=this.length();return t===0?(this._x=0,this._y=0,this._z=0,this._w=1):(t=1/t,this._x=this._x*t,this._y=this._y*t,this._z=this._z*t,this._w=this._w*t),this._onChangeCallback(),this}multiply(t){return this.multiplyQuaternions(this,t)}premultiply(t){return this.multiplyQuaternions(t,this)}multiplyQuaternions(t,e){let n=t._x,s=t._y,r=t._z,a=t._w,o=e._x,l=e._y,c=e._z,h=e._w;return this._x=n*h+a*o+s*c-r*l,this._y=s*h+a*l+r*o-n*c,this._z=r*h+a*c+n*l-s*o,this._w=a*h-n*o-s*l-r*c,this._onChangeCallback(),this}slerp(t,e){if(e===0)return this;if(e===1)return this.copy(t);let n=this._x,s=this._y,r=this._z,a=this._w,o=a*t._w+n*t._x+s*t._y+r*t._z;if(o<0?(this._w=-t._w,this._x=-t._x,this._y=-t._y,this._z=-t._z,o=-o):this.copy(t),o>=1)return this._w=a,this._x=n,this._y=s,this._z=r,this;let l=1-o*o;if(l<=Number.EPSILON){let p=1-e;return this._w=p*a+e*this._w,this._x=p*n+e*this._x,this._y=p*s+e*this._y,this._z=p*r+e*this._z,this.normalize(),this}let c=Math.sqrt(l),h=Math.atan2(c,o),u=Math.sin((1-e)*h)/c,d=Math.sin(e*h)/c;return this._w=a*u+this._w*d,this._x=n*u+this._x*d,this._y=s*u+this._y*d,this._z=r*u+this._z*d,this._onChangeCallback(),this}slerpQuaternions(t,e,n){return this.copy(t).slerp(e,n)}random(){let t=Math.random(),e=Math.sqrt(1-t),n=Math.sqrt(t),s=2*Math.PI*Math.random(),r=2*Math.PI*Math.random();return this.set(e*Math.cos(s),n*Math.sin(r),n*Math.cos(r),e*Math.sin(s))}equals(t){return t._x===this._x&&t._y===this._y&&t._z===this._z&&t._w===this._w}fromArray(t,e=0){return this._x=t[e],this._y=t[e+1],this._z=t[e+2],this._w=t[e+3],this._onChangeCallback(),this}toArray(t=[],e=0){return t[e]=this._x,t[e+1]=this._y,t[e+2]=this._z,t[e+3]=this._w,t}fromBufferAttribute(t,e){return this._x=t.getX(e),this._y=t.getY(e),this._z=t.getZ(e),this._w=t.getW(e),this._onChangeCallback(),this}toJSON(){return this.toArray()}_onChange(t){return this._onChangeCallback=t,this}_onChangeCallback(){}*[Symbol.iterator](){yield this._x,yield this._y,yield this._z,yield this._w}},O=class i{constructor(t=0,e=0,n=0){i.prototype.isVector3=!0,this.x=t,this.y=e,this.z=n}set(t,e,n){return n===void 0&&(n=this.z),this.x=t,this.y=e,this.z=n,this}setScalar(t){return this.x=t,this.y=t,this.z=t,this}setX(t){return this.x=t,this}setY(t){return this.y=t,this}setZ(t){return this.z=t,this}setComponent(t,e){switch(t){case 0:this.x=e;break;case 1:this.y=e;break;case 2:this.z=e;break;default:throw new Error("index is out of range: "+t)}return this}getComponent(t){switch(t){case 0:return this.x;case 1:return this.y;case 2:return this.z;default:throw new Error("index is out of range: "+t)}}clone(){return new this.constructor(this.x,this.y,this.z)}copy(t){return this.x=t.x,this.y=t.y,this.z=t.z,this}add(t){return this.x+=t.x,this.y+=t.y,this.z+=t.z,this}addScalar(t){return this.x+=t,this.y+=t,this.z+=t,this}addVectors(t,e){return this.x=t.x+e.x,this.y=t.y+e.y,this.z=t.z+e.z,this}addScaledVector(t,e){return this.x+=t.x*e,this.y+=t.y*e,this.z+=t.z*e,this}sub(t){return this.x-=t.x,this.y-=t.y,this.z-=t.z,this}subScalar(t){return this.x-=t,this.y-=t,this.z-=t,this}subVectors(t,e){return this.x=t.x-e.x,this.y=t.y-e.y,this.z=t.z-e.z,this}multiply(t){return this.x*=t.x,this.y*=t.y,this.z*=t.z,this}multiplyScalar(t){return this.x*=t,this.y*=t,this.z*=t,this}multiplyVectors(t,e){return this.x=t.x*e.x,this.y=t.y*e.y,this.z=t.z*e.z,this}applyEuler(t){return this.applyQuaternion(kh.setFromEuler(t))}applyAxisAngle(t,e){return this.applyQuaternion(kh.setFromAxisAngle(t,e))}applyMatrix3(t){let e=this.x,n=this.y,s=this.z,r=t.elements;return this.x=r[0]*e+r[3]*n+r[6]*s,this.y=r[1]*e+r[4]*n+r[7]*s,this.z=r[2]*e+r[5]*n+r[8]*s,this}applyNormalMatrix(t){return this.applyMatrix3(t).normalize()}applyMatrix4(t){let e=this.x,n=this.y,s=this.z,r=t.elements,a=1/(r[3]*e+r[7]*n+r[11]*s+r[15]);return this.x=(r[0]*e+r[4]*n+r[8]*s+r[12])*a,this.y=(r[1]*e+r[5]*n+r[9]*s+r[13])*a,this.z=(r[2]*e+r[6]*n+r[10]*s+r[14])*a,this}applyQuaternion(t){let e=this.x,n=this.y,s=this.z,r=t.x,a=t.y,o=t.z,l=t.w,c=2*(a*s-o*n),h=2*(o*e-r*s),u=2*(r*n-a*e);return this.x=e+l*c+a*u-o*h,this.y=n+l*h+o*c-r*u,this.z=s+l*u+r*h-a*c,this}project(t){return this.applyMatrix4(t.matrixWorldInverse).applyMatrix4(t.projectionMatrix)}unproject(t){return this.applyMatrix4(t.projectionMatrixInverse).applyMatrix4(t.matrixWorld)}transformDirection(t){let e=this.x,n=this.y,s=this.z,r=t.elements;return this.x=r[0]*e+r[4]*n+r[8]*s,this.y=r[1]*e+r[5]*n+r[9]*s,this.z=r[2]*e+r[6]*n+r[10]*s,this.normalize()}divide(t){return this.x/=t.x,this.y/=t.y,this.z/=t.z,this}divideScalar(t){return this.multiplyScalar(1/t)}min(t){return this.x=Math.min(this.x,t.x),this.y=Math.min(this.y,t.y),this.z=Math.min(this.z,t.z),this}max(t){return this.x=Math.max(this.x,t.x),this.y=Math.max(this.y,t.y),this.z=Math.max(this.z,t.z),this}clamp(t,e){return this.x=Math.max(t.x,Math.min(e.x,this.x)),this.y=Math.max(t.y,Math.min(e.y,this.y)),this.z=Math.max(t.z,Math.min(e.z,this.z)),this}clampScalar(t,e){return this.x=Math.max(t,Math.min(e,this.x)),this.y=Math.max(t,Math.min(e,this.y)),this.z=Math.max(t,Math.min(e,this.z)),this}clampLength(t,e){let n=this.length();return this.divideScalar(n||1).multiplyScalar(Math.max(t,Math.min(e,n)))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this.z=Math.floor(this.z),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this.z=Math.ceil(this.z),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this.z=Math.round(this.z),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this.z=Math.trunc(this.z),this}negate(){return this.x=-this.x,this.y=-this.y,this.z=-this.z,this}dot(t){return this.x*t.x+this.y*t.y+this.z*t.z}lengthSq(){return this.x*this.x+this.y*this.y+this.z*this.z}length(){return Math.sqrt(this.x*this.x+this.y*this.y+this.z*this.z)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)+Math.abs(this.z)}normalize(){return this.divideScalar(this.length()||1)}setLength(t){return this.normalize().multiplyScalar(t)}lerp(t,e){return this.x+=(t.x-this.x)*e,this.y+=(t.y-this.y)*e,this.z+=(t.z-this.z)*e,this}lerpVectors(t,e,n){return this.x=t.x+(e.x-t.x)*n,this.y=t.y+(e.y-t.y)*n,this.z=t.z+(e.z-t.z)*n,this}cross(t){return this.crossVectors(this,t)}crossVectors(t,e){let n=t.x,s=t.y,r=t.z,a=e.x,o=e.y,l=e.z;return this.x=s*l-r*o,this.y=r*a-n*l,this.z=n*o-s*a,this}projectOnVector(t){let e=t.lengthSq();if(e===0)return this.set(0,0,0);let n=t.dot(this)/e;return this.copy(t).multiplyScalar(n)}projectOnPlane(t){return $a.copy(this).projectOnVector(t),this.sub($a)}reflect(t){return this.sub($a.copy(t).multiplyScalar(2*this.dot(t)))}angleTo(t){let e=Math.sqrt(this.lengthSq()*t.lengthSq());if(e===0)return Math.PI/2;let n=this.dot(t)/e;return Math.acos(cn(n,-1,1))}distanceTo(t){return Math.sqrt(this.distanceToSquared(t))}distanceToSquared(t){let e=this.x-t.x,n=this.y-t.y,s=this.z-t.z;return e*e+n*n+s*s}manhattanDistanceTo(t){return Math.abs(this.x-t.x)+Math.abs(this.y-t.y)+Math.abs(this.z-t.z)}setFromSpherical(t){return this.setFromSphericalCoords(t.radius,t.phi,t.theta)}setFromSphericalCoords(t,e,n){let s=Math.sin(e)*t;return this.x=s*Math.sin(n),this.y=Math.cos(e)*t,this.z=s*Math.cos(n),this}setFromCylindrical(t){return this.setFromCylindricalCoords(t.radius,t.theta,t.y)}setFromCylindricalCoords(t,e,n){return this.x=t*Math.sin(e),this.y=n,this.z=t*Math.cos(e),this}setFromMatrixPosition(t){let e=t.elements;return this.x=e[12],this.y=e[13],this.z=e[14],this}setFromMatrixScale(t){let e=this.setFromMatrixColumn(t,0).length(),n=this.setFromMatrixColumn(t,1).length(),s=this.setFromMatrixColumn(t,2).length();return this.x=e,this.y=n,this.z=s,this}setFromMatrixColumn(t,e){return this.fromArray(t.elements,e*4)}setFromMatrix3Column(t,e){return this.fromArray(t.elements,e*3)}setFromEuler(t){return this.x=t._x,this.y=t._y,this.z=t._z,this}setFromColor(t){return this.x=t.r,this.y=t.g,this.z=t.b,this}equals(t){return t.x===this.x&&t.y===this.y&&t.z===this.z}fromArray(t,e=0){return this.x=t[e],this.y=t[e+1],this.z=t[e+2],this}toArray(t=[],e=0){return t[e]=this.x,t[e+1]=this.y,t[e+2]=this.z,t}fromBufferAttribute(t,e){return this.x=t.getX(e),this.y=t.getY(e),this.z=t.getZ(e),this}random(){return this.x=Math.random(),this.y=Math.random(),this.z=Math.random(),this}randomDirection(){let t=(Math.random()-.5)*2,e=Math.random()*Math.PI*2,n=Math.sqrt(1-t**2);return this.x=n*Math.cos(e),this.y=n*Math.sin(e),this.z=t,this}*[Symbol.iterator](){yield this.x,yield this.y,yield this.z}},$a=new O,kh=new ti,Ci=class{constructor(t=new O(1/0,1/0,1/0),e=new O(-1/0,-1/0,-1/0)){this.isBox3=!0,this.min=t,this.max=e}set(t,e){return this.min.copy(t),this.max.copy(e),this}setFromArray(t){this.makeEmpty();for(let e=0,n=t.length;e<n;e+=3)this.expandByPoint(Jn.fromArray(t,e));return this}setFromBufferAttribute(t){this.makeEmpty();for(let e=0,n=t.count;e<n;e++)this.expandByPoint(Jn.fromBufferAttribute(t,e));return this}setFromPoints(t){this.makeEmpty();for(let e=0,n=t.length;e<n;e++)this.expandByPoint(t[e]);return this}setFromCenterAndSize(t,e){let n=Jn.copy(e).multiplyScalar(.5);return this.min.copy(t).sub(n),this.max.copy(t).add(n),this}setFromObject(t,e=!1){return this.makeEmpty(),this.expandByObject(t,e)}clone(){return new this.constructor().copy(this)}copy(t){return this.min.copy(t.min),this.max.copy(t.max),this}makeEmpty(){return this.min.x=this.min.y=this.min.z=1/0,this.max.x=this.max.y=this.max.z=-1/0,this}isEmpty(){return this.max.x<this.min.x||this.max.y<this.min.y||this.max.z<this.min.z}getCenter(t){return this.isEmpty()?t.set(0,0,0):t.addVectors(this.min,this.max).multiplyScalar(.5)}getSize(t){return this.isEmpty()?t.set(0,0,0):t.subVectors(this.max,this.min)}expandByPoint(t){return this.min.min(t),this.max.max(t),this}expandByVector(t){return this.min.sub(t),this.max.add(t),this}expandByScalar(t){return this.min.addScalar(-t),this.max.addScalar(t),this}expandByObject(t,e=!1){t.updateWorldMatrix(!1,!1);let n=t.geometry;if(n!==void 0){let r=n.getAttribute("position");if(e===!0&&r!==void 0&&t.isInstancedMesh!==!0)for(let a=0,o=r.count;a<o;a++)t.isMesh===!0?t.getVertexPosition(a,Jn):Jn.fromBufferAttribute(r,a),Jn.applyMatrix4(t.matrixWorld),this.expandByPoint(Jn);else t.boundingBox!==void 0?(t.boundingBox===null&&t.computeBoundingBox(),lo.copy(t.boundingBox)):(n.boundingBox===null&&n.computeBoundingBox(),lo.copy(n.boundingBox)),lo.applyMatrix4(t.matrixWorld),this.union(lo)}let s=t.children;for(let r=0,a=s.length;r<a;r++)this.expandByObject(s[r],e);return this}containsPoint(t){return!(t.x<this.min.x||t.x>this.max.x||t.y<this.min.y||t.y>this.max.y||t.z<this.min.z||t.z>this.max.z)}containsBox(t){return this.min.x<=t.min.x&&t.max.x<=this.max.x&&this.min.y<=t.min.y&&t.max.y<=this.max.y&&this.min.z<=t.min.z&&t.max.z<=this.max.z}getParameter(t,e){return e.set((t.x-this.min.x)/(this.max.x-this.min.x),(t.y-this.min.y)/(this.max.y-this.min.y),(t.z-this.min.z)/(this.max.z-this.min.z))}intersectsBox(t){return!(t.max.x<this.min.x||t.min.x>this.max.x||t.max.y<this.min.y||t.min.y>this.max.y||t.max.z<this.min.z||t.min.z>this.max.z)}intersectsSphere(t){return this.clampPoint(t.center,Jn),Jn.distanceToSquared(t.center)<=t.radius*t.radius}intersectsPlane(t){let e,n;return t.normal.x>0?(e=t.normal.x*this.min.x,n=t.normal.x*this.max.x):(e=t.normal.x*this.max.x,n=t.normal.x*this.min.x),t.normal.y>0?(e+=t.normal.y*this.min.y,n+=t.normal.y*this.max.y):(e+=t.normal.y*this.max.y,n+=t.normal.y*this.min.y),t.normal.z>0?(e+=t.normal.z*this.min.z,n+=t.normal.z*this.max.z):(e+=t.normal.z*this.max.z,n+=t.normal.z*this.min.z),e<=-t.constant&&n>=-t.constant}intersectsTriangle(t){if(this.isEmpty())return!1;this.getCenter(mr),co.subVectors(this.max,mr),Rs.subVectors(t.a,mr),Cs.subVectors(t.b,mr),Ps.subVectors(t.c,mr),Fi.subVectors(Cs,Rs),Oi.subVectors(Ps,Cs),ss.subVectors(Rs,Ps);let e=[0,-Fi.z,Fi.y,0,-Oi.z,Oi.y,0,-ss.z,ss.y,Fi.z,0,-Fi.x,Oi.z,0,-Oi.x,ss.z,0,-ss.x,-Fi.y,Fi.x,0,-Oi.y,Oi.x,0,-ss.y,ss.x,0];return!Ja(e,Rs,Cs,Ps,co)||(e=[1,0,0,0,1,0,0,0,1],!Ja(e,Rs,Cs,Ps,co))?!1:(ho.crossVectors(Fi,Oi),e=[ho.x,ho.y,ho.z],Ja(e,Rs,Cs,Ps,co))}clampPoint(t,e){return e.copy(t).clamp(this.min,this.max)}distanceToPoint(t){return this.clampPoint(t,Jn).distanceTo(t)}getBoundingSphere(t){return this.isEmpty()?t.makeEmpty():(this.getCenter(t.center),t.radius=this.getSize(Jn).length()*.5),t}intersect(t){return this.min.max(t.min),this.max.min(t.max),this.isEmpty()&&this.makeEmpty(),this}union(t){return this.min.min(t.min),this.max.max(t.max),this}applyMatrix4(t){return this.isEmpty()?this:(vi[0].set(this.min.x,this.min.y,this.min.z).applyMatrix4(t),vi[1].set(this.min.x,this.min.y,this.max.z).applyMatrix4(t),vi[2].set(this.min.x,this.max.y,this.min.z).applyMatrix4(t),vi[3].set(this.min.x,this.max.y,this.max.z).applyMatrix4(t),vi[4].set(this.max.x,this.min.y,this.min.z).applyMatrix4(t),vi[5].set(this.max.x,this.min.y,this.max.z).applyMatrix4(t),vi[6].set(this.max.x,this.max.y,this.min.z).applyMatrix4(t),vi[7].set(this.max.x,this.max.y,this.max.z).applyMatrix4(t),this.setFromPoints(vi),this)}translate(t){return this.min.add(t),this.max.add(t),this}equals(t){return t.min.equals(this.min)&&t.max.equals(this.max)}},vi=[new O,new O,new O,new O,new O,new O,new O,new O],Jn=new O,lo=new Ci,Rs=new O,Cs=new O,Ps=new O,Fi=new O,Oi=new O,ss=new O,mr=new O,co=new O,ho=new O,rs=new O;function Ja(i,t,e,n,s){for(let r=0,a=i.length-3;r<=a;r+=3){rs.fromArray(i,r);let o=s.x*Math.abs(rs.x)+s.y*Math.abs(rs.y)+s.z*Math.abs(rs.z),l=t.dot(rs),c=e.dot(rs),h=n.dot(rs);if(Math.max(-Math.max(l,c,h),Math.min(l,c,h))>o)return!1}return!0}var Fd=new Ci,gr=new O,Ka=new O,Zi=class{constructor(t=new O,e=-1){this.isSphere=!0,this.center=t,this.radius=e}set(t,e){return this.center.copy(t),this.radius=e,this}setFromPoints(t,e){let n=this.center;e!==void 0?n.copy(e):Fd.setFromPoints(t).getCenter(n);let s=0;for(let r=0,a=t.length;r<a;r++)s=Math.max(s,n.distanceToSquared(t[r]));return this.radius=Math.sqrt(s),this}copy(t){return this.center.copy(t.center),this.radius=t.radius,this}isEmpty(){return this.radius<0}makeEmpty(){return this.center.set(0,0,0),this.radius=-1,this}containsPoint(t){return t.distanceToSquared(this.center)<=this.radius*this.radius}distanceToPoint(t){return t.distanceTo(this.center)-this.radius}intersectsSphere(t){let e=this.radius+t.radius;return t.center.distanceToSquared(this.center)<=e*e}intersectsBox(t){return t.intersectsSphere(this)}intersectsPlane(t){return Math.abs(t.distanceToPoint(this.center))<=this.radius}clampPoint(t,e){let n=this.center.distanceToSquared(t);return e.copy(t),n>this.radius*this.radius&&(e.sub(this.center).normalize(),e.multiplyScalar(this.radius).add(this.center)),e}getBoundingBox(t){return this.isEmpty()?(t.makeEmpty(),t):(t.set(this.center,this.center),t.expandByScalar(this.radius),t)}applyMatrix4(t){return this.center.applyMatrix4(t),this.radius=this.radius*t.getMaxScaleOnAxis(),this}translate(t){return this.center.add(t),this}expandByPoint(t){if(this.isEmpty())return this.center.copy(t),this.radius=0,this;gr.subVectors(t,this.center);let e=gr.lengthSq();if(e>this.radius*this.radius){let n=Math.sqrt(e),s=(n-this.radius)*.5;this.center.addScaledVector(gr,s/n),this.radius+=s}return this}union(t){return t.isEmpty()?this:this.isEmpty()?(this.copy(t),this):(this.center.equals(t.center)===!0?this.radius=Math.max(this.radius,t.radius):(Ka.subVectors(t.center,this.center).setLength(t.radius),this.expandByPoint(gr.copy(t.center).add(Ka)),this.expandByPoint(gr.copy(t.center).sub(Ka))),this)}equals(t){return t.center.equals(this.center)&&t.radius===this.radius}clone(){return new this.constructor().copy(this)}},yi=new O,ja=new O,uo=new O,Bi=new O,Qa=new O,fo=new O,tl=new O,Ur=class{constructor(t=new O,e=new O(0,0,-1)){this.origin=t,this.direction=e}set(t,e){return this.origin.copy(t),this.direction.copy(e),this}copy(t){return this.origin.copy(t.origin),this.direction.copy(t.direction),this}at(t,e){return e.copy(this.origin).addScaledVector(this.direction,t)}lookAt(t){return this.direction.copy(t).sub(this.origin).normalize(),this}recast(t){return this.origin.copy(this.at(t,yi)),this}closestPointToPoint(t,e){e.subVectors(t,this.origin);let n=e.dot(this.direction);return n<0?e.copy(this.origin):e.copy(this.origin).addScaledVector(this.direction,n)}distanceToPoint(t){return Math.sqrt(this.distanceSqToPoint(t))}distanceSqToPoint(t){let e=yi.subVectors(t,this.origin).dot(this.direction);return e<0?this.origin.distanceToSquared(t):(yi.copy(this.origin).addScaledVector(this.direction,e),yi.distanceToSquared(t))}distanceSqToSegment(t,e,n,s){ja.copy(t).add(e).multiplyScalar(.5),uo.copy(e).sub(t).normalize(),Bi.copy(this.origin).sub(ja);let r=t.distanceTo(e)*.5,a=-this.direction.dot(uo),o=Bi.dot(this.direction),l=-Bi.dot(uo),c=Bi.lengthSq(),h=Math.abs(1-a*a),u,d,p,x;if(h>0)if(u=a*l-o,d=a*o-l,x=r*h,u>=0)if(d>=-x)if(d<=x){let y=1/h;u*=y,d*=y,p=u*(u+a*d+2*o)+d*(a*u+d+2*l)+c}else d=r,u=Math.max(0,-(a*d+o)),p=-u*u+d*(d+2*l)+c;else d=-r,u=Math.max(0,-(a*d+o)),p=-u*u+d*(d+2*l)+c;else d<=-x?(u=Math.max(0,-(-a*r+o)),d=u>0?-r:Math.min(Math.max(-r,-l),r),p=-u*u+d*(d+2*l)+c):d<=x?(u=0,d=Math.min(Math.max(-r,-l),r),p=d*(d+2*l)+c):(u=Math.max(0,-(a*r+o)),d=u>0?r:Math.min(Math.max(-r,-l),r),p=-u*u+d*(d+2*l)+c);else d=a>0?-r:r,u=Math.max(0,-(a*d+o)),p=-u*u+d*(d+2*l)+c;return n&&n.copy(this.origin).addScaledVector(this.direction,u),s&&s.copy(ja).addScaledVector(uo,d),p}intersectSphere(t,e){yi.subVectors(t.center,this.origin);let n=yi.dot(this.direction),s=yi.dot(yi)-n*n,r=t.radius*t.radius;if(s>r)return null;let a=Math.sqrt(r-s),o=n-a,l=n+a;return l<0?null:o<0?this.at(l,e):this.at(o,e)}intersectsSphere(t){return this.distanceSqToPoint(t.center)<=t.radius*t.radius}distanceToPlane(t){let e=t.normal.dot(this.direction);if(e===0)return t.distanceToPoint(this.origin)===0?0:null;let n=-(this.origin.dot(t.normal)+t.constant)/e;return n>=0?n:null}intersectPlane(t,e){let n=this.distanceToPlane(t);return n===null?null:this.at(n,e)}intersectsPlane(t){let e=t.distanceToPoint(this.origin);return e===0||t.normal.dot(this.direction)*e<0}intersectBox(t,e){let n,s,r,a,o,l,c=1/this.direction.x,h=1/this.direction.y,u=1/this.direction.z,d=this.origin;return c>=0?(n=(t.min.x-d.x)*c,s=(t.max.x-d.x)*c):(n=(t.max.x-d.x)*c,s=(t.min.x-d.x)*c),h>=0?(r=(t.min.y-d.y)*h,a=(t.max.y-d.y)*h):(r=(t.max.y-d.y)*h,a=(t.min.y-d.y)*h),n>a||r>s||((r>n||isNaN(n))&&(n=r),(a<s||isNaN(s))&&(s=a),u>=0?(o=(t.min.z-d.z)*u,l=(t.max.z-d.z)*u):(o=(t.max.z-d.z)*u,l=(t.min.z-d.z)*u),n>l||o>s)||((o>n||n!==n)&&(n=o),(l<s||s!==s)&&(s=l),s<0)?null:this.at(n>=0?n:s,e)}intersectsBox(t){return this.intersectBox(t,yi)!==null}intersectTriangle(t,e,n,s,r){Qa.subVectors(e,t),fo.subVectors(n,t),tl.crossVectors(Qa,fo);let a=this.direction.dot(tl),o;if(a>0){if(s)return null;o=1}else if(a<0)o=-1,a=-a;else return null;Bi.subVectors(this.origin,t);let l=o*this.direction.dot(fo.crossVectors(Bi,fo));if(l<0)return null;let c=o*this.direction.dot(Qa.cross(Bi));if(c<0||l+c>a)return null;let h=-o*Bi.dot(tl);return h<0?null:this.at(h/a,r)}applyMatrix4(t){return this.origin.applyMatrix4(t),this.direction.transformDirection(t),this}equals(t){return t.origin.equals(this.origin)&&t.direction.equals(this.direction)}clone(){return new this.constructor().copy(this)}},De=class i{constructor(t,e,n,s,r,a,o,l,c,h,u,d,p,x,y,g){i.prototype.isMatrix4=!0,this.elements=[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],t!==void 0&&this.set(t,e,n,s,r,a,o,l,c,h,u,d,p,x,y,g)}set(t,e,n,s,r,a,o,l,c,h,u,d,p,x,y,g){let m=this.elements;return m[0]=t,m[4]=e,m[8]=n,m[12]=s,m[1]=r,m[5]=a,m[9]=o,m[13]=l,m[2]=c,m[6]=h,m[10]=u,m[14]=d,m[3]=p,m[7]=x,m[11]=y,m[15]=g,this}identity(){return this.set(1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1),this}clone(){return new i().fromArray(this.elements)}copy(t){let e=this.elements,n=t.elements;return e[0]=n[0],e[1]=n[1],e[2]=n[2],e[3]=n[3],e[4]=n[4],e[5]=n[5],e[6]=n[6],e[7]=n[7],e[8]=n[8],e[9]=n[9],e[10]=n[10],e[11]=n[11],e[12]=n[12],e[13]=n[13],e[14]=n[14],e[15]=n[15],this}copyPosition(t){let e=this.elements,n=t.elements;return e[12]=n[12],e[13]=n[13],e[14]=n[14],this}setFromMatrix3(t){let e=t.elements;return this.set(e[0],e[3],e[6],0,e[1],e[4],e[7],0,e[2],e[5],e[8],0,0,0,0,1),this}extractBasis(t,e,n){return t.setFromMatrixColumn(this,0),e.setFromMatrixColumn(this,1),n.setFromMatrixColumn(this,2),this}makeBasis(t,e,n){return this.set(t.x,e.x,n.x,0,t.y,e.y,n.y,0,t.z,e.z,n.z,0,0,0,0,1),this}extractRotation(t){let e=this.elements,n=t.elements,s=1/Is.setFromMatrixColumn(t,0).length(),r=1/Is.setFromMatrixColumn(t,1).length(),a=1/Is.setFromMatrixColumn(t,2).length();return e[0]=n[0]*s,e[1]=n[1]*s,e[2]=n[2]*s,e[3]=0,e[4]=n[4]*r,e[5]=n[5]*r,e[6]=n[6]*r,e[7]=0,e[8]=n[8]*a,e[9]=n[9]*a,e[10]=n[10]*a,e[11]=0,e[12]=0,e[13]=0,e[14]=0,e[15]=1,this}makeRotationFromEuler(t){let e=this.elements,n=t.x,s=t.y,r=t.z,a=Math.cos(n),o=Math.sin(n),l=Math.cos(s),c=Math.sin(s),h=Math.cos(r),u=Math.sin(r);if(t.order==="XYZ"){let d=a*h,p=a*u,x=o*h,y=o*u;e[0]=l*h,e[4]=-l*u,e[8]=c,e[1]=p+x*c,e[5]=d-y*c,e[9]=-o*l,e[2]=y-d*c,e[6]=x+p*c,e[10]=a*l}else if(t.order==="YXZ"){let d=l*h,p=l*u,x=c*h,y=c*u;e[0]=d+y*o,e[4]=x*o-p,e[8]=a*c,e[1]=a*u,e[5]=a*h,e[9]=-o,e[2]=p*o-x,e[6]=y+d*o,e[10]=a*l}else if(t.order==="ZXY"){let d=l*h,p=l*u,x=c*h,y=c*u;e[0]=d-y*o,e[4]=-a*u,e[8]=x+p*o,e[1]=p+x*o,e[5]=a*h,e[9]=y-d*o,e[2]=-a*c,e[6]=o,e[10]=a*l}else if(t.order==="ZYX"){let d=a*h,p=a*u,x=o*h,y=o*u;e[0]=l*h,e[4]=x*c-p,e[8]=d*c+y,e[1]=l*u,e[5]=y*c+d,e[9]=p*c-x,e[2]=-c,e[6]=o*l,e[10]=a*l}else if(t.order==="YZX"){let d=a*l,p=a*c,x=o*l,y=o*c;e[0]=l*h,e[4]=y-d*u,e[8]=x*u+p,e[1]=u,e[5]=a*h,e[9]=-o*h,e[2]=-c*h,e[6]=p*u+x,e[10]=d-y*u}else if(t.order==="XZY"){let d=a*l,p=a*c,x=o*l,y=o*c;e[0]=l*h,e[4]=-u,e[8]=c*h,e[1]=d*u+y,e[5]=a*h,e[9]=p*u-x,e[2]=x*u-p,e[6]=o*h,e[10]=y*u+d}return e[3]=0,e[7]=0,e[11]=0,e[12]=0,e[13]=0,e[14]=0,e[15]=1,this}makeRotationFromQuaternion(t){return this.compose(Od,t,Bd)}lookAt(t,e,n){let s=this.elements;return Ln.subVectors(t,e),Ln.lengthSq()===0&&(Ln.z=1),Ln.normalize(),zi.crossVectors(n,Ln),zi.lengthSq()===0&&(Math.abs(n.z)===1?Ln.x+=1e-4:Ln.z+=1e-4,Ln.normalize(),zi.crossVectors(n,Ln)),zi.normalize(),po.crossVectors(Ln,zi),s[0]=zi.x,s[4]=po.x,s[8]=Ln.x,s[1]=zi.y,s[5]=po.y,s[9]=Ln.y,s[2]=zi.z,s[6]=po.z,s[10]=Ln.z,this}multiply(t){return this.multiplyMatrices(this,t)}premultiply(t){return this.multiplyMatrices(t,this)}multiplyMatrices(t,e){let n=t.elements,s=e.elements,r=this.elements,a=n[0],o=n[4],l=n[8],c=n[12],h=n[1],u=n[5],d=n[9],p=n[13],x=n[2],y=n[6],g=n[10],m=n[14],w=n[3],v=n[7],I=n[11],H=n[15],U=s[0],N=s[4],Y=s[8],b=s[12],P=s[1],X=s[5],rt=s[9],_t=s[13],k=s[2],q=s[6],j=s[10],et=s[14],ut=s[3],tt=s[7],at=s[11],lt=s[15];return r[0]=a*U+o*P+l*k+c*ut,r[4]=a*N+o*X+l*q+c*tt,r[8]=a*Y+o*rt+l*j+c*at,r[12]=a*b+o*_t+l*et+c*lt,r[1]=h*U+u*P+d*k+p*ut,r[5]=h*N+u*X+d*q+p*tt,r[9]=h*Y+u*rt+d*j+p*at,r[13]=h*b+u*_t+d*et+p*lt,r[2]=x*U+y*P+g*k+m*ut,r[6]=x*N+y*X+g*q+m*tt,r[10]=x*Y+y*rt+g*j+m*at,r[14]=x*b+y*_t+g*et+m*lt,r[3]=w*U+v*P+I*k+H*ut,r[7]=w*N+v*X+I*q+H*tt,r[11]=w*Y+v*rt+I*j+H*at,r[15]=w*b+v*_t+I*et+H*lt,this}multiplyScalar(t){let e=this.elements;return e[0]*=t,e[4]*=t,e[8]*=t,e[12]*=t,e[1]*=t,e[5]*=t,e[9]*=t,e[13]*=t,e[2]*=t,e[6]*=t,e[10]*=t,e[14]*=t,e[3]*=t,e[7]*=t,e[11]*=t,e[15]*=t,this}determinant(){let t=this.elements,e=t[0],n=t[4],s=t[8],r=t[12],a=t[1],o=t[5],l=t[9],c=t[13],h=t[2],u=t[6],d=t[10],p=t[14],x=t[3],y=t[7],g=t[11],m=t[15];return x*(+r*l*u-s*c*u-r*o*d+n*c*d+s*o*p-n*l*p)+y*(+e*l*p-e*c*d+r*a*d-s*a*p+s*c*h-r*l*h)+g*(+e*c*u-e*o*p-r*a*u+n*a*p+r*o*h-n*c*h)+m*(-s*o*h-e*l*u+e*o*d+s*a*u-n*a*d+n*l*h)}transpose(){let t=this.elements,e;return e=t[1],t[1]=t[4],t[4]=e,e=t[2],t[2]=t[8],t[8]=e,e=t[6],t[6]=t[9],t[9]=e,e=t[3],t[3]=t[12],t[12]=e,e=t[7],t[7]=t[13],t[13]=e,e=t[11],t[11]=t[14],t[14]=e,this}setPosition(t,e,n){let s=this.elements;return t.isVector3?(s[12]=t.x,s[13]=t.y,s[14]=t.z):(s[12]=t,s[13]=e,s[14]=n),this}invert(){let t=this.elements,e=t[0],n=t[1],s=t[2],r=t[3],a=t[4],o=t[5],l=t[6],c=t[7],h=t[8],u=t[9],d=t[10],p=t[11],x=t[12],y=t[13],g=t[14],m=t[15],w=u*g*c-y*d*c+y*l*p-o*g*p-u*l*m+o*d*m,v=x*d*c-h*g*c-x*l*p+a*g*p+h*l*m-a*d*m,I=h*y*c-x*u*c+x*o*p-a*y*p-h*o*m+a*u*m,H=x*u*l-h*y*l-x*o*d+a*y*d+h*o*g-a*u*g,U=e*w+n*v+s*I+r*H;if(U===0)return this.set(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);let N=1/U;return t[0]=w*N,t[1]=(y*d*r-u*g*r-y*s*p+n*g*p+u*s*m-n*d*m)*N,t[2]=(o*g*r-y*l*r+y*s*c-n*g*c-o*s*m+n*l*m)*N,t[3]=(u*l*r-o*d*r-u*s*c+n*d*c+o*s*p-n*l*p)*N,t[4]=v*N,t[5]=(h*g*r-x*d*r+x*s*p-e*g*p-h*s*m+e*d*m)*N,t[6]=(x*l*r-a*g*r-x*s*c+e*g*c+a*s*m-e*l*m)*N,t[7]=(a*d*r-h*l*r+h*s*c-e*d*c-a*s*p+e*l*p)*N,t[8]=I*N,t[9]=(x*u*r-h*y*r-x*n*p+e*y*p+h*n*m-e*u*m)*N,t[10]=(a*y*r-x*o*r+x*n*c-e*y*c-a*n*m+e*o*m)*N,t[11]=(h*o*r-a*u*r-h*n*c+e*u*c+a*n*p-e*o*p)*N,t[12]=H*N,t[13]=(h*y*s-x*u*s+x*n*d-e*y*d-h*n*g+e*u*g)*N,t[14]=(x*o*s-a*y*s-x*n*l+e*y*l+a*n*g-e*o*g)*N,t[15]=(a*u*s-h*o*s+h*n*l-e*u*l-a*n*d+e*o*d)*N,this}scale(t){let e=this.elements,n=t.x,s=t.y,r=t.z;return e[0]*=n,e[4]*=s,e[8]*=r,e[1]*=n,e[5]*=s,e[9]*=r,e[2]*=n,e[6]*=s,e[10]*=r,e[3]*=n,e[7]*=s,e[11]*=r,this}getMaxScaleOnAxis(){let t=this.elements,e=t[0]*t[0]+t[1]*t[1]+t[2]*t[2],n=t[4]*t[4]+t[5]*t[5]+t[6]*t[6],s=t[8]*t[8]+t[9]*t[9]+t[10]*t[10];return Math.sqrt(Math.max(e,n,s))}makeTranslation(t,e,n){return t.isVector3?this.set(1,0,0,t.x,0,1,0,t.y,0,0,1,t.z,0,0,0,1):this.set(1,0,0,t,0,1,0,e,0,0,1,n,0,0,0,1),this}makeRotationX(t){let e=Math.cos(t),n=Math.sin(t);return this.set(1,0,0,0,0,e,-n,0,0,n,e,0,0,0,0,1),this}makeRotationY(t){let e=Math.cos(t),n=Math.sin(t);return this.set(e,0,n,0,0,1,0,0,-n,0,e,0,0,0,0,1),this}makeRotationZ(t){let e=Math.cos(t),n=Math.sin(t);return this.set(e,-n,0,0,n,e,0,0,0,0,1,0,0,0,0,1),this}makeRotationAxis(t,e){let n=Math.cos(e),s=Math.sin(e),r=1-n,a=t.x,o=t.y,l=t.z,c=r*a,h=r*o;return this.set(c*a+n,c*o-s*l,c*l+s*o,0,c*o+s*l,h*o+n,h*l-s*a,0,c*l-s*o,h*l+s*a,r*l*l+n,0,0,0,0,1),this}makeScale(t,e,n){return this.set(t,0,0,0,0,e,0,0,0,0,n,0,0,0,0,1),this}makeShear(t,e,n,s,r,a){return this.set(1,n,r,0,t,1,a,0,e,s,1,0,0,0,0,1),this}compose(t,e,n){let s=this.elements,r=e._x,a=e._y,o=e._z,l=e._w,c=r+r,h=a+a,u=o+o,d=r*c,p=r*h,x=r*u,y=a*h,g=a*u,m=o*u,w=l*c,v=l*h,I=l*u,H=n.x,U=n.y,N=n.z;return s[0]=(1-(y+m))*H,s[1]=(p+I)*H,s[2]=(x-v)*H,s[3]=0,s[4]=(p-I)*U,s[5]=(1-(d+m))*U,s[6]=(g+w)*U,s[7]=0,s[8]=(x+v)*N,s[9]=(g-w)*N,s[10]=(1-(d+y))*N,s[11]=0,s[12]=t.x,s[13]=t.y,s[14]=t.z,s[15]=1,this}decompose(t,e,n){let s=this.elements,r=Is.set(s[0],s[1],s[2]).length(),a=Is.set(s[4],s[5],s[6]).length(),o=Is.set(s[8],s[9],s[10]).length();this.determinant()<0&&(r=-r),t.x=s[12],t.y=s[13],t.z=s[14],Kn.copy(this);let c=1/r,h=1/a,u=1/o;return Kn.elements[0]*=c,Kn.elements[1]*=c,Kn.elements[2]*=c,Kn.elements[4]*=h,Kn.elements[5]*=h,Kn.elements[6]*=h,Kn.elements[8]*=u,Kn.elements[9]*=u,Kn.elements[10]*=u,e.setFromRotationMatrix(Kn),n.x=r,n.y=a,n.z=o,this}makePerspective(t,e,n,s,r,a,o=Ti){let l=this.elements,c=2*r/(e-t),h=2*r/(n-s),u=(e+t)/(e-t),d=(n+s)/(n-s),p,x;if(o===Ti)p=-(a+r)/(a-r),x=-2*a*r/(a-r);else if(o===Go)p=-a/(a-r),x=-a*r/(a-r);else throw new Error("THREE.Matrix4.makePerspective(): Invalid coordinate system: "+o);return l[0]=c,l[4]=0,l[8]=u,l[12]=0,l[1]=0,l[5]=h,l[9]=d,l[13]=0,l[2]=0,l[6]=0,l[10]=p,l[14]=x,l[3]=0,l[7]=0,l[11]=-1,l[15]=0,this}makeOrthographic(t,e,n,s,r,a,o=Ti){let l=this.elements,c=1/(e-t),h=1/(n-s),u=1/(a-r),d=(e+t)*c,p=(n+s)*h,x,y;if(o===Ti)x=(a+r)*u,y=-2*u;else if(o===Go)x=r*u,y=-1*u;else throw new Error("THREE.Matrix4.makeOrthographic(): Invalid coordinate system: "+o);return l[0]=2*c,l[4]=0,l[8]=0,l[12]=-d,l[1]=0,l[5]=2*h,l[9]=0,l[13]=-p,l[2]=0,l[6]=0,l[10]=y,l[14]=-x,l[3]=0,l[7]=0,l[11]=0,l[15]=1,this}equals(t){let e=this.elements,n=t.elements;for(let s=0;s<16;s++)if(e[s]!==n[s])return!1;return!0}fromArray(t,e=0){for(let n=0;n<16;n++)this.elements[n]=t[n+e];return this}toArray(t=[],e=0){let n=this.elements;return t[e]=n[0],t[e+1]=n[1],t[e+2]=n[2],t[e+3]=n[3],t[e+4]=n[4],t[e+5]=n[5],t[e+6]=n[6],t[e+7]=n[7],t[e+8]=n[8],t[e+9]=n[9],t[e+10]=n[10],t[e+11]=n[11],t[e+12]=n[12],t[e+13]=n[13],t[e+14]=n[14],t[e+15]=n[15],t}},Is=new O,Kn=new De,Od=new O(0,0,0),Bd=new O(1,1,1),zi=new O,po=new O,Ln=new O,Vh=new De,Gh=new ti,ms=class i{constructor(t=0,e=0,n=0,s=i.DEFAULT_ORDER){this.isEuler=!0,this._x=t,this._y=e,this._z=n,this._order=s}get x(){return this._x}set x(t){this._x=t,this._onChangeCallback()}get y(){return this._y}set y(t){this._y=t,this._onChangeCallback()}get z(){return this._z}set z(t){this._z=t,this._onChangeCallback()}get order(){return this._order}set order(t){this._order=t,this._onChangeCallback()}set(t,e,n,s=this._order){return this._x=t,this._y=e,this._z=n,this._order=s,this._onChangeCallback(),this}clone(){return new this.constructor(this._x,this._y,this._z,this._order)}copy(t){return this._x=t._x,this._y=t._y,this._z=t._z,this._order=t._order,this._onChangeCallback(),this}setFromRotationMatrix(t,e=this._order,n=!0){let s=t.elements,r=s[0],a=s[4],o=s[8],l=s[1],c=s[5],h=s[9],u=s[2],d=s[6],p=s[10];switch(e){case"XYZ":this._y=Math.asin(cn(o,-1,1)),Math.abs(o)<.9999999?(this._x=Math.atan2(-h,p),this._z=Math.atan2(-a,r)):(this._x=Math.atan2(d,c),this._z=0);break;case"YXZ":this._x=Math.asin(-cn(h,-1,1)),Math.abs(h)<.9999999?(this._y=Math.atan2(o,p),this._z=Math.atan2(l,c)):(this._y=Math.atan2(-u,r),this._z=0);break;case"ZXY":this._x=Math.asin(cn(d,-1,1)),Math.abs(d)<.9999999?(this._y=Math.atan2(-u,p),this._z=Math.atan2(-a,c)):(this._y=0,this._z=Math.atan2(l,r));break;case"ZYX":this._y=Math.asin(-cn(u,-1,1)),Math.abs(u)<.9999999?(this._x=Math.atan2(d,p),this._z=Math.atan2(l,r)):(this._x=0,this._z=Math.atan2(-a,c));break;case"YZX":this._z=Math.asin(cn(l,-1,1)),Math.abs(l)<.9999999?(this._x=Math.atan2(-h,c),this._y=Math.atan2(-u,r)):(this._x=0,this._y=Math.atan2(o,p));break;case"XZY":this._z=Math.asin(-cn(a,-1,1)),Math.abs(a)<.9999999?(this._x=Math.atan2(d,c),this._y=Math.atan2(o,r)):(this._x=Math.atan2(-h,p),this._y=0);break;default:console.warn("THREE.Euler: .setFromRotationMatrix() encountered an unknown order: "+e)}return this._order=e,n===!0&&this._onChangeCallback(),this}setFromQuaternion(t,e,n){return Vh.makeRotationFromQuaternion(t),this.setFromRotationMatrix(Vh,e,n)}setFromVector3(t,e=this._order){return this.set(t.x,t.y,t.z,e)}reorder(t){return Gh.setFromEuler(this),this.setFromQuaternion(Gh,t)}equals(t){return t._x===this._x&&t._y===this._y&&t._z===this._z&&t._order===this._order}fromArray(t){return this._x=t[0],this._y=t[1],this._z=t[2],t[3]!==void 0&&(this._order=t[3]),this._onChangeCallback(),this}toArray(t=[],e=0){return t[e]=this._x,t[e+1]=this._y,t[e+2]=this._z,t[e+3]=this._order,t}_onChange(t){return this._onChangeCallback=t,this}_onChangeCallback(){}*[Symbol.iterator](){yield this._x,yield this._y,yield this._z,yield this._order}};ms.DEFAULT_ORDER="XYZ";var Dr=class{constructor(){this.mask=1}set(t){this.mask=(1<<t|0)>>>0}enable(t){this.mask|=1<<t|0}enableAll(){this.mask=-1}toggle(t){this.mask^=1<<t|0}disable(t){this.mask&=~(1<<t|0)}disableAll(){this.mask=0}test(t){return(this.mask&t.mask)!==0}isEnabled(t){return(this.mask&(1<<t|0))!==0}},zd=0,Wh=new O,Ls=new ti,Mi=new De,mo=new O,_r=new O,Hd=new O,kd=new ti,Xh=new O(1,0,0),Yh=new O(0,1,0),qh=new O(0,0,1),Vd={type:"added"},Gd={type:"removed"},bn=class i extends qi{constructor(){super(),this.isObject3D=!0,Object.defineProperty(this,"id",{value:zd++}),this.uuid=ys(),this.name="",this.type="Object3D",this.parent=null,this.children=[],this.up=i.DEFAULT_UP.clone();let t=new O,e=new ms,n=new ti,s=new O(1,1,1);function r(){n.setFromEuler(e,!1)}function a(){e.setFromQuaternion(n,void 0,!1)}e._onChange(r),n._onChange(a),Object.defineProperties(this,{position:{configurable:!0,enumerable:!0,value:t},rotation:{configurable:!0,enumerable:!0,value:e},quaternion:{configurable:!0,enumerable:!0,value:n},scale:{configurable:!0,enumerable:!0,value:s},modelViewMatrix:{value:new De},normalMatrix:{value:new ve}}),this.matrix=new De,this.matrixWorld=new De,this.matrixAutoUpdate=i.DEFAULT_MATRIX_AUTO_UPDATE,this.matrixWorldAutoUpdate=i.DEFAULT_MATRIX_WORLD_AUTO_UPDATE,this.matrixWorldNeedsUpdate=!1,this.layers=new Dr,this.visible=!0,this.castShadow=!1,this.receiveShadow=!1,this.frustumCulled=!0,this.renderOrder=0,this.animations=[],this.userData={}}onBeforeShadow(){}onAfterShadow(){}onBeforeRender(){}onAfterRender(){}applyMatrix4(t){this.matrixAutoUpdate&&this.updateMatrix(),this.matrix.premultiply(t),this.matrix.decompose(this.position,this.quaternion,this.scale)}applyQuaternion(t){return this.quaternion.premultiply(t),this}setRotationFromAxisAngle(t,e){this.quaternion.setFromAxisAngle(t,e)}setRotationFromEuler(t){this.quaternion.setFromEuler(t,!0)}setRotationFromMatrix(t){this.quaternion.setFromRotationMatrix(t)}setRotationFromQuaternion(t){this.quaternion.copy(t)}rotateOnAxis(t,e){return Ls.setFromAxisAngle(t,e),this.quaternion.multiply(Ls),this}rotateOnWorldAxis(t,e){return Ls.setFromAxisAngle(t,e),this.quaternion.premultiply(Ls),this}rotateX(t){return this.rotateOnAxis(Xh,t)}rotateY(t){return this.rotateOnAxis(Yh,t)}rotateZ(t){return this.rotateOnAxis(qh,t)}translateOnAxis(t,e){return Wh.copy(t).applyQuaternion(this.quaternion),this.position.add(Wh.multiplyScalar(e)),this}translateX(t){return this.translateOnAxis(Xh,t)}translateY(t){return this.translateOnAxis(Yh,t)}translateZ(t){return this.translateOnAxis(qh,t)}localToWorld(t){return this.updateWorldMatrix(!0,!1),t.applyMatrix4(this.matrixWorld)}worldToLocal(t){return this.updateWorldMatrix(!0,!1),t.applyMatrix4(Mi.copy(this.matrixWorld).invert())}lookAt(t,e,n){t.isVector3?mo.copy(t):mo.set(t,e,n);let s=this.parent;this.updateWorldMatrix(!0,!1),_r.setFromMatrixPosition(this.matrixWorld),this.isCamera||this.isLight?Mi.lookAt(_r,mo,this.up):Mi.lookAt(mo,_r,this.up),this.quaternion.setFromRotationMatrix(Mi),s&&(Mi.extractRotation(s.matrixWorld),Ls.setFromRotationMatrix(Mi),this.quaternion.premultiply(Ls.invert()))}add(t){if(arguments.length>1){for(let e=0;e<arguments.length;e++)this.add(arguments[e]);return this}return t===this?(console.error("THREE.Object3D.add: object can't be added as a child of itself.",t),this):(t&&t.isObject3D?(t.parent!==null&&t.parent.remove(t),t.parent=this,this.children.push(t),t.dispatchEvent(Vd)):console.error("THREE.Object3D.add: object not an instance of THREE.Object3D.",t),this)}remove(t){if(arguments.length>1){for(let n=0;n<arguments.length;n++)this.remove(arguments[n]);return this}let e=this.children.indexOf(t);return e!==-1&&(t.parent=null,this.children.splice(e,1),t.dispatchEvent(Gd)),this}removeFromParent(){let t=this.parent;return t!==null&&t.remove(this),this}clear(){return this.remove(...this.children)}attach(t){return this.updateWorldMatrix(!0,!1),Mi.copy(this.matrixWorld).invert(),t.parent!==null&&(t.parent.updateWorldMatrix(!0,!1),Mi.multiply(t.parent.matrixWorld)),t.applyMatrix4(Mi),this.add(t),t.updateWorldMatrix(!1,!0),this}getObjectById(t){return this.getObjectByProperty("id",t)}getObjectByName(t){return this.getObjectByProperty("name",t)}getObjectByProperty(t,e){if(this[t]===e)return this;for(let n=0,s=this.children.length;n<s;n++){let a=this.children[n].getObjectByProperty(t,e);if(a!==void 0)return a}}getObjectsByProperty(t,e,n=[]){this[t]===e&&n.push(this);let s=this.children;for(let r=0,a=s.length;r<a;r++)s[r].getObjectsByProperty(t,e,n);return n}getWorldPosition(t){return this.updateWorldMatrix(!0,!1),t.setFromMatrixPosition(this.matrixWorld)}getWorldQuaternion(t){return this.updateWorldMatrix(!0,!1),this.matrixWorld.decompose(_r,t,Hd),t}getWorldScale(t){return this.updateWorldMatrix(!0,!1),this.matrixWorld.decompose(_r,kd,t),t}getWorldDirection(t){this.updateWorldMatrix(!0,!1);let e=this.matrixWorld.elements;return t.set(e[8],e[9],e[10]).normalize()}raycast(){}traverse(t){t(this);let e=this.children;for(let n=0,s=e.length;n<s;n++)e[n].traverse(t)}traverseVisible(t){if(this.visible===!1)return;t(this);let e=this.children;for(let n=0,s=e.length;n<s;n++)e[n].traverseVisible(t)}traverseAncestors(t){let e=this.parent;e!==null&&(t(e),e.traverseAncestors(t))}updateMatrix(){this.matrix.compose(this.position,this.quaternion,this.scale),this.matrixWorldNeedsUpdate=!0}updateMatrixWorld(t){this.matrixAutoUpdate&&this.updateMatrix(),(this.matrixWorldNeedsUpdate||t)&&(this.parent===null?this.matrixWorld.copy(this.matrix):this.matrixWorld.multiplyMatrices(this.parent.matrixWorld,this.matrix),this.matrixWorldNeedsUpdate=!1,t=!0);let e=this.children;for(let n=0,s=e.length;n<s;n++){let r=e[n];(r.matrixWorldAutoUpdate===!0||t===!0)&&r.updateMatrixWorld(t)}}updateWorldMatrix(t,e){let n=this.parent;if(t===!0&&n!==null&&n.matrixWorldAutoUpdate===!0&&n.updateWorldMatrix(!0,!1),this.matrixAutoUpdate&&this.updateMatrix(),this.parent===null?this.matrixWorld.copy(this.matrix):this.matrixWorld.multiplyMatrices(this.parent.matrixWorld,this.matrix),e===!0){let s=this.children;for(let r=0,a=s.length;r<a;r++){let o=s[r];o.matrixWorldAutoUpdate===!0&&o.updateWorldMatrix(!1,!0)}}}toJSON(t){let e=t===void 0||typeof t=="string",n={};e&&(t={geometries:{},materials:{},textures:{},images:{},shapes:{},skeletons:{},animations:{},nodes:{}},n.metadata={version:4.6,type:"Object",generator:"Object3D.toJSON"});let s={};s.uuid=this.uuid,s.type=this.type,this.name!==""&&(s.name=this.name),this.castShadow===!0&&(s.castShadow=!0),this.receiveShadow===!0&&(s.receiveShadow=!0),this.visible===!1&&(s.visible=!1),this.frustumCulled===!1&&(s.frustumCulled=!1),this.renderOrder!==0&&(s.renderOrder=this.renderOrder),Object.keys(this.userData).length>0&&(s.userData=this.userData),s.layers=this.layers.mask,s.matrix=this.matrix.toArray(),s.up=this.up.toArray(),this.matrixAutoUpdate===!1&&(s.matrixAutoUpdate=!1),this.isInstancedMesh&&(s.type="InstancedMesh",s.count=this.count,s.instanceMatrix=this.instanceMatrix.toJSON(),this.instanceColor!==null&&(s.instanceColor=this.instanceColor.toJSON())),this.isBatchedMesh&&(s.type="BatchedMesh",s.perObjectFrustumCulled=this.perObjectFrustumCulled,s.sortObjects=this.sortObjects,s.drawRanges=this._drawRanges,s.reservedRanges=this._reservedRanges,s.visibility=this._visibility,s.active=this._active,s.bounds=this._bounds.map(o=>({boxInitialized:o.boxInitialized,boxMin:o.box.min.toArray(),boxMax:o.box.max.toArray(),sphereInitialized:o.sphereInitialized,sphereRadius:o.sphere.radius,sphereCenter:o.sphere.center.toArray()})),s.maxGeometryCount=this._maxGeometryCount,s.maxVertexCount=this._maxVertexCount,s.maxIndexCount=this._maxIndexCount,s.geometryInitialized=this._geometryInitialized,s.geometryCount=this._geometryCount,s.matricesTexture=this._matricesTexture.toJSON(t),this.boundingSphere!==null&&(s.boundingSphere={center:s.boundingSphere.center.toArray(),radius:s.boundingSphere.radius}),this.boundingBox!==null&&(s.boundingBox={min:s.boundingBox.min.toArray(),max:s.boundingBox.max.toArray()}));function r(o,l){return o[l.uuid]===void 0&&(o[l.uuid]=l.toJSON(t)),l.uuid}if(this.isScene)this.background&&(this.background.isColor?s.background=this.background.toJSON():this.background.isTexture&&(s.background=this.background.toJSON(t).uuid)),this.environment&&this.environment.isTexture&&this.environment.isRenderTargetTexture!==!0&&(s.environment=this.environment.toJSON(t).uuid);else if(this.isMesh||this.isLine||this.isPoints){s.geometry=r(t.geometries,this.geometry);let o=this.geometry.parameters;if(o!==void 0&&o.shapes!==void 0){let l=o.shapes;if(Array.isArray(l))for(let c=0,h=l.length;c<h;c++){let u=l[c];r(t.shapes,u)}else r(t.shapes,l)}}if(this.isSkinnedMesh&&(s.bindMode=this.bindMode,s.bindMatrix=this.bindMatrix.toArray(),this.skeleton!==void 0&&(r(t.skeletons,this.skeleton),s.skeleton=this.skeleton.uuid)),this.material!==void 0)if(Array.isArray(this.material)){let o=[];for(let l=0,c=this.material.length;l<c;l++)o.push(r(t.materials,this.material[l]));s.material=o}else s.material=r(t.materials,this.material);if(this.children.length>0){s.children=[];for(let o=0;o<this.children.length;o++)s.children.push(this.children[o].toJSON(t).object)}if(this.animations.length>0){s.animations=[];for(let o=0;o<this.animations.length;o++){let l=this.animations[o];s.animations.push(r(t.animations,l))}}if(e){let o=a(t.geometries),l=a(t.materials),c=a(t.textures),h=a(t.images),u=a(t.shapes),d=a(t.skeletons),p=a(t.animations),x=a(t.nodes);o.length>0&&(n.geometries=o),l.length>0&&(n.materials=l),c.length>0&&(n.textures=c),h.length>0&&(n.images=h),u.length>0&&(n.shapes=u),d.length>0&&(n.skeletons=d),p.length>0&&(n.animations=p),x.length>0&&(n.nodes=x)}return n.object=s,n;function a(o){let l=[];for(let c in o){let h=o[c];delete h.metadata,l.push(h)}return l}}clone(t){return new this.constructor().copy(this,t)}copy(t,e=!0){if(this.name=t.name,this.up.copy(t.up),this.position.copy(t.position),this.rotation.order=t.rotation.order,this.quaternion.copy(t.quaternion),this.scale.copy(t.scale),this.matrix.copy(t.matrix),this.matrixWorld.copy(t.matrixWorld),this.matrixAutoUpdate=t.matrixAutoUpdate,this.matrixWorldAutoUpdate=t.matrixWorldAutoUpdate,this.matrixWorldNeedsUpdate=t.matrixWorldNeedsUpdate,this.layers.mask=t.layers.mask,this.visible=t.visible,this.castShadow=t.castShadow,this.receiveShadow=t.receiveShadow,this.frustumCulled=t.frustumCulled,this.renderOrder=t.renderOrder,this.animations=t.animations.slice(),this.userData=JSON.parse(JSON.stringify(t.userData)),e===!0)for(let n=0;n<t.children.length;n++){let s=t.children[n];this.add(s.clone())}return this}};bn.DEFAULT_UP=new O(0,1,0);bn.DEFAULT_MATRIX_AUTO_UPDATE=!0;bn.DEFAULT_MATRIX_WORLD_AUTO_UPDATE=!0;var jn=new O,Si=new O,el=new O,bi=new O,Us=new O,Ds=new O,Zh=new O,nl=new O,il=new O,sl=new O,go=!1,Ws=class i{constructor(t=new O,e=new O,n=new O){this.a=t,this.b=e,this.c=n}static getNormal(t,e,n,s){s.subVectors(n,e),jn.subVectors(t,e),s.cross(jn);let r=s.lengthSq();return r>0?s.multiplyScalar(1/Math.sqrt(r)):s.set(0,0,0)}static getBarycoord(t,e,n,s,r){jn.subVectors(s,e),Si.subVectors(n,e),el.subVectors(t,e);let a=jn.dot(jn),o=jn.dot(Si),l=jn.dot(el),c=Si.dot(Si),h=Si.dot(el),u=a*c-o*o;if(u===0)return r.set(0,0,0),null;let d=1/u,p=(c*l-o*h)*d,x=(a*h-o*l)*d;return r.set(1-p-x,x,p)}static containsPoint(t,e,n,s){return this.getBarycoord(t,e,n,s,bi)===null?!1:bi.x>=0&&bi.y>=0&&bi.x+bi.y<=1}static getUV(t,e,n,s,r,a,o,l){return go===!1&&(console.warn("THREE.Triangle.getUV() has been renamed to THREE.Triangle.getInterpolation()."),go=!0),this.getInterpolation(t,e,n,s,r,a,o,l)}static getInterpolation(t,e,n,s,r,a,o,l){return this.getBarycoord(t,e,n,s,bi)===null?(l.x=0,l.y=0,"z"in l&&(l.z=0),"w"in l&&(l.w=0),null):(l.setScalar(0),l.addScaledVector(r,bi.x),l.addScaledVector(a,bi.y),l.addScaledVector(o,bi.z),l)}static isFrontFacing(t,e,n,s){return jn.subVectors(n,e),Si.subVectors(t,e),jn.cross(Si).dot(s)<0}set(t,e,n){return this.a.copy(t),this.b.copy(e),this.c.copy(n),this}setFromPointsAndIndices(t,e,n,s){return this.a.copy(t[e]),this.b.copy(t[n]),this.c.copy(t[s]),this}setFromAttributeAndIndices(t,e,n,s){return this.a.fromBufferAttribute(t,e),this.b.fromBufferAttribute(t,n),this.c.fromBufferAttribute(t,s),this}clone(){return new this.constructor().copy(this)}copy(t){return this.a.copy(t.a),this.b.copy(t.b),this.c.copy(t.c),this}getArea(){return jn.subVectors(this.c,this.b),Si.subVectors(this.a,this.b),jn.cross(Si).length()*.5}getMidpoint(t){return t.addVectors(this.a,this.b).add(this.c).multiplyScalar(1/3)}getNormal(t){return i.getNormal(this.a,this.b,this.c,t)}getPlane(t){return t.setFromCoplanarPoints(this.a,this.b,this.c)}getBarycoord(t,e){return i.getBarycoord(t,this.a,this.b,this.c,e)}getUV(t,e,n,s,r){return go===!1&&(console.warn("THREE.Triangle.getUV() has been renamed to THREE.Triangle.getInterpolation()."),go=!0),i.getInterpolation(t,this.a,this.b,this.c,e,n,s,r)}getInterpolation(t,e,n,s,r){return i.getInterpolation(t,this.a,this.b,this.c,e,n,s,r)}containsPoint(t){return i.containsPoint(t,this.a,this.b,this.c)}isFrontFacing(t){return i.isFrontFacing(this.a,this.b,this.c,t)}intersectsBox(t){return t.intersectsTriangle(this)}closestPointToPoint(t,e){let n=this.a,s=this.b,r=this.c,a,o;Us.subVectors(s,n),Ds.subVectors(r,n),nl.subVectors(t,n);let l=Us.dot(nl),c=Ds.dot(nl);if(l<=0&&c<=0)return e.copy(n);il.subVectors(t,s);let h=Us.dot(il),u=Ds.dot(il);if(h>=0&&u<=h)return e.copy(s);let d=l*u-h*c;if(d<=0&&l>=0&&h<=0)return a=l/(l-h),e.copy(n).addScaledVector(Us,a);sl.subVectors(t,r);let p=Us.dot(sl),x=Ds.dot(sl);if(x>=0&&p<=x)return e.copy(r);let y=p*c-l*x;if(y<=0&&c>=0&&x<=0)return o=c/(c-x),e.copy(n).addScaledVector(Ds,o);let g=h*x-p*u;if(g<=0&&u-h>=0&&p-x>=0)return Zh.subVectors(r,s),o=(u-h)/(u-h+(p-x)),e.copy(s).addScaledVector(Zh,o);let m=1/(g+y+d);return a=y*m,o=d*m,e.copy(n).addScaledVector(Us,a).addScaledVector(Ds,o)}equals(t){return t.a.equals(this.a)&&t.b.equals(this.b)&&t.c.equals(this.c)}},Zu={aliceblue:15792383,antiquewhite:16444375,aqua:65535,aquamarine:8388564,azure:15794175,beige:16119260,bisque:16770244,black:0,blanchedalmond:16772045,blue:255,blueviolet:9055202,brown:10824234,burlywood:14596231,cadetblue:6266528,chartreuse:8388352,chocolate:13789470,coral:16744272,cornflowerblue:6591981,cornsilk:16775388,crimson:14423100,cyan:65535,darkblue:139,darkcyan:35723,darkgoldenrod:12092939,darkgray:11119017,darkgreen:25600,darkgrey:11119017,darkkhaki:12433259,darkmagenta:9109643,darkolivegreen:5597999,darkorange:16747520,darkorchid:10040012,darkred:9109504,darksalmon:15308410,darkseagreen:9419919,darkslateblue:4734347,darkslategray:3100495,darkslategrey:3100495,darkturquoise:52945,darkviolet:9699539,deeppink:16716947,deepskyblue:49151,dimgray:6908265,dimgrey:6908265,dodgerblue:2003199,firebrick:11674146,floralwhite:16775920,forestgreen:2263842,fuchsia:16711935,gainsboro:14474460,ghostwhite:16316671,gold:16766720,goldenrod:14329120,gray:8421504,green:32768,greenyellow:11403055,grey:8421504,honeydew:15794160,hotpink:16738740,indianred:13458524,indigo:4915330,ivory:16777200,khaki:15787660,lavender:15132410,lavenderblush:16773365,lawngreen:8190976,lemonchiffon:16775885,lightblue:11393254,lightcoral:15761536,lightcyan:14745599,lightgoldenrodyellow:16448210,lightgray:13882323,lightgreen:9498256,lightgrey:13882323,lightpink:16758465,lightsalmon:16752762,lightseagreen:2142890,lightskyblue:8900346,lightslategray:7833753,lightslategrey:7833753,lightsteelblue:11584734,lightyellow:16777184,lime:65280,limegreen:3329330,linen:16445670,magenta:16711935,maroon:8388608,mediumaquamarine:6737322,mediumblue:205,mediumorchid:12211667,mediumpurple:9662683,mediumseagreen:3978097,mediumslateblue:8087790,mediumspringgreen:64154,mediumturquoise:4772300,mediumvioletred:13047173,midnightblue:1644912,mintcream:16121850,mistyrose:16770273,moccasin:16770229,navajowhite:16768685,navy:128,oldlace:16643558,olive:8421376,olivedrab:7048739,orange:16753920,orangered:16729344,orchid:14315734,palegoldenrod:15657130,palegreen:10025880,paleturquoise:11529966,palevioletred:14381203,papayawhip:16773077,peachpuff:16767673,peru:13468991,pink:16761035,plum:14524637,powderblue:11591910,purple:8388736,rebeccapurple:6697881,red:16711680,rosybrown:12357519,royalblue:4286945,saddlebrown:9127187,salmon:16416882,sandybrown:16032864,seagreen:3050327,seashell:16774638,sienna:10506797,silver:12632256,skyblue:8900331,slateblue:6970061,slategray:7372944,slategrey:7372944,snow:16775930,springgreen:65407,steelblue:4620980,tan:13808780,teal:32896,thistle:14204888,tomato:16737095,turquoise:4251856,violet:15631086,wheat:16113331,white:16777215,whitesmoke:16119285,yellow:16776960,yellowgreen:10145074},Hi={h:0,s:0,l:0},_o={h:0,s:0,l:0};function rl(i,t,e){return e<0&&(e+=1),e>1&&(e-=1),e<1/6?i+(t-i)*6*e:e<1/2?t:e<2/3?i+(t-i)*6*(2/3-e):i}var ge=class{constructor(t,e,n){return this.isColor=!0,this.r=1,this.g=1,this.b=1,this.set(t,e,n)}set(t,e,n){if(e===void 0&&n===void 0){let s=t;s&&s.isColor?this.copy(s):typeof s=="number"?this.setHex(s):typeof s=="string"&&this.setStyle(s)}else this.setRGB(t,e,n);return this}setScalar(t){return this.r=t,this.g=t,this.b=t,this}setHex(t,e=Je){return t=Math.floor(t),this.r=(t>>16&255)/255,this.g=(t>>8&255)/255,this.b=(t&255)/255,Ue.toWorkingColorSpace(this,e),this}setRGB(t,e,n,s=Ue.workingColorSpace){return this.r=t,this.g=e,this.b=n,Ue.toWorkingColorSpace(this,s),this}setHSL(t,e,n,s=Ue.workingColorSpace){if(t=mc(t,1),e=cn(e,0,1),n=cn(n,0,1),e===0)this.r=this.g=this.b=n;else{let r=n<=.5?n*(1+e):n+e-n*e,a=2*n-r;this.r=rl(a,r,t+1/3),this.g=rl(a,r,t),this.b=rl(a,r,t-1/3)}return Ue.toWorkingColorSpace(this,s),this}setStyle(t,e=Je){function n(r){r!==void 0&&parseFloat(r)<1&&console.warn("THREE.Color: Alpha component of "+t+" will be ignored.")}let s;if(s=/^(\w+)\(([^\)]*)\)/.exec(t)){let r,a=s[1],o=s[2];switch(a){case"rgb":case"rgba":if(r=/^\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*(\d*\.?\d+)\s*)?$/.exec(o))return n(r[4]),this.setRGB(Math.min(255,parseInt(r[1],10))/255,Math.min(255,parseInt(r[2],10))/255,Math.min(255,parseInt(r[3],10))/255,e);if(r=/^\s*(\d+)\%\s*,\s*(\d+)\%\s*,\s*(\d+)\%\s*(?:,\s*(\d*\.?\d+)\s*)?$/.exec(o))return n(r[4]),this.setRGB(Math.min(100,parseInt(r[1],10))/100,Math.min(100,parseInt(r[2],10))/100,Math.min(100,parseInt(r[3],10))/100,e);break;case"hsl":case"hsla":if(r=/^\s*(\d*\.?\d+)\s*,\s*(\d*\.?\d+)\%\s*,\s*(\d*\.?\d+)\%\s*(?:,\s*(\d*\.?\d+)\s*)?$/.exec(o))return n(r[4]),this.setHSL(parseFloat(r[1])/360,parseFloat(r[2])/100,parseFloat(r[3])/100,e);break;default:console.warn("THREE.Color: Unknown color model "+t)}}else if(s=/^\#([A-Fa-f\d]+)$/.exec(t)){let r=s[1],a=r.length;if(a===3)return this.setRGB(parseInt(r.charAt(0),16)/15,parseInt(r.charAt(1),16)/15,parseInt(r.charAt(2),16)/15,e);if(a===6)return this.setHex(parseInt(r,16),e);console.warn("THREE.Color: Invalid hex color "+t)}else if(t&&t.length>0)return this.setColorName(t,e);return this}setColorName(t,e=Je){let n=Zu[t.toLowerCase()];return n!==void 0?this.setHex(n,e):console.warn("THREE.Color: Unknown color "+t),this}clone(){return new this.constructor(this.r,this.g,this.b)}copy(t){return this.r=t.r,this.g=t.g,this.b=t.b,this}copySRGBToLinear(t){return this.r=Js(t.r),this.g=Js(t.g),this.b=Js(t.b),this}copyLinearToSRGB(t){return this.r=qa(t.r),this.g=qa(t.g),this.b=qa(t.b),this}convertSRGBToLinear(){return this.copySRGBToLinear(this),this}convertLinearToSRGB(){return this.copyLinearToSRGB(this),this}getHex(t=Je){return Ue.fromWorkingColorSpace(yn.copy(this),t),Math.round(cn(yn.r*255,0,255))*65536+Math.round(cn(yn.g*255,0,255))*256+Math.round(cn(yn.b*255,0,255))}getHexString(t=Je){return("000000"+this.getHex(t).toString(16)).slice(-6)}getHSL(t,e=Ue.workingColorSpace){Ue.fromWorkingColorSpace(yn.copy(this),e);let n=yn.r,s=yn.g,r=yn.b,a=Math.max(n,s,r),o=Math.min(n,s,r),l,c,h=(o+a)/2;if(o===a)l=0,c=0;else{let u=a-o;switch(c=h<=.5?u/(a+o):u/(2-a-o),a){case n:l=(s-r)/u+(s<r?6:0);break;case s:l=(r-n)/u+2;break;case r:l=(n-s)/u+4;break}l/=6}return t.h=l,t.s=c,t.l=h,t}getRGB(t,e=Ue.workingColorSpace){return Ue.fromWorkingColorSpace(yn.copy(this),e),t.r=yn.r,t.g=yn.g,t.b=yn.b,t}getStyle(t=Je){Ue.fromWorkingColorSpace(yn.copy(this),t);let e=yn.r,n=yn.g,s=yn.b;return t!==Je?`color(${t} ${e.toFixed(3)} ${n.toFixed(3)} ${s.toFixed(3)})`:`rgb(${Math.round(e*255)},${Math.round(n*255)},${Math.round(s*255)})`}offsetHSL(t,e,n){return this.getHSL(Hi),this.setHSL(Hi.h+t,Hi.s+e,Hi.l+n)}add(t){return this.r+=t.r,this.g+=t.g,this.b+=t.b,this}addColors(t,e){return this.r=t.r+e.r,this.g=t.g+e.g,this.b=t.b+e.b,this}addScalar(t){return this.r+=t,this.g+=t,this.b+=t,this}sub(t){return this.r=Math.max(0,this.r-t.r),this.g=Math.max(0,this.g-t.g),this.b=Math.max(0,this.b-t.b),this}multiply(t){return this.r*=t.r,this.g*=t.g,this.b*=t.b,this}multiplyScalar(t){return this.r*=t,this.g*=t,this.b*=t,this}lerp(t,e){return this.r+=(t.r-this.r)*e,this.g+=(t.g-this.g)*e,this.b+=(t.b-this.b)*e,this}lerpColors(t,e,n){return this.r=t.r+(e.r-t.r)*n,this.g=t.g+(e.g-t.g)*n,this.b=t.b+(e.b-t.b)*n,this}lerpHSL(t,e){this.getHSL(Hi),t.getHSL(_o);let n=br(Hi.h,_o.h,e),s=br(Hi.s,_o.s,e),r=br(Hi.l,_o.l,e);return this.setHSL(n,s,r),this}setFromVector3(t){return this.r=t.x,this.g=t.y,this.b=t.z,this}applyMatrix3(t){let e=this.r,n=this.g,s=this.b,r=t.elements;return this.r=r[0]*e+r[3]*n+r[6]*s,this.g=r[1]*e+r[4]*n+r[7]*s,this.b=r[2]*e+r[5]*n+r[8]*s,this}equals(t){return t.r===this.r&&t.g===this.g&&t.b===this.b}fromArray(t,e=0){return this.r=t[e],this.g=t[e+1],this.b=t[e+2],this}toArray(t=[],e=0){return t[e]=this.r,t[e+1]=this.g,t[e+2]=this.b,t}fromBufferAttribute(t,e){return this.r=t.getX(e),this.g=t.getY(e),this.b=t.getZ(e),this}toJSON(){return this.getHex()}*[Symbol.iterator](){yield this.r,yield this.g,yield this.b}},yn=new ge;ge.NAMES=Zu;var Wd=0,$i=class extends qi{constructor(){super(),this.isMaterial=!0,Object.defineProperty(this,"id",{value:Wd++}),this.uuid=ys(),this.name="",this.type="Material",this.blending=$s,this.side=Yi,this.vertexColors=!1,this.opacity=1,this.transparent=!1,this.alphaHash=!1,this.blendSrc=vl,this.blendDst=yl,this.blendEquation=cs,this.blendSrcAlpha=null,this.blendDstAlpha=null,this.blendEquationAlpha=null,this.blendColor=new ge(0,0,0),this.blendAlpha=0,this.depthFunc=Oo,this.depthTest=!0,this.depthWrite=!0,this.stencilWriteMask=255,this.stencilFunc=Dh,this.stencilRef=0,this.stencilFuncMask=255,this.stencilFail=Ts,this.stencilZFail=Ts,this.stencilZPass=Ts,this.stencilWrite=!1,this.clippingPlanes=null,this.clipIntersection=!1,this.clipShadows=!1,this.shadowSide=null,this.colorWrite=!0,this.precision=null,this.polygonOffset=!1,this.polygonOffsetFactor=0,this.polygonOffsetUnits=0,this.dithering=!1,this.alphaToCoverage=!1,this.premultipliedAlpha=!1,this.forceSinglePass=!1,this.visible=!0,this.toneMapped=!0,this.userData={},this.version=0,this._alphaTest=0}get alphaTest(){return this._alphaTest}set alphaTest(t){this._alphaTest>0!=t>0&&this.version++,this._alphaTest=t}onBuild(){}onBeforeRender(){}onBeforeCompile(){}customProgramCacheKey(){return this.onBeforeCompile.toString()}setValues(t){if(t!==void 0)for(let e in t){let n=t[e];if(n===void 0){console.warn(`THREE.Material: parameter '${e}' has value of undefined.`);continue}let s=this[e];if(s===void 0){console.warn(`THREE.Material: '${e}' is not a property of THREE.${this.type}.`);continue}s&&s.isColor?s.set(n):s&&s.isVector3&&n&&n.isVector3?s.copy(n):this[e]=n}}toJSON(t){let e=t===void 0||typeof t=="string";e&&(t={textures:{},images:{}});let n={metadata:{version:4.6,type:"Material",generator:"Material.toJSON"}};n.uuid=this.uuid,n.type=this.type,this.name!==""&&(n.name=this.name),this.color&&this.color.isColor&&(n.color=this.color.getHex()),this.roughness!==void 0&&(n.roughness=this.roughness),this.metalness!==void 0&&(n.metalness=this.metalness),this.sheen!==void 0&&(n.sheen=this.sheen),this.sheenColor&&this.sheenColor.isColor&&(n.sheenColor=this.sheenColor.getHex()),this.sheenRoughness!==void 0&&(n.sheenRoughness=this.sheenRoughness),this.emissive&&this.emissive.isColor&&(n.emissive=this.emissive.getHex()),this.emissiveIntensity&&this.emissiveIntensity!==1&&(n.emissiveIntensity=this.emissiveIntensity),this.specular&&this.specular.isColor&&(n.specular=this.specular.getHex()),this.specularIntensity!==void 0&&(n.specularIntensity=this.specularIntensity),this.specularColor&&this.specularColor.isColor&&(n.specularColor=this.specularColor.getHex()),this.shininess!==void 0&&(n.shininess=this.shininess),this.clearcoat!==void 0&&(n.clearcoat=this.clearcoat),this.clearcoatRoughness!==void 0&&(n.clearcoatRoughness=this.clearcoatRoughness),this.clearcoatMap&&this.clearcoatMap.isTexture&&(n.clearcoatMap=this.clearcoatMap.toJSON(t).uuid),this.clearcoatRoughnessMap&&this.clearcoatRoughnessMap.isTexture&&(n.clearcoatRoughnessMap=this.clearcoatRoughnessMap.toJSON(t).uuid),this.clearcoatNormalMap&&this.clearcoatNormalMap.isTexture&&(n.clearcoatNormalMap=this.clearcoatNormalMap.toJSON(t).uuid,n.clearcoatNormalScale=this.clearcoatNormalScale.toArray()),this.iridescence!==void 0&&(n.iridescence=this.iridescence),this.iridescenceIOR!==void 0&&(n.iridescenceIOR=this.iridescenceIOR),this.iridescenceThicknessRange!==void 0&&(n.iridescenceThicknessRange=this.iridescenceThicknessRange),this.iridescenceMap&&this.iridescenceMap.isTexture&&(n.iridescenceMap=this.iridescenceMap.toJSON(t).uuid),this.iridescenceThicknessMap&&this.iridescenceThicknessMap.isTexture&&(n.iridescenceThicknessMap=this.iridescenceThicknessMap.toJSON(t).uuid),this.anisotropy!==void 0&&(n.anisotropy=this.anisotropy),this.anisotropyRotation!==void 0&&(n.anisotropyRotation=this.anisotropyRotation),this.anisotropyMap&&this.anisotropyMap.isTexture&&(n.anisotropyMap=this.anisotropyMap.toJSON(t).uuid),this.map&&this.map.isTexture&&(n.map=this.map.toJSON(t).uuid),this.matcap&&this.matcap.isTexture&&(n.matcap=this.matcap.toJSON(t).uuid),this.alphaMap&&this.alphaMap.isTexture&&(n.alphaMap=this.alphaMap.toJSON(t).uuid),this.lightMap&&this.lightMap.isTexture&&(n.lightMap=this.lightMap.toJSON(t).uuid,n.lightMapIntensity=this.lightMapIntensity),this.aoMap&&this.aoMap.isTexture&&(n.aoMap=this.aoMap.toJSON(t).uuid,n.aoMapIntensity=this.aoMapIntensity),this.bumpMap&&this.bumpMap.isTexture&&(n.bumpMap=this.bumpMap.toJSON(t).uuid,n.bumpScale=this.bumpScale),this.normalMap&&this.normalMap.isTexture&&(n.normalMap=this.normalMap.toJSON(t).uuid,n.normalMapType=this.normalMapType,n.normalScale=this.normalScale.toArray()),this.displacementMap&&this.displacementMap.isTexture&&(n.displacementMap=this.displacementMap.toJSON(t).uuid,n.displacementScale=this.displacementScale,n.displacementBias=this.displacementBias),this.roughnessMap&&this.roughnessMap.isTexture&&(n.roughnessMap=this.roughnessMap.toJSON(t).uuid),this.metalnessMap&&this.metalnessMap.isTexture&&(n.metalnessMap=this.metalnessMap.toJSON(t).uuid),this.emissiveMap&&this.emissiveMap.isTexture&&(n.emissiveMap=this.emissiveMap.toJSON(t).uuid),this.specularMap&&this.specularMap.isTexture&&(n.specularMap=this.specularMap.toJSON(t).uuid),this.specularIntensityMap&&this.specularIntensityMap.isTexture&&(n.specularIntensityMap=this.specularIntensityMap.toJSON(t).uuid),this.specularColorMap&&this.specularColorMap.isTexture&&(n.specularColorMap=this.specularColorMap.toJSON(t).uuid),this.envMap&&this.envMap.isTexture&&(n.envMap=this.envMap.toJSON(t).uuid,this.combine!==void 0&&(n.combine=this.combine)),this.envMapIntensity!==void 0&&(n.envMapIntensity=this.envMapIntensity),this.reflectivity!==void 0&&(n.reflectivity=this.reflectivity),this.refractionRatio!==void 0&&(n.refractionRatio=this.refractionRatio),this.gradientMap&&this.gradientMap.isTexture&&(n.gradientMap=this.gradientMap.toJSON(t).uuid),this.transmission!==void 0&&(n.transmission=this.transmission),this.transmissionMap&&this.transmissionMap.isTexture&&(n.transmissionMap=this.transmissionMap.toJSON(t).uuid),this.thickness!==void 0&&(n.thickness=this.thickness),this.thicknessMap&&this.thicknessMap.isTexture&&(n.thicknessMap=this.thicknessMap.toJSON(t).uuid),this.attenuationDistance!==void 0&&this.attenuationDistance!==1/0&&(n.attenuationDistance=this.attenuationDistance),this.attenuationColor!==void 0&&(n.attenuationColor=this.attenuationColor.getHex()),this.size!==void 0&&(n.size=this.size),this.shadowSide!==null&&(n.shadowSide=this.shadowSide),this.sizeAttenuation!==void 0&&(n.sizeAttenuation=this.sizeAttenuation),this.blending!==$s&&(n.blending=this.blending),this.side!==Yi&&(n.side=this.side),this.vertexColors===!0&&(n.vertexColors=!0),this.opacity<1&&(n.opacity=this.opacity),this.transparent===!0&&(n.transparent=!0),this.blendSrc!==vl&&(n.blendSrc=this.blendSrc),this.blendDst!==yl&&(n.blendDst=this.blendDst),this.blendEquation!==cs&&(n.blendEquation=this.blendEquation),this.blendSrcAlpha!==null&&(n.blendSrcAlpha=this.blendSrcAlpha),this.blendDstAlpha!==null&&(n.blendDstAlpha=this.blendDstAlpha),this.blendEquationAlpha!==null&&(n.blendEquationAlpha=this.blendEquationAlpha),this.blendColor&&this.blendColor.isColor&&(n.blendColor=this.blendColor.getHex()),this.blendAlpha!==0&&(n.blendAlpha=this.blendAlpha),this.depthFunc!==Oo&&(n.depthFunc=this.depthFunc),this.depthTest===!1&&(n.depthTest=this.depthTest),this.depthWrite===!1&&(n.depthWrite=this.depthWrite),this.colorWrite===!1&&(n.colorWrite=this.colorWrite),this.stencilWriteMask!==255&&(n.stencilWriteMask=this.stencilWriteMask),this.stencilFunc!==Dh&&(n.stencilFunc=this.stencilFunc),this.stencilRef!==0&&(n.stencilRef=this.stencilRef),this.stencilFuncMask!==255&&(n.stencilFuncMask=this.stencilFuncMask),this.stencilFail!==Ts&&(n.stencilFail=this.stencilFail),this.stencilZFail!==Ts&&(n.stencilZFail=this.stencilZFail),this.stencilZPass!==Ts&&(n.stencilZPass=this.stencilZPass),this.stencilWrite===!0&&(n.stencilWrite=this.stencilWrite),this.rotation!==void 0&&this.rotation!==0&&(n.rotation=this.rotation),this.polygonOffset===!0&&(n.polygonOffset=!0),this.polygonOffsetFactor!==0&&(n.polygonOffsetFactor=this.polygonOffsetFactor),this.polygonOffsetUnits!==0&&(n.polygonOffsetUnits=this.polygonOffsetUnits),this.linewidth!==void 0&&this.linewidth!==1&&(n.linewidth=this.linewidth),this.dashSize!==void 0&&(n.dashSize=this.dashSize),this.gapSize!==void 0&&(n.gapSize=this.gapSize),this.scale!==void 0&&(n.scale=this.scale),this.dithering===!0&&(n.dithering=!0),this.alphaTest>0&&(n.alphaTest=this.alphaTest),this.alphaHash===!0&&(n.alphaHash=!0),this.alphaToCoverage===!0&&(n.alphaToCoverage=!0),this.premultipliedAlpha===!0&&(n.premultipliedAlpha=!0),this.forceSinglePass===!0&&(n.forceSinglePass=!0),this.wireframe===!0&&(n.wireframe=!0),this.wireframeLinewidth>1&&(n.wireframeLinewidth=this.wireframeLinewidth),this.wireframeLinecap!=="round"&&(n.wireframeLinecap=this.wireframeLinecap),this.wireframeLinejoin!=="round"&&(n.wireframeLinejoin=this.wireframeLinejoin),this.flatShading===!0&&(n.flatShading=!0),this.visible===!1&&(n.visible=!1),this.toneMapped===!1&&(n.toneMapped=!1),this.fog===!1&&(n.fog=!1),Object.keys(this.userData).length>0&&(n.userData=this.userData);function s(r){let a=[];for(let o in r){let l=r[o];delete l.metadata,a.push(l)}return a}if(e){let r=s(t.textures),a=s(t.images);r.length>0&&(n.textures=r),a.length>0&&(n.images=a)}return n}clone(){return new this.constructor().copy(this)}copy(t){this.name=t.name,this.blending=t.blending,this.side=t.side,this.vertexColors=t.vertexColors,this.opacity=t.opacity,this.transparent=t.transparent,this.blendSrc=t.blendSrc,this.blendDst=t.blendDst,this.blendEquation=t.blendEquation,this.blendSrcAlpha=t.blendSrcAlpha,this.blendDstAlpha=t.blendDstAlpha,this.blendEquationAlpha=t.blendEquationAlpha,this.blendColor.copy(t.blendColor),this.blendAlpha=t.blendAlpha,this.depthFunc=t.depthFunc,this.depthTest=t.depthTest,this.depthWrite=t.depthWrite,this.stencilWriteMask=t.stencilWriteMask,this.stencilFunc=t.stencilFunc,this.stencilRef=t.stencilRef,this.stencilFuncMask=t.stencilFuncMask,this.stencilFail=t.stencilFail,this.stencilZFail=t.stencilZFail,this.stencilZPass=t.stencilZPass,this.stencilWrite=t.stencilWrite;let e=t.clippingPlanes,n=null;if(e!==null){let s=e.length;n=new Array(s);for(let r=0;r!==s;++r)n[r]=e[r].clone()}return this.clippingPlanes=n,this.clipIntersection=t.clipIntersection,this.clipShadows=t.clipShadows,this.shadowSide=t.shadowSide,this.colorWrite=t.colorWrite,this.precision=t.precision,this.polygonOffset=t.polygonOffset,this.polygonOffsetFactor=t.polygonOffsetFactor,this.polygonOffsetUnits=t.polygonOffsetUnits,this.dithering=t.dithering,this.alphaTest=t.alphaTest,this.alphaHash=t.alphaHash,this.alphaToCoverage=t.alphaToCoverage,this.premultipliedAlpha=t.premultipliedAlpha,this.forceSinglePass=t.forceSinglePass,this.visible=t.visible,this.toneMapped=t.toneMapped,this.userData=JSON.parse(JSON.stringify(t.userData)),this}dispose(){this.dispatchEvent({type:"dispose"})}set needsUpdate(t){t===!0&&this.version++}},gs=class extends $i{constructor(t){super(),this.isMeshBasicMaterial=!0,this.type="MeshBasicMaterial",this.color=new ge(16777215),this.map=null,this.lightMap=null,this.lightMapIntensity=1,this.aoMap=null,this.aoMapIntensity=1,this.specularMap=null,this.alphaMap=null,this.envMap=null,this.combine=Nu,this.reflectivity=1,this.refractionRatio=.98,this.wireframe=!1,this.wireframeLinewidth=1,this.wireframeLinecap="round",this.wireframeLinejoin="round",this.fog=!0,this.setValues(t)}copy(t){return super.copy(t),this.color.copy(t.color),this.map=t.map,this.lightMap=t.lightMap,this.lightMapIntensity=t.lightMapIntensity,this.aoMap=t.aoMap,this.aoMapIntensity=t.aoMapIntensity,this.specularMap=t.specularMap,this.alphaMap=t.alphaMap,this.envMap=t.envMap,this.combine=t.combine,this.reflectivity=t.reflectivity,this.refractionRatio=t.refractionRatio,this.wireframe=t.wireframe,this.wireframeLinewidth=t.wireframeLinewidth,this.wireframeLinecap=t.wireframeLinecap,this.wireframeLinejoin=t.wireframeLinejoin,this.fog=t.fog,this}};var Qe=new O,xo=new xt,gn=class{constructor(t,e,n=!1){if(Array.isArray(t))throw new TypeError("THREE.BufferAttribute: array should be a Typed Array.");this.isBufferAttribute=!0,this.name="",this.array=t,this.itemSize=e,this.count=t!==void 0?t.length/e:0,this.normalized=n,this.usage=Nh,this._updateRange={offset:0,count:-1},this.updateRanges=[],this.gpuType=Vi,this.version=0}onUploadCallback(){}set needsUpdate(t){t===!0&&this.version++}get updateRange(){return console.warn("THREE.BufferAttribute: updateRange() is deprecated and will be removed in r169. Use addUpdateRange() instead."),this._updateRange}setUsage(t){return this.usage=t,this}addUpdateRange(t,e){this.updateRanges.push({start:t,count:e})}clearUpdateRanges(){this.updateRanges.length=0}copy(t){return this.name=t.name,this.array=new t.array.constructor(t.array),this.itemSize=t.itemSize,this.count=t.count,this.normalized=t.normalized,this.usage=t.usage,this.gpuType=t.gpuType,this}copyAt(t,e,n){t*=this.itemSize,n*=e.itemSize;for(let s=0,r=this.itemSize;s<r;s++)this.array[t+s]=e.array[n+s];return this}copyArray(t){return this.array.set(t),this}applyMatrix3(t){if(this.itemSize===2)for(let e=0,n=this.count;e<n;e++)xo.fromBufferAttribute(this,e),xo.applyMatrix3(t),this.setXY(e,xo.x,xo.y);else if(this.itemSize===3)for(let e=0,n=this.count;e<n;e++)Qe.fromBufferAttribute(this,e),Qe.applyMatrix3(t),this.setXYZ(e,Qe.x,Qe.y,Qe.z);return this}applyMatrix4(t){for(let e=0,n=this.count;e<n;e++)Qe.fromBufferAttribute(this,e),Qe.applyMatrix4(t),this.setXYZ(e,Qe.x,Qe.y,Qe.z);return this}applyNormalMatrix(t){for(let e=0,n=this.count;e<n;e++)Qe.fromBufferAttribute(this,e),Qe.applyNormalMatrix(t),this.setXYZ(e,Qe.x,Qe.y,Qe.z);return this}transformDirection(t){for(let e=0,n=this.count;e<n;e++)Qe.fromBufferAttribute(this,e),Qe.transformDirection(t),this.setXYZ(e,Qe.x,Qe.y,Qe.z);return this}set(t,e=0){return this.array.set(t,e),this}getComponent(t,e){let n=this.array[t*this.itemSize+e];return this.normalized&&(n=Gs(n,this.array)),n}setComponent(t,e,n){return this.normalized&&(n=wn(n,this.array)),this.array[t*this.itemSize+e]=n,this}getX(t){let e=this.array[t*this.itemSize];return this.normalized&&(e=Gs(e,this.array)),e}setX(t,e){return this.normalized&&(e=wn(e,this.array)),this.array[t*this.itemSize]=e,this}getY(t){let e=this.array[t*this.itemSize+1];return this.normalized&&(e=Gs(e,this.array)),e}setY(t,e){return this.normalized&&(e=wn(e,this.array)),this.array[t*this.itemSize+1]=e,this}getZ(t){let e=this.array[t*this.itemSize+2];return this.normalized&&(e=Gs(e,this.array)),e}setZ(t,e){return this.normalized&&(e=wn(e,this.array)),this.array[t*this.itemSize+2]=e,this}getW(t){let e=this.array[t*this.itemSize+3];return this.normalized&&(e=Gs(e,this.array)),e}setW(t,e){return this.normalized&&(e=wn(e,this.array)),this.array[t*this.itemSize+3]=e,this}setXY(t,e,n){return t*=this.itemSize,this.normalized&&(e=wn(e,this.array),n=wn(n,this.array)),this.array[t+0]=e,this.array[t+1]=n,this}setXYZ(t,e,n,s){return t*=this.itemSize,this.normalized&&(e=wn(e,this.array),n=wn(n,this.array),s=wn(s,this.array)),this.array[t+0]=e,this.array[t+1]=n,this.array[t+2]=s,this}setXYZW(t,e,n,s,r){return t*=this.itemSize,this.normalized&&(e=wn(e,this.array),n=wn(n,this.array),s=wn(s,this.array),r=wn(r,this.array)),this.array[t+0]=e,this.array[t+1]=n,this.array[t+2]=s,this.array[t+3]=r,this}onUpload(t){return this.onUploadCallback=t,this}clone(){return new this.constructor(this.array,this.itemSize).copy(this)}toJSON(){let t={itemSize:this.itemSize,type:this.array.constructor.name,array:Array.from(this.array),normalized:this.normalized};return this.name!==""&&(t.name=this.name),this.usage!==Nh&&(t.usage=this.usage),t}};var Zo=class extends gn{constructor(t,e,n){super(new Uint16Array(t),e,n)}};var $o=class extends gn{constructor(t,e,n){super(new Uint32Array(t),e,n)}};var _e=class extends gn{constructor(t,e,n){super(new Float32Array(t),e,n)}};var Xd=0,Hn=new De,ol=new bn,Ns=new O,Un=new Ci,xr=new Ci,ln=new O,qe=class i extends qi{constructor(){super(),this.isBufferGeometry=!0,Object.defineProperty(this,"id",{value:Xd++}),this.uuid=ys(),this.name="",this.type="BufferGeometry",this.index=null,this.attributes={},this.morphAttributes={},this.morphTargetsRelative=!1,this.groups=[],this.boundingBox=null,this.boundingSphere=null,this.drawRange={start:0,count:1/0},this.userData={}}getIndex(){return this.index}setIndex(t){return Array.isArray(t)?this.index=new(qu(t)?$o:Zo)(t,1):this.index=t,this}getAttribute(t){return this.attributes[t]}setAttribute(t,e){return this.attributes[t]=e,this}deleteAttribute(t){return delete this.attributes[t],this}hasAttribute(t){return this.attributes[t]!==void 0}addGroup(t,e,n=0){this.groups.push({start:t,count:e,materialIndex:n})}clearGroups(){this.groups=[]}setDrawRange(t,e){this.drawRange.start=t,this.drawRange.count=e}applyMatrix4(t){let e=this.attributes.position;e!==void 0&&(e.applyMatrix4(t),e.needsUpdate=!0);let n=this.attributes.normal;if(n!==void 0){let r=new ve().getNormalMatrix(t);n.applyNormalMatrix(r),n.needsUpdate=!0}let s=this.attributes.tangent;return s!==void 0&&(s.transformDirection(t),s.needsUpdate=!0),this.boundingBox!==null&&this.computeBoundingBox(),this.boundingSphere!==null&&this.computeBoundingSphere(),this}applyQuaternion(t){return Hn.makeRotationFromQuaternion(t),this.applyMatrix4(Hn),this}rotateX(t){return Hn.makeRotationX(t),this.applyMatrix4(Hn),this}rotateY(t){return Hn.makeRotationY(t),this.applyMatrix4(Hn),this}rotateZ(t){return Hn.makeRotationZ(t),this.applyMatrix4(Hn),this}translate(t,e,n){return Hn.makeTranslation(t,e,n),this.applyMatrix4(Hn),this}scale(t,e,n){return Hn.makeScale(t,e,n),this.applyMatrix4(Hn),this}lookAt(t){return ol.lookAt(t),ol.updateMatrix(),this.applyMatrix4(ol.matrix),this}center(){return this.computeBoundingBox(),this.boundingBox.getCenter(Ns).negate(),this.translate(Ns.x,Ns.y,Ns.z),this}setFromPoints(t){let e=[];for(let n=0,s=t.length;n<s;n++){let r=t[n];e.push(r.x,r.y,r.z||0)}return this.setAttribute("position",new _e(e,3)),this}computeBoundingBox(){this.boundingBox===null&&(this.boundingBox=new Ci);let t=this.attributes.position,e=this.morphAttributes.position;if(t&&t.isGLBufferAttribute){console.error('THREE.BufferGeometry.computeBoundingBox(): GLBufferAttribute requires a manual bounding box. Alternatively set "mesh.frustumCulled" to "false".',this),this.boundingBox.set(new O(-1/0,-1/0,-1/0),new O(1/0,1/0,1/0));return}if(t!==void 0){if(this.boundingBox.setFromBufferAttribute(t),e)for(let n=0,s=e.length;n<s;n++){let r=e[n];Un.setFromBufferAttribute(r),this.morphTargetsRelative?(ln.addVectors(this.boundingBox.min,Un.min),this.boundingBox.expandByPoint(ln),ln.addVectors(this.boundingBox.max,Un.max),this.boundingBox.expandByPoint(ln)):(this.boundingBox.expandByPoint(Un.min),this.boundingBox.expandByPoint(Un.max))}}else this.boundingBox.makeEmpty();(isNaN(this.boundingBox.min.x)||isNaN(this.boundingBox.min.y)||isNaN(this.boundingBox.min.z))&&console.error('THREE.BufferGeometry.computeBoundingBox(): Computed min/max have NaN values. The "position" attribute is likely to have NaN values.',this)}computeBoundingSphere(){this.boundingSphere===null&&(this.boundingSphere=new Zi);let t=this.attributes.position,e=this.morphAttributes.position;if(t&&t.isGLBufferAttribute){console.error('THREE.BufferGeometry.computeBoundingSphere(): GLBufferAttribute requires a manual bounding sphere. Alternatively set "mesh.frustumCulled" to "false".',this),this.boundingSphere.set(new O,1/0);return}if(t){let n=this.boundingSphere.center;if(Un.setFromBufferAttribute(t),e)for(let r=0,a=e.length;r<a;r++){let o=e[r];xr.setFromBufferAttribute(o),this.morphTargetsRelative?(ln.addVectors(Un.min,xr.min),Un.expandByPoint(ln),ln.addVectors(Un.max,xr.max),Un.expandByPoint(ln)):(Un.expandByPoint(xr.min),Un.expandByPoint(xr.max))}Un.getCenter(n);let s=0;for(let r=0,a=t.count;r<a;r++)ln.fromBufferAttribute(t,r),s=Math.max(s,n.distanceToSquared(ln));if(e)for(let r=0,a=e.length;r<a;r++){let o=e[r],l=this.morphTargetsRelative;for(let c=0,h=o.count;c<h;c++)ln.fromBufferAttribute(o,c),l&&(Ns.fromBufferAttribute(t,c),ln.add(Ns)),s=Math.max(s,n.distanceToSquared(ln))}this.boundingSphere.radius=Math.sqrt(s),isNaN(this.boundingSphere.radius)&&console.error('THREE.BufferGeometry.computeBoundingSphere(): Computed radius is NaN. The "position" attribute is likely to have NaN values.',this)}}computeTangents(){let t=this.index,e=this.attributes;if(t===null||e.position===void 0||e.normal===void 0||e.uv===void 0){console.error("THREE.BufferGeometry: .computeTangents() failed. Missing required attributes (index, position, normal or uv)");return}let n=t.array,s=e.position.array,r=e.normal.array,a=e.uv.array,o=s.length/3;this.hasAttribute("tangent")===!1&&this.setAttribute("tangent",new gn(new Float32Array(4*o),4));let l=this.getAttribute("tangent").array,c=[],h=[];for(let P=0;P<o;P++)c[P]=new O,h[P]=new O;let u=new O,d=new O,p=new O,x=new xt,y=new xt,g=new xt,m=new O,w=new O;function v(P,X,rt){u.fromArray(s,P*3),d.fromArray(s,X*3),p.fromArray(s,rt*3),x.fromArray(a,P*2),y.fromArray(a,X*2),g.fromArray(a,rt*2),d.sub(u),p.sub(u),y.sub(x),g.sub(x);let _t=1/(y.x*g.y-g.x*y.y);isFinite(_t)&&(m.copy(d).multiplyScalar(g.y).addScaledVector(p,-y.y).multiplyScalar(_t),w.copy(p).multiplyScalar(y.x).addScaledVector(d,-g.x).multiplyScalar(_t),c[P].add(m),c[X].add(m),c[rt].add(m),h[P].add(w),h[X].add(w),h[rt].add(w))}let I=this.groups;I.length===0&&(I=[{start:0,count:n.length}]);for(let P=0,X=I.length;P<X;++P){let rt=I[P],_t=rt.start,k=rt.count;for(let q=_t,j=_t+k;q<j;q+=3)v(n[q+0],n[q+1],n[q+2])}let H=new O,U=new O,N=new O,Y=new O;function b(P){N.fromArray(r,P*3),Y.copy(N);let X=c[P];H.copy(X),H.sub(N.multiplyScalar(N.dot(X))).normalize(),U.crossVectors(Y,X);let _t=U.dot(h[P])<0?-1:1;l[P*4]=H.x,l[P*4+1]=H.y,l[P*4+2]=H.z,l[P*4+3]=_t}for(let P=0,X=I.length;P<X;++P){let rt=I[P],_t=rt.start,k=rt.count;for(let q=_t,j=_t+k;q<j;q+=3)b(n[q+0]),b(n[q+1]),b(n[q+2])}}computeVertexNormals(){let t=this.index,e=this.getAttribute("position");if(e!==void 0){let n=this.getAttribute("normal");if(n===void 0)n=new gn(new Float32Array(e.count*3),3),this.setAttribute("normal",n);else for(let d=0,p=n.count;d<p;d++)n.setXYZ(d,0,0,0);let s=new O,r=new O,a=new O,o=new O,l=new O,c=new O,h=new O,u=new O;if(t)for(let d=0,p=t.count;d<p;d+=3){let x=t.getX(d+0),y=t.getX(d+1),g=t.getX(d+2);s.fromBufferAttribute(e,x),r.fromBufferAttribute(e,y),a.fromBufferAttribute(e,g),h.subVectors(a,r),u.subVectors(s,r),h.cross(u),o.fromBufferAttribute(n,x),l.fromBufferAttribute(n,y),c.fromBufferAttribute(n,g),o.add(h),l.add(h),c.add(h),n.setXYZ(x,o.x,o.y,o.z),n.setXYZ(y,l.x,l.y,l.z),n.setXYZ(g,c.x,c.y,c.z)}else for(let d=0,p=e.count;d<p;d+=3)s.fromBufferAttribute(e,d+0),r.fromBufferAttribute(e,d+1),a.fromBufferAttribute(e,d+2),h.subVectors(a,r),u.subVectors(s,r),h.cross(u),n.setXYZ(d+0,h.x,h.y,h.z),n.setXYZ(d+1,h.x,h.y,h.z),n.setXYZ(d+2,h.x,h.y,h.z);this.normalizeNormals(),n.needsUpdate=!0}}normalizeNormals(){let t=this.attributes.normal;for(let e=0,n=t.count;e<n;e++)ln.fromBufferAttribute(t,e),ln.normalize(),t.setXYZ(e,ln.x,ln.y,ln.z)}toNonIndexed(){function t(o,l){let c=o.array,h=o.itemSize,u=o.normalized,d=new c.constructor(l.length*h),p=0,x=0;for(let y=0,g=l.length;y<g;y++){o.isInterleavedBufferAttribute?p=l[y]*o.data.stride+o.offset:p=l[y]*h;for(let m=0;m<h;m++)d[x++]=c[p++]}return new gn(d,h,u)}if(this.index===null)return console.warn("THREE.BufferGeometry.toNonIndexed(): BufferGeometry is already non-indexed."),this;let e=new i,n=this.index.array,s=this.attributes;for(let o in s){let l=s[o],c=t(l,n);e.setAttribute(o,c)}let r=this.morphAttributes;for(let o in r){let l=[],c=r[o];for(let h=0,u=c.length;h<u;h++){let d=c[h],p=t(d,n);l.push(p)}e.morphAttributes[o]=l}e.morphTargetsRelative=this.morphTargetsRelative;let a=this.groups;for(let o=0,l=a.length;o<l;o++){let c=a[o];e.addGroup(c.start,c.count,c.materialIndex)}return e}toJSON(){let t={metadata:{version:4.6,type:"BufferGeometry",generator:"BufferGeometry.toJSON"}};if(t.uuid=this.uuid,t.type=this.type,this.name!==""&&(t.name=this.name),Object.keys(this.userData).length>0&&(t.userData=this.userData),this.parameters!==void 0){let l=this.parameters;for(let c in l)l[c]!==void 0&&(t[c]=l[c]);return t}t.data={attributes:{}};let e=this.index;e!==null&&(t.data.index={type:e.array.constructor.name,array:Array.prototype.slice.call(e.array)});let n=this.attributes;for(let l in n){let c=n[l];t.data.attributes[l]=c.toJSON(t.data)}let s={},r=!1;for(let l in this.morphAttributes){let c=this.morphAttributes[l],h=[];for(let u=0,d=c.length;u<d;u++){let p=c[u];h.push(p.toJSON(t.data))}h.length>0&&(s[l]=h,r=!0)}r&&(t.data.morphAttributes=s,t.data.morphTargetsRelative=this.morphTargetsRelative);let a=this.groups;a.length>0&&(t.data.groups=JSON.parse(JSON.stringify(a)));let o=this.boundingSphere;return o!==null&&(t.data.boundingSphere={center:o.center.toArray(),radius:o.radius}),t}clone(){return new this.constructor().copy(this)}copy(t){this.index=null,this.attributes={},this.morphAttributes={},this.groups=[],this.boundingBox=null,this.boundingSphere=null;let e={};this.name=t.name;let n=t.index;n!==null&&this.setIndex(n.clone(e));let s=t.attributes;for(let c in s){let h=s[c];this.setAttribute(c,h.clone(e))}let r=t.morphAttributes;for(let c in r){let h=[],u=r[c];for(let d=0,p=u.length;d<p;d++)h.push(u[d].clone(e));this.morphAttributes[c]=h}this.morphTargetsRelative=t.morphTargetsRelative;let a=t.groups;for(let c=0,h=a.length;c<h;c++){let u=a[c];this.addGroup(u.start,u.count,u.materialIndex)}let o=t.boundingBox;o!==null&&(this.boundingBox=o.clone());let l=t.boundingSphere;return l!==null&&(this.boundingSphere=l.clone()),this.drawRange.start=t.drawRange.start,this.drawRange.count=t.drawRange.count,this.userData=t.userData,this}dispose(){this.dispatchEvent({type:"dispose"})}},$h=new De,os=new Ur,vo=new Zi,Jh=new O,Fs=new O,Os=new O,Bs=new O,al=new O,yo=new O,Mo=new xt,So=new xt,bo=new xt,Kh=new O,jh=new O,Qh=new O,Eo=new O,wo=new O,Ce=class extends bn{constructor(t=new qe,e=new gs){super(),this.isMesh=!0,this.type="Mesh",this.geometry=t,this.material=e,this.updateMorphTargets()}copy(t,e){return super.copy(t,e),t.morphTargetInfluences!==void 0&&(this.morphTargetInfluences=t.morphTargetInfluences.slice()),t.morphTargetDictionary!==void 0&&(this.morphTargetDictionary=Object.assign({},t.morphTargetDictionary)),this.material=Array.isArray(t.material)?t.material.slice():t.material,this.geometry=t.geometry,this}updateMorphTargets(){let e=this.geometry.morphAttributes,n=Object.keys(e);if(n.length>0){let s=e[n[0]];if(s!==void 0){this.morphTargetInfluences=[],this.morphTargetDictionary={};for(let r=0,a=s.length;r<a;r++){let o=s[r].name||String(r);this.morphTargetInfluences.push(0),this.morphTargetDictionary[o]=r}}}}getVertexPosition(t,e){let n=this.geometry,s=n.attributes.position,r=n.morphAttributes.position,a=n.morphTargetsRelative;e.fromBufferAttribute(s,t);let o=this.morphTargetInfluences;if(r&&o){yo.set(0,0,0);for(let l=0,c=r.length;l<c;l++){let h=o[l],u=r[l];h!==0&&(al.fromBufferAttribute(u,t),a?yo.addScaledVector(al,h):yo.addScaledVector(al.sub(e),h))}e.add(yo)}return e}raycast(t,e){let n=this.geometry,s=this.material,r=this.matrixWorld;s!==void 0&&(n.boundingSphere===null&&n.computeBoundingSphere(),vo.copy(n.boundingSphere),vo.applyMatrix4(r),os.copy(t.ray).recast(t.near),!(vo.containsPoint(os.origin)===!1&&(os.intersectSphere(vo,Jh)===null||os.origin.distanceToSquared(Jh)>(t.far-t.near)**2))&&($h.copy(r).invert(),os.copy(t.ray).applyMatrix4($h),!(n.boundingBox!==null&&os.intersectsBox(n.boundingBox)===!1)&&this._computeIntersections(t,e,os)))}_computeIntersections(t,e,n){let s,r=this.geometry,a=this.material,o=r.index,l=r.attributes.position,c=r.attributes.uv,h=r.attributes.uv1,u=r.attributes.normal,d=r.groups,p=r.drawRange;if(o!==null)if(Array.isArray(a))for(let x=0,y=d.length;x<y;x++){let g=d[x],m=a[g.materialIndex],w=Math.max(g.start,p.start),v=Math.min(o.count,Math.min(g.start+g.count,p.start+p.count));for(let I=w,H=v;I<H;I+=3){let U=o.getX(I),N=o.getX(I+1),Y=o.getX(I+2);s=To(this,m,t,n,c,h,u,U,N,Y),s&&(s.faceIndex=Math.floor(I/3),s.face.materialIndex=g.materialIndex,e.push(s))}}else{let x=Math.max(0,p.start),y=Math.min(o.count,p.start+p.count);for(let g=x,m=y;g<m;g+=3){let w=o.getX(g),v=o.getX(g+1),I=o.getX(g+2);s=To(this,a,t,n,c,h,u,w,v,I),s&&(s.faceIndex=Math.floor(g/3),e.push(s))}}else if(l!==void 0)if(Array.isArray(a))for(let x=0,y=d.length;x<y;x++){let g=d[x],m=a[g.materialIndex],w=Math.max(g.start,p.start),v=Math.min(l.count,Math.min(g.start+g.count,p.start+p.count));for(let I=w,H=v;I<H;I+=3){let U=I,N=I+1,Y=I+2;s=To(this,m,t,n,c,h,u,U,N,Y),s&&(s.faceIndex=Math.floor(I/3),s.face.materialIndex=g.materialIndex,e.push(s))}}else{let x=Math.max(0,p.start),y=Math.min(l.count,p.start+p.count);for(let g=x,m=y;g<m;g+=3){let w=g,v=g+1,I=g+2;s=To(this,a,t,n,c,h,u,w,v,I),s&&(s.faceIndex=Math.floor(g/3),e.push(s))}}}};function Yd(i,t,e,n,s,r,a,o){let l;if(t.side===Sn?l=n.intersectTriangle(a,r,s,!0,o):l=n.intersectTriangle(s,r,a,t.side===Yi,o),l===null)return null;wo.copy(o),wo.applyMatrix4(i.matrixWorld);let c=e.ray.origin.distanceTo(wo);return c<e.near||c>e.far?null:{distance:c,point:wo.clone(),object:i}}function To(i,t,e,n,s,r,a,o,l,c){i.getVertexPosition(o,Fs),i.getVertexPosition(l,Os),i.getVertexPosition(c,Bs);let h=Yd(i,t,e,n,Fs,Os,Bs,Eo);if(h){s&&(Mo.fromBufferAttribute(s,o),So.fromBufferAttribute(s,l),bo.fromBufferAttribute(s,c),h.uv=Ws.getInterpolation(Eo,Fs,Os,Bs,Mo,So,bo,new xt)),r&&(Mo.fromBufferAttribute(r,o),So.fromBufferAttribute(r,l),bo.fromBufferAttribute(r,c),h.uv1=Ws.getInterpolation(Eo,Fs,Os,Bs,Mo,So,bo,new xt),h.uv2=h.uv1),a&&(Kh.fromBufferAttribute(a,o),jh.fromBufferAttribute(a,l),Qh.fromBufferAttribute(a,c),h.normal=Ws.getInterpolation(Eo,Fs,Os,Bs,Kh,jh,Qh,new O),h.normal.dot(n.direction)>0&&h.normal.multiplyScalar(-1));let u={a:o,b:l,c,normal:new O,materialIndex:0};Ws.getNormal(Fs,Os,Bs,u.normal),h.face=u}return h}var Ae=class i extends qe{constructor(t=1,e=1,n=1,s=1,r=1,a=1){super(),this.type="BoxGeometry",this.parameters={width:t,height:e,depth:n,widthSegments:s,heightSegments:r,depthSegments:a};let o=this;s=Math.floor(s),r=Math.floor(r),a=Math.floor(a);let l=[],c=[],h=[],u=[],d=0,p=0;x("z","y","x",-1,-1,n,e,t,a,r,0),x("z","y","x",1,-1,n,e,-t,a,r,1),x("x","z","y",1,1,t,n,e,s,a,2),x("x","z","y",1,-1,t,n,-e,s,a,3),x("x","y","z",1,-1,t,e,n,s,r,4),x("x","y","z",-1,-1,t,e,-n,s,r,5),this.setIndex(l),this.setAttribute("position",new _e(c,3)),this.setAttribute("normal",new _e(h,3)),this.setAttribute("uv",new _e(u,2));function x(y,g,m,w,v,I,H,U,N,Y,b){let P=I/N,X=H/Y,rt=I/2,_t=H/2,k=U/2,q=N+1,j=Y+1,et=0,ut=0,tt=new O;for(let at=0;at<j;at++){let lt=at*X-_t;for(let Ut=0;Ut<q;Ut++){let nt=Ut*P-rt;tt[y]=nt*w,tt[g]=lt*v,tt[m]=k,c.push(tt.x,tt.y,tt.z),tt[y]=0,tt[g]=0,tt[m]=U>0?1:-1,h.push(tt.x,tt.y,tt.z),u.push(Ut/N),u.push(1-at/Y),et+=1}}for(let at=0;at<Y;at++)for(let lt=0;lt<N;lt++){let Ut=d+lt+q*at,nt=d+lt+q*(at+1),ht=d+(lt+1)+q*(at+1),Dt=d+(lt+1)+q*at;l.push(Ut,nt,Dt),l.push(nt,ht,Dt),ut+=6}o.addGroup(p,ut,b),p+=ut,d+=et}}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.width,t.height,t.depth,t.widthSegments,t.heightSegments,t.depthSegments)}};function nr(i){let t={};for(let e in i){t[e]={};for(let n in i[e]){let s=i[e][n];s&&(s.isColor||s.isMatrix3||s.isMatrix4||s.isVector2||s.isVector3||s.isVector4||s.isTexture||s.isQuaternion)?s.isRenderTargetTexture?(console.warn("UniformsUtils: Textures of render targets cannot be cloned via cloneUniforms() or mergeUniforms()."),t[e][n]=null):t[e][n]=s.clone():Array.isArray(s)?t[e][n]=s.slice():t[e][n]=s}}return t}function Tn(i){let t={};for(let e=0;e<i.length;e++){let n=nr(i[e]);for(let s in n)t[s]=n[s]}return t}function qd(i){let t=[];for(let e=0;e<i.length;e++)t.push(i[e].clone());return t}function $u(i){return i.getRenderTarget()===null?i.outputColorSpace:Ue.workingColorSpace}var gc={clone:nr,merge:Tn},Zd=`void main() {
	gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );
}`,$d=`void main() {
	gl_FragColor = vec4( 1.0, 0.0, 0.0, 1.0 );
}`,_n=class extends $i{constructor(t){super(),this.isShaderMaterial=!0,this.type="ShaderMaterial",this.defines={},this.uniforms={},this.uniformsGroups=[],this.vertexShader=Zd,this.fragmentShader=$d,this.linewidth=1,this.wireframe=!1,this.wireframeLinewidth=1,this.fog=!1,this.lights=!1,this.clipping=!1,this.forceSinglePass=!0,this.extensions={derivatives:!1,fragDepth:!1,drawBuffers:!1,shaderTextureLOD:!1,clipCullDistance:!1},this.defaultAttributeValues={color:[1,1,1],uv:[0,0],uv1:[0,0]},this.index0AttributeName=void 0,this.uniformsNeedUpdate=!1,this.glslVersion=null,t!==void 0&&this.setValues(t)}copy(t){return super.copy(t),this.fragmentShader=t.fragmentShader,this.vertexShader=t.vertexShader,this.uniforms=nr(t.uniforms),this.uniformsGroups=qd(t.uniformsGroups),this.defines=Object.assign({},t.defines),this.wireframe=t.wireframe,this.wireframeLinewidth=t.wireframeLinewidth,this.fog=t.fog,this.lights=t.lights,this.clipping=t.clipping,this.extensions=Object.assign({},t.extensions),this.glslVersion=t.glslVersion,this}toJSON(t){let e=super.toJSON(t);e.glslVersion=this.glslVersion,e.uniforms={};for(let s in this.uniforms){let a=this.uniforms[s].value;a&&a.isTexture?e.uniforms[s]={type:"t",value:a.toJSON(t).uuid}:a&&a.isColor?e.uniforms[s]={type:"c",value:a.getHex()}:a&&a.isVector2?e.uniforms[s]={type:"v2",value:a.toArray()}:a&&a.isVector3?e.uniforms[s]={type:"v3",value:a.toArray()}:a&&a.isVector4?e.uniforms[s]={type:"v4",value:a.toArray()}:a&&a.isMatrix3?e.uniforms[s]={type:"m3",value:a.toArray()}:a&&a.isMatrix4?e.uniforms[s]={type:"m4",value:a.toArray()}:e.uniforms[s]={value:a}}Object.keys(this.defines).length>0&&(e.defines=this.defines),e.vertexShader=this.vertexShader,e.fragmentShader=this.fragmentShader,e.lights=this.lights,e.clipping=this.clipping;let n={};for(let s in this.extensions)this.extensions[s]===!0&&(n[s]=!0);return Object.keys(n).length>0&&(e.extensions=n),e}},Jo=class extends bn{constructor(){super(),this.isCamera=!0,this.type="Camera",this.matrixWorldInverse=new De,this.projectionMatrix=new De,this.projectionMatrixInverse=new De,this.coordinateSystem=Ti}copy(t,e){return super.copy(t,e),this.matrixWorldInverse.copy(t.matrixWorldInverse),this.projectionMatrix.copy(t.projectionMatrix),this.projectionMatrixInverse.copy(t.projectionMatrixInverse),this.coordinateSystem=t.coordinateSystem,this}getWorldDirection(t){return super.getWorldDirection(t).negate()}updateMatrixWorld(t){super.updateMatrixWorld(t),this.matrixWorldInverse.copy(this.matrixWorld).invert()}updateWorldMatrix(t,e){super.updateWorldMatrix(t,e),this.matrixWorldInverse.copy(this.matrixWorld).invert()}clone(){return new this.constructor().copy(this)}},Mn=class extends Jo{constructor(t=50,e=1,n=.1,s=2e3){super(),this.isPerspectiveCamera=!0,this.type="PerspectiveCamera",this.fov=t,this.zoom=1,this.near=n,this.far=s,this.focus=10,this.aspect=e,this.view=null,this.filmGauge=35,this.filmOffset=0,this.updateProjectionMatrix()}copy(t,e){return super.copy(t,e),this.fov=t.fov,this.zoom=t.zoom,this.near=t.near,this.far=t.far,this.focus=t.focus,this.aspect=t.aspect,this.view=t.view===null?null:Object.assign({},t.view),this.filmGauge=t.filmGauge,this.filmOffset=t.filmOffset,this}setFocalLength(t){let e=.5*this.getFilmHeight()/t;this.fov=Ir*2*Math.atan(e),this.updateProjectionMatrix()}getFocalLength(){let t=Math.tan(Sr*.5*this.fov);return .5*this.getFilmHeight()/t}getEffectiveFOV(){return Ir*2*Math.atan(Math.tan(Sr*.5*this.fov)/this.zoom)}getFilmWidth(){return this.filmGauge*Math.min(this.aspect,1)}getFilmHeight(){return this.filmGauge/Math.max(this.aspect,1)}setViewOffset(t,e,n,s,r,a){this.aspect=t/e,this.view===null&&(this.view={enabled:!0,fullWidth:1,fullHeight:1,offsetX:0,offsetY:0,width:1,height:1}),this.view.enabled=!0,this.view.fullWidth=t,this.view.fullHeight=e,this.view.offsetX=n,this.view.offsetY=s,this.view.width=r,this.view.height=a,this.updateProjectionMatrix()}clearViewOffset(){this.view!==null&&(this.view.enabled=!1),this.updateProjectionMatrix()}updateProjectionMatrix(){let t=this.near,e=t*Math.tan(Sr*.5*this.fov)/this.zoom,n=2*e,s=this.aspect*n,r=-.5*s,a=this.view;if(this.view!==null&&this.view.enabled){let l=a.fullWidth,c=a.fullHeight;r+=a.offsetX*s/l,e-=a.offsetY*n/c,s*=a.width/l,n*=a.height/c}let o=this.filmOffset;o!==0&&(r+=t*o/this.getFilmWidth()),this.projectionMatrix.makePerspective(r,r+s,e,e-n,t,this.far,this.coordinateSystem),this.projectionMatrixInverse.copy(this.projectionMatrix).invert()}toJSON(t){let e=super.toJSON(t);return e.object.fov=this.fov,e.object.zoom=this.zoom,e.object.near=this.near,e.object.far=this.far,e.object.focus=this.focus,e.object.aspect=this.aspect,this.view!==null&&(e.object.view=Object.assign({},this.view)),e.object.filmGauge=this.filmGauge,e.object.filmOffset=this.filmOffset,e}},zs=-90,Hs=1,Rl=class extends bn{constructor(t,e,n){super(),this.type="CubeCamera",this.renderTarget=n,this.coordinateSystem=null,this.activeMipmapLevel=0;let s=new Mn(zs,Hs,t,e);s.layers=this.layers,this.add(s);let r=new Mn(zs,Hs,t,e);r.layers=this.layers,this.add(r);let a=new Mn(zs,Hs,t,e);a.layers=this.layers,this.add(a);let o=new Mn(zs,Hs,t,e);o.layers=this.layers,this.add(o);let l=new Mn(zs,Hs,t,e);l.layers=this.layers,this.add(l);let c=new Mn(zs,Hs,t,e);c.layers=this.layers,this.add(c)}updateCoordinateSystem(){let t=this.coordinateSystem,e=this.children.concat(),[n,s,r,a,o,l]=e;for(let c of e)this.remove(c);if(t===Ti)n.up.set(0,1,0),n.lookAt(1,0,0),s.up.set(0,1,0),s.lookAt(-1,0,0),r.up.set(0,0,-1),r.lookAt(0,1,0),a.up.set(0,0,1),a.lookAt(0,-1,0),o.up.set(0,1,0),o.lookAt(0,0,1),l.up.set(0,1,0),l.lookAt(0,0,-1);else if(t===Go)n.up.set(0,-1,0),n.lookAt(-1,0,0),s.up.set(0,-1,0),s.lookAt(1,0,0),r.up.set(0,0,1),r.lookAt(0,1,0),a.up.set(0,0,-1),a.lookAt(0,-1,0),o.up.set(0,-1,0),o.lookAt(0,0,1),l.up.set(0,-1,0),l.lookAt(0,0,-1);else throw new Error("THREE.CubeCamera.updateCoordinateSystem(): Invalid coordinate system: "+t);for(let c of e)this.add(c),c.updateMatrixWorld()}update(t,e){this.parent===null&&this.updateMatrixWorld();let{renderTarget:n,activeMipmapLevel:s}=this;this.coordinateSystem!==t.coordinateSystem&&(this.coordinateSystem=t.coordinateSystem,this.updateCoordinateSystem());let[r,a,o,l,c,h]=this.children,u=t.getRenderTarget(),d=t.getActiveCubeFace(),p=t.getActiveMipmapLevel(),x=t.xr.enabled;t.xr.enabled=!1;let y=n.texture.generateMipmaps;n.texture.generateMipmaps=!1,t.setRenderTarget(n,0,s),t.render(e,r),t.setRenderTarget(n,1,s),t.render(e,a),t.setRenderTarget(n,2,s),t.render(e,o),t.setRenderTarget(n,3,s),t.render(e,l),t.setRenderTarget(n,4,s),t.render(e,c),n.texture.generateMipmaps=y,t.setRenderTarget(n,5,s),t.render(e,h),t.setRenderTarget(u,d,p),t.xr.enabled=x,n.texture.needsPMREMUpdate=!0}},Ko=class extends Dn{constructor(t,e,n,s,r,a,o,l,c,h){t=t!==void 0?t:[],e=e!==void 0?e:Qs,super(t,e,n,s,r,a,o,l,c,h),this.isCubeTexture=!0,this.flipY=!1}get images(){return this.image}set images(t){this.image=t}},Cl=class extends Ri{constructor(t=1,e={}){super(t,t,e),this.isWebGLCubeRenderTarget=!0;let n={width:t,height:t,depth:1},s=[n,n,n,n,n,n];e.encoding!==void 0&&(Er("THREE.WebGLCubeRenderTarget: option.encoding has been replaced by option.colorSpace."),e.colorSpace=e.encoding===ds?Je:Vn),this.texture=new Ko(s,e.mapping,e.wrapS,e.wrapT,e.magFilter,e.minFilter,e.format,e.type,e.anisotropy,e.colorSpace),this.texture.isRenderTargetTexture=!0,this.texture.generateMipmaps=e.generateMipmaps!==void 0?e.generateMipmaps:!1,this.texture.minFilter=e.minFilter!==void 0?e.minFilter:kn}fromEquirectangularTexture(t,e){this.texture.type=e.type,this.texture.colorSpace=e.colorSpace,this.texture.generateMipmaps=e.generateMipmaps,this.texture.minFilter=e.minFilter,this.texture.magFilter=e.magFilter;let n={uniforms:{tEquirect:{value:null}},vertexShader:`

				varying vec3 vWorldDirection;

				vec3 transformDirection( in vec3 dir, in mat4 matrix ) {

					return normalize( ( matrix * vec4( dir, 0.0 ) ).xyz );

				}

				void main() {

					vWorldDirection = transformDirection( position, modelMatrix );

					#include <begin_vertex>
					#include <project_vertex>

				}
			`,fragmentShader:`

				uniform sampler2D tEquirect;

				varying vec3 vWorldDirection;

				#include <common>

				void main() {

					vec3 direction = normalize( vWorldDirection );

					vec2 sampleUV = equirectUv( direction );

					gl_FragColor = texture2D( tEquirect, sampleUV );

				}
			`},s=new Ae(5,5,5),r=new _n({name:"CubemapFromEquirect",uniforms:nr(n.uniforms),vertexShader:n.vertexShader,fragmentShader:n.fragmentShader,side:Sn,blending:Gi});r.uniforms.tEquirect.value=e;let a=new Ce(s,r),o=e.minFilter;return e.minFilter===Cr&&(e.minFilter=kn),new Rl(1,10,this).update(t,a),e.minFilter=o,a.geometry.dispose(),a.material.dispose(),this}clear(t,e,n,s){let r=t.getRenderTarget();for(let a=0;a<6;a++)t.setRenderTarget(this,a),t.clear(e,n,s);t.setRenderTarget(r)}},ll=new O,Jd=new O,Kd=new ve,wi=class{constructor(t=new O(1,0,0),e=0){this.isPlane=!0,this.normal=t,this.constant=e}set(t,e){return this.normal.copy(t),this.constant=e,this}setComponents(t,e,n,s){return this.normal.set(t,e,n),this.constant=s,this}setFromNormalAndCoplanarPoint(t,e){return this.normal.copy(t),this.constant=-e.dot(this.normal),this}setFromCoplanarPoints(t,e,n){let s=ll.subVectors(n,e).cross(Jd.subVectors(t,e)).normalize();return this.setFromNormalAndCoplanarPoint(s,t),this}copy(t){return this.normal.copy(t.normal),this.constant=t.constant,this}normalize(){let t=1/this.normal.length();return this.normal.multiplyScalar(t),this.constant*=t,this}negate(){return this.constant*=-1,this.normal.negate(),this}distanceToPoint(t){return this.normal.dot(t)+this.constant}distanceToSphere(t){return this.distanceToPoint(t.center)-t.radius}projectPoint(t,e){return e.copy(t).addScaledVector(this.normal,-this.distanceToPoint(t))}intersectLine(t,e){let n=t.delta(ll),s=this.normal.dot(n);if(s===0)return this.distanceToPoint(t.start)===0?e.copy(t.start):null;let r=-(t.start.dot(this.normal)+this.constant)/s;return r<0||r>1?null:e.copy(t.start).addScaledVector(n,r)}intersectsLine(t){let e=this.distanceToPoint(t.start),n=this.distanceToPoint(t.end);return e<0&&n>0||n<0&&e>0}intersectsBox(t){return t.intersectsPlane(this)}intersectsSphere(t){return t.intersectsPlane(this)}coplanarPoint(t){return t.copy(this.normal).multiplyScalar(-this.constant)}applyMatrix4(t,e){let n=e||Kd.getNormalMatrix(t),s=this.coplanarPoint(ll).applyMatrix4(t),r=this.normal.applyMatrix3(n).normalize();return this.constant=-s.dot(r),this}translate(t){return this.constant-=t.dot(this.normal),this}equals(t){return t.normal.equals(this.normal)&&t.constant===this.constant}clone(){return new this.constructor().copy(this)}},as=new Zi,Ao=new O,Nr=class{constructor(t=new wi,e=new wi,n=new wi,s=new wi,r=new wi,a=new wi){this.planes=[t,e,n,s,r,a]}set(t,e,n,s,r,a){let o=this.planes;return o[0].copy(t),o[1].copy(e),o[2].copy(n),o[3].copy(s),o[4].copy(r),o[5].copy(a),this}copy(t){let e=this.planes;for(let n=0;n<6;n++)e[n].copy(t.planes[n]);return this}setFromProjectionMatrix(t,e=Ti){let n=this.planes,s=t.elements,r=s[0],a=s[1],o=s[2],l=s[3],c=s[4],h=s[5],u=s[6],d=s[7],p=s[8],x=s[9],y=s[10],g=s[11],m=s[12],w=s[13],v=s[14],I=s[15];if(n[0].setComponents(l-r,d-c,g-p,I-m).normalize(),n[1].setComponents(l+r,d+c,g+p,I+m).normalize(),n[2].setComponents(l+a,d+h,g+x,I+w).normalize(),n[3].setComponents(l-a,d-h,g-x,I-w).normalize(),n[4].setComponents(l-o,d-u,g-y,I-v).normalize(),e===Ti)n[5].setComponents(l+o,d+u,g+y,I+v).normalize();else if(e===Go)n[5].setComponents(o,u,y,v).normalize();else throw new Error("THREE.Frustum.setFromProjectionMatrix(): Invalid coordinate system: "+e);return this}intersectsObject(t){if(t.boundingSphere!==void 0)t.boundingSphere===null&&t.computeBoundingSphere(),as.copy(t.boundingSphere).applyMatrix4(t.matrixWorld);else{let e=t.geometry;e.boundingSphere===null&&e.computeBoundingSphere(),as.copy(e.boundingSphere).applyMatrix4(t.matrixWorld)}return this.intersectsSphere(as)}intersectsSprite(t){return as.center.set(0,0,0),as.radius=.7071067811865476,as.applyMatrix4(t.matrixWorld),this.intersectsSphere(as)}intersectsSphere(t){let e=this.planes,n=t.center,s=-t.radius;for(let r=0;r<6;r++)if(e[r].distanceToPoint(n)<s)return!1;return!0}intersectsBox(t){let e=this.planes;for(let n=0;n<6;n++){let s=e[n];if(Ao.x=s.normal.x>0?t.max.x:t.min.x,Ao.y=s.normal.y>0?t.max.y:t.min.y,Ao.z=s.normal.z>0?t.max.z:t.min.z,s.distanceToPoint(Ao)<0)return!1}return!0}containsPoint(t){let e=this.planes;for(let n=0;n<6;n++)if(e[n].distanceToPoint(t)<0)return!1;return!0}clone(){return new this.constructor().copy(this)}};function Ju(){let i=null,t=!1,e=null,n=null;function s(r,a){e(r,a),n=i.requestAnimationFrame(s)}return{start:function(){t!==!0&&e!==null&&(n=i.requestAnimationFrame(s),t=!0)},stop:function(){i.cancelAnimationFrame(n),t=!1},setAnimationLoop:function(r){e=r},setContext:function(r){i=r}}}function jd(i,t){let e=t.isWebGL2,n=new WeakMap;function s(c,h){let u=c.array,d=c.usage,p=u.byteLength,x=i.createBuffer();i.bindBuffer(h,x),i.bufferData(h,u,d),c.onUploadCallback();let y;if(u instanceof Float32Array)y=i.FLOAT;else if(u instanceof Uint16Array)if(c.isFloat16BufferAttribute)if(e)y=i.HALF_FLOAT;else throw new Error("THREE.WebGLAttributes: Usage of Float16BufferAttribute requires WebGL2.");else y=i.UNSIGNED_SHORT;else if(u instanceof Int16Array)y=i.SHORT;else if(u instanceof Uint32Array)y=i.UNSIGNED_INT;else if(u instanceof Int32Array)y=i.INT;else if(u instanceof Int8Array)y=i.BYTE;else if(u instanceof Uint8Array)y=i.UNSIGNED_BYTE;else if(u instanceof Uint8ClampedArray)y=i.UNSIGNED_BYTE;else throw new Error("THREE.WebGLAttributes: Unsupported buffer data format: "+u);return{buffer:x,type:y,bytesPerElement:u.BYTES_PER_ELEMENT,version:c.version,size:p}}function r(c,h,u){let d=h.array,p=h._updateRange,x=h.updateRanges;if(i.bindBuffer(u,c),p.count===-1&&x.length===0&&i.bufferSubData(u,0,d),x.length!==0){for(let y=0,g=x.length;y<g;y++){let m=x[y];e?i.bufferSubData(u,m.start*d.BYTES_PER_ELEMENT,d,m.start,m.count):i.bufferSubData(u,m.start*d.BYTES_PER_ELEMENT,d.subarray(m.start,m.start+m.count))}h.clearUpdateRanges()}p.count!==-1&&(e?i.bufferSubData(u,p.offset*d.BYTES_PER_ELEMENT,d,p.offset,p.count):i.bufferSubData(u,p.offset*d.BYTES_PER_ELEMENT,d.subarray(p.offset,p.offset+p.count)),p.count=-1),h.onUploadCallback()}function a(c){return c.isInterleavedBufferAttribute&&(c=c.data),n.get(c)}function o(c){c.isInterleavedBufferAttribute&&(c=c.data);let h=n.get(c);h&&(i.deleteBuffer(h.buffer),n.delete(c))}function l(c,h){if(c.isGLBufferAttribute){let d=n.get(c);(!d||d.version<c.version)&&n.set(c,{buffer:c.buffer,type:c.type,bytesPerElement:c.elementSize,version:c.version});return}c.isInterleavedBufferAttribute&&(c=c.data);let u=n.get(c);if(u===void 0)n.set(c,s(c,h));else if(u.version<c.version){if(u.size!==c.array.byteLength)throw new Error("THREE.WebGLAttributes: The size of the buffer attribute's array buffer does not match the original size. Resizing buffer attributes is not supported.");r(u.buffer,c,h),u.version=c.version}}return{get:a,remove:o,update:l}}var hn=class i extends qe{constructor(t=1,e=1,n=1,s=1){super(),this.type="PlaneGeometry",this.parameters={width:t,height:e,widthSegments:n,heightSegments:s};let r=t/2,a=e/2,o=Math.floor(n),l=Math.floor(s),c=o+1,h=l+1,u=t/o,d=e/l,p=[],x=[],y=[],g=[];for(let m=0;m<h;m++){let w=m*d-a;for(let v=0;v<c;v++){let I=v*u-r;x.push(I,-w,0),y.push(0,0,1),g.push(v/o),g.push(1-m/l)}}for(let m=0;m<l;m++)for(let w=0;w<o;w++){let v=w+c*m,I=w+c*(m+1),H=w+1+c*(m+1),U=w+1+c*m;p.push(v,I,U),p.push(I,H,U)}this.setIndex(p),this.setAttribute("position",new _e(x,3)),this.setAttribute("normal",new _e(y,3)),this.setAttribute("uv",new _e(g,2))}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.width,t.height,t.widthSegments,t.heightSegments)}},Qd=`#ifdef USE_ALPHAHASH
	if ( diffuseColor.a < getAlphaHashThreshold( vPosition ) ) discard;
#endif`,tp=`#ifdef USE_ALPHAHASH
	const float ALPHA_HASH_SCALE = 0.05;
	float hash2D( vec2 value ) {
		return fract( 1.0e4 * sin( 17.0 * value.x + 0.1 * value.y ) * ( 0.1 + abs( sin( 13.0 * value.y + value.x ) ) ) );
	}
	float hash3D( vec3 value ) {
		return hash2D( vec2( hash2D( value.xy ), value.z ) );
	}
	float getAlphaHashThreshold( vec3 position ) {
		float maxDeriv = max(
			length( dFdx( position.xyz ) ),
			length( dFdy( position.xyz ) )
		);
		float pixScale = 1.0 / ( ALPHA_HASH_SCALE * maxDeriv );
		vec2 pixScales = vec2(
			exp2( floor( log2( pixScale ) ) ),
			exp2( ceil( log2( pixScale ) ) )
		);
		vec2 alpha = vec2(
			hash3D( floor( pixScales.x * position.xyz ) ),
			hash3D( floor( pixScales.y * position.xyz ) )
		);
		float lerpFactor = fract( log2( pixScale ) );
		float x = ( 1.0 - lerpFactor ) * alpha.x + lerpFactor * alpha.y;
		float a = min( lerpFactor, 1.0 - lerpFactor );
		vec3 cases = vec3(
			x * x / ( 2.0 * a * ( 1.0 - a ) ),
			( x - 0.5 * a ) / ( 1.0 - a ),
			1.0 - ( ( 1.0 - x ) * ( 1.0 - x ) / ( 2.0 * a * ( 1.0 - a ) ) )
		);
		float threshold = ( x < ( 1.0 - a ) )
			? ( ( x < a ) ? cases.x : cases.y )
			: cases.z;
		return clamp( threshold , 1.0e-6, 1.0 );
	}
#endif`,ep=`#ifdef USE_ALPHAMAP
	diffuseColor.a *= texture2D( alphaMap, vAlphaMapUv ).g;
#endif`,np=`#ifdef USE_ALPHAMAP
	uniform sampler2D alphaMap;
#endif`,ip=`#ifdef USE_ALPHATEST
	if ( diffuseColor.a < alphaTest ) discard;
#endif`,sp=`#ifdef USE_ALPHATEST
	uniform float alphaTest;
#endif`,rp=`#ifdef USE_AOMAP
	float ambientOcclusion = ( texture2D( aoMap, vAoMapUv ).r - 1.0 ) * aoMapIntensity + 1.0;
	reflectedLight.indirectDiffuse *= ambientOcclusion;
	#if defined( USE_CLEARCOAT ) 
		clearcoatSpecularIndirect *= ambientOcclusion;
	#endif
	#if defined( USE_SHEEN ) 
		sheenSpecularIndirect *= ambientOcclusion;
	#endif
	#if defined( USE_ENVMAP ) && defined( STANDARD )
		float dotNV = saturate( dot( geometryNormal, geometryViewDir ) );
		reflectedLight.indirectSpecular *= computeSpecularOcclusion( dotNV, ambientOcclusion, material.roughness );
	#endif
#endif`,op=`#ifdef USE_AOMAP
	uniform sampler2D aoMap;
	uniform float aoMapIntensity;
#endif`,ap=`#ifdef USE_BATCHING
	attribute float batchId;
	uniform highp sampler2D batchingTexture;
	mat4 getBatchingMatrix( const in float i ) {
		int size = textureSize( batchingTexture, 0 ).x;
		int j = int( i ) * 4;
		int x = j % size;
		int y = j / size;
		vec4 v1 = texelFetch( batchingTexture, ivec2( x, y ), 0 );
		vec4 v2 = texelFetch( batchingTexture, ivec2( x + 1, y ), 0 );
		vec4 v3 = texelFetch( batchingTexture, ivec2( x + 2, y ), 0 );
		vec4 v4 = texelFetch( batchingTexture, ivec2( x + 3, y ), 0 );
		return mat4( v1, v2, v3, v4 );
	}
#endif`,lp=`#ifdef USE_BATCHING
	mat4 batchingMatrix = getBatchingMatrix( batchId );
#endif`,cp=`vec3 transformed = vec3( position );
#ifdef USE_ALPHAHASH
	vPosition = vec3( position );
#endif`,hp=`vec3 objectNormal = vec3( normal );
#ifdef USE_TANGENT
	vec3 objectTangent = vec3( tangent.xyz );
#endif`,up=`float G_BlinnPhong_Implicit( ) {
	return 0.25;
}
float D_BlinnPhong( const in float shininess, const in float dotNH ) {
	return RECIPROCAL_PI * ( shininess * 0.5 + 1.0 ) * pow( dotNH, shininess );
}
vec3 BRDF_BlinnPhong( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in vec3 specularColor, const in float shininess ) {
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNH = saturate( dot( normal, halfDir ) );
	float dotVH = saturate( dot( viewDir, halfDir ) );
	vec3 F = F_Schlick( specularColor, 1.0, dotVH );
	float G = G_BlinnPhong_Implicit( );
	float D = D_BlinnPhong( shininess, dotNH );
	return F * ( G * D );
} // validated`,fp=`#ifdef USE_IRIDESCENCE
	const mat3 XYZ_TO_REC709 = mat3(
		 3.2404542, -0.9692660,  0.0556434,
		-1.5371385,  1.8760108, -0.2040259,
		-0.4985314,  0.0415560,  1.0572252
	);
	vec3 Fresnel0ToIor( vec3 fresnel0 ) {
		vec3 sqrtF0 = sqrt( fresnel0 );
		return ( vec3( 1.0 ) + sqrtF0 ) / ( vec3( 1.0 ) - sqrtF0 );
	}
	vec3 IorToFresnel0( vec3 transmittedIor, float incidentIor ) {
		return pow2( ( transmittedIor - vec3( incidentIor ) ) / ( transmittedIor + vec3( incidentIor ) ) );
	}
	float IorToFresnel0( float transmittedIor, float incidentIor ) {
		return pow2( ( transmittedIor - incidentIor ) / ( transmittedIor + incidentIor ));
	}
	vec3 evalSensitivity( float OPD, vec3 shift ) {
		float phase = 2.0 * PI * OPD * 1.0e-9;
		vec3 val = vec3( 5.4856e-13, 4.4201e-13, 5.2481e-13 );
		vec3 pos = vec3( 1.6810e+06, 1.7953e+06, 2.2084e+06 );
		vec3 var = vec3( 4.3278e+09, 9.3046e+09, 6.6121e+09 );
		vec3 xyz = val * sqrt( 2.0 * PI * var ) * cos( pos * phase + shift ) * exp( - pow2( phase ) * var );
		xyz.x += 9.7470e-14 * sqrt( 2.0 * PI * 4.5282e+09 ) * cos( 2.2399e+06 * phase + shift[ 0 ] ) * exp( - 4.5282e+09 * pow2( phase ) );
		xyz /= 1.0685e-7;
		vec3 rgb = XYZ_TO_REC709 * xyz;
		return rgb;
	}
	vec3 evalIridescence( float outsideIOR, float eta2, float cosTheta1, float thinFilmThickness, vec3 baseF0 ) {
		vec3 I;
		float iridescenceIOR = mix( outsideIOR, eta2, smoothstep( 0.0, 0.03, thinFilmThickness ) );
		float sinTheta2Sq = pow2( outsideIOR / iridescenceIOR ) * ( 1.0 - pow2( cosTheta1 ) );
		float cosTheta2Sq = 1.0 - sinTheta2Sq;
		if ( cosTheta2Sq < 0.0 ) {
			return vec3( 1.0 );
		}
		float cosTheta2 = sqrt( cosTheta2Sq );
		float R0 = IorToFresnel0( iridescenceIOR, outsideIOR );
		float R12 = F_Schlick( R0, 1.0, cosTheta1 );
		float T121 = 1.0 - R12;
		float phi12 = 0.0;
		if ( iridescenceIOR < outsideIOR ) phi12 = PI;
		float phi21 = PI - phi12;
		vec3 baseIOR = Fresnel0ToIor( clamp( baseF0, 0.0, 0.9999 ) );		vec3 R1 = IorToFresnel0( baseIOR, iridescenceIOR );
		vec3 R23 = F_Schlick( R1, 1.0, cosTheta2 );
		vec3 phi23 = vec3( 0.0 );
		if ( baseIOR[ 0 ] < iridescenceIOR ) phi23[ 0 ] = PI;
		if ( baseIOR[ 1 ] < iridescenceIOR ) phi23[ 1 ] = PI;
		if ( baseIOR[ 2 ] < iridescenceIOR ) phi23[ 2 ] = PI;
		float OPD = 2.0 * iridescenceIOR * thinFilmThickness * cosTheta2;
		vec3 phi = vec3( phi21 ) + phi23;
		vec3 R123 = clamp( R12 * R23, 1e-5, 0.9999 );
		vec3 r123 = sqrt( R123 );
		vec3 Rs = pow2( T121 ) * R23 / ( vec3( 1.0 ) - R123 );
		vec3 C0 = R12 + Rs;
		I = C0;
		vec3 Cm = Rs - T121;
		for ( int m = 1; m <= 2; ++ m ) {
			Cm *= r123;
			vec3 Sm = 2.0 * evalSensitivity( float( m ) * OPD, float( m ) * phi );
			I += Cm * Sm;
		}
		return max( I, vec3( 0.0 ) );
	}
#endif`,dp=`#ifdef USE_BUMPMAP
	uniform sampler2D bumpMap;
	uniform float bumpScale;
	vec2 dHdxy_fwd() {
		vec2 dSTdx = dFdx( vBumpMapUv );
		vec2 dSTdy = dFdy( vBumpMapUv );
		float Hll = bumpScale * texture2D( bumpMap, vBumpMapUv ).x;
		float dBx = bumpScale * texture2D( bumpMap, vBumpMapUv + dSTdx ).x - Hll;
		float dBy = bumpScale * texture2D( bumpMap, vBumpMapUv + dSTdy ).x - Hll;
		return vec2( dBx, dBy );
	}
	vec3 perturbNormalArb( vec3 surf_pos, vec3 surf_norm, vec2 dHdxy, float faceDirection ) {
		vec3 vSigmaX = normalize( dFdx( surf_pos.xyz ) );
		vec3 vSigmaY = normalize( dFdy( surf_pos.xyz ) );
		vec3 vN = surf_norm;
		vec3 R1 = cross( vSigmaY, vN );
		vec3 R2 = cross( vN, vSigmaX );
		float fDet = dot( vSigmaX, R1 ) * faceDirection;
		vec3 vGrad = sign( fDet ) * ( dHdxy.x * R1 + dHdxy.y * R2 );
		return normalize( abs( fDet ) * surf_norm - vGrad );
	}
#endif`,pp=`#if NUM_CLIPPING_PLANES > 0
	vec4 plane;
	#pragma unroll_loop_start
	for ( int i = 0; i < UNION_CLIPPING_PLANES; i ++ ) {
		plane = clippingPlanes[ i ];
		if ( dot( vClipPosition, plane.xyz ) > plane.w ) discard;
	}
	#pragma unroll_loop_end
	#if UNION_CLIPPING_PLANES < NUM_CLIPPING_PLANES
		bool clipped = true;
		#pragma unroll_loop_start
		for ( int i = UNION_CLIPPING_PLANES; i < NUM_CLIPPING_PLANES; i ++ ) {
			plane = clippingPlanes[ i ];
			clipped = ( dot( vClipPosition, plane.xyz ) > plane.w ) && clipped;
		}
		#pragma unroll_loop_end
		if ( clipped ) discard;
	#endif
#endif`,mp=`#if NUM_CLIPPING_PLANES > 0
	varying vec3 vClipPosition;
	uniform vec4 clippingPlanes[ NUM_CLIPPING_PLANES ];
#endif`,gp=`#if NUM_CLIPPING_PLANES > 0
	varying vec3 vClipPosition;
#endif`,_p=`#if NUM_CLIPPING_PLANES > 0
	vClipPosition = - mvPosition.xyz;
#endif`,xp=`#if defined( USE_COLOR_ALPHA )
	diffuseColor *= vColor;
#elif defined( USE_COLOR )
	diffuseColor.rgb *= vColor;
#endif`,vp=`#if defined( USE_COLOR_ALPHA )
	varying vec4 vColor;
#elif defined( USE_COLOR )
	varying vec3 vColor;
#endif`,yp=`#if defined( USE_COLOR_ALPHA )
	varying vec4 vColor;
#elif defined( USE_COLOR ) || defined( USE_INSTANCING_COLOR )
	varying vec3 vColor;
#endif`,Mp=`#if defined( USE_COLOR_ALPHA )
	vColor = vec4( 1.0 );
#elif defined( USE_COLOR ) || defined( USE_INSTANCING_COLOR )
	vColor = vec3( 1.0 );
#endif
#ifdef USE_COLOR
	vColor *= color;
#endif
#ifdef USE_INSTANCING_COLOR
	vColor.xyz *= instanceColor.xyz;
#endif`,Sp=`#define PI 3.141592653589793
#define PI2 6.283185307179586
#define PI_HALF 1.5707963267948966
#define RECIPROCAL_PI 0.3183098861837907
#define RECIPROCAL_PI2 0.15915494309189535
#define EPSILON 1e-6
#ifndef saturate
#define saturate( a ) clamp( a, 0.0, 1.0 )
#endif
#define whiteComplement( a ) ( 1.0 - saturate( a ) )
float pow2( const in float x ) { return x*x; }
vec3 pow2( const in vec3 x ) { return x*x; }
float pow3( const in float x ) { return x*x*x; }
float pow4( const in float x ) { float x2 = x*x; return x2*x2; }
float max3( const in vec3 v ) { return max( max( v.x, v.y ), v.z ); }
float average( const in vec3 v ) { return dot( v, vec3( 0.3333333 ) ); }
highp float rand( const in vec2 uv ) {
	const highp float a = 12.9898, b = 78.233, c = 43758.5453;
	highp float dt = dot( uv.xy, vec2( a,b ) ), sn = mod( dt, PI );
	return fract( sin( sn ) * c );
}
#ifdef HIGH_PRECISION
	float precisionSafeLength( vec3 v ) { return length( v ); }
#else
	float precisionSafeLength( vec3 v ) {
		float maxComponent = max3( abs( v ) );
		return length( v / maxComponent ) * maxComponent;
	}
#endif
struct IncidentLight {
	vec3 color;
	vec3 direction;
	bool visible;
};
struct ReflectedLight {
	vec3 directDiffuse;
	vec3 directSpecular;
	vec3 indirectDiffuse;
	vec3 indirectSpecular;
};
#ifdef USE_ALPHAHASH
	varying vec3 vPosition;
#endif
vec3 transformDirection( in vec3 dir, in mat4 matrix ) {
	return normalize( ( matrix * vec4( dir, 0.0 ) ).xyz );
}
vec3 inverseTransformDirection( in vec3 dir, in mat4 matrix ) {
	return normalize( ( vec4( dir, 0.0 ) * matrix ).xyz );
}
mat3 transposeMat3( const in mat3 m ) {
	mat3 tmp;
	tmp[ 0 ] = vec3( m[ 0 ].x, m[ 1 ].x, m[ 2 ].x );
	tmp[ 1 ] = vec3( m[ 0 ].y, m[ 1 ].y, m[ 2 ].y );
	tmp[ 2 ] = vec3( m[ 0 ].z, m[ 1 ].z, m[ 2 ].z );
	return tmp;
}
float luminance( const in vec3 rgb ) {
	const vec3 weights = vec3( 0.2126729, 0.7151522, 0.0721750 );
	return dot( weights, rgb );
}
bool isPerspectiveMatrix( mat4 m ) {
	return m[ 2 ][ 3 ] == - 1.0;
}
vec2 equirectUv( in vec3 dir ) {
	float u = atan( dir.z, dir.x ) * RECIPROCAL_PI2 + 0.5;
	float v = asin( clamp( dir.y, - 1.0, 1.0 ) ) * RECIPROCAL_PI + 0.5;
	return vec2( u, v );
}
vec3 BRDF_Lambert( const in vec3 diffuseColor ) {
	return RECIPROCAL_PI * diffuseColor;
}
vec3 F_Schlick( const in vec3 f0, const in float f90, const in float dotVH ) {
	float fresnel = exp2( ( - 5.55473 * dotVH - 6.98316 ) * dotVH );
	return f0 * ( 1.0 - fresnel ) + ( f90 * fresnel );
}
float F_Schlick( const in float f0, const in float f90, const in float dotVH ) {
	float fresnel = exp2( ( - 5.55473 * dotVH - 6.98316 ) * dotVH );
	return f0 * ( 1.0 - fresnel ) + ( f90 * fresnel );
} // validated`,bp=`#ifdef ENVMAP_TYPE_CUBE_UV
	#define cubeUV_minMipLevel 4.0
	#define cubeUV_minTileSize 16.0
	float getFace( vec3 direction ) {
		vec3 absDirection = abs( direction );
		float face = - 1.0;
		if ( absDirection.x > absDirection.z ) {
			if ( absDirection.x > absDirection.y )
				face = direction.x > 0.0 ? 0.0 : 3.0;
			else
				face = direction.y > 0.0 ? 1.0 : 4.0;
		} else {
			if ( absDirection.z > absDirection.y )
				face = direction.z > 0.0 ? 2.0 : 5.0;
			else
				face = direction.y > 0.0 ? 1.0 : 4.0;
		}
		return face;
	}
	vec2 getUV( vec3 direction, float face ) {
		vec2 uv;
		if ( face == 0.0 ) {
			uv = vec2( direction.z, direction.y ) / abs( direction.x );
		} else if ( face == 1.0 ) {
			uv = vec2( - direction.x, - direction.z ) / abs( direction.y );
		} else if ( face == 2.0 ) {
			uv = vec2( - direction.x, direction.y ) / abs( direction.z );
		} else if ( face == 3.0 ) {
			uv = vec2( - direction.z, direction.y ) / abs( direction.x );
		} else if ( face == 4.0 ) {
			uv = vec2( - direction.x, direction.z ) / abs( direction.y );
		} else {
			uv = vec2( direction.x, direction.y ) / abs( direction.z );
		}
		return 0.5 * ( uv + 1.0 );
	}
	vec3 bilinearCubeUV( sampler2D envMap, vec3 direction, float mipInt ) {
		float face = getFace( direction );
		float filterInt = max( cubeUV_minMipLevel - mipInt, 0.0 );
		mipInt = max( mipInt, cubeUV_minMipLevel );
		float faceSize = exp2( mipInt );
		highp vec2 uv = getUV( direction, face ) * ( faceSize - 2.0 ) + 1.0;
		if ( face > 2.0 ) {
			uv.y += faceSize;
			face -= 3.0;
		}
		uv.x += face * faceSize;
		uv.x += filterInt * 3.0 * cubeUV_minTileSize;
		uv.y += 4.0 * ( exp2( CUBEUV_MAX_MIP ) - faceSize );
		uv.x *= CUBEUV_TEXEL_WIDTH;
		uv.y *= CUBEUV_TEXEL_HEIGHT;
		#ifdef texture2DGradEXT
			return texture2DGradEXT( envMap, uv, vec2( 0.0 ), vec2( 0.0 ) ).rgb;
		#else
			return texture2D( envMap, uv ).rgb;
		#endif
	}
	#define cubeUV_r0 1.0
	#define cubeUV_m0 - 2.0
	#define cubeUV_r1 0.8
	#define cubeUV_m1 - 1.0
	#define cubeUV_r4 0.4
	#define cubeUV_m4 2.0
	#define cubeUV_r5 0.305
	#define cubeUV_m5 3.0
	#define cubeUV_r6 0.21
	#define cubeUV_m6 4.0
	float roughnessToMip( float roughness ) {
		float mip = 0.0;
		if ( roughness >= cubeUV_r1 ) {
			mip = ( cubeUV_r0 - roughness ) * ( cubeUV_m1 - cubeUV_m0 ) / ( cubeUV_r0 - cubeUV_r1 ) + cubeUV_m0;
		} else if ( roughness >= cubeUV_r4 ) {
			mip = ( cubeUV_r1 - roughness ) * ( cubeUV_m4 - cubeUV_m1 ) / ( cubeUV_r1 - cubeUV_r4 ) + cubeUV_m1;
		} else if ( roughness >= cubeUV_r5 ) {
			mip = ( cubeUV_r4 - roughness ) * ( cubeUV_m5 - cubeUV_m4 ) / ( cubeUV_r4 - cubeUV_r5 ) + cubeUV_m4;
		} else if ( roughness >= cubeUV_r6 ) {
			mip = ( cubeUV_r5 - roughness ) * ( cubeUV_m6 - cubeUV_m5 ) / ( cubeUV_r5 - cubeUV_r6 ) + cubeUV_m5;
		} else {
			mip = - 2.0 * log2( 1.16 * roughness );		}
		return mip;
	}
	vec4 textureCubeUV( sampler2D envMap, vec3 sampleDir, float roughness ) {
		float mip = clamp( roughnessToMip( roughness ), cubeUV_m0, CUBEUV_MAX_MIP );
		float mipF = fract( mip );
		float mipInt = floor( mip );
		vec3 color0 = bilinearCubeUV( envMap, sampleDir, mipInt );
		if ( mipF == 0.0 ) {
			return vec4( color0, 1.0 );
		} else {
			vec3 color1 = bilinearCubeUV( envMap, sampleDir, mipInt + 1.0 );
			return vec4( mix( color0, color1, mipF ), 1.0 );
		}
	}
#endif`,Ep=`vec3 transformedNormal = objectNormal;
#ifdef USE_TANGENT
	vec3 transformedTangent = objectTangent;
#endif
#ifdef USE_BATCHING
	mat3 bm = mat3( batchingMatrix );
	transformedNormal /= vec3( dot( bm[ 0 ], bm[ 0 ] ), dot( bm[ 1 ], bm[ 1 ] ), dot( bm[ 2 ], bm[ 2 ] ) );
	transformedNormal = bm * transformedNormal;
	#ifdef USE_TANGENT
		transformedTangent = bm * transformedTangent;
	#endif
#endif
#ifdef USE_INSTANCING
	mat3 im = mat3( instanceMatrix );
	transformedNormal /= vec3( dot( im[ 0 ], im[ 0 ] ), dot( im[ 1 ], im[ 1 ] ), dot( im[ 2 ], im[ 2 ] ) );
	transformedNormal = im * transformedNormal;
	#ifdef USE_TANGENT
		transformedTangent = im * transformedTangent;
	#endif
#endif
transformedNormal = normalMatrix * transformedNormal;
#ifdef FLIP_SIDED
	transformedNormal = - transformedNormal;
#endif
#ifdef USE_TANGENT
	transformedTangent = ( modelViewMatrix * vec4( transformedTangent, 0.0 ) ).xyz;
	#ifdef FLIP_SIDED
		transformedTangent = - transformedTangent;
	#endif
#endif`,wp=`#ifdef USE_DISPLACEMENTMAP
	uniform sampler2D displacementMap;
	uniform float displacementScale;
	uniform float displacementBias;
#endif`,Tp=`#ifdef USE_DISPLACEMENTMAP
	transformed += normalize( objectNormal ) * ( texture2D( displacementMap, vDisplacementMapUv ).x * displacementScale + displacementBias );
#endif`,Ap=`#ifdef USE_EMISSIVEMAP
	vec4 emissiveColor = texture2D( emissiveMap, vEmissiveMapUv );
	totalEmissiveRadiance *= emissiveColor.rgb;
#endif`,Rp=`#ifdef USE_EMISSIVEMAP
	uniform sampler2D emissiveMap;
#endif`,Cp="gl_FragColor = linearToOutputTexel( gl_FragColor );",Pp=`
const mat3 LINEAR_SRGB_TO_LINEAR_DISPLAY_P3 = mat3(
	vec3( 0.8224621, 0.177538, 0.0 ),
	vec3( 0.0331941, 0.9668058, 0.0 ),
	vec3( 0.0170827, 0.0723974, 0.9105199 )
);
const mat3 LINEAR_DISPLAY_P3_TO_LINEAR_SRGB = mat3(
	vec3( 1.2249401, - 0.2249404, 0.0 ),
	vec3( - 0.0420569, 1.0420571, 0.0 ),
	vec3( - 0.0196376, - 0.0786361, 1.0982735 )
);
vec4 LinearSRGBToLinearDisplayP3( in vec4 value ) {
	return vec4( value.rgb * LINEAR_SRGB_TO_LINEAR_DISPLAY_P3, value.a );
}
vec4 LinearDisplayP3ToLinearSRGB( in vec4 value ) {
	return vec4( value.rgb * LINEAR_DISPLAY_P3_TO_LINEAR_SRGB, value.a );
}
vec4 LinearTransferOETF( in vec4 value ) {
	return value;
}
vec4 sRGBTransferOETF( in vec4 value ) {
	return vec4( mix( pow( value.rgb, vec3( 0.41666 ) ) * 1.055 - vec3( 0.055 ), value.rgb * 12.92, vec3( lessThanEqual( value.rgb, vec3( 0.0031308 ) ) ) ), value.a );
}
vec4 LinearToLinear( in vec4 value ) {
	return value;
}
vec4 LinearTosRGB( in vec4 value ) {
	return sRGBTransferOETF( value );
}`,Ip=`#ifdef USE_ENVMAP
	#ifdef ENV_WORLDPOS
		vec3 cameraToFrag;
		if ( isOrthographic ) {
			cameraToFrag = normalize( vec3( - viewMatrix[ 0 ][ 2 ], - viewMatrix[ 1 ][ 2 ], - viewMatrix[ 2 ][ 2 ] ) );
		} else {
			cameraToFrag = normalize( vWorldPosition - cameraPosition );
		}
		vec3 worldNormal = inverseTransformDirection( normal, viewMatrix );
		#ifdef ENVMAP_MODE_REFLECTION
			vec3 reflectVec = reflect( cameraToFrag, worldNormal );
		#else
			vec3 reflectVec = refract( cameraToFrag, worldNormal, refractionRatio );
		#endif
	#else
		vec3 reflectVec = vReflect;
	#endif
	#ifdef ENVMAP_TYPE_CUBE
		vec4 envColor = textureCube( envMap, vec3( flipEnvMap * reflectVec.x, reflectVec.yz ) );
	#else
		vec4 envColor = vec4( 0.0 );
	#endif
	#ifdef ENVMAP_BLENDING_MULTIPLY
		outgoingLight = mix( outgoingLight, outgoingLight * envColor.xyz, specularStrength * reflectivity );
	#elif defined( ENVMAP_BLENDING_MIX )
		outgoingLight = mix( outgoingLight, envColor.xyz, specularStrength * reflectivity );
	#elif defined( ENVMAP_BLENDING_ADD )
		outgoingLight += envColor.xyz * specularStrength * reflectivity;
	#endif
#endif`,Lp=`#ifdef USE_ENVMAP
	uniform float envMapIntensity;
	uniform float flipEnvMap;
	#ifdef ENVMAP_TYPE_CUBE
		uniform samplerCube envMap;
	#else
		uniform sampler2D envMap;
	#endif
	
#endif`,Up=`#ifdef USE_ENVMAP
	uniform float reflectivity;
	#if defined( USE_BUMPMAP ) || defined( USE_NORMALMAP ) || defined( PHONG ) || defined( LAMBERT )
		#define ENV_WORLDPOS
	#endif
	#ifdef ENV_WORLDPOS
		varying vec3 vWorldPosition;
		uniform float refractionRatio;
	#else
		varying vec3 vReflect;
	#endif
#endif`,Dp=`#ifdef USE_ENVMAP
	#if defined( USE_BUMPMAP ) || defined( USE_NORMALMAP ) || defined( PHONG ) || defined( LAMBERT )
		#define ENV_WORLDPOS
	#endif
	#ifdef ENV_WORLDPOS
		
		varying vec3 vWorldPosition;
	#else
		varying vec3 vReflect;
		uniform float refractionRatio;
	#endif
#endif`,Np=`#ifdef USE_ENVMAP
	#ifdef ENV_WORLDPOS
		vWorldPosition = worldPosition.xyz;
	#else
		vec3 cameraToVertex;
		if ( isOrthographic ) {
			cameraToVertex = normalize( vec3( - viewMatrix[ 0 ][ 2 ], - viewMatrix[ 1 ][ 2 ], - viewMatrix[ 2 ][ 2 ] ) );
		} else {
			cameraToVertex = normalize( worldPosition.xyz - cameraPosition );
		}
		vec3 worldNormal = inverseTransformDirection( transformedNormal, viewMatrix );
		#ifdef ENVMAP_MODE_REFLECTION
			vReflect = reflect( cameraToVertex, worldNormal );
		#else
			vReflect = refract( cameraToVertex, worldNormal, refractionRatio );
		#endif
	#endif
#endif`,Fp=`#ifdef USE_FOG
	vFogDepth = - mvPosition.z;
#endif`,Op=`#ifdef USE_FOG
	varying float vFogDepth;
#endif`,Bp=`#ifdef USE_FOG
	#ifdef FOG_EXP2
		float fogFactor = 1.0 - exp( - fogDensity * fogDensity * vFogDepth * vFogDepth );
	#else
		float fogFactor = smoothstep( fogNear, fogFar, vFogDepth );
	#endif
	gl_FragColor.rgb = mix( gl_FragColor.rgb, fogColor, fogFactor );
#endif`,zp=`#ifdef USE_FOG
	uniform vec3 fogColor;
	varying float vFogDepth;
	#ifdef FOG_EXP2
		uniform float fogDensity;
	#else
		uniform float fogNear;
		uniform float fogFar;
	#endif
#endif`,Hp=`#ifdef USE_GRADIENTMAP
	uniform sampler2D gradientMap;
#endif
vec3 getGradientIrradiance( vec3 normal, vec3 lightDirection ) {
	float dotNL = dot( normal, lightDirection );
	vec2 coord = vec2( dotNL * 0.5 + 0.5, 0.0 );
	#ifdef USE_GRADIENTMAP
		return vec3( texture2D( gradientMap, coord ).r );
	#else
		vec2 fw = fwidth( coord ) * 0.5;
		return mix( vec3( 0.7 ), vec3( 1.0 ), smoothstep( 0.7 - fw.x, 0.7 + fw.x, coord.x ) );
	#endif
}`,kp=`#ifdef USE_LIGHTMAP
	vec4 lightMapTexel = texture2D( lightMap, vLightMapUv );
	vec3 lightMapIrradiance = lightMapTexel.rgb * lightMapIntensity;
	reflectedLight.indirectDiffuse += lightMapIrradiance;
#endif`,Vp=`#ifdef USE_LIGHTMAP
	uniform sampler2D lightMap;
	uniform float lightMapIntensity;
#endif`,Gp=`LambertMaterial material;
material.diffuseColor = diffuseColor.rgb;
material.specularStrength = specularStrength;`,Wp=`varying vec3 vViewPosition;
struct LambertMaterial {
	vec3 diffuseColor;
	float specularStrength;
};
void RE_Direct_Lambert( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in LambertMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectDiffuse_Lambert( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in LambertMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_Lambert
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Lambert`,Xp=`uniform bool receiveShadow;
uniform vec3 ambientLightColor;
#if defined( USE_LIGHT_PROBES )
	uniform vec3 lightProbe[ 9 ];
#endif
vec3 shGetIrradianceAt( in vec3 normal, in vec3 shCoefficients[ 9 ] ) {
	float x = normal.x, y = normal.y, z = normal.z;
	vec3 result = shCoefficients[ 0 ] * 0.886227;
	result += shCoefficients[ 1 ] * 2.0 * 0.511664 * y;
	result += shCoefficients[ 2 ] * 2.0 * 0.511664 * z;
	result += shCoefficients[ 3 ] * 2.0 * 0.511664 * x;
	result += shCoefficients[ 4 ] * 2.0 * 0.429043 * x * y;
	result += shCoefficients[ 5 ] * 2.0 * 0.429043 * y * z;
	result += shCoefficients[ 6 ] * ( 0.743125 * z * z - 0.247708 );
	result += shCoefficients[ 7 ] * 2.0 * 0.429043 * x * z;
	result += shCoefficients[ 8 ] * 0.429043 * ( x * x - y * y );
	return result;
}
vec3 getLightProbeIrradiance( const in vec3 lightProbe[ 9 ], const in vec3 normal ) {
	vec3 worldNormal = inverseTransformDirection( normal, viewMatrix );
	vec3 irradiance = shGetIrradianceAt( worldNormal, lightProbe );
	return irradiance;
}
vec3 getAmbientLightIrradiance( const in vec3 ambientLightColor ) {
	vec3 irradiance = ambientLightColor;
	return irradiance;
}
float getDistanceAttenuation( const in float lightDistance, const in float cutoffDistance, const in float decayExponent ) {
	#if defined ( LEGACY_LIGHTS )
		if ( cutoffDistance > 0.0 && decayExponent > 0.0 ) {
			return pow( saturate( - lightDistance / cutoffDistance + 1.0 ), decayExponent );
		}
		return 1.0;
	#else
		float distanceFalloff = 1.0 / max( pow( lightDistance, decayExponent ), 0.01 );
		if ( cutoffDistance > 0.0 ) {
			distanceFalloff *= pow2( saturate( 1.0 - pow4( lightDistance / cutoffDistance ) ) );
		}
		return distanceFalloff;
	#endif
}
float getSpotAttenuation( const in float coneCosine, const in float penumbraCosine, const in float angleCosine ) {
	return smoothstep( coneCosine, penumbraCosine, angleCosine );
}
#if NUM_DIR_LIGHTS > 0
	struct DirectionalLight {
		vec3 direction;
		vec3 color;
	};
	uniform DirectionalLight directionalLights[ NUM_DIR_LIGHTS ];
	void getDirectionalLightInfo( const in DirectionalLight directionalLight, out IncidentLight light ) {
		light.color = directionalLight.color;
		light.direction = directionalLight.direction;
		light.visible = true;
	}
#endif
#if NUM_POINT_LIGHTS > 0
	struct PointLight {
		vec3 position;
		vec3 color;
		float distance;
		float decay;
	};
	uniform PointLight pointLights[ NUM_POINT_LIGHTS ];
	void getPointLightInfo( const in PointLight pointLight, const in vec3 geometryPosition, out IncidentLight light ) {
		vec3 lVector = pointLight.position - geometryPosition;
		light.direction = normalize( lVector );
		float lightDistance = length( lVector );
		light.color = pointLight.color;
		light.color *= getDistanceAttenuation( lightDistance, pointLight.distance, pointLight.decay );
		light.visible = ( light.color != vec3( 0.0 ) );
	}
#endif
#if NUM_SPOT_LIGHTS > 0
	struct SpotLight {
		vec3 position;
		vec3 direction;
		vec3 color;
		float distance;
		float decay;
		float coneCos;
		float penumbraCos;
	};
	uniform SpotLight spotLights[ NUM_SPOT_LIGHTS ];
	void getSpotLightInfo( const in SpotLight spotLight, const in vec3 geometryPosition, out IncidentLight light ) {
		vec3 lVector = spotLight.position - geometryPosition;
		light.direction = normalize( lVector );
		float angleCos = dot( light.direction, spotLight.direction );
		float spotAttenuation = getSpotAttenuation( spotLight.coneCos, spotLight.penumbraCos, angleCos );
		if ( spotAttenuation > 0.0 ) {
			float lightDistance = length( lVector );
			light.color = spotLight.color * spotAttenuation;
			light.color *= getDistanceAttenuation( lightDistance, spotLight.distance, spotLight.decay );
			light.visible = ( light.color != vec3( 0.0 ) );
		} else {
			light.color = vec3( 0.0 );
			light.visible = false;
		}
	}
#endif
#if NUM_RECT_AREA_LIGHTS > 0
	struct RectAreaLight {
		vec3 color;
		vec3 position;
		vec3 halfWidth;
		vec3 halfHeight;
	};
	uniform sampler2D ltc_1;	uniform sampler2D ltc_2;
	uniform RectAreaLight rectAreaLights[ NUM_RECT_AREA_LIGHTS ];
#endif
#if NUM_HEMI_LIGHTS > 0
	struct HemisphereLight {
		vec3 direction;
		vec3 skyColor;
		vec3 groundColor;
	};
	uniform HemisphereLight hemisphereLights[ NUM_HEMI_LIGHTS ];
	vec3 getHemisphereLightIrradiance( const in HemisphereLight hemiLight, const in vec3 normal ) {
		float dotNL = dot( normal, hemiLight.direction );
		float hemiDiffuseWeight = 0.5 * dotNL + 0.5;
		vec3 irradiance = mix( hemiLight.groundColor, hemiLight.skyColor, hemiDiffuseWeight );
		return irradiance;
	}
#endif`,Yp=`#ifdef USE_ENVMAP
	vec3 getIBLIrradiance( const in vec3 normal ) {
		#ifdef ENVMAP_TYPE_CUBE_UV
			vec3 worldNormal = inverseTransformDirection( normal, viewMatrix );
			vec4 envMapColor = textureCubeUV( envMap, worldNormal, 1.0 );
			return PI * envMapColor.rgb * envMapIntensity;
		#else
			return vec3( 0.0 );
		#endif
	}
	vec3 getIBLRadiance( const in vec3 viewDir, const in vec3 normal, const in float roughness ) {
		#ifdef ENVMAP_TYPE_CUBE_UV
			vec3 reflectVec = reflect( - viewDir, normal );
			reflectVec = normalize( mix( reflectVec, normal, roughness * roughness) );
			reflectVec = inverseTransformDirection( reflectVec, viewMatrix );
			vec4 envMapColor = textureCubeUV( envMap, reflectVec, roughness );
			return envMapColor.rgb * envMapIntensity;
		#else
			return vec3( 0.0 );
		#endif
	}
	#ifdef USE_ANISOTROPY
		vec3 getIBLAnisotropyRadiance( const in vec3 viewDir, const in vec3 normal, const in float roughness, const in vec3 bitangent, const in float anisotropy ) {
			#ifdef ENVMAP_TYPE_CUBE_UV
				vec3 bentNormal = cross( bitangent, viewDir );
				bentNormal = normalize( cross( bentNormal, bitangent ) );
				bentNormal = normalize( mix( bentNormal, normal, pow2( pow2( 1.0 - anisotropy * ( 1.0 - roughness ) ) ) ) );
				return getIBLRadiance( viewDir, bentNormal, roughness );
			#else
				return vec3( 0.0 );
			#endif
		}
	#endif
#endif`,qp=`ToonMaterial material;
material.diffuseColor = diffuseColor.rgb;`,Zp=`varying vec3 vViewPosition;
struct ToonMaterial {
	vec3 diffuseColor;
};
void RE_Direct_Toon( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in ToonMaterial material, inout ReflectedLight reflectedLight ) {
	vec3 irradiance = getGradientIrradiance( geometryNormal, directLight.direction ) * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectDiffuse_Toon( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in ToonMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_Toon
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Toon`,$p=`BlinnPhongMaterial material;
material.diffuseColor = diffuseColor.rgb;
material.specularColor = specular;
material.specularShininess = shininess;
material.specularStrength = specularStrength;`,Jp=`varying vec3 vViewPosition;
struct BlinnPhongMaterial {
	vec3 diffuseColor;
	vec3 specularColor;
	float specularShininess;
	float specularStrength;
};
void RE_Direct_BlinnPhong( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in BlinnPhongMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
	reflectedLight.directSpecular += irradiance * BRDF_BlinnPhong( directLight.direction, geometryViewDir, geometryNormal, material.specularColor, material.specularShininess ) * material.specularStrength;
}
void RE_IndirectDiffuse_BlinnPhong( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in BlinnPhongMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_BlinnPhong
#define RE_IndirectDiffuse		RE_IndirectDiffuse_BlinnPhong`,Kp=`PhysicalMaterial material;
material.diffuseColor = diffuseColor.rgb * ( 1.0 - metalnessFactor );
vec3 dxy = max( abs( dFdx( nonPerturbedNormal ) ), abs( dFdy( nonPerturbedNormal ) ) );
float geometryRoughness = max( max( dxy.x, dxy.y ), dxy.z );
material.roughness = max( roughnessFactor, 0.0525 );material.roughness += geometryRoughness;
material.roughness = min( material.roughness, 1.0 );
#ifdef IOR
	material.ior = ior;
	#ifdef USE_SPECULAR
		float specularIntensityFactor = specularIntensity;
		vec3 specularColorFactor = specularColor;
		#ifdef USE_SPECULAR_COLORMAP
			specularColorFactor *= texture2D( specularColorMap, vSpecularColorMapUv ).rgb;
		#endif
		#ifdef USE_SPECULAR_INTENSITYMAP
			specularIntensityFactor *= texture2D( specularIntensityMap, vSpecularIntensityMapUv ).a;
		#endif
		material.specularF90 = mix( specularIntensityFactor, 1.0, metalnessFactor );
	#else
		float specularIntensityFactor = 1.0;
		vec3 specularColorFactor = vec3( 1.0 );
		material.specularF90 = 1.0;
	#endif
	material.specularColor = mix( min( pow2( ( material.ior - 1.0 ) / ( material.ior + 1.0 ) ) * specularColorFactor, vec3( 1.0 ) ) * specularIntensityFactor, diffuseColor.rgb, metalnessFactor );
#else
	material.specularColor = mix( vec3( 0.04 ), diffuseColor.rgb, metalnessFactor );
	material.specularF90 = 1.0;
#endif
#ifdef USE_CLEARCOAT
	material.clearcoat = clearcoat;
	material.clearcoatRoughness = clearcoatRoughness;
	material.clearcoatF0 = vec3( 0.04 );
	material.clearcoatF90 = 1.0;
	#ifdef USE_CLEARCOATMAP
		material.clearcoat *= texture2D( clearcoatMap, vClearcoatMapUv ).x;
	#endif
	#ifdef USE_CLEARCOAT_ROUGHNESSMAP
		material.clearcoatRoughness *= texture2D( clearcoatRoughnessMap, vClearcoatRoughnessMapUv ).y;
	#endif
	material.clearcoat = saturate( material.clearcoat );	material.clearcoatRoughness = max( material.clearcoatRoughness, 0.0525 );
	material.clearcoatRoughness += geometryRoughness;
	material.clearcoatRoughness = min( material.clearcoatRoughness, 1.0 );
#endif
#ifdef USE_IRIDESCENCE
	material.iridescence = iridescence;
	material.iridescenceIOR = iridescenceIOR;
	#ifdef USE_IRIDESCENCEMAP
		material.iridescence *= texture2D( iridescenceMap, vIridescenceMapUv ).r;
	#endif
	#ifdef USE_IRIDESCENCE_THICKNESSMAP
		material.iridescenceThickness = (iridescenceThicknessMaximum - iridescenceThicknessMinimum) * texture2D( iridescenceThicknessMap, vIridescenceThicknessMapUv ).g + iridescenceThicknessMinimum;
	#else
		material.iridescenceThickness = iridescenceThicknessMaximum;
	#endif
#endif
#ifdef USE_SHEEN
	material.sheenColor = sheenColor;
	#ifdef USE_SHEEN_COLORMAP
		material.sheenColor *= texture2D( sheenColorMap, vSheenColorMapUv ).rgb;
	#endif
	material.sheenRoughness = clamp( sheenRoughness, 0.07, 1.0 );
	#ifdef USE_SHEEN_ROUGHNESSMAP
		material.sheenRoughness *= texture2D( sheenRoughnessMap, vSheenRoughnessMapUv ).a;
	#endif
#endif
#ifdef USE_ANISOTROPY
	#ifdef USE_ANISOTROPYMAP
		mat2 anisotropyMat = mat2( anisotropyVector.x, anisotropyVector.y, - anisotropyVector.y, anisotropyVector.x );
		vec3 anisotropyPolar = texture2D( anisotropyMap, vAnisotropyMapUv ).rgb;
		vec2 anisotropyV = anisotropyMat * normalize( 2.0 * anisotropyPolar.rg - vec2( 1.0 ) ) * anisotropyPolar.b;
	#else
		vec2 anisotropyV = anisotropyVector;
	#endif
	material.anisotropy = length( anisotropyV );
	if( material.anisotropy == 0.0 ) {
		anisotropyV = vec2( 1.0, 0.0 );
	} else {
		anisotropyV /= material.anisotropy;
		material.anisotropy = saturate( material.anisotropy );
	}
	material.alphaT = mix( pow2( material.roughness ), 1.0, pow2( material.anisotropy ) );
	material.anisotropyT = tbn[ 0 ] * anisotropyV.x + tbn[ 1 ] * anisotropyV.y;
	material.anisotropyB = tbn[ 1 ] * anisotropyV.x - tbn[ 0 ] * anisotropyV.y;
#endif`,jp=`struct PhysicalMaterial {
	vec3 diffuseColor;
	float roughness;
	vec3 specularColor;
	float specularF90;
	#ifdef USE_CLEARCOAT
		float clearcoat;
		float clearcoatRoughness;
		vec3 clearcoatF0;
		float clearcoatF90;
	#endif
	#ifdef USE_IRIDESCENCE
		float iridescence;
		float iridescenceIOR;
		float iridescenceThickness;
		vec3 iridescenceFresnel;
		vec3 iridescenceF0;
	#endif
	#ifdef USE_SHEEN
		vec3 sheenColor;
		float sheenRoughness;
	#endif
	#ifdef IOR
		float ior;
	#endif
	#ifdef USE_TRANSMISSION
		float transmission;
		float transmissionAlpha;
		float thickness;
		float attenuationDistance;
		vec3 attenuationColor;
	#endif
	#ifdef USE_ANISOTROPY
		float anisotropy;
		float alphaT;
		vec3 anisotropyT;
		vec3 anisotropyB;
	#endif
};
vec3 clearcoatSpecularDirect = vec3( 0.0 );
vec3 clearcoatSpecularIndirect = vec3( 0.0 );
vec3 sheenSpecularDirect = vec3( 0.0 );
vec3 sheenSpecularIndirect = vec3(0.0 );
vec3 Schlick_to_F0( const in vec3 f, const in float f90, const in float dotVH ) {
    float x = clamp( 1.0 - dotVH, 0.0, 1.0 );
    float x2 = x * x;
    float x5 = clamp( x * x2 * x2, 0.0, 0.9999 );
    return ( f - vec3( f90 ) * x5 ) / ( 1.0 - x5 );
}
float V_GGX_SmithCorrelated( const in float alpha, const in float dotNL, const in float dotNV ) {
	float a2 = pow2( alpha );
	float gv = dotNL * sqrt( a2 + ( 1.0 - a2 ) * pow2( dotNV ) );
	float gl = dotNV * sqrt( a2 + ( 1.0 - a2 ) * pow2( dotNL ) );
	return 0.5 / max( gv + gl, EPSILON );
}
float D_GGX( const in float alpha, const in float dotNH ) {
	float a2 = pow2( alpha );
	float denom = pow2( dotNH ) * ( a2 - 1.0 ) + 1.0;
	return RECIPROCAL_PI * a2 / pow2( denom );
}
#ifdef USE_ANISOTROPY
	float V_GGX_SmithCorrelated_Anisotropic( const in float alphaT, const in float alphaB, const in float dotTV, const in float dotBV, const in float dotTL, const in float dotBL, const in float dotNV, const in float dotNL ) {
		float gv = dotNL * length( vec3( alphaT * dotTV, alphaB * dotBV, dotNV ) );
		float gl = dotNV * length( vec3( alphaT * dotTL, alphaB * dotBL, dotNL ) );
		float v = 0.5 / ( gv + gl );
		return saturate(v);
	}
	float D_GGX_Anisotropic( const in float alphaT, const in float alphaB, const in float dotNH, const in float dotTH, const in float dotBH ) {
		float a2 = alphaT * alphaB;
		highp vec3 v = vec3( alphaB * dotTH, alphaT * dotBH, a2 * dotNH );
		highp float v2 = dot( v, v );
		float w2 = a2 / v2;
		return RECIPROCAL_PI * a2 * pow2 ( w2 );
	}
#endif
#ifdef USE_CLEARCOAT
	vec3 BRDF_GGX_Clearcoat( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in PhysicalMaterial material) {
		vec3 f0 = material.clearcoatF0;
		float f90 = material.clearcoatF90;
		float roughness = material.clearcoatRoughness;
		float alpha = pow2( roughness );
		vec3 halfDir = normalize( lightDir + viewDir );
		float dotNL = saturate( dot( normal, lightDir ) );
		float dotNV = saturate( dot( normal, viewDir ) );
		float dotNH = saturate( dot( normal, halfDir ) );
		float dotVH = saturate( dot( viewDir, halfDir ) );
		vec3 F = F_Schlick( f0, f90, dotVH );
		float V = V_GGX_SmithCorrelated( alpha, dotNL, dotNV );
		float D = D_GGX( alpha, dotNH );
		return F * ( V * D );
	}
#endif
vec3 BRDF_GGX( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in PhysicalMaterial material ) {
	vec3 f0 = material.specularColor;
	float f90 = material.specularF90;
	float roughness = material.roughness;
	float alpha = pow2( roughness );
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNL = saturate( dot( normal, lightDir ) );
	float dotNV = saturate( dot( normal, viewDir ) );
	float dotNH = saturate( dot( normal, halfDir ) );
	float dotVH = saturate( dot( viewDir, halfDir ) );
	vec3 F = F_Schlick( f0, f90, dotVH );
	#ifdef USE_IRIDESCENCE
		F = mix( F, material.iridescenceFresnel, material.iridescence );
	#endif
	#ifdef USE_ANISOTROPY
		float dotTL = dot( material.anisotropyT, lightDir );
		float dotTV = dot( material.anisotropyT, viewDir );
		float dotTH = dot( material.anisotropyT, halfDir );
		float dotBL = dot( material.anisotropyB, lightDir );
		float dotBV = dot( material.anisotropyB, viewDir );
		float dotBH = dot( material.anisotropyB, halfDir );
		float V = V_GGX_SmithCorrelated_Anisotropic( material.alphaT, alpha, dotTV, dotBV, dotTL, dotBL, dotNV, dotNL );
		float D = D_GGX_Anisotropic( material.alphaT, alpha, dotNH, dotTH, dotBH );
	#else
		float V = V_GGX_SmithCorrelated( alpha, dotNL, dotNV );
		float D = D_GGX( alpha, dotNH );
	#endif
	return F * ( V * D );
}
vec2 LTC_Uv( const in vec3 N, const in vec3 V, const in float roughness ) {
	const float LUT_SIZE = 64.0;
	const float LUT_SCALE = ( LUT_SIZE - 1.0 ) / LUT_SIZE;
	const float LUT_BIAS = 0.5 / LUT_SIZE;
	float dotNV = saturate( dot( N, V ) );
	vec2 uv = vec2( roughness, sqrt( 1.0 - dotNV ) );
	uv = uv * LUT_SCALE + LUT_BIAS;
	return uv;
}
float LTC_ClippedSphereFormFactor( const in vec3 f ) {
	float l = length( f );
	return max( ( l * l + f.z ) / ( l + 1.0 ), 0.0 );
}
vec3 LTC_EdgeVectorFormFactor( const in vec3 v1, const in vec3 v2 ) {
	float x = dot( v1, v2 );
	float y = abs( x );
	float a = 0.8543985 + ( 0.4965155 + 0.0145206 * y ) * y;
	float b = 3.4175940 + ( 4.1616724 + y ) * y;
	float v = a / b;
	float theta_sintheta = ( x > 0.0 ) ? v : 0.5 * inversesqrt( max( 1.0 - x * x, 1e-7 ) ) - v;
	return cross( v1, v2 ) * theta_sintheta;
}
vec3 LTC_Evaluate( const in vec3 N, const in vec3 V, const in vec3 P, const in mat3 mInv, const in vec3 rectCoords[ 4 ] ) {
	vec3 v1 = rectCoords[ 1 ] - rectCoords[ 0 ];
	vec3 v2 = rectCoords[ 3 ] - rectCoords[ 0 ];
	vec3 lightNormal = cross( v1, v2 );
	if( dot( lightNormal, P - rectCoords[ 0 ] ) < 0.0 ) return vec3( 0.0 );
	vec3 T1, T2;
	T1 = normalize( V - N * dot( V, N ) );
	T2 = - cross( N, T1 );
	mat3 mat = mInv * transposeMat3( mat3( T1, T2, N ) );
	vec3 coords[ 4 ];
	coords[ 0 ] = mat * ( rectCoords[ 0 ] - P );
	coords[ 1 ] = mat * ( rectCoords[ 1 ] - P );
	coords[ 2 ] = mat * ( rectCoords[ 2 ] - P );
	coords[ 3 ] = mat * ( rectCoords[ 3 ] - P );
	coords[ 0 ] = normalize( coords[ 0 ] );
	coords[ 1 ] = normalize( coords[ 1 ] );
	coords[ 2 ] = normalize( coords[ 2 ] );
	coords[ 3 ] = normalize( coords[ 3 ] );
	vec3 vectorFormFactor = vec3( 0.0 );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 0 ], coords[ 1 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 1 ], coords[ 2 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 2 ], coords[ 3 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 3 ], coords[ 0 ] );
	float result = LTC_ClippedSphereFormFactor( vectorFormFactor );
	return vec3( result );
}
#if defined( USE_SHEEN )
float D_Charlie( float roughness, float dotNH ) {
	float alpha = pow2( roughness );
	float invAlpha = 1.0 / alpha;
	float cos2h = dotNH * dotNH;
	float sin2h = max( 1.0 - cos2h, 0.0078125 );
	return ( 2.0 + invAlpha ) * pow( sin2h, invAlpha * 0.5 ) / ( 2.0 * PI );
}
float V_Neubelt( float dotNV, float dotNL ) {
	return saturate( 1.0 / ( 4.0 * ( dotNL + dotNV - dotNL * dotNV ) ) );
}
vec3 BRDF_Sheen( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, vec3 sheenColor, const in float sheenRoughness ) {
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNL = saturate( dot( normal, lightDir ) );
	float dotNV = saturate( dot( normal, viewDir ) );
	float dotNH = saturate( dot( normal, halfDir ) );
	float D = D_Charlie( sheenRoughness, dotNH );
	float V = V_Neubelt( dotNV, dotNL );
	return sheenColor * ( D * V );
}
#endif
float IBLSheenBRDF( const in vec3 normal, const in vec3 viewDir, const in float roughness ) {
	float dotNV = saturate( dot( normal, viewDir ) );
	float r2 = roughness * roughness;
	float a = roughness < 0.25 ? -339.2 * r2 + 161.4 * roughness - 25.9 : -8.48 * r2 + 14.3 * roughness - 9.95;
	float b = roughness < 0.25 ? 44.0 * r2 - 23.7 * roughness + 3.26 : 1.97 * r2 - 3.27 * roughness + 0.72;
	float DG = exp( a * dotNV + b ) + ( roughness < 0.25 ? 0.0 : 0.1 * ( roughness - 0.25 ) );
	return saturate( DG * RECIPROCAL_PI );
}
vec2 DFGApprox( const in vec3 normal, const in vec3 viewDir, const in float roughness ) {
	float dotNV = saturate( dot( normal, viewDir ) );
	const vec4 c0 = vec4( - 1, - 0.0275, - 0.572, 0.022 );
	const vec4 c1 = vec4( 1, 0.0425, 1.04, - 0.04 );
	vec4 r = roughness * c0 + c1;
	float a004 = min( r.x * r.x, exp2( - 9.28 * dotNV ) ) * r.x + r.y;
	vec2 fab = vec2( - 1.04, 1.04 ) * a004 + r.zw;
	return fab;
}
vec3 EnvironmentBRDF( const in vec3 normal, const in vec3 viewDir, const in vec3 specularColor, const in float specularF90, const in float roughness ) {
	vec2 fab = DFGApprox( normal, viewDir, roughness );
	return specularColor * fab.x + specularF90 * fab.y;
}
#ifdef USE_IRIDESCENCE
void computeMultiscatteringIridescence( const in vec3 normal, const in vec3 viewDir, const in vec3 specularColor, const in float specularF90, const in float iridescence, const in vec3 iridescenceF0, const in float roughness, inout vec3 singleScatter, inout vec3 multiScatter ) {
#else
void computeMultiscattering( const in vec3 normal, const in vec3 viewDir, const in vec3 specularColor, const in float specularF90, const in float roughness, inout vec3 singleScatter, inout vec3 multiScatter ) {
#endif
	vec2 fab = DFGApprox( normal, viewDir, roughness );
	#ifdef USE_IRIDESCENCE
		vec3 Fr = mix( specularColor, iridescenceF0, iridescence );
	#else
		vec3 Fr = specularColor;
	#endif
	vec3 FssEss = Fr * fab.x + specularF90 * fab.y;
	float Ess = fab.x + fab.y;
	float Ems = 1.0 - Ess;
	vec3 Favg = Fr + ( 1.0 - Fr ) * 0.047619;	vec3 Fms = FssEss * Favg / ( 1.0 - Ems * Favg );
	singleScatter += FssEss;
	multiScatter += Fms * Ems;
}
#if NUM_RECT_AREA_LIGHTS > 0
	void RE_Direct_RectArea_Physical( const in RectAreaLight rectAreaLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
		vec3 normal = geometryNormal;
		vec3 viewDir = geometryViewDir;
		vec3 position = geometryPosition;
		vec3 lightPos = rectAreaLight.position;
		vec3 halfWidth = rectAreaLight.halfWidth;
		vec3 halfHeight = rectAreaLight.halfHeight;
		vec3 lightColor = rectAreaLight.color;
		float roughness = material.roughness;
		vec3 rectCoords[ 4 ];
		rectCoords[ 0 ] = lightPos + halfWidth - halfHeight;		rectCoords[ 1 ] = lightPos - halfWidth - halfHeight;
		rectCoords[ 2 ] = lightPos - halfWidth + halfHeight;
		rectCoords[ 3 ] = lightPos + halfWidth + halfHeight;
		vec2 uv = LTC_Uv( normal, viewDir, roughness );
		vec4 t1 = texture2D( ltc_1, uv );
		vec4 t2 = texture2D( ltc_2, uv );
		mat3 mInv = mat3(
			vec3( t1.x, 0, t1.y ),
			vec3(    0, 1,    0 ),
			vec3( t1.z, 0, t1.w )
		);
		vec3 fresnel = ( material.specularColor * t2.x + ( vec3( 1.0 ) - material.specularColor ) * t2.y );
		reflectedLight.directSpecular += lightColor * fresnel * LTC_Evaluate( normal, viewDir, position, mInv, rectCoords );
		reflectedLight.directDiffuse += lightColor * material.diffuseColor * LTC_Evaluate( normal, viewDir, position, mat3( 1.0 ), rectCoords );
	}
#endif
void RE_Direct_Physical( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	#ifdef USE_CLEARCOAT
		float dotNLcc = saturate( dot( geometryClearcoatNormal, directLight.direction ) );
		vec3 ccIrradiance = dotNLcc * directLight.color;
		clearcoatSpecularDirect += ccIrradiance * BRDF_GGX_Clearcoat( directLight.direction, geometryViewDir, geometryClearcoatNormal, material );
	#endif
	#ifdef USE_SHEEN
		sheenSpecularDirect += irradiance * BRDF_Sheen( directLight.direction, geometryViewDir, geometryNormal, material.sheenColor, material.sheenRoughness );
	#endif
	reflectedLight.directSpecular += irradiance * BRDF_GGX( directLight.direction, geometryViewDir, geometryNormal, material );
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectDiffuse_Physical( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectSpecular_Physical( const in vec3 radiance, const in vec3 irradiance, const in vec3 clearcoatRadiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight) {
	#ifdef USE_CLEARCOAT
		clearcoatSpecularIndirect += clearcoatRadiance * EnvironmentBRDF( geometryClearcoatNormal, geometryViewDir, material.clearcoatF0, material.clearcoatF90, material.clearcoatRoughness );
	#endif
	#ifdef USE_SHEEN
		sheenSpecularIndirect += irradiance * material.sheenColor * IBLSheenBRDF( geometryNormal, geometryViewDir, material.sheenRoughness );
	#endif
	vec3 singleScattering = vec3( 0.0 );
	vec3 multiScattering = vec3( 0.0 );
	vec3 cosineWeightedIrradiance = irradiance * RECIPROCAL_PI;
	#ifdef USE_IRIDESCENCE
		computeMultiscatteringIridescence( geometryNormal, geometryViewDir, material.specularColor, material.specularF90, material.iridescence, material.iridescenceFresnel, material.roughness, singleScattering, multiScattering );
	#else
		computeMultiscattering( geometryNormal, geometryViewDir, material.specularColor, material.specularF90, material.roughness, singleScattering, multiScattering );
	#endif
	vec3 totalScattering = singleScattering + multiScattering;
	vec3 diffuse = material.diffuseColor * ( 1.0 - max( max( totalScattering.r, totalScattering.g ), totalScattering.b ) );
	reflectedLight.indirectSpecular += radiance * singleScattering;
	reflectedLight.indirectSpecular += multiScattering * cosineWeightedIrradiance;
	reflectedLight.indirectDiffuse += diffuse * cosineWeightedIrradiance;
}
#define RE_Direct				RE_Direct_Physical
#define RE_Direct_RectArea		RE_Direct_RectArea_Physical
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Physical
#define RE_IndirectSpecular		RE_IndirectSpecular_Physical
float computeSpecularOcclusion( const in float dotNV, const in float ambientOcclusion, const in float roughness ) {
	return saturate( pow( dotNV + ambientOcclusion, exp2( - 16.0 * roughness - 1.0 ) ) - 1.0 + ambientOcclusion );
}`,Qp=`
vec3 geometryPosition = - vViewPosition;
vec3 geometryNormal = normal;
vec3 geometryViewDir = ( isOrthographic ) ? vec3( 0, 0, 1 ) : normalize( vViewPosition );
vec3 geometryClearcoatNormal = vec3( 0.0 );
#ifdef USE_CLEARCOAT
	geometryClearcoatNormal = clearcoatNormal;
#endif
#ifdef USE_IRIDESCENCE
	float dotNVi = saturate( dot( normal, geometryViewDir ) );
	if ( material.iridescenceThickness == 0.0 ) {
		material.iridescence = 0.0;
	} else {
		material.iridescence = saturate( material.iridescence );
	}
	if ( material.iridescence > 0.0 ) {
		material.iridescenceFresnel = evalIridescence( 1.0, material.iridescenceIOR, dotNVi, material.iridescenceThickness, material.specularColor );
		material.iridescenceF0 = Schlick_to_F0( material.iridescenceFresnel, 1.0, dotNVi );
	}
#endif
IncidentLight directLight;
#if ( NUM_POINT_LIGHTS > 0 ) && defined( RE_Direct )
	PointLight pointLight;
	#if defined( USE_SHADOWMAP ) && NUM_POINT_LIGHT_SHADOWS > 0
	PointLightShadow pointLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_POINT_LIGHTS; i ++ ) {
		pointLight = pointLights[ i ];
		getPointLightInfo( pointLight, geometryPosition, directLight );
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_POINT_LIGHT_SHADOWS )
		pointLightShadow = pointLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getPointShadow( pointShadowMap[ i ], pointLightShadow.shadowMapSize, pointLightShadow.shadowBias, pointLightShadow.shadowRadius, vPointShadowCoord[ i ], pointLightShadow.shadowCameraNear, pointLightShadow.shadowCameraFar ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_SPOT_LIGHTS > 0 ) && defined( RE_Direct )
	SpotLight spotLight;
	vec4 spotColor;
	vec3 spotLightCoord;
	bool inSpotLightMap;
	#if defined( USE_SHADOWMAP ) && NUM_SPOT_LIGHT_SHADOWS > 0
	SpotLightShadow spotLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHTS; i ++ ) {
		spotLight = spotLights[ i ];
		getSpotLightInfo( spotLight, geometryPosition, directLight );
		#if ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS )
		#define SPOT_LIGHT_MAP_INDEX UNROLLED_LOOP_INDEX
		#elif ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
		#define SPOT_LIGHT_MAP_INDEX NUM_SPOT_LIGHT_MAPS
		#else
		#define SPOT_LIGHT_MAP_INDEX ( UNROLLED_LOOP_INDEX - NUM_SPOT_LIGHT_SHADOWS + NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS )
		#endif
		#if ( SPOT_LIGHT_MAP_INDEX < NUM_SPOT_LIGHT_MAPS )
			spotLightCoord = vSpotLightCoord[ i ].xyz / vSpotLightCoord[ i ].w;
			inSpotLightMap = all( lessThan( abs( spotLightCoord * 2. - 1. ), vec3( 1.0 ) ) );
			spotColor = texture2D( spotLightMap[ SPOT_LIGHT_MAP_INDEX ], spotLightCoord.xy );
			directLight.color = inSpotLightMap ? directLight.color * spotColor.rgb : directLight.color;
		#endif
		#undef SPOT_LIGHT_MAP_INDEX
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
		spotLightShadow = spotLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getShadow( spotShadowMap[ i ], spotLightShadow.shadowMapSize, spotLightShadow.shadowBias, spotLightShadow.shadowRadius, vSpotLightCoord[ i ] ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_DIR_LIGHTS > 0 ) && defined( RE_Direct )
	DirectionalLight directionalLight;
	#if defined( USE_SHADOWMAP ) && NUM_DIR_LIGHT_SHADOWS > 0
	DirectionalLightShadow directionalLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_DIR_LIGHTS; i ++ ) {
		directionalLight = directionalLights[ i ];
		getDirectionalLightInfo( directionalLight, directLight );
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_DIR_LIGHT_SHADOWS )
		directionalLightShadow = directionalLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getShadow( directionalShadowMap[ i ], directionalLightShadow.shadowMapSize, directionalLightShadow.shadowBias, directionalLightShadow.shadowRadius, vDirectionalShadowCoord[ i ] ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_RECT_AREA_LIGHTS > 0 ) && defined( RE_Direct_RectArea )
	RectAreaLight rectAreaLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_RECT_AREA_LIGHTS; i ++ ) {
		rectAreaLight = rectAreaLights[ i ];
		RE_Direct_RectArea( rectAreaLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if defined( RE_IndirectDiffuse )
	vec3 iblIrradiance = vec3( 0.0 );
	vec3 irradiance = getAmbientLightIrradiance( ambientLightColor );
	#if defined( USE_LIGHT_PROBES )
		irradiance += getLightProbeIrradiance( lightProbe, geometryNormal );
	#endif
	#if ( NUM_HEMI_LIGHTS > 0 )
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_HEMI_LIGHTS; i ++ ) {
			irradiance += getHemisphereLightIrradiance( hemisphereLights[ i ], geometryNormal );
		}
		#pragma unroll_loop_end
	#endif
#endif
#if defined( RE_IndirectSpecular )
	vec3 radiance = vec3( 0.0 );
	vec3 clearcoatRadiance = vec3( 0.0 );
#endif`,tm=`#if defined( RE_IndirectDiffuse )
	#ifdef USE_LIGHTMAP
		vec4 lightMapTexel = texture2D( lightMap, vLightMapUv );
		vec3 lightMapIrradiance = lightMapTexel.rgb * lightMapIntensity;
		irradiance += lightMapIrradiance;
	#endif
	#if defined( USE_ENVMAP ) && defined( STANDARD ) && defined( ENVMAP_TYPE_CUBE_UV )
		iblIrradiance += getIBLIrradiance( geometryNormal );
	#endif
#endif
#if defined( USE_ENVMAP ) && defined( RE_IndirectSpecular )
	#ifdef USE_ANISOTROPY
		radiance += getIBLAnisotropyRadiance( geometryViewDir, geometryNormal, material.roughness, material.anisotropyB, material.anisotropy );
	#else
		radiance += getIBLRadiance( geometryViewDir, geometryNormal, material.roughness );
	#endif
	#ifdef USE_CLEARCOAT
		clearcoatRadiance += getIBLRadiance( geometryViewDir, geometryClearcoatNormal, material.clearcoatRoughness );
	#endif
#endif`,em=`#if defined( RE_IndirectDiffuse )
	RE_IndirectDiffuse( irradiance, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
#endif
#if defined( RE_IndirectSpecular )
	RE_IndirectSpecular( radiance, iblIrradiance, clearcoatRadiance, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
#endif`,nm=`#if defined( USE_LOGDEPTHBUF ) && defined( USE_LOGDEPTHBUF_EXT )
	gl_FragDepthEXT = vIsPerspective == 0.0 ? gl_FragCoord.z : log2( vFragDepth ) * logDepthBufFC * 0.5;
#endif`,im=`#if defined( USE_LOGDEPTHBUF ) && defined( USE_LOGDEPTHBUF_EXT )
	uniform float logDepthBufFC;
	varying float vFragDepth;
	varying float vIsPerspective;
#endif`,sm=`#ifdef USE_LOGDEPTHBUF
	#ifdef USE_LOGDEPTHBUF_EXT
		varying float vFragDepth;
		varying float vIsPerspective;
	#else
		uniform float logDepthBufFC;
	#endif
#endif`,rm=`#ifdef USE_LOGDEPTHBUF
	#ifdef USE_LOGDEPTHBUF_EXT
		vFragDepth = 1.0 + gl_Position.w;
		vIsPerspective = float( isPerspectiveMatrix( projectionMatrix ) );
	#else
		if ( isPerspectiveMatrix( projectionMatrix ) ) {
			gl_Position.z = log2( max( EPSILON, gl_Position.w + 1.0 ) ) * logDepthBufFC - 1.0;
			gl_Position.z *= gl_Position.w;
		}
	#endif
#endif`,om=`#ifdef USE_MAP
	vec4 sampledDiffuseColor = texture2D( map, vMapUv );
	#ifdef DECODE_VIDEO_TEXTURE
		sampledDiffuseColor = vec4( mix( pow( sampledDiffuseColor.rgb * 0.9478672986 + vec3( 0.0521327014 ), vec3( 2.4 ) ), sampledDiffuseColor.rgb * 0.0773993808, vec3( lessThanEqual( sampledDiffuseColor.rgb, vec3( 0.04045 ) ) ) ), sampledDiffuseColor.w );
	
	#endif
	diffuseColor *= sampledDiffuseColor;
#endif`,am=`#ifdef USE_MAP
	uniform sampler2D map;
#endif`,lm=`#if defined( USE_MAP ) || defined( USE_ALPHAMAP )
	#if defined( USE_POINTS_UV )
		vec2 uv = vUv;
	#else
		vec2 uv = ( uvTransform * vec3( gl_PointCoord.x, 1.0 - gl_PointCoord.y, 1 ) ).xy;
	#endif
#endif
#ifdef USE_MAP
	diffuseColor *= texture2D( map, uv );
#endif
#ifdef USE_ALPHAMAP
	diffuseColor.a *= texture2D( alphaMap, uv ).g;
#endif`,cm=`#if defined( USE_POINTS_UV )
	varying vec2 vUv;
#else
	#if defined( USE_MAP ) || defined( USE_ALPHAMAP )
		uniform mat3 uvTransform;
	#endif
#endif
#ifdef USE_MAP
	uniform sampler2D map;
#endif
#ifdef USE_ALPHAMAP
	uniform sampler2D alphaMap;
#endif`,hm=`float metalnessFactor = metalness;
#ifdef USE_METALNESSMAP
	vec4 texelMetalness = texture2D( metalnessMap, vMetalnessMapUv );
	metalnessFactor *= texelMetalness.b;
#endif`,um=`#ifdef USE_METALNESSMAP
	uniform sampler2D metalnessMap;
#endif`,fm=`#if defined( USE_MORPHCOLORS ) && defined( MORPHTARGETS_TEXTURE )
	vColor *= morphTargetBaseInfluence;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		#if defined( USE_COLOR_ALPHA )
			if ( morphTargetInfluences[ i ] != 0.0 ) vColor += getMorph( gl_VertexID, i, 2 ) * morphTargetInfluences[ i ];
		#elif defined( USE_COLOR )
			if ( morphTargetInfluences[ i ] != 0.0 ) vColor += getMorph( gl_VertexID, i, 2 ).rgb * morphTargetInfluences[ i ];
		#endif
	}
#endif`,dm=`#ifdef USE_MORPHNORMALS
	objectNormal *= morphTargetBaseInfluence;
	#ifdef MORPHTARGETS_TEXTURE
		for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
			if ( morphTargetInfluences[ i ] != 0.0 ) objectNormal += getMorph( gl_VertexID, i, 1 ).xyz * morphTargetInfluences[ i ];
		}
	#else
		objectNormal += morphNormal0 * morphTargetInfluences[ 0 ];
		objectNormal += morphNormal1 * morphTargetInfluences[ 1 ];
		objectNormal += morphNormal2 * morphTargetInfluences[ 2 ];
		objectNormal += morphNormal3 * morphTargetInfluences[ 3 ];
	#endif
#endif`,pm=`#ifdef USE_MORPHTARGETS
	uniform float morphTargetBaseInfluence;
	#ifdef MORPHTARGETS_TEXTURE
		uniform float morphTargetInfluences[ MORPHTARGETS_COUNT ];
		uniform sampler2DArray morphTargetsTexture;
		uniform ivec2 morphTargetsTextureSize;
		vec4 getMorph( const in int vertexIndex, const in int morphTargetIndex, const in int offset ) {
			int texelIndex = vertexIndex * MORPHTARGETS_TEXTURE_STRIDE + offset;
			int y = texelIndex / morphTargetsTextureSize.x;
			int x = texelIndex - y * morphTargetsTextureSize.x;
			ivec3 morphUV = ivec3( x, y, morphTargetIndex );
			return texelFetch( morphTargetsTexture, morphUV, 0 );
		}
	#else
		#ifndef USE_MORPHNORMALS
			uniform float morphTargetInfluences[ 8 ];
		#else
			uniform float morphTargetInfluences[ 4 ];
		#endif
	#endif
#endif`,mm=`#ifdef USE_MORPHTARGETS
	transformed *= morphTargetBaseInfluence;
	#ifdef MORPHTARGETS_TEXTURE
		for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
			if ( morphTargetInfluences[ i ] != 0.0 ) transformed += getMorph( gl_VertexID, i, 0 ).xyz * morphTargetInfluences[ i ];
		}
	#else
		transformed += morphTarget0 * morphTargetInfluences[ 0 ];
		transformed += morphTarget1 * morphTargetInfluences[ 1 ];
		transformed += morphTarget2 * morphTargetInfluences[ 2 ];
		transformed += morphTarget3 * morphTargetInfluences[ 3 ];
		#ifndef USE_MORPHNORMALS
			transformed += morphTarget4 * morphTargetInfluences[ 4 ];
			transformed += morphTarget5 * morphTargetInfluences[ 5 ];
			transformed += morphTarget6 * morphTargetInfluences[ 6 ];
			transformed += morphTarget7 * morphTargetInfluences[ 7 ];
		#endif
	#endif
#endif`,gm=`float faceDirection = gl_FrontFacing ? 1.0 : - 1.0;
#ifdef FLAT_SHADED
	vec3 fdx = dFdx( vViewPosition );
	vec3 fdy = dFdy( vViewPosition );
	vec3 normal = normalize( cross( fdx, fdy ) );
#else
	vec3 normal = normalize( vNormal );
	#ifdef DOUBLE_SIDED
		normal *= faceDirection;
	#endif
#endif
#if defined( USE_NORMALMAP_TANGENTSPACE ) || defined( USE_CLEARCOAT_NORMALMAP ) || defined( USE_ANISOTROPY )
	#ifdef USE_TANGENT
		mat3 tbn = mat3( normalize( vTangent ), normalize( vBitangent ), normal );
	#else
		mat3 tbn = getTangentFrame( - vViewPosition, normal,
		#if defined( USE_NORMALMAP )
			vNormalMapUv
		#elif defined( USE_CLEARCOAT_NORMALMAP )
			vClearcoatNormalMapUv
		#else
			vUv
		#endif
		);
	#endif
	#if defined( DOUBLE_SIDED ) && ! defined( FLAT_SHADED )
		tbn[0] *= faceDirection;
		tbn[1] *= faceDirection;
	#endif
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	#ifdef USE_TANGENT
		mat3 tbn2 = mat3( normalize( vTangent ), normalize( vBitangent ), normal );
	#else
		mat3 tbn2 = getTangentFrame( - vViewPosition, normal, vClearcoatNormalMapUv );
	#endif
	#if defined( DOUBLE_SIDED ) && ! defined( FLAT_SHADED )
		tbn2[0] *= faceDirection;
		tbn2[1] *= faceDirection;
	#endif
#endif
vec3 nonPerturbedNormal = normal;`,_m=`#ifdef USE_NORMALMAP_OBJECTSPACE
	normal = texture2D( normalMap, vNormalMapUv ).xyz * 2.0 - 1.0;
	#ifdef FLIP_SIDED
		normal = - normal;
	#endif
	#ifdef DOUBLE_SIDED
		normal = normal * faceDirection;
	#endif
	normal = normalize( normalMatrix * normal );
#elif defined( USE_NORMALMAP_TANGENTSPACE )
	vec3 mapN = texture2D( normalMap, vNormalMapUv ).xyz * 2.0 - 1.0;
	mapN.xy *= normalScale;
	normal = normalize( tbn * mapN );
#elif defined( USE_BUMPMAP )
	normal = perturbNormalArb( - vViewPosition, normal, dHdxy_fwd(), faceDirection );
#endif`,xm=`#ifndef FLAT_SHADED
	varying vec3 vNormal;
	#ifdef USE_TANGENT
		varying vec3 vTangent;
		varying vec3 vBitangent;
	#endif
#endif`,vm=`#ifndef FLAT_SHADED
	varying vec3 vNormal;
	#ifdef USE_TANGENT
		varying vec3 vTangent;
		varying vec3 vBitangent;
	#endif
#endif`,ym=`#ifndef FLAT_SHADED
	vNormal = normalize( transformedNormal );
	#ifdef USE_TANGENT
		vTangent = normalize( transformedTangent );
		vBitangent = normalize( cross( vNormal, vTangent ) * tangent.w );
	#endif
#endif`,Mm=`#ifdef USE_NORMALMAP
	uniform sampler2D normalMap;
	uniform vec2 normalScale;
#endif
#ifdef USE_NORMALMAP_OBJECTSPACE
	uniform mat3 normalMatrix;
#endif
#if ! defined ( USE_TANGENT ) && ( defined ( USE_NORMALMAP_TANGENTSPACE ) || defined ( USE_CLEARCOAT_NORMALMAP ) || defined( USE_ANISOTROPY ) )
	mat3 getTangentFrame( vec3 eye_pos, vec3 surf_norm, vec2 uv ) {
		vec3 q0 = dFdx( eye_pos.xyz );
		vec3 q1 = dFdy( eye_pos.xyz );
		vec2 st0 = dFdx( uv.st );
		vec2 st1 = dFdy( uv.st );
		vec3 N = surf_norm;
		vec3 q1perp = cross( q1, N );
		vec3 q0perp = cross( N, q0 );
		vec3 T = q1perp * st0.x + q0perp * st1.x;
		vec3 B = q1perp * st0.y + q0perp * st1.y;
		float det = max( dot( T, T ), dot( B, B ) );
		float scale = ( det == 0.0 ) ? 0.0 : inversesqrt( det );
		return mat3( T * scale, B * scale, N );
	}
#endif`,Sm=`#ifdef USE_CLEARCOAT
	vec3 clearcoatNormal = nonPerturbedNormal;
#endif`,bm=`#ifdef USE_CLEARCOAT_NORMALMAP
	vec3 clearcoatMapN = texture2D( clearcoatNormalMap, vClearcoatNormalMapUv ).xyz * 2.0 - 1.0;
	clearcoatMapN.xy *= clearcoatNormalScale;
	clearcoatNormal = normalize( tbn2 * clearcoatMapN );
#endif`,Em=`#ifdef USE_CLEARCOATMAP
	uniform sampler2D clearcoatMap;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	uniform sampler2D clearcoatNormalMap;
	uniform vec2 clearcoatNormalScale;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	uniform sampler2D clearcoatRoughnessMap;
#endif`,wm=`#ifdef USE_IRIDESCENCEMAP
	uniform sampler2D iridescenceMap;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	uniform sampler2D iridescenceThicknessMap;
#endif`,Tm=`#ifdef OPAQUE
diffuseColor.a = 1.0;
#endif
#ifdef USE_TRANSMISSION
diffuseColor.a *= material.transmissionAlpha;
#endif
gl_FragColor = vec4( outgoingLight, diffuseColor.a );`,Am=`vec3 packNormalToRGB( const in vec3 normal ) {
	return normalize( normal ) * 0.5 + 0.5;
}
vec3 unpackRGBToNormal( const in vec3 rgb ) {
	return 2.0 * rgb.xyz - 1.0;
}
const float PackUpscale = 256. / 255.;const float UnpackDownscale = 255. / 256.;
const vec3 PackFactors = vec3( 256. * 256. * 256., 256. * 256., 256. );
const vec4 UnpackFactors = UnpackDownscale / vec4( PackFactors, 1. );
const float ShiftRight8 = 1. / 256.;
vec4 packDepthToRGBA( const in float v ) {
	vec4 r = vec4( fract( v * PackFactors ), v );
	r.yzw -= r.xyz * ShiftRight8;	return r * PackUpscale;
}
float unpackRGBAToDepth( const in vec4 v ) {
	return dot( v, UnpackFactors );
}
vec2 packDepthToRG( in highp float v ) {
	return packDepthToRGBA( v ).yx;
}
float unpackRGToDepth( const in highp vec2 v ) {
	return unpackRGBAToDepth( vec4( v.xy, 0.0, 0.0 ) );
}
vec4 pack2HalfToRGBA( vec2 v ) {
	vec4 r = vec4( v.x, fract( v.x * 255.0 ), v.y, fract( v.y * 255.0 ) );
	return vec4( r.x - r.y / 255.0, r.y, r.z - r.w / 255.0, r.w );
}
vec2 unpackRGBATo2Half( vec4 v ) {
	return vec2( v.x + ( v.y / 255.0 ), v.z + ( v.w / 255.0 ) );
}
float viewZToOrthographicDepth( const in float viewZ, const in float near, const in float far ) {
	return ( viewZ + near ) / ( near - far );
}
float orthographicDepthToViewZ( const in float depth, const in float near, const in float far ) {
	return depth * ( near - far ) - near;
}
float viewZToPerspectiveDepth( const in float viewZ, const in float near, const in float far ) {
	return ( ( near + viewZ ) * far ) / ( ( far - near ) * viewZ );
}
float perspectiveDepthToViewZ( const in float depth, const in float near, const in float far ) {
	return ( near * far ) / ( ( far - near ) * depth - far );
}`,Rm=`#ifdef PREMULTIPLIED_ALPHA
	gl_FragColor.rgb *= gl_FragColor.a;
#endif`,Cm=`vec4 mvPosition = vec4( transformed, 1.0 );
#ifdef USE_BATCHING
	mvPosition = batchingMatrix * mvPosition;
#endif
#ifdef USE_INSTANCING
	mvPosition = instanceMatrix * mvPosition;
#endif
mvPosition = modelViewMatrix * mvPosition;
gl_Position = projectionMatrix * mvPosition;`,Pm=`#ifdef DITHERING
	gl_FragColor.rgb = dithering( gl_FragColor.rgb );
#endif`,Im=`#ifdef DITHERING
	vec3 dithering( vec3 color ) {
		float grid_position = rand( gl_FragCoord.xy );
		vec3 dither_shift_RGB = vec3( 0.25 / 255.0, -0.25 / 255.0, 0.25 / 255.0 );
		dither_shift_RGB = mix( 2.0 * dither_shift_RGB, -2.0 * dither_shift_RGB, grid_position );
		return color + dither_shift_RGB;
	}
#endif`,Lm=`float roughnessFactor = roughness;
#ifdef USE_ROUGHNESSMAP
	vec4 texelRoughness = texture2D( roughnessMap, vRoughnessMapUv );
	roughnessFactor *= texelRoughness.g;
#endif`,Um=`#ifdef USE_ROUGHNESSMAP
	uniform sampler2D roughnessMap;
#endif`,Dm=`#if NUM_SPOT_LIGHT_COORDS > 0
	varying vec4 vSpotLightCoord[ NUM_SPOT_LIGHT_COORDS ];
#endif
#if NUM_SPOT_LIGHT_MAPS > 0
	uniform sampler2D spotLightMap[ NUM_SPOT_LIGHT_MAPS ];
#endif
#ifdef USE_SHADOWMAP
	#if NUM_DIR_LIGHT_SHADOWS > 0
		uniform sampler2D directionalShadowMap[ NUM_DIR_LIGHT_SHADOWS ];
		varying vec4 vDirectionalShadowCoord[ NUM_DIR_LIGHT_SHADOWS ];
		struct DirectionalLightShadow {
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform DirectionalLightShadow directionalLightShadows[ NUM_DIR_LIGHT_SHADOWS ];
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
		uniform sampler2D spotShadowMap[ NUM_SPOT_LIGHT_SHADOWS ];
		struct SpotLightShadow {
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform SpotLightShadow spotLightShadows[ NUM_SPOT_LIGHT_SHADOWS ];
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		uniform sampler2D pointShadowMap[ NUM_POINT_LIGHT_SHADOWS ];
		varying vec4 vPointShadowCoord[ NUM_POINT_LIGHT_SHADOWS ];
		struct PointLightShadow {
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
			float shadowCameraNear;
			float shadowCameraFar;
		};
		uniform PointLightShadow pointLightShadows[ NUM_POINT_LIGHT_SHADOWS ];
	#endif
	float texture2DCompare( sampler2D depths, vec2 uv, float compare ) {
		return step( compare, unpackRGBAToDepth( texture2D( depths, uv ) ) );
	}
	vec2 texture2DDistribution( sampler2D shadow, vec2 uv ) {
		return unpackRGBATo2Half( texture2D( shadow, uv ) );
	}
	float VSMShadow (sampler2D shadow, vec2 uv, float compare ){
		float occlusion = 1.0;
		vec2 distribution = texture2DDistribution( shadow, uv );
		float hard_shadow = step( compare , distribution.x );
		if (hard_shadow != 1.0 ) {
			float distance = compare - distribution.x ;
			float variance = max( 0.00000, distribution.y * distribution.y );
			float softness_probability = variance / (variance + distance * distance );			softness_probability = clamp( ( softness_probability - 0.3 ) / ( 0.95 - 0.3 ), 0.0, 1.0 );			occlusion = clamp( max( hard_shadow, softness_probability ), 0.0, 1.0 );
		}
		return occlusion;
	}
	float getShadow( sampler2D shadowMap, vec2 shadowMapSize, float shadowBias, float shadowRadius, vec4 shadowCoord ) {
		float shadow = 1.0;
		shadowCoord.xyz /= shadowCoord.w;
		shadowCoord.z += shadowBias;
		bool inFrustum = shadowCoord.x >= 0.0 && shadowCoord.x <= 1.0 && shadowCoord.y >= 0.0 && shadowCoord.y <= 1.0;
		bool frustumTest = inFrustum && shadowCoord.z <= 1.0;
		if ( frustumTest ) {
		#if defined( SHADOWMAP_TYPE_PCF )
			vec2 texelSize = vec2( 1.0 ) / shadowMapSize;
			float dx0 = - texelSize.x * shadowRadius;
			float dy0 = - texelSize.y * shadowRadius;
			float dx1 = + texelSize.x * shadowRadius;
			float dy1 = + texelSize.y * shadowRadius;
			float dx2 = dx0 / 2.0;
			float dy2 = dy0 / 2.0;
			float dx3 = dx1 / 2.0;
			float dy3 = dy1 / 2.0;
			shadow = (
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx0, dy0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( 0.0, dy0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx1, dy0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx2, dy2 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( 0.0, dy2 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx3, dy2 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx0, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx2, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy, shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx3, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx1, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx2, dy3 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( 0.0, dy3 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx3, dy3 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx0, dy1 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( 0.0, dy1 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, shadowCoord.xy + vec2( dx1, dy1 ), shadowCoord.z )
			) * ( 1.0 / 17.0 );
		#elif defined( SHADOWMAP_TYPE_PCF_SOFT )
			vec2 texelSize = vec2( 1.0 ) / shadowMapSize;
			float dx = texelSize.x;
			float dy = texelSize.y;
			vec2 uv = shadowCoord.xy;
			vec2 f = fract( uv * shadowMapSize + 0.5 );
			uv -= f * texelSize;
			shadow = (
				texture2DCompare( shadowMap, uv, shadowCoord.z ) +
				texture2DCompare( shadowMap, uv + vec2( dx, 0.0 ), shadowCoord.z ) +
				texture2DCompare( shadowMap, uv + vec2( 0.0, dy ), shadowCoord.z ) +
				texture2DCompare( shadowMap, uv + texelSize, shadowCoord.z ) +
				mix( texture2DCompare( shadowMap, uv + vec2( -dx, 0.0 ), shadowCoord.z ),
					 texture2DCompare( shadowMap, uv + vec2( 2.0 * dx, 0.0 ), shadowCoord.z ),
					 f.x ) +
				mix( texture2DCompare( shadowMap, uv + vec2( -dx, dy ), shadowCoord.z ),
					 texture2DCompare( shadowMap, uv + vec2( 2.0 * dx, dy ), shadowCoord.z ),
					 f.x ) +
				mix( texture2DCompare( shadowMap, uv + vec2( 0.0, -dy ), shadowCoord.z ),
					 texture2DCompare( shadowMap, uv + vec2( 0.0, 2.0 * dy ), shadowCoord.z ),
					 f.y ) +
				mix( texture2DCompare( shadowMap, uv + vec2( dx, -dy ), shadowCoord.z ),
					 texture2DCompare( shadowMap, uv + vec2( dx, 2.0 * dy ), shadowCoord.z ),
					 f.y ) +
				mix( mix( texture2DCompare( shadowMap, uv + vec2( -dx, -dy ), shadowCoord.z ),
						  texture2DCompare( shadowMap, uv + vec2( 2.0 * dx, -dy ), shadowCoord.z ),
						  f.x ),
					 mix( texture2DCompare( shadowMap, uv + vec2( -dx, 2.0 * dy ), shadowCoord.z ),
						  texture2DCompare( shadowMap, uv + vec2( 2.0 * dx, 2.0 * dy ), shadowCoord.z ),
						  f.x ),
					 f.y )
			) * ( 1.0 / 9.0 );
		#elif defined( SHADOWMAP_TYPE_VSM )
			shadow = VSMShadow( shadowMap, shadowCoord.xy, shadowCoord.z );
		#else
			shadow = texture2DCompare( shadowMap, shadowCoord.xy, shadowCoord.z );
		#endif
		}
		return shadow;
	}
	vec2 cubeToUV( vec3 v, float texelSizeY ) {
		vec3 absV = abs( v );
		float scaleToCube = 1.0 / max( absV.x, max( absV.y, absV.z ) );
		absV *= scaleToCube;
		v *= scaleToCube * ( 1.0 - 2.0 * texelSizeY );
		vec2 planar = v.xy;
		float almostATexel = 1.5 * texelSizeY;
		float almostOne = 1.0 - almostATexel;
		if ( absV.z >= almostOne ) {
			if ( v.z > 0.0 )
				planar.x = 4.0 - v.x;
		} else if ( absV.x >= almostOne ) {
			float signX = sign( v.x );
			planar.x = v.z * signX + 2.0 * signX;
		} else if ( absV.y >= almostOne ) {
			float signY = sign( v.y );
			planar.x = v.x + 2.0 * signY + 2.0;
			planar.y = v.z * signY - 2.0;
		}
		return vec2( 0.125, 0.25 ) * planar + vec2( 0.375, 0.75 );
	}
	float getPointShadow( sampler2D shadowMap, vec2 shadowMapSize, float shadowBias, float shadowRadius, vec4 shadowCoord, float shadowCameraNear, float shadowCameraFar ) {
		vec2 texelSize = vec2( 1.0 ) / ( shadowMapSize * vec2( 4.0, 2.0 ) );
		vec3 lightToPosition = shadowCoord.xyz;
		float dp = ( length( lightToPosition ) - shadowCameraNear ) / ( shadowCameraFar - shadowCameraNear );		dp += shadowBias;
		vec3 bd3D = normalize( lightToPosition );
		#if defined( SHADOWMAP_TYPE_PCF ) || defined( SHADOWMAP_TYPE_PCF_SOFT ) || defined( SHADOWMAP_TYPE_VSM )
			vec2 offset = vec2( - 1, 1 ) * shadowRadius * texelSize.y;
			return (
				texture2DCompare( shadowMap, cubeToUV( bd3D + offset.xyy, texelSize.y ), dp ) +
				texture2DCompare( shadowMap, cubeToUV( bd3D + offset.yyy, texelSize.y ), dp ) +
				texture2DCompare( shadowMap, cubeToUV( bd3D + offset.xyx, texelSize.y ), dp ) +
				texture2DCompare( shadowMap, cubeToUV( bd3D + offset.yyx, texelSize.y ), dp ) +
				texture2DCompare( shadowMap, cubeToUV( bd3D, texelSize.y ), dp ) +
				texture2DCompare( shadowMap, cubeToUV( bd3D + offset.xxy, texelSize.y ), dp ) +
				texture2DCompare( shadowMap, cubeToUV( bd3D + offset.yxy, texelSize.y ), dp ) +
				texture2DCompare( shadowMap, cubeToUV( bd3D + offset.xxx, texelSize.y ), dp ) +
				texture2DCompare( shadowMap, cubeToUV( bd3D + offset.yxx, texelSize.y ), dp )
			) * ( 1.0 / 9.0 );
		#else
			return texture2DCompare( shadowMap, cubeToUV( bd3D, texelSize.y ), dp );
		#endif
	}
#endif`,Nm=`#if NUM_SPOT_LIGHT_COORDS > 0
	uniform mat4 spotLightMatrix[ NUM_SPOT_LIGHT_COORDS ];
	varying vec4 vSpotLightCoord[ NUM_SPOT_LIGHT_COORDS ];
#endif
#ifdef USE_SHADOWMAP
	#if NUM_DIR_LIGHT_SHADOWS > 0
		uniform mat4 directionalShadowMatrix[ NUM_DIR_LIGHT_SHADOWS ];
		varying vec4 vDirectionalShadowCoord[ NUM_DIR_LIGHT_SHADOWS ];
		struct DirectionalLightShadow {
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform DirectionalLightShadow directionalLightShadows[ NUM_DIR_LIGHT_SHADOWS ];
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
		struct SpotLightShadow {
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform SpotLightShadow spotLightShadows[ NUM_SPOT_LIGHT_SHADOWS ];
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		uniform mat4 pointShadowMatrix[ NUM_POINT_LIGHT_SHADOWS ];
		varying vec4 vPointShadowCoord[ NUM_POINT_LIGHT_SHADOWS ];
		struct PointLightShadow {
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
			float shadowCameraNear;
			float shadowCameraFar;
		};
		uniform PointLightShadow pointLightShadows[ NUM_POINT_LIGHT_SHADOWS ];
	#endif
#endif`,Fm=`#if ( defined( USE_SHADOWMAP ) && ( NUM_DIR_LIGHT_SHADOWS > 0 || NUM_POINT_LIGHT_SHADOWS > 0 ) ) || ( NUM_SPOT_LIGHT_COORDS > 0 )
	vec3 shadowWorldNormal = inverseTransformDirection( transformedNormal, viewMatrix );
	vec4 shadowWorldPosition;
#endif
#if defined( USE_SHADOWMAP )
	#if NUM_DIR_LIGHT_SHADOWS > 0
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_DIR_LIGHT_SHADOWS; i ++ ) {
			shadowWorldPosition = worldPosition + vec4( shadowWorldNormal * directionalLightShadows[ i ].shadowNormalBias, 0 );
			vDirectionalShadowCoord[ i ] = directionalShadowMatrix[ i ] * shadowWorldPosition;
		}
		#pragma unroll_loop_end
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_POINT_LIGHT_SHADOWS; i ++ ) {
			shadowWorldPosition = worldPosition + vec4( shadowWorldNormal * pointLightShadows[ i ].shadowNormalBias, 0 );
			vPointShadowCoord[ i ] = pointShadowMatrix[ i ] * shadowWorldPosition;
		}
		#pragma unroll_loop_end
	#endif
#endif
#if NUM_SPOT_LIGHT_COORDS > 0
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHT_COORDS; i ++ ) {
		shadowWorldPosition = worldPosition;
		#if ( defined( USE_SHADOWMAP ) && UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
			shadowWorldPosition.xyz += shadowWorldNormal * spotLightShadows[ i ].shadowNormalBias;
		#endif
		vSpotLightCoord[ i ] = spotLightMatrix[ i ] * shadowWorldPosition;
	}
	#pragma unroll_loop_end
#endif`,Om=`float getShadowMask() {
	float shadow = 1.0;
	#ifdef USE_SHADOWMAP
	#if NUM_DIR_LIGHT_SHADOWS > 0
	DirectionalLightShadow directionalLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_DIR_LIGHT_SHADOWS; i ++ ) {
		directionalLight = directionalLightShadows[ i ];
		shadow *= receiveShadow ? getShadow( directionalShadowMap[ i ], directionalLight.shadowMapSize, directionalLight.shadowBias, directionalLight.shadowRadius, vDirectionalShadowCoord[ i ] ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
	SpotLightShadow spotLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHT_SHADOWS; i ++ ) {
		spotLight = spotLightShadows[ i ];
		shadow *= receiveShadow ? getShadow( spotShadowMap[ i ], spotLight.shadowMapSize, spotLight.shadowBias, spotLight.shadowRadius, vSpotLightCoord[ i ] ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
	PointLightShadow pointLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_POINT_LIGHT_SHADOWS; i ++ ) {
		pointLight = pointLightShadows[ i ];
		shadow *= receiveShadow ? getPointShadow( pointShadowMap[ i ], pointLight.shadowMapSize, pointLight.shadowBias, pointLight.shadowRadius, vPointShadowCoord[ i ], pointLight.shadowCameraNear, pointLight.shadowCameraFar ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#endif
	return shadow;
}`,Bm=`#ifdef USE_SKINNING
	mat4 boneMatX = getBoneMatrix( skinIndex.x );
	mat4 boneMatY = getBoneMatrix( skinIndex.y );
	mat4 boneMatZ = getBoneMatrix( skinIndex.z );
	mat4 boneMatW = getBoneMatrix( skinIndex.w );
#endif`,zm=`#ifdef USE_SKINNING
	uniform mat4 bindMatrix;
	uniform mat4 bindMatrixInverse;
	uniform highp sampler2D boneTexture;
	mat4 getBoneMatrix( const in float i ) {
		int size = textureSize( boneTexture, 0 ).x;
		int j = int( i ) * 4;
		int x = j % size;
		int y = j / size;
		vec4 v1 = texelFetch( boneTexture, ivec2( x, y ), 0 );
		vec4 v2 = texelFetch( boneTexture, ivec2( x + 1, y ), 0 );
		vec4 v3 = texelFetch( boneTexture, ivec2( x + 2, y ), 0 );
		vec4 v4 = texelFetch( boneTexture, ivec2( x + 3, y ), 0 );
		return mat4( v1, v2, v3, v4 );
	}
#endif`,Hm=`#ifdef USE_SKINNING
	vec4 skinVertex = bindMatrix * vec4( transformed, 1.0 );
	vec4 skinned = vec4( 0.0 );
	skinned += boneMatX * skinVertex * skinWeight.x;
	skinned += boneMatY * skinVertex * skinWeight.y;
	skinned += boneMatZ * skinVertex * skinWeight.z;
	skinned += boneMatW * skinVertex * skinWeight.w;
	transformed = ( bindMatrixInverse * skinned ).xyz;
#endif`,km=`#ifdef USE_SKINNING
	mat4 skinMatrix = mat4( 0.0 );
	skinMatrix += skinWeight.x * boneMatX;
	skinMatrix += skinWeight.y * boneMatY;
	skinMatrix += skinWeight.z * boneMatZ;
	skinMatrix += skinWeight.w * boneMatW;
	skinMatrix = bindMatrixInverse * skinMatrix * bindMatrix;
	objectNormal = vec4( skinMatrix * vec4( objectNormal, 0.0 ) ).xyz;
	#ifdef USE_TANGENT
		objectTangent = vec4( skinMatrix * vec4( objectTangent, 0.0 ) ).xyz;
	#endif
#endif`,Vm=`float specularStrength;
#ifdef USE_SPECULARMAP
	vec4 texelSpecular = texture2D( specularMap, vSpecularMapUv );
	specularStrength = texelSpecular.r;
#else
	specularStrength = 1.0;
#endif`,Gm=`#ifdef USE_SPECULARMAP
	uniform sampler2D specularMap;
#endif`,Wm=`#if defined( TONE_MAPPING )
	gl_FragColor.rgb = toneMapping( gl_FragColor.rgb );
#endif`,Xm=`#ifndef saturate
#define saturate( a ) clamp( a, 0.0, 1.0 )
#endif
uniform float toneMappingExposure;
vec3 LinearToneMapping( vec3 color ) {
	return saturate( toneMappingExposure * color );
}
vec3 ReinhardToneMapping( vec3 color ) {
	color *= toneMappingExposure;
	return saturate( color / ( vec3( 1.0 ) + color ) );
}
vec3 OptimizedCineonToneMapping( vec3 color ) {
	color *= toneMappingExposure;
	color = max( vec3( 0.0 ), color - 0.004 );
	return pow( ( color * ( 6.2 * color + 0.5 ) ) / ( color * ( 6.2 * color + 1.7 ) + 0.06 ), vec3( 2.2 ) );
}
vec3 RRTAndODTFit( vec3 v ) {
	vec3 a = v * ( v + 0.0245786 ) - 0.000090537;
	vec3 b = v * ( 0.983729 * v + 0.4329510 ) + 0.238081;
	return a / b;
}
vec3 ACESFilmicToneMapping( vec3 color ) {
	const mat3 ACESInputMat = mat3(
		vec3( 0.59719, 0.07600, 0.02840 ),		vec3( 0.35458, 0.90834, 0.13383 ),
		vec3( 0.04823, 0.01566, 0.83777 )
	);
	const mat3 ACESOutputMat = mat3(
		vec3(  1.60475, -0.10208, -0.00327 ),		vec3( -0.53108,  1.10813, -0.07276 ),
		vec3( -0.07367, -0.00605,  1.07602 )
	);
	color *= toneMappingExposure / 0.6;
	color = ACESInputMat * color;
	color = RRTAndODTFit( color );
	color = ACESOutputMat * color;
	return saturate( color );
}
const mat3 LINEAR_REC2020_TO_LINEAR_SRGB = mat3(
	vec3( 1.6605, - 0.1246, - 0.0182 ),
	vec3( - 0.5876, 1.1329, - 0.1006 ),
	vec3( - 0.0728, - 0.0083, 1.1187 )
);
const mat3 LINEAR_SRGB_TO_LINEAR_REC2020 = mat3(
	vec3( 0.6274, 0.0691, 0.0164 ),
	vec3( 0.3293, 0.9195, 0.0880 ),
	vec3( 0.0433, 0.0113, 0.8956 )
);
vec3 agxDefaultContrastApprox( vec3 x ) {
	vec3 x2 = x * x;
	vec3 x4 = x2 * x2;
	return + 15.5 * x4 * x2
		- 40.14 * x4 * x
		+ 31.96 * x4
		- 6.868 * x2 * x
		+ 0.4298 * x2
		+ 0.1191 * x
		- 0.00232;
}
vec3 AgXToneMapping( vec3 color ) {
	const mat3 AgXInsetMatrix = mat3(
		vec3( 0.856627153315983, 0.137318972929847, 0.11189821299995 ),
		vec3( 0.0951212405381588, 0.761241990602591, 0.0767994186031903 ),
		vec3( 0.0482516061458583, 0.101439036467562, 0.811302368396859 )
	);
	const mat3 AgXOutsetMatrix = mat3(
		vec3( 1.1271005818144368, - 0.1413297634984383, - 0.14132976349843826 ),
		vec3( - 0.11060664309660323, 1.157823702216272, - 0.11060664309660294 ),
		vec3( - 0.016493938717834573, - 0.016493938717834257, 1.2519364065950405 )
	);
	const float AgxMinEv = - 12.47393;	const float AgxMaxEv = 4.026069;
	color = LINEAR_SRGB_TO_LINEAR_REC2020 * color;
	color *= toneMappingExposure;
	color = AgXInsetMatrix * color;
	color = max( color, 1e-10 );	color = log2( color );
	color = ( color - AgxMinEv ) / ( AgxMaxEv - AgxMinEv );
	color = clamp( color, 0.0, 1.0 );
	color = agxDefaultContrastApprox( color );
	color = AgXOutsetMatrix * color;
	color = pow( max( vec3( 0.0 ), color ), vec3( 2.2 ) );
	color = LINEAR_REC2020_TO_LINEAR_SRGB * color;
	return color;
}
vec3 CustomToneMapping( vec3 color ) { return color; }`,Ym=`#ifdef USE_TRANSMISSION
	material.transmission = transmission;
	material.transmissionAlpha = 1.0;
	material.thickness = thickness;
	material.attenuationDistance = attenuationDistance;
	material.attenuationColor = attenuationColor;
	#ifdef USE_TRANSMISSIONMAP
		material.transmission *= texture2D( transmissionMap, vTransmissionMapUv ).r;
	#endif
	#ifdef USE_THICKNESSMAP
		material.thickness *= texture2D( thicknessMap, vThicknessMapUv ).g;
	#endif
	vec3 pos = vWorldPosition;
	vec3 v = normalize( cameraPosition - pos );
	vec3 n = inverseTransformDirection( normal, viewMatrix );
	vec4 transmitted = getIBLVolumeRefraction(
		n, v, material.roughness, material.diffuseColor, material.specularColor, material.specularF90,
		pos, modelMatrix, viewMatrix, projectionMatrix, material.ior, material.thickness,
		material.attenuationColor, material.attenuationDistance );
	material.transmissionAlpha = mix( material.transmissionAlpha, transmitted.a, material.transmission );
	totalDiffuse = mix( totalDiffuse, transmitted.rgb, material.transmission );
#endif`,qm=`#ifdef USE_TRANSMISSION
	uniform float transmission;
	uniform float thickness;
	uniform float attenuationDistance;
	uniform vec3 attenuationColor;
	#ifdef USE_TRANSMISSIONMAP
		uniform sampler2D transmissionMap;
	#endif
	#ifdef USE_THICKNESSMAP
		uniform sampler2D thicknessMap;
	#endif
	uniform vec2 transmissionSamplerSize;
	uniform sampler2D transmissionSamplerMap;
	uniform mat4 modelMatrix;
	uniform mat4 projectionMatrix;
	varying vec3 vWorldPosition;
	float w0( float a ) {
		return ( 1.0 / 6.0 ) * ( a * ( a * ( - a + 3.0 ) - 3.0 ) + 1.0 );
	}
	float w1( float a ) {
		return ( 1.0 / 6.0 ) * ( a *  a * ( 3.0 * a - 6.0 ) + 4.0 );
	}
	float w2( float a ){
		return ( 1.0 / 6.0 ) * ( a * ( a * ( - 3.0 * a + 3.0 ) + 3.0 ) + 1.0 );
	}
	float w3( float a ) {
		return ( 1.0 / 6.0 ) * ( a * a * a );
	}
	float g0( float a ) {
		return w0( a ) + w1( a );
	}
	float g1( float a ) {
		return w2( a ) + w3( a );
	}
	float h0( float a ) {
		return - 1.0 + w1( a ) / ( w0( a ) + w1( a ) );
	}
	float h1( float a ) {
		return 1.0 + w3( a ) / ( w2( a ) + w3( a ) );
	}
	vec4 bicubic( sampler2D tex, vec2 uv, vec4 texelSize, float lod ) {
		uv = uv * texelSize.zw + 0.5;
		vec2 iuv = floor( uv );
		vec2 fuv = fract( uv );
		float g0x = g0( fuv.x );
		float g1x = g1( fuv.x );
		float h0x = h0( fuv.x );
		float h1x = h1( fuv.x );
		float h0y = h0( fuv.y );
		float h1y = h1( fuv.y );
		vec2 p0 = ( vec2( iuv.x + h0x, iuv.y + h0y ) - 0.5 ) * texelSize.xy;
		vec2 p1 = ( vec2( iuv.x + h1x, iuv.y + h0y ) - 0.5 ) * texelSize.xy;
		vec2 p2 = ( vec2( iuv.x + h0x, iuv.y + h1y ) - 0.5 ) * texelSize.xy;
		vec2 p3 = ( vec2( iuv.x + h1x, iuv.y + h1y ) - 0.5 ) * texelSize.xy;
		return g0( fuv.y ) * ( g0x * textureLod( tex, p0, lod ) + g1x * textureLod( tex, p1, lod ) ) +
			g1( fuv.y ) * ( g0x * textureLod( tex, p2, lod ) + g1x * textureLod( tex, p3, lod ) );
	}
	vec4 textureBicubic( sampler2D sampler, vec2 uv, float lod ) {
		vec2 fLodSize = vec2( textureSize( sampler, int( lod ) ) );
		vec2 cLodSize = vec2( textureSize( sampler, int( lod + 1.0 ) ) );
		vec2 fLodSizeInv = 1.0 / fLodSize;
		vec2 cLodSizeInv = 1.0 / cLodSize;
		vec4 fSample = bicubic( sampler, uv, vec4( fLodSizeInv, fLodSize ), floor( lod ) );
		vec4 cSample = bicubic( sampler, uv, vec4( cLodSizeInv, cLodSize ), ceil( lod ) );
		return mix( fSample, cSample, fract( lod ) );
	}
	vec3 getVolumeTransmissionRay( const in vec3 n, const in vec3 v, const in float thickness, const in float ior, const in mat4 modelMatrix ) {
		vec3 refractionVector = refract( - v, normalize( n ), 1.0 / ior );
		vec3 modelScale;
		modelScale.x = length( vec3( modelMatrix[ 0 ].xyz ) );
		modelScale.y = length( vec3( modelMatrix[ 1 ].xyz ) );
		modelScale.z = length( vec3( modelMatrix[ 2 ].xyz ) );
		return normalize( refractionVector ) * thickness * modelScale;
	}
	float applyIorToRoughness( const in float roughness, const in float ior ) {
		return roughness * clamp( ior * 2.0 - 2.0, 0.0, 1.0 );
	}
	vec4 getTransmissionSample( const in vec2 fragCoord, const in float roughness, const in float ior ) {
		float lod = log2( transmissionSamplerSize.x ) * applyIorToRoughness( roughness, ior );
		return textureBicubic( transmissionSamplerMap, fragCoord.xy, lod );
	}
	vec3 volumeAttenuation( const in float transmissionDistance, const in vec3 attenuationColor, const in float attenuationDistance ) {
		if ( isinf( attenuationDistance ) ) {
			return vec3( 1.0 );
		} else {
			vec3 attenuationCoefficient = -log( attenuationColor ) / attenuationDistance;
			vec3 transmittance = exp( - attenuationCoefficient * transmissionDistance );			return transmittance;
		}
	}
	vec4 getIBLVolumeRefraction( const in vec3 n, const in vec3 v, const in float roughness, const in vec3 diffuseColor,
		const in vec3 specularColor, const in float specularF90, const in vec3 position, const in mat4 modelMatrix,
		const in mat4 viewMatrix, const in mat4 projMatrix, const in float ior, const in float thickness,
		const in vec3 attenuationColor, const in float attenuationDistance ) {
		vec3 transmissionRay = getVolumeTransmissionRay( n, v, thickness, ior, modelMatrix );
		vec3 refractedRayExit = position + transmissionRay;
		vec4 ndcPos = projMatrix * viewMatrix * vec4( refractedRayExit, 1.0 );
		vec2 refractionCoords = ndcPos.xy / ndcPos.w;
		refractionCoords += 1.0;
		refractionCoords /= 2.0;
		vec4 transmittedLight = getTransmissionSample( refractionCoords, roughness, ior );
		vec3 transmittance = diffuseColor * volumeAttenuation( length( transmissionRay ), attenuationColor, attenuationDistance );
		vec3 attenuatedColor = transmittance * transmittedLight.rgb;
		vec3 F = EnvironmentBRDF( n, v, specularColor, specularF90, roughness );
		float transmittanceFactor = ( transmittance.r + transmittance.g + transmittance.b ) / 3.0;
		return vec4( ( 1.0 - F ) * attenuatedColor, 1.0 - ( 1.0 - transmittedLight.a ) * transmittanceFactor );
	}
#endif`,Zm=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	varying vec2 vUv;
#endif
#ifdef USE_MAP
	varying vec2 vMapUv;
#endif
#ifdef USE_ALPHAMAP
	varying vec2 vAlphaMapUv;
#endif
#ifdef USE_LIGHTMAP
	varying vec2 vLightMapUv;
#endif
#ifdef USE_AOMAP
	varying vec2 vAoMapUv;
#endif
#ifdef USE_BUMPMAP
	varying vec2 vBumpMapUv;
#endif
#ifdef USE_NORMALMAP
	varying vec2 vNormalMapUv;
#endif
#ifdef USE_EMISSIVEMAP
	varying vec2 vEmissiveMapUv;
#endif
#ifdef USE_METALNESSMAP
	varying vec2 vMetalnessMapUv;
#endif
#ifdef USE_ROUGHNESSMAP
	varying vec2 vRoughnessMapUv;
#endif
#ifdef USE_ANISOTROPYMAP
	varying vec2 vAnisotropyMapUv;
#endif
#ifdef USE_CLEARCOATMAP
	varying vec2 vClearcoatMapUv;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	varying vec2 vClearcoatNormalMapUv;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	varying vec2 vClearcoatRoughnessMapUv;
#endif
#ifdef USE_IRIDESCENCEMAP
	varying vec2 vIridescenceMapUv;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	varying vec2 vIridescenceThicknessMapUv;
#endif
#ifdef USE_SHEEN_COLORMAP
	varying vec2 vSheenColorMapUv;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	varying vec2 vSheenRoughnessMapUv;
#endif
#ifdef USE_SPECULARMAP
	varying vec2 vSpecularMapUv;
#endif
#ifdef USE_SPECULAR_COLORMAP
	varying vec2 vSpecularColorMapUv;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	varying vec2 vSpecularIntensityMapUv;
#endif
#ifdef USE_TRANSMISSIONMAP
	uniform mat3 transmissionMapTransform;
	varying vec2 vTransmissionMapUv;
#endif
#ifdef USE_THICKNESSMAP
	uniform mat3 thicknessMapTransform;
	varying vec2 vThicknessMapUv;
#endif`,$m=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	varying vec2 vUv;
#endif
#ifdef USE_MAP
	uniform mat3 mapTransform;
	varying vec2 vMapUv;
#endif
#ifdef USE_ALPHAMAP
	uniform mat3 alphaMapTransform;
	varying vec2 vAlphaMapUv;
#endif
#ifdef USE_LIGHTMAP
	uniform mat3 lightMapTransform;
	varying vec2 vLightMapUv;
#endif
#ifdef USE_AOMAP
	uniform mat3 aoMapTransform;
	varying vec2 vAoMapUv;
#endif
#ifdef USE_BUMPMAP
	uniform mat3 bumpMapTransform;
	varying vec2 vBumpMapUv;
#endif
#ifdef USE_NORMALMAP
	uniform mat3 normalMapTransform;
	varying vec2 vNormalMapUv;
#endif
#ifdef USE_DISPLACEMENTMAP
	uniform mat3 displacementMapTransform;
	varying vec2 vDisplacementMapUv;
#endif
#ifdef USE_EMISSIVEMAP
	uniform mat3 emissiveMapTransform;
	varying vec2 vEmissiveMapUv;
#endif
#ifdef USE_METALNESSMAP
	uniform mat3 metalnessMapTransform;
	varying vec2 vMetalnessMapUv;
#endif
#ifdef USE_ROUGHNESSMAP
	uniform mat3 roughnessMapTransform;
	varying vec2 vRoughnessMapUv;
#endif
#ifdef USE_ANISOTROPYMAP
	uniform mat3 anisotropyMapTransform;
	varying vec2 vAnisotropyMapUv;
#endif
#ifdef USE_CLEARCOATMAP
	uniform mat3 clearcoatMapTransform;
	varying vec2 vClearcoatMapUv;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	uniform mat3 clearcoatNormalMapTransform;
	varying vec2 vClearcoatNormalMapUv;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	uniform mat3 clearcoatRoughnessMapTransform;
	varying vec2 vClearcoatRoughnessMapUv;
#endif
#ifdef USE_SHEEN_COLORMAP
	uniform mat3 sheenColorMapTransform;
	varying vec2 vSheenColorMapUv;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	uniform mat3 sheenRoughnessMapTransform;
	varying vec2 vSheenRoughnessMapUv;
#endif
#ifdef USE_IRIDESCENCEMAP
	uniform mat3 iridescenceMapTransform;
	varying vec2 vIridescenceMapUv;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	uniform mat3 iridescenceThicknessMapTransform;
	varying vec2 vIridescenceThicknessMapUv;
#endif
#ifdef USE_SPECULARMAP
	uniform mat3 specularMapTransform;
	varying vec2 vSpecularMapUv;
#endif
#ifdef USE_SPECULAR_COLORMAP
	uniform mat3 specularColorMapTransform;
	varying vec2 vSpecularColorMapUv;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	uniform mat3 specularIntensityMapTransform;
	varying vec2 vSpecularIntensityMapUv;
#endif
#ifdef USE_TRANSMISSIONMAP
	uniform mat3 transmissionMapTransform;
	varying vec2 vTransmissionMapUv;
#endif
#ifdef USE_THICKNESSMAP
	uniform mat3 thicknessMapTransform;
	varying vec2 vThicknessMapUv;
#endif`,Jm=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	vUv = vec3( uv, 1 ).xy;
#endif
#ifdef USE_MAP
	vMapUv = ( mapTransform * vec3( MAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ALPHAMAP
	vAlphaMapUv = ( alphaMapTransform * vec3( ALPHAMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_LIGHTMAP
	vLightMapUv = ( lightMapTransform * vec3( LIGHTMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_AOMAP
	vAoMapUv = ( aoMapTransform * vec3( AOMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_BUMPMAP
	vBumpMapUv = ( bumpMapTransform * vec3( BUMPMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_NORMALMAP
	vNormalMapUv = ( normalMapTransform * vec3( NORMALMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_DISPLACEMENTMAP
	vDisplacementMapUv = ( displacementMapTransform * vec3( DISPLACEMENTMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_EMISSIVEMAP
	vEmissiveMapUv = ( emissiveMapTransform * vec3( EMISSIVEMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_METALNESSMAP
	vMetalnessMapUv = ( metalnessMapTransform * vec3( METALNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ROUGHNESSMAP
	vRoughnessMapUv = ( roughnessMapTransform * vec3( ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ANISOTROPYMAP
	vAnisotropyMapUv = ( anisotropyMapTransform * vec3( ANISOTROPYMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOATMAP
	vClearcoatMapUv = ( clearcoatMapTransform * vec3( CLEARCOATMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	vClearcoatNormalMapUv = ( clearcoatNormalMapTransform * vec3( CLEARCOAT_NORMALMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	vClearcoatRoughnessMapUv = ( clearcoatRoughnessMapTransform * vec3( CLEARCOAT_ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_IRIDESCENCEMAP
	vIridescenceMapUv = ( iridescenceMapTransform * vec3( IRIDESCENCEMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	vIridescenceThicknessMapUv = ( iridescenceThicknessMapTransform * vec3( IRIDESCENCE_THICKNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SHEEN_COLORMAP
	vSheenColorMapUv = ( sheenColorMapTransform * vec3( SHEEN_COLORMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	vSheenRoughnessMapUv = ( sheenRoughnessMapTransform * vec3( SHEEN_ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULARMAP
	vSpecularMapUv = ( specularMapTransform * vec3( SPECULARMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULAR_COLORMAP
	vSpecularColorMapUv = ( specularColorMapTransform * vec3( SPECULAR_COLORMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	vSpecularIntensityMapUv = ( specularIntensityMapTransform * vec3( SPECULAR_INTENSITYMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_TRANSMISSIONMAP
	vTransmissionMapUv = ( transmissionMapTransform * vec3( TRANSMISSIONMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_THICKNESSMAP
	vThicknessMapUv = ( thicknessMapTransform * vec3( THICKNESSMAP_UV, 1 ) ).xy;
#endif`,Km=`#if defined( USE_ENVMAP ) || defined( DISTANCE ) || defined ( USE_SHADOWMAP ) || defined ( USE_TRANSMISSION ) || NUM_SPOT_LIGHT_COORDS > 0
	vec4 worldPosition = vec4( transformed, 1.0 );
	#ifdef USE_BATCHING
		worldPosition = batchingMatrix * worldPosition;
	#endif
	#ifdef USE_INSTANCING
		worldPosition = instanceMatrix * worldPosition;
	#endif
	worldPosition = modelMatrix * worldPosition;
#endif`,jm=`varying vec2 vUv;
uniform mat3 uvTransform;
void main() {
	vUv = ( uvTransform * vec3( uv, 1 ) ).xy;
	gl_Position = vec4( position.xy, 1.0, 1.0 );
}`,Qm=`uniform sampler2D t2D;
uniform float backgroundIntensity;
varying vec2 vUv;
void main() {
	vec4 texColor = texture2D( t2D, vUv );
	#ifdef DECODE_VIDEO_TEXTURE
		texColor = vec4( mix( pow( texColor.rgb * 0.9478672986 + vec3( 0.0521327014 ), vec3( 2.4 ) ), texColor.rgb * 0.0773993808, vec3( lessThanEqual( texColor.rgb, vec3( 0.04045 ) ) ) ), texColor.w );
	#endif
	texColor.rgb *= backgroundIntensity;
	gl_FragColor = texColor;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,tg=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
	gl_Position.z = gl_Position.w;
}`,eg=`#ifdef ENVMAP_TYPE_CUBE
	uniform samplerCube envMap;
#elif defined( ENVMAP_TYPE_CUBE_UV )
	uniform sampler2D envMap;
#endif
uniform float flipEnvMap;
uniform float backgroundBlurriness;
uniform float backgroundIntensity;
varying vec3 vWorldDirection;
#include <cube_uv_reflection_fragment>
void main() {
	#ifdef ENVMAP_TYPE_CUBE
		vec4 texColor = textureCube( envMap, vec3( flipEnvMap * vWorldDirection.x, vWorldDirection.yz ) );
	#elif defined( ENVMAP_TYPE_CUBE_UV )
		vec4 texColor = textureCubeUV( envMap, vWorldDirection, backgroundBlurriness );
	#else
		vec4 texColor = vec4( 0.0, 0.0, 0.0, 1.0 );
	#endif
	texColor.rgb *= backgroundIntensity;
	gl_FragColor = texColor;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,ng=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
	gl_Position.z = gl_Position.w;
}`,ig=`uniform samplerCube tCube;
uniform float tFlip;
uniform float opacity;
varying vec3 vWorldDirection;
void main() {
	vec4 texColor = textureCube( tCube, vec3( tFlip * vWorldDirection.x, vWorldDirection.yz ) );
	gl_FragColor = texColor;
	gl_FragColor.a *= opacity;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,sg=`#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
varying vec2 vHighPrecisionZW;
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <skinbase_vertex>
	#ifdef USE_DISPLACEMENTMAP
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vHighPrecisionZW = gl_Position.zw;
}`,rg=`#if DEPTH_PACKING == 3200
	uniform float opacity;
#endif
#include <common>
#include <packing>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
varying vec2 vHighPrecisionZW;
void main() {
	#include <clipping_planes_fragment>
	vec4 diffuseColor = vec4( 1.0 );
	#if DEPTH_PACKING == 3200
		diffuseColor.a = opacity;
	#endif
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <logdepthbuf_fragment>
	float fragCoordZ = 0.5 * vHighPrecisionZW[0] / vHighPrecisionZW[1] + 0.5;
	#if DEPTH_PACKING == 3200
		gl_FragColor = vec4( vec3( 1.0 - fragCoordZ ), opacity );
	#elif DEPTH_PACKING == 3201
		gl_FragColor = packDepthToRGBA( fragCoordZ );
	#endif
}`,og=`#define DISTANCE
varying vec3 vWorldPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <skinbase_vertex>
	#ifdef USE_DISPLACEMENTMAP
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <worldpos_vertex>
	#include <clipping_planes_vertex>
	vWorldPosition = worldPosition.xyz;
}`,ag=`#define DISTANCE
uniform vec3 referencePosition;
uniform float nearDistance;
uniform float farDistance;
varying vec3 vWorldPosition;
#include <common>
#include <packing>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <clipping_planes_pars_fragment>
void main () {
	#include <clipping_planes_fragment>
	vec4 diffuseColor = vec4( 1.0 );
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	float dist = length( vWorldPosition - referencePosition );
	dist = ( dist - nearDistance ) / ( farDistance - nearDistance );
	dist = saturate( dist );
	gl_FragColor = packDepthToRGBA( dist );
}`,lg=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
}`,cg=`uniform sampler2D tEquirect;
varying vec3 vWorldDirection;
#include <common>
void main() {
	vec3 direction = normalize( vWorldDirection );
	vec2 sampleUV = equirectUv( direction );
	gl_FragColor = texture2D( tEquirect, sampleUV );
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,hg=`uniform float scale;
attribute float lineDistance;
varying float vLineDistance;
#include <common>
#include <uv_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	vLineDistance = scale * lineDistance;
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphcolor_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
}`,ug=`uniform vec3 diffuse;
uniform float opacity;
uniform float dashSize;
uniform float totalSize;
varying float vLineDistance;
#include <common>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	#include <clipping_planes_fragment>
	if ( mod( vLineDistance, totalSize ) > dashSize ) {
		discard;
	}
	vec3 outgoingLight = vec3( 0.0 );
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
}`,fg=`#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#if defined ( USE_ENVMAP ) || defined ( USE_SKINNING )
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinbase_vertex>
		#include <skinnormal_vertex>
		#include <defaultnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <fog_vertex>
}`,dg=`uniform vec3 diffuse;
uniform float opacity;
#ifndef FLAT_SHADED
	varying vec3 vNormal;
#endif
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <fog_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	#include <clipping_planes_fragment>
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	#ifdef USE_LIGHTMAP
		vec4 lightMapTexel = texture2D( lightMap, vLightMapUv );
		reflectedLight.indirectDiffuse += lightMapTexel.rgb * lightMapIntensity * RECIPROCAL_PI;
	#else
		reflectedLight.indirectDiffuse += vec3( 1.0 );
	#endif
	#include <aomap_fragment>
	reflectedLight.indirectDiffuse *= diffuseColor.rgb;
	vec3 outgoingLight = reflectedLight.indirectDiffuse;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,pg=`#define LAMBERT
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,mg=`#define LAMBERT
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float opacity;
#include <common>
#include <packing>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_lambert_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	#include <clipping_planes_fragment>
	vec4 diffuseColor = vec4( diffuse, opacity );
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_lambert_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + totalEmissiveRadiance;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,gg=`#define MATCAP
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <color_pars_vertex>
#include <displacementmap_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
	vViewPosition = - mvPosition.xyz;
}`,_g=`#define MATCAP
uniform vec3 diffuse;
uniform float opacity;
uniform sampler2D matcap;
varying vec3 vViewPosition;
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <normal_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	#include <clipping_planes_fragment>
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	vec3 viewDir = normalize( vViewPosition );
	vec3 x = normalize( vec3( viewDir.z, 0.0, - viewDir.x ) );
	vec3 y = cross( viewDir, x );
	vec2 uv = vec2( dot( x, normal ), dot( y, normal ) ) * 0.495 + 0.5;
	#ifdef USE_MATCAP
		vec4 matcapColor = texture2D( matcap, uv );
	#else
		vec4 matcapColor = vec4( vec3( mix( 0.2, 0.8, uv.y ) ), 1.0 );
	#endif
	vec3 outgoingLight = diffuseColor.rgb * matcapColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,xg=`#define NORMAL
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	varying vec3 vViewPosition;
#endif
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	vViewPosition = - mvPosition.xyz;
#endif
}`,vg=`#define NORMAL
uniform float opacity;
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	varying vec3 vViewPosition;
#endif
#include <packing>
#include <uv_pars_fragment>
#include <normal_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	#include <clipping_planes_fragment>
	#include <logdepthbuf_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	gl_FragColor = vec4( packNormalToRGB( normal ), opacity );
	#ifdef OPAQUE
		gl_FragColor.a = 1.0;
	#endif
}`,yg=`#define PHONG
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,Mg=`#define PHONG
uniform vec3 diffuse;
uniform vec3 emissive;
uniform vec3 specular;
uniform float shininess;
uniform float opacity;
#include <common>
#include <packing>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_phong_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	#include <clipping_planes_fragment>
	vec4 diffuseColor = vec4( diffuse, opacity );
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_phong_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + reflectedLight.directSpecular + reflectedLight.indirectSpecular + totalEmissiveRadiance;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,Sg=`#define STANDARD
varying vec3 vViewPosition;
#ifdef USE_TRANSMISSION
	varying vec3 vWorldPosition;
#endif
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
#ifdef USE_TRANSMISSION
	vWorldPosition = worldPosition.xyz;
#endif
}`,bg=`#define STANDARD
#ifdef PHYSICAL
	#define IOR
	#define USE_SPECULAR
#endif
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float roughness;
uniform float metalness;
uniform float opacity;
#ifdef IOR
	uniform float ior;
#endif
#ifdef USE_SPECULAR
	uniform float specularIntensity;
	uniform vec3 specularColor;
	#ifdef USE_SPECULAR_COLORMAP
		uniform sampler2D specularColorMap;
	#endif
	#ifdef USE_SPECULAR_INTENSITYMAP
		uniform sampler2D specularIntensityMap;
	#endif
#endif
#ifdef USE_CLEARCOAT
	uniform float clearcoat;
	uniform float clearcoatRoughness;
#endif
#ifdef USE_IRIDESCENCE
	uniform float iridescence;
	uniform float iridescenceIOR;
	uniform float iridescenceThicknessMinimum;
	uniform float iridescenceThicknessMaximum;
#endif
#ifdef USE_SHEEN
	uniform vec3 sheenColor;
	uniform float sheenRoughness;
	#ifdef USE_SHEEN_COLORMAP
		uniform sampler2D sheenColorMap;
	#endif
	#ifdef USE_SHEEN_ROUGHNESSMAP
		uniform sampler2D sheenRoughnessMap;
	#endif
#endif
#ifdef USE_ANISOTROPY
	uniform vec2 anisotropyVector;
	#ifdef USE_ANISOTROPYMAP
		uniform sampler2D anisotropyMap;
	#endif
#endif
varying vec3 vViewPosition;
#include <common>
#include <packing>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <iridescence_fragment>
#include <cube_uv_reflection_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_physical_pars_fragment>
#include <fog_pars_fragment>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_physical_pars_fragment>
#include <transmission_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <clearcoat_pars_fragment>
#include <iridescence_pars_fragment>
#include <roughnessmap_pars_fragment>
#include <metalnessmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	#include <clipping_planes_fragment>
	vec4 diffuseColor = vec4( diffuse, opacity );
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <roughnessmap_fragment>
	#include <metalnessmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <clearcoat_normal_fragment_begin>
	#include <clearcoat_normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_physical_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 totalDiffuse = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse;
	vec3 totalSpecular = reflectedLight.directSpecular + reflectedLight.indirectSpecular;
	#include <transmission_fragment>
	vec3 outgoingLight = totalDiffuse + totalSpecular + totalEmissiveRadiance;
	#ifdef USE_SHEEN
		float sheenEnergyComp = 1.0 - 0.157 * max3( material.sheenColor );
		outgoingLight = outgoingLight * sheenEnergyComp + sheenSpecularDirect + sheenSpecularIndirect;
	#endif
	#ifdef USE_CLEARCOAT
		float dotNVcc = saturate( dot( geometryClearcoatNormal, geometryViewDir ) );
		vec3 Fcc = F_Schlick( material.clearcoatF0, material.clearcoatF90, dotNVcc );
		outgoingLight = outgoingLight * ( 1.0 - material.clearcoat * Fcc ) + ( clearcoatSpecularDirect + clearcoatSpecularIndirect ) * material.clearcoat;
	#endif
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,Eg=`#define TOON
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,wg=`#define TOON
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float opacity;
#include <common>
#include <packing>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <gradientmap_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_toon_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	#include <clipping_planes_fragment>
	vec4 diffuseColor = vec4( diffuse, opacity );
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_toon_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + totalEmissiveRadiance;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,Tg=`uniform float size;
uniform float scale;
#include <common>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
#ifdef USE_POINTS_UV
	varying vec2 vUv;
	uniform mat3 uvTransform;
#endif
void main() {
	#ifdef USE_POINTS_UV
		vUv = ( uvTransform * vec3( uv, 1 ) ).xy;
	#endif
	#include <color_vertex>
	#include <morphcolor_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <project_vertex>
	gl_PointSize = size;
	#ifdef USE_SIZEATTENUATION
		bool isPerspective = isPerspectiveMatrix( projectionMatrix );
		if ( isPerspective ) gl_PointSize *= ( scale / - mvPosition.z );
	#endif
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <worldpos_vertex>
	#include <fog_vertex>
}`,Ag=`uniform vec3 diffuse;
uniform float opacity;
#include <common>
#include <color_pars_fragment>
#include <map_particle_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	#include <clipping_planes_fragment>
	vec3 outgoingLight = vec3( 0.0 );
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <logdepthbuf_fragment>
	#include <map_particle_fragment>
	#include <color_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
}`,Rg=`#include <common>
#include <batching_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <shadowmap_pars_vertex>
void main() {
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,Cg=`uniform vec3 color;
uniform float opacity;
#include <common>
#include <packing>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <logdepthbuf_pars_fragment>
#include <shadowmap_pars_fragment>
#include <shadowmask_pars_fragment>
void main() {
	#include <logdepthbuf_fragment>
	gl_FragColor = vec4( color, opacity * ( 1.0 - getShadowMask() ) );
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
}`,Pg=`uniform float rotation;
uniform vec2 center;
#include <common>
#include <uv_pars_vertex>
#include <fog_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	vec4 mvPosition = modelViewMatrix * vec4( 0.0, 0.0, 0.0, 1.0 );
	vec2 scale;
	scale.x = length( vec3( modelMatrix[ 0 ].x, modelMatrix[ 0 ].y, modelMatrix[ 0 ].z ) );
	scale.y = length( vec3( modelMatrix[ 1 ].x, modelMatrix[ 1 ].y, modelMatrix[ 1 ].z ) );
	#ifndef USE_SIZEATTENUATION
		bool isPerspective = isPerspectiveMatrix( projectionMatrix );
		if ( isPerspective ) scale *= - mvPosition.z;
	#endif
	vec2 alignedPosition = ( position.xy - ( center - vec2( 0.5 ) ) ) * scale;
	vec2 rotatedPosition;
	rotatedPosition.x = cos( rotation ) * alignedPosition.x - sin( rotation ) * alignedPosition.y;
	rotatedPosition.y = sin( rotation ) * alignedPosition.x + cos( rotation ) * alignedPosition.y;
	mvPosition.xy += rotatedPosition;
	gl_Position = projectionMatrix * mvPosition;
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
}`,Ig=`uniform vec3 diffuse;
uniform float opacity;
#include <common>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	#include <clipping_planes_fragment>
	vec3 outgoingLight = vec3( 0.0 );
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
}`,de={alphahash_fragment:Qd,alphahash_pars_fragment:tp,alphamap_fragment:ep,alphamap_pars_fragment:np,alphatest_fragment:ip,alphatest_pars_fragment:sp,aomap_fragment:rp,aomap_pars_fragment:op,batching_pars_vertex:ap,batching_vertex:lp,begin_vertex:cp,beginnormal_vertex:hp,bsdfs:up,iridescence_fragment:fp,bumpmap_pars_fragment:dp,clipping_planes_fragment:pp,clipping_planes_pars_fragment:mp,clipping_planes_pars_vertex:gp,clipping_planes_vertex:_p,color_fragment:xp,color_pars_fragment:vp,color_pars_vertex:yp,color_vertex:Mp,common:Sp,cube_uv_reflection_fragment:bp,defaultnormal_vertex:Ep,displacementmap_pars_vertex:wp,displacementmap_vertex:Tp,emissivemap_fragment:Ap,emissivemap_pars_fragment:Rp,colorspace_fragment:Cp,colorspace_pars_fragment:Pp,envmap_fragment:Ip,envmap_common_pars_fragment:Lp,envmap_pars_fragment:Up,envmap_pars_vertex:Dp,envmap_physical_pars_fragment:Yp,envmap_vertex:Np,fog_vertex:Fp,fog_pars_vertex:Op,fog_fragment:Bp,fog_pars_fragment:zp,gradientmap_pars_fragment:Hp,lightmap_fragment:kp,lightmap_pars_fragment:Vp,lights_lambert_fragment:Gp,lights_lambert_pars_fragment:Wp,lights_pars_begin:Xp,lights_toon_fragment:qp,lights_toon_pars_fragment:Zp,lights_phong_fragment:$p,lights_phong_pars_fragment:Jp,lights_physical_fragment:Kp,lights_physical_pars_fragment:jp,lights_fragment_begin:Qp,lights_fragment_maps:tm,lights_fragment_end:em,logdepthbuf_fragment:nm,logdepthbuf_pars_fragment:im,logdepthbuf_pars_vertex:sm,logdepthbuf_vertex:rm,map_fragment:om,map_pars_fragment:am,map_particle_fragment:lm,map_particle_pars_fragment:cm,metalnessmap_fragment:hm,metalnessmap_pars_fragment:um,morphcolor_vertex:fm,morphnormal_vertex:dm,morphtarget_pars_vertex:pm,morphtarget_vertex:mm,normal_fragment_begin:gm,normal_fragment_maps:_m,normal_pars_fragment:xm,normal_pars_vertex:vm,normal_vertex:ym,normalmap_pars_fragment:Mm,clearcoat_normal_fragment_begin:Sm,clearcoat_normal_fragment_maps:bm,clearcoat_pars_fragment:Em,iridescence_pars_fragment:wm,opaque_fragment:Tm,packing:Am,premultiplied_alpha_fragment:Rm,project_vertex:Cm,dithering_fragment:Pm,dithering_pars_fragment:Im,roughnessmap_fragment:Lm,roughnessmap_pars_fragment:Um,shadowmap_pars_fragment:Dm,shadowmap_pars_vertex:Nm,shadowmap_vertex:Fm,shadowmask_pars_fragment:Om,skinbase_vertex:Bm,skinning_pars_vertex:zm,skinning_vertex:Hm,skinnormal_vertex:km,specularmap_fragment:Vm,specularmap_pars_fragment:Gm,tonemapping_fragment:Wm,tonemapping_pars_fragment:Xm,transmission_fragment:Ym,transmission_pars_fragment:qm,uv_pars_fragment:Zm,uv_pars_vertex:$m,uv_vertex:Jm,worldpos_vertex:Km,background_vert:jm,background_frag:Qm,backgroundCube_vert:tg,backgroundCube_frag:eg,cube_vert:ng,cube_frag:ig,depth_vert:sg,depth_frag:rg,distanceRGBA_vert:og,distanceRGBA_frag:ag,equirect_vert:lg,equirect_frag:cg,linedashed_vert:hg,linedashed_frag:ug,meshbasic_vert:fg,meshbasic_frag:dg,meshlambert_vert:pg,meshlambert_frag:mg,meshmatcap_vert:gg,meshmatcap_frag:_g,meshnormal_vert:xg,meshnormal_frag:vg,meshphong_vert:yg,meshphong_frag:Mg,meshphysical_vert:Sg,meshphysical_frag:bg,meshtoon_vert:Eg,meshtoon_frag:wg,points_vert:Tg,points_frag:Ag,shadow_vert:Rg,shadow_frag:Cg,sprite_vert:Pg,sprite_frag:Ig},Ct={common:{diffuse:{value:new ge(16777215)},opacity:{value:1},map:{value:null},mapTransform:{value:new ve},alphaMap:{value:null},alphaMapTransform:{value:new ve},alphaTest:{value:0}},specularmap:{specularMap:{value:null},specularMapTransform:{value:new ve}},envmap:{envMap:{value:null},flipEnvMap:{value:-1},reflectivity:{value:1},ior:{value:1.5},refractionRatio:{value:.98}},aomap:{aoMap:{value:null},aoMapIntensity:{value:1},aoMapTransform:{value:new ve}},lightmap:{lightMap:{value:null},lightMapIntensity:{value:1},lightMapTransform:{value:new ve}},bumpmap:{bumpMap:{value:null},bumpMapTransform:{value:new ve},bumpScale:{value:1}},normalmap:{normalMap:{value:null},normalMapTransform:{value:new ve},normalScale:{value:new xt(1,1)}},displacementmap:{displacementMap:{value:null},displacementMapTransform:{value:new ve},displacementScale:{value:1},displacementBias:{value:0}},emissivemap:{emissiveMap:{value:null},emissiveMapTransform:{value:new ve}},metalnessmap:{metalnessMap:{value:null},metalnessMapTransform:{value:new ve}},roughnessmap:{roughnessMap:{value:null},roughnessMapTransform:{value:new ve}},gradientmap:{gradientMap:{value:null}},fog:{fogDensity:{value:25e-5},fogNear:{value:1},fogFar:{value:2e3},fogColor:{value:new ge(16777215)}},lights:{ambientLightColor:{value:[]},lightProbe:{value:[]},directionalLights:{value:[],properties:{direction:{},color:{}}},directionalLightShadows:{value:[],properties:{shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{}}},directionalShadowMap:{value:[]},directionalShadowMatrix:{value:[]},spotLights:{value:[],properties:{color:{},position:{},direction:{},distance:{},coneCos:{},penumbraCos:{},decay:{}}},spotLightShadows:{value:[],properties:{shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{}}},spotLightMap:{value:[]},spotShadowMap:{value:[]},spotLightMatrix:{value:[]},pointLights:{value:[],properties:{color:{},position:{},decay:{},distance:{}}},pointLightShadows:{value:[],properties:{shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{},shadowCameraNear:{},shadowCameraFar:{}}},pointShadowMap:{value:[]},pointShadowMatrix:{value:[]},hemisphereLights:{value:[],properties:{direction:{},skyColor:{},groundColor:{}}},rectAreaLights:{value:[],properties:{color:{},position:{},width:{},height:{}}},ltc_1:{value:null},ltc_2:{value:null}},points:{diffuse:{value:new ge(16777215)},opacity:{value:1},size:{value:1},scale:{value:1},map:{value:null},alphaMap:{value:null},alphaMapTransform:{value:new ve},alphaTest:{value:0},uvTransform:{value:new ve}},sprite:{diffuse:{value:new ge(16777215)},opacity:{value:1},center:{value:new xt(.5,.5)},rotation:{value:0},map:{value:null},mapTransform:{value:new ve},alphaMap:{value:null},alphaMapTransform:{value:new ve},alphaTest:{value:0}}},ui={basic:{uniforms:Tn([Ct.common,Ct.specularmap,Ct.envmap,Ct.aomap,Ct.lightmap,Ct.fog]),vertexShader:de.meshbasic_vert,fragmentShader:de.meshbasic_frag},lambert:{uniforms:Tn([Ct.common,Ct.specularmap,Ct.envmap,Ct.aomap,Ct.lightmap,Ct.emissivemap,Ct.bumpmap,Ct.normalmap,Ct.displacementmap,Ct.fog,Ct.lights,{emissive:{value:new ge(0)}}]),vertexShader:de.meshlambert_vert,fragmentShader:de.meshlambert_frag},phong:{uniforms:Tn([Ct.common,Ct.specularmap,Ct.envmap,Ct.aomap,Ct.lightmap,Ct.emissivemap,Ct.bumpmap,Ct.normalmap,Ct.displacementmap,Ct.fog,Ct.lights,{emissive:{value:new ge(0)},specular:{value:new ge(1118481)},shininess:{value:30}}]),vertexShader:de.meshphong_vert,fragmentShader:de.meshphong_frag},standard:{uniforms:Tn([Ct.common,Ct.envmap,Ct.aomap,Ct.lightmap,Ct.emissivemap,Ct.bumpmap,Ct.normalmap,Ct.displacementmap,Ct.roughnessmap,Ct.metalnessmap,Ct.fog,Ct.lights,{emissive:{value:new ge(0)},roughness:{value:1},metalness:{value:0},envMapIntensity:{value:1}}]),vertexShader:de.meshphysical_vert,fragmentShader:de.meshphysical_frag},toon:{uniforms:Tn([Ct.common,Ct.aomap,Ct.lightmap,Ct.emissivemap,Ct.bumpmap,Ct.normalmap,Ct.displacementmap,Ct.gradientmap,Ct.fog,Ct.lights,{emissive:{value:new ge(0)}}]),vertexShader:de.meshtoon_vert,fragmentShader:de.meshtoon_frag},matcap:{uniforms:Tn([Ct.common,Ct.bumpmap,Ct.normalmap,Ct.displacementmap,Ct.fog,{matcap:{value:null}}]),vertexShader:de.meshmatcap_vert,fragmentShader:de.meshmatcap_frag},points:{uniforms:Tn([Ct.points,Ct.fog]),vertexShader:de.points_vert,fragmentShader:de.points_frag},dashed:{uniforms:Tn([Ct.common,Ct.fog,{scale:{value:1},dashSize:{value:1},totalSize:{value:2}}]),vertexShader:de.linedashed_vert,fragmentShader:de.linedashed_frag},depth:{uniforms:Tn([Ct.common,Ct.displacementmap]),vertexShader:de.depth_vert,fragmentShader:de.depth_frag},normal:{uniforms:Tn([Ct.common,Ct.bumpmap,Ct.normalmap,Ct.displacementmap,{opacity:{value:1}}]),vertexShader:de.meshnormal_vert,fragmentShader:de.meshnormal_frag},sprite:{uniforms:Tn([Ct.sprite,Ct.fog]),vertexShader:de.sprite_vert,fragmentShader:de.sprite_frag},background:{uniforms:{uvTransform:{value:new ve},t2D:{value:null},backgroundIntensity:{value:1}},vertexShader:de.background_vert,fragmentShader:de.background_frag},backgroundCube:{uniforms:{envMap:{value:null},flipEnvMap:{value:-1},backgroundBlurriness:{value:0},backgroundIntensity:{value:1}},vertexShader:de.backgroundCube_vert,fragmentShader:de.backgroundCube_frag},cube:{uniforms:{tCube:{value:null},tFlip:{value:-1},opacity:{value:1}},vertexShader:de.cube_vert,fragmentShader:de.cube_frag},equirect:{uniforms:{tEquirect:{value:null}},vertexShader:de.equirect_vert,fragmentShader:de.equirect_frag},distanceRGBA:{uniforms:Tn([Ct.common,Ct.displacementmap,{referencePosition:{value:new O},nearDistance:{value:1},farDistance:{value:1e3}}]),vertexShader:de.distanceRGBA_vert,fragmentShader:de.distanceRGBA_frag},shadow:{uniforms:Tn([Ct.lights,Ct.fog,{color:{value:new ge(0)},opacity:{value:1}}]),vertexShader:de.shadow_vert,fragmentShader:de.shadow_frag}};ui.physical={uniforms:Tn([ui.standard.uniforms,{clearcoat:{value:0},clearcoatMap:{value:null},clearcoatMapTransform:{value:new ve},clearcoatNormalMap:{value:null},clearcoatNormalMapTransform:{value:new ve},clearcoatNormalScale:{value:new xt(1,1)},clearcoatRoughness:{value:0},clearcoatRoughnessMap:{value:null},clearcoatRoughnessMapTransform:{value:new ve},iridescence:{value:0},iridescenceMap:{value:null},iridescenceMapTransform:{value:new ve},iridescenceIOR:{value:1.3},iridescenceThicknessMinimum:{value:100},iridescenceThicknessMaximum:{value:400},iridescenceThicknessMap:{value:null},iridescenceThicknessMapTransform:{value:new ve},sheen:{value:0},sheenColor:{value:new ge(0)},sheenColorMap:{value:null},sheenColorMapTransform:{value:new ve},sheenRoughness:{value:1},sheenRoughnessMap:{value:null},sheenRoughnessMapTransform:{value:new ve},transmission:{value:0},transmissionMap:{value:null},transmissionMapTransform:{value:new ve},transmissionSamplerSize:{value:new xt},transmissionSamplerMap:{value:null},thickness:{value:0},thicknessMap:{value:null},thicknessMapTransform:{value:new ve},attenuationDistance:{value:0},attenuationColor:{value:new ge(0)},specularColor:{value:new ge(1,1,1)},specularColorMap:{value:null},specularColorMapTransform:{value:new ve},specularIntensity:{value:1},specularIntensityMap:{value:null},specularIntensityMapTransform:{value:new ve},anisotropyVector:{value:new xt},anisotropyMap:{value:null},anisotropyMapTransform:{value:new ve}}]),vertexShader:de.meshphysical_vert,fragmentShader:de.meshphysical_frag};var Ro={r:0,b:0,g:0};function Lg(i,t,e,n,s,r,a){let o=new ge(0),l=r===!0?0:1,c,h,u=null,d=0,p=null;function x(g,m){let w=!1,v=m.isScene===!0?m.background:null;v&&v.isTexture&&(v=(m.backgroundBlurriness>0?e:t).get(v)),v===null?y(o,l):v&&v.isColor&&(y(v,1),w=!0);let I=i.xr.getEnvironmentBlendMode();I==="additive"?n.buffers.color.setClear(0,0,0,1,a):I==="alpha-blend"&&n.buffers.color.setClear(0,0,0,0,a),(i.autoClear||w)&&i.clear(i.autoClearColor,i.autoClearDepth,i.autoClearStencil),v&&(v.isCubeTexture||v.mapping===ga)?(h===void 0&&(h=new Ce(new Ae(1,1,1),new _n({name:"BackgroundCubeMaterial",uniforms:nr(ui.backgroundCube.uniforms),vertexShader:ui.backgroundCube.vertexShader,fragmentShader:ui.backgroundCube.fragmentShader,side:Sn,depthTest:!1,depthWrite:!1,fog:!1})),h.geometry.deleteAttribute("normal"),h.geometry.deleteAttribute("uv"),h.onBeforeRender=function(H,U,N){this.matrixWorld.copyPosition(N.matrixWorld)},Object.defineProperty(h.material,"envMap",{get:function(){return this.uniforms.envMap.value}}),s.update(h)),h.material.uniforms.envMap.value=v,h.material.uniforms.flipEnvMap.value=v.isCubeTexture&&v.isRenderTargetTexture===!1?-1:1,h.material.uniforms.backgroundBlurriness.value=m.backgroundBlurriness,h.material.uniforms.backgroundIntensity.value=m.backgroundIntensity,h.material.toneMapped=Ue.getTransfer(v.colorSpace)!==ke,(u!==v||d!==v.version||p!==i.toneMapping)&&(h.material.needsUpdate=!0,u=v,d=v.version,p=i.toneMapping),h.layers.enableAll(),g.unshift(h,h.geometry,h.material,0,0,null)):v&&v.isTexture&&(c===void 0&&(c=new Ce(new hn(2,2),new _n({name:"BackgroundMaterial",uniforms:nr(ui.background.uniforms),vertexShader:ui.background.vertexShader,fragmentShader:ui.background.fragmentShader,side:Yi,depthTest:!1,depthWrite:!1,fog:!1})),c.geometry.deleteAttribute("normal"),Object.defineProperty(c.material,"map",{get:function(){return this.uniforms.t2D.value}}),s.update(c)),c.material.uniforms.t2D.value=v,c.material.uniforms.backgroundIntensity.value=m.backgroundIntensity,c.material.toneMapped=Ue.getTransfer(v.colorSpace)!==ke,v.matrixAutoUpdate===!0&&v.updateMatrix(),c.material.uniforms.uvTransform.value.copy(v.matrix),(u!==v||d!==v.version||p!==i.toneMapping)&&(c.material.needsUpdate=!0,u=v,d=v.version,p=i.toneMapping),c.layers.enableAll(),g.unshift(c,c.geometry,c.material,0,0,null))}function y(g,m){g.getRGB(Ro,$u(i)),n.buffers.color.setClear(Ro.r,Ro.g,Ro.b,m,a)}return{getClearColor:function(){return o},setClearColor:function(g,m=1){o.set(g),l=m,y(o,l)},getClearAlpha:function(){return l},setClearAlpha:function(g){l=g,y(o,l)},render:x}}function Ug(i,t,e,n){let s=i.getParameter(i.MAX_VERTEX_ATTRIBS),r=n.isWebGL2?null:t.get("OES_vertex_array_object"),a=n.isWebGL2||r!==null,o={},l=g(null),c=l,h=!1;function u(k,q,j,et,ut){let tt=!1;if(a){let at=y(et,j,q);c!==at&&(c=at,p(c.object)),tt=m(k,et,j,ut),tt&&w(k,et,j,ut)}else{let at=q.wireframe===!0;(c.geometry!==et.id||c.program!==j.id||c.wireframe!==at)&&(c.geometry=et.id,c.program=j.id,c.wireframe=at,tt=!0)}ut!==null&&e.update(ut,i.ELEMENT_ARRAY_BUFFER),(tt||h)&&(h=!1,Y(k,q,j,et),ut!==null&&i.bindBuffer(i.ELEMENT_ARRAY_BUFFER,e.get(ut).buffer))}function d(){return n.isWebGL2?i.createVertexArray():r.createVertexArrayOES()}function p(k){return n.isWebGL2?i.bindVertexArray(k):r.bindVertexArrayOES(k)}function x(k){return n.isWebGL2?i.deleteVertexArray(k):r.deleteVertexArrayOES(k)}function y(k,q,j){let et=j.wireframe===!0,ut=o[k.id];ut===void 0&&(ut={},o[k.id]=ut);let tt=ut[q.id];tt===void 0&&(tt={},ut[q.id]=tt);let at=tt[et];return at===void 0&&(at=g(d()),tt[et]=at),at}function g(k){let q=[],j=[],et=[];for(let ut=0;ut<s;ut++)q[ut]=0,j[ut]=0,et[ut]=0;return{geometry:null,program:null,wireframe:!1,newAttributes:q,enabledAttributes:j,attributeDivisors:et,object:k,attributes:{},index:null}}function m(k,q,j,et){let ut=c.attributes,tt=q.attributes,at=0,lt=j.getAttributes();for(let Ut in lt)if(lt[Ut].location>=0){let ht=ut[Ut],Dt=tt[Ut];if(Dt===void 0&&(Ut==="instanceMatrix"&&k.instanceMatrix&&(Dt=k.instanceMatrix),Ut==="instanceColor"&&k.instanceColor&&(Dt=k.instanceColor)),ht===void 0||ht.attribute!==Dt||Dt&&ht.data!==Dt.data)return!0;at++}return c.attributesNum!==at||c.index!==et}function w(k,q,j,et){let ut={},tt=q.attributes,at=0,lt=j.getAttributes();for(let Ut in lt)if(lt[Ut].location>=0){let ht=tt[Ut];ht===void 0&&(Ut==="instanceMatrix"&&k.instanceMatrix&&(ht=k.instanceMatrix),Ut==="instanceColor"&&k.instanceColor&&(ht=k.instanceColor));let Dt={};Dt.attribute=ht,ht&&ht.data&&(Dt.data=ht.data),ut[Ut]=Dt,at++}c.attributes=ut,c.attributesNum=at,c.index=et}function v(){let k=c.newAttributes;for(let q=0,j=k.length;q<j;q++)k[q]=0}function I(k){H(k,0)}function H(k,q){let j=c.newAttributes,et=c.enabledAttributes,ut=c.attributeDivisors;j[k]=1,et[k]===0&&(i.enableVertexAttribArray(k),et[k]=1),ut[k]!==q&&((n.isWebGL2?i:t.get("ANGLE_instanced_arrays"))[n.isWebGL2?"vertexAttribDivisor":"vertexAttribDivisorANGLE"](k,q),ut[k]=q)}function U(){let k=c.newAttributes,q=c.enabledAttributes;for(let j=0,et=q.length;j<et;j++)q[j]!==k[j]&&(i.disableVertexAttribArray(j),q[j]=0)}function N(k,q,j,et,ut,tt,at){at===!0?i.vertexAttribIPointer(k,q,j,ut,tt):i.vertexAttribPointer(k,q,j,et,ut,tt)}function Y(k,q,j,et){if(n.isWebGL2===!1&&(k.isInstancedMesh||et.isInstancedBufferGeometry)&&t.get("ANGLE_instanced_arrays")===null)return;v();let ut=et.attributes,tt=j.getAttributes(),at=q.defaultAttributeValues;for(let lt in tt){let Ut=tt[lt];if(Ut.location>=0){let nt=ut[lt];if(nt===void 0&&(lt==="instanceMatrix"&&k.instanceMatrix&&(nt=k.instanceMatrix),lt==="instanceColor"&&k.instanceColor&&(nt=k.instanceColor)),nt!==void 0){let ht=nt.normalized,Dt=nt.itemSize,Bt=e.get(nt);if(Bt===void 0)continue;let zt=Bt.buffer,ne=Bt.type,Zt=Bt.bytesPerElement,Wt=n.isWebGL2===!0&&(ne===i.INT||ne===i.UNSIGNED_INT||nt.gpuType===Ou);if(nt.isInterleavedBufferAttribute){let ae=nt.data,F=ae.stride,Et=nt.offset;if(ae.isInstancedInterleavedBuffer){for(let st=0;st<Ut.locationSize;st++)H(Ut.location+st,ae.meshPerAttribute);k.isInstancedMesh!==!0&&et._maxInstanceCount===void 0&&(et._maxInstanceCount=ae.meshPerAttribute*ae.count)}else for(let st=0;st<Ut.locationSize;st++)I(Ut.location+st);i.bindBuffer(i.ARRAY_BUFFER,zt);for(let st=0;st<Ut.locationSize;st++)N(Ut.location+st,Dt/Ut.locationSize,ne,ht,F*Zt,(Et+Dt/Ut.locationSize*st)*Zt,Wt)}else{if(nt.isInstancedBufferAttribute){for(let ae=0;ae<Ut.locationSize;ae++)H(Ut.location+ae,nt.meshPerAttribute);k.isInstancedMesh!==!0&&et._maxInstanceCount===void 0&&(et._maxInstanceCount=nt.meshPerAttribute*nt.count)}else for(let ae=0;ae<Ut.locationSize;ae++)I(Ut.location+ae);i.bindBuffer(i.ARRAY_BUFFER,zt);for(let ae=0;ae<Ut.locationSize;ae++)N(Ut.location+ae,Dt/Ut.locationSize,ne,ht,Dt*Zt,Dt/Ut.locationSize*ae*Zt,Wt)}}else if(at!==void 0){let ht=at[lt];if(ht!==void 0)switch(ht.length){case 2:i.vertexAttrib2fv(Ut.location,ht);break;case 3:i.vertexAttrib3fv(Ut.location,ht);break;case 4:i.vertexAttrib4fv(Ut.location,ht);break;default:i.vertexAttrib1fv(Ut.location,ht)}}}}U()}function b(){rt();for(let k in o){let q=o[k];for(let j in q){let et=q[j];for(let ut in et)x(et[ut].object),delete et[ut];delete q[j]}delete o[k]}}function P(k){if(o[k.id]===void 0)return;let q=o[k.id];for(let j in q){let et=q[j];for(let ut in et)x(et[ut].object),delete et[ut];delete q[j]}delete o[k.id]}function X(k){for(let q in o){let j=o[q];if(j[k.id]===void 0)continue;let et=j[k.id];for(let ut in et)x(et[ut].object),delete et[ut];delete j[k.id]}}function rt(){_t(),h=!0,c!==l&&(c=l,p(c.object))}function _t(){l.geometry=null,l.program=null,l.wireframe=!1}return{setup:u,reset:rt,resetDefaultState:_t,dispose:b,releaseStatesOfGeometry:P,releaseStatesOfProgram:X,initAttributes:v,enableAttribute:I,disableUnusedAttributes:U}}function Dg(i,t,e,n){let s=n.isWebGL2,r;function a(h){r=h}function o(h,u){i.drawArrays(r,h,u),e.update(u,r,1)}function l(h,u,d){if(d===0)return;let p,x;if(s)p=i,x="drawArraysInstanced";else if(p=t.get("ANGLE_instanced_arrays"),x="drawArraysInstancedANGLE",p===null){console.error("THREE.WebGLBufferRenderer: using THREE.InstancedBufferGeometry but hardware does not support extension ANGLE_instanced_arrays.");return}p[x](r,h,u,d),e.update(u,r,d)}function c(h,u,d){if(d===0)return;let p=t.get("WEBGL_multi_draw");if(p===null)for(let x=0;x<d;x++)this.render(h[x],u[x]);else{p.multiDrawArraysWEBGL(r,h,0,u,0,d);let x=0;for(let y=0;y<d;y++)x+=u[y];e.update(x,r,1)}}this.setMode=a,this.render=o,this.renderInstances=l,this.renderMultiDraw=c}function Ng(i,t,e){let n;function s(){if(n!==void 0)return n;if(t.has("EXT_texture_filter_anisotropic")===!0){let N=t.get("EXT_texture_filter_anisotropic");n=i.getParameter(N.MAX_TEXTURE_MAX_ANISOTROPY_EXT)}else n=0;return n}function r(N){if(N==="highp"){if(i.getShaderPrecisionFormat(i.VERTEX_SHADER,i.HIGH_FLOAT).precision>0&&i.getShaderPrecisionFormat(i.FRAGMENT_SHADER,i.HIGH_FLOAT).precision>0)return"highp";N="mediump"}return N==="mediump"&&i.getShaderPrecisionFormat(i.VERTEX_SHADER,i.MEDIUM_FLOAT).precision>0&&i.getShaderPrecisionFormat(i.FRAGMENT_SHADER,i.MEDIUM_FLOAT).precision>0?"mediump":"lowp"}let a=typeof WebGL2RenderingContext!="undefined"&&i.constructor.name==="WebGL2RenderingContext",o=e.precision!==void 0?e.precision:"highp",l=r(o);l!==o&&(console.warn("THREE.WebGLRenderer:",o,"not supported, using",l,"instead."),o=l);let c=a||t.has("WEBGL_draw_buffers"),h=e.logarithmicDepthBuffer===!0,u=i.getParameter(i.MAX_TEXTURE_IMAGE_UNITS),d=i.getParameter(i.MAX_VERTEX_TEXTURE_IMAGE_UNITS),p=i.getParameter(i.MAX_TEXTURE_SIZE),x=i.getParameter(i.MAX_CUBE_MAP_TEXTURE_SIZE),y=i.getParameter(i.MAX_VERTEX_ATTRIBS),g=i.getParameter(i.MAX_VERTEX_UNIFORM_VECTORS),m=i.getParameter(i.MAX_VARYING_VECTORS),w=i.getParameter(i.MAX_FRAGMENT_UNIFORM_VECTORS),v=d>0,I=a||t.has("OES_texture_float"),H=v&&I,U=a?i.getParameter(i.MAX_SAMPLES):0;return{isWebGL2:a,drawBuffers:c,getMaxAnisotropy:s,getMaxPrecision:r,precision:o,logarithmicDepthBuffer:h,maxTextures:u,maxVertexTextures:d,maxTextureSize:p,maxCubemapSize:x,maxAttributes:y,maxVertexUniforms:g,maxVaryings:m,maxFragmentUniforms:w,vertexTextures:v,floatFragmentTextures:I,floatVertexTextures:H,maxSamples:U}}function Fg(i){let t=this,e=null,n=0,s=!1,r=!1,a=new wi,o=new ve,l={value:null,needsUpdate:!1};this.uniform=l,this.numPlanes=0,this.numIntersection=0,this.init=function(u,d){let p=u.length!==0||d||n!==0||s;return s=d,n=u.length,p},this.beginShadows=function(){r=!0,h(null)},this.endShadows=function(){r=!1},this.setGlobalState=function(u,d){e=h(u,d,0)},this.setState=function(u,d,p){let x=u.clippingPlanes,y=u.clipIntersection,g=u.clipShadows,m=i.get(u);if(!s||x===null||x.length===0||r&&!g)r?h(null):c();else{let w=r?0:n,v=w*4,I=m.clippingState||null;l.value=I,I=h(x,d,v,p);for(let H=0;H!==v;++H)I[H]=e[H];m.clippingState=I,this.numIntersection=y?this.numPlanes:0,this.numPlanes+=w}};function c(){l.value!==e&&(l.value=e,l.needsUpdate=n>0),t.numPlanes=n,t.numIntersection=0}function h(u,d,p,x){let y=u!==null?u.length:0,g=null;if(y!==0){if(g=l.value,x!==!0||g===null){let m=p+y*4,w=d.matrixWorldInverse;o.getNormalMatrix(w),(g===null||g.length<m)&&(g=new Float32Array(m));for(let v=0,I=p;v!==y;++v,I+=4)a.copy(u[v]).applyMatrix4(w,o),a.normal.toArray(g,I),g[I+3]=a.constant}l.value=g,l.needsUpdate=!0}return t.numPlanes=y,t.numIntersection=0,g}}function Og(i){let t=new WeakMap;function e(a,o){return o===Ml?a.mapping=Qs:o===Sl&&(a.mapping=tr),a}function n(a){if(a&&a.isTexture){let o=a.mapping;if(o===Ml||o===Sl)if(t.has(a)){let l=t.get(a).texture;return e(l,a.mapping)}else{let l=a.image;if(l&&l.height>0){let c=new Cl(l.height/2);return c.fromEquirectangularTexture(i,a),t.set(a,c),a.addEventListener("dispose",s),e(c.texture,a.mapping)}else return null}}return a}function s(a){let o=a.target;o.removeEventListener("dispose",s);let l=t.get(o);l!==void 0&&(t.delete(o),l.dispose())}function r(){t=new WeakMap}return{get:n,dispose:r}}var jo=class extends Jo{constructor(t=-1,e=1,n=1,s=-1,r=.1,a=2e3){super(),this.isOrthographicCamera=!0,this.type="OrthographicCamera",this.zoom=1,this.view=null,this.left=t,this.right=e,this.top=n,this.bottom=s,this.near=r,this.far=a,this.updateProjectionMatrix()}copy(t,e){return super.copy(t,e),this.left=t.left,this.right=t.right,this.top=t.top,this.bottom=t.bottom,this.near=t.near,this.far=t.far,this.zoom=t.zoom,this.view=t.view===null?null:Object.assign({},t.view),this}setViewOffset(t,e,n,s,r,a){this.view===null&&(this.view={enabled:!0,fullWidth:1,fullHeight:1,offsetX:0,offsetY:0,width:1,height:1}),this.view.enabled=!0,this.view.fullWidth=t,this.view.fullHeight=e,this.view.offsetX=n,this.view.offsetY=s,this.view.width=r,this.view.height=a,this.updateProjectionMatrix()}clearViewOffset(){this.view!==null&&(this.view.enabled=!1),this.updateProjectionMatrix()}updateProjectionMatrix(){let t=(this.right-this.left)/(2*this.zoom),e=(this.top-this.bottom)/(2*this.zoom),n=(this.right+this.left)/2,s=(this.top+this.bottom)/2,r=n-t,a=n+t,o=s+e,l=s-e;if(this.view!==null&&this.view.enabled){let c=(this.right-this.left)/this.view.fullWidth/this.zoom,h=(this.top-this.bottom)/this.view.fullHeight/this.zoom;r+=c*this.view.offsetX,a=r+c*this.view.width,o-=h*this.view.offsetY,l=o-h*this.view.height}this.projectionMatrix.makeOrthographic(r,a,o,l,this.near,this.far,this.coordinateSystem),this.projectionMatrixInverse.copy(this.projectionMatrix).invert()}toJSON(t){let e=super.toJSON(t);return e.object.zoom=this.zoom,e.object.left=this.left,e.object.right=this.right,e.object.top=this.top,e.object.bottom=this.bottom,e.object.near=this.near,e.object.far=this.far,this.view!==null&&(e.object.view=Object.assign({},this.view)),e}},Xs=4,tu=[.125,.215,.35,.446,.526,.582],hs=20,cl=new jo,eu=new ge,hl=null,ul=0,fl=0,ls=(1+Math.sqrt(5))/2,ks=1/ls,nu=[new O(1,1,1),new O(-1,1,1),new O(1,1,-1),new O(-1,1,-1),new O(0,ls,ks),new O(0,ls,-ks),new O(ks,0,ls),new O(-ks,0,ls),new O(ls,ks,0),new O(-ls,ks,0)],ir=class{constructor(t){this._renderer=t,this._pingPongRenderTarget=null,this._lodMax=0,this._cubeSize=0,this._lodPlanes=[],this._sizeLods=[],this._sigmas=[],this._blurMaterial=null,this._cubemapMaterial=null,this._equirectMaterial=null,this._compileMaterial(this._blurMaterial)}fromScene(t,e=0,n=.1,s=100){hl=this._renderer.getRenderTarget(),ul=this._renderer.getActiveCubeFace(),fl=this._renderer.getActiveMipmapLevel(),this._setSize(256);let r=this._allocateTargets();return r.depthBuffer=!0,this._sceneToCubeUV(t,n,s,r),e>0&&this._blur(r,0,0,e),this._applyPMREM(r),this._cleanup(r),r}fromEquirectangular(t,e=null){return this._fromTexture(t,e)}fromCubemap(t,e=null){return this._fromTexture(t,e)}compileCubemapShader(){this._cubemapMaterial===null&&(this._cubemapMaterial=ru(),this._compileMaterial(this._cubemapMaterial))}compileEquirectangularShader(){this._equirectMaterial===null&&(this._equirectMaterial=su(),this._compileMaterial(this._equirectMaterial))}dispose(){this._dispose(),this._cubemapMaterial!==null&&this._cubemapMaterial.dispose(),this._equirectMaterial!==null&&this._equirectMaterial.dispose()}_setSize(t){this._lodMax=Math.floor(Math.log2(t)),this._cubeSize=Math.pow(2,this._lodMax)}_dispose(){this._blurMaterial!==null&&this._blurMaterial.dispose(),this._pingPongRenderTarget!==null&&this._pingPongRenderTarget.dispose();for(let t=0;t<this._lodPlanes.length;t++)this._lodPlanes[t].dispose()}_cleanup(t){this._renderer.setRenderTarget(hl,ul,fl),t.scissorTest=!1,Co(t,0,0,t.width,t.height)}_fromTexture(t,e){t.mapping===Qs||t.mapping===tr?this._setSize(t.image.length===0?16:t.image[0].width||t.image[0].image.width):this._setSize(t.image.width/4),hl=this._renderer.getRenderTarget(),ul=this._renderer.getActiveCubeFace(),fl=this._renderer.getActiveMipmapLevel();let n=e||this._allocateTargets();return this._textureToCubeUV(t,n),this._applyPMREM(n),this._cleanup(n),n}_allocateTargets(){let t=3*Math.max(this._cubeSize,112),e=4*this._cubeSize,n={magFilter:kn,minFilter:kn,generateMipmaps:!1,type:Pr,format:Qn,colorSpace:Ai,depthBuffer:!1},s=iu(t,e,n);if(this._pingPongRenderTarget===null||this._pingPongRenderTarget.width!==t||this._pingPongRenderTarget.height!==e){this._pingPongRenderTarget!==null&&this._dispose(),this._pingPongRenderTarget=iu(t,e,n);let{_lodMax:r}=this;({sizeLods:this._sizeLods,lodPlanes:this._lodPlanes,sigmas:this._sigmas}=Bg(r)),this._blurMaterial=zg(r,t,e)}return s}_compileMaterial(t){let e=new Ce(this._lodPlanes[0],t);this._renderer.compile(e,cl)}_sceneToCubeUV(t,e,n,s){let o=new Mn(90,1,e,n),l=[1,-1,1,1,1,1],c=[1,1,1,-1,-1,-1],h=this._renderer,u=h.autoClear,d=h.toneMapping;h.getClearColor(eu),h.toneMapping=Wi,h.autoClear=!1;let p=new gs({name:"PMREM.Background",side:Sn,depthWrite:!1,depthTest:!1}),x=new Ce(new Ae,p),y=!1,g=t.background;g?g.isColor&&(p.color.copy(g),t.background=null,y=!0):(p.color.copy(eu),y=!0);for(let m=0;m<6;m++){let w=m%3;w===0?(o.up.set(0,l[m],0),o.lookAt(c[m],0,0)):w===1?(o.up.set(0,0,l[m]),o.lookAt(0,c[m],0)):(o.up.set(0,l[m],0),o.lookAt(0,0,c[m]));let v=this._cubeSize;Co(s,w*v,m>2?v:0,v,v),h.setRenderTarget(s),y&&h.render(x,o),h.render(t,o)}x.geometry.dispose(),x.material.dispose(),h.toneMapping=d,h.autoClear=u,t.background=g}_textureToCubeUV(t,e){let n=this._renderer,s=t.mapping===Qs||t.mapping===tr;s?(this._cubemapMaterial===null&&(this._cubemapMaterial=ru()),this._cubemapMaterial.uniforms.flipEnvMap.value=t.isRenderTargetTexture===!1?-1:1):this._equirectMaterial===null&&(this._equirectMaterial=su());let r=s?this._cubemapMaterial:this._equirectMaterial,a=new Ce(this._lodPlanes[0],r),o=r.uniforms;o.envMap.value=t;let l=this._cubeSize;Co(e,0,0,3*l,2*l),n.setRenderTarget(e),n.render(a,cl)}_applyPMREM(t){let e=this._renderer,n=e.autoClear;e.autoClear=!1;for(let s=1;s<this._lodPlanes.length;s++){let r=Math.sqrt(this._sigmas[s]*this._sigmas[s]-this._sigmas[s-1]*this._sigmas[s-1]),a=nu[(s-1)%nu.length];this._blur(t,s-1,s,r,a)}e.autoClear=n}_blur(t,e,n,s,r){let a=this._pingPongRenderTarget;this._halfBlur(t,a,e,n,s,"latitudinal",r),this._halfBlur(a,t,n,n,s,"longitudinal",r)}_halfBlur(t,e,n,s,r,a,o){let l=this._renderer,c=this._blurMaterial;a!=="latitudinal"&&a!=="longitudinal"&&console.error("blur direction must be either latitudinal or longitudinal!");let h=3,u=new Ce(this._lodPlanes[s],c),d=c.uniforms,p=this._sizeLods[n]-1,x=isFinite(r)?Math.PI/(2*p):2*Math.PI/(2*hs-1),y=r/x,g=isFinite(r)?1+Math.floor(h*y):hs;g>hs&&console.warn(`sigmaRadians, ${r}, is too large and will clip, as it requested ${g} samples when the maximum is set to ${hs}`);let m=[],w=0;for(let N=0;N<hs;++N){let Y=N/y,b=Math.exp(-Y*Y/2);m.push(b),N===0?w+=b:N<g&&(w+=2*b)}for(let N=0;N<m.length;N++)m[N]=m[N]/w;d.envMap.value=t.texture,d.samples.value=g,d.weights.value=m,d.latitudinal.value=a==="latitudinal",o&&(d.poleAxis.value=o);let{_lodMax:v}=this;d.dTheta.value=x,d.mipInt.value=v-n;let I=this._sizeLods[s],H=3*I*(s>v-Xs?s-v+Xs:0),U=4*(this._cubeSize-I);Co(e,H,U,3*I,2*I),l.setRenderTarget(e),l.render(u,cl)}};function Bg(i){let t=[],e=[],n=[],s=i,r=i-Xs+1+tu.length;for(let a=0;a<r;a++){let o=Math.pow(2,s);e.push(o);let l=1/o;a>i-Xs?l=tu[a-i+Xs-1]:a===0&&(l=0),n.push(l);let c=1/(o-2),h=-c,u=1+c,d=[h,h,u,h,u,u,h,h,u,u,h,u],p=6,x=6,y=3,g=2,m=1,w=new Float32Array(y*x*p),v=new Float32Array(g*x*p),I=new Float32Array(m*x*p);for(let U=0;U<p;U++){let N=U%3*2/3-1,Y=U>2?0:-1,b=[N,Y,0,N+2/3,Y,0,N+2/3,Y+1,0,N,Y,0,N+2/3,Y+1,0,N,Y+1,0];w.set(b,y*x*U),v.set(d,g*x*U);let P=[U,U,U,U,U,U];I.set(P,m*x*U)}let H=new qe;H.setAttribute("position",new gn(w,y)),H.setAttribute("uv",new gn(v,g)),H.setAttribute("faceIndex",new gn(I,m)),t.push(H),s>Xs&&s--}return{lodPlanes:t,sizeLods:e,sigmas:n}}function iu(i,t,e){let n=new Ri(i,t,e);return n.texture.mapping=ga,n.texture.name="PMREM.cubeUv",n.scissorTest=!0,n}function Co(i,t,e,n,s){i.viewport.set(t,e,n,s),i.scissor.set(t,e,n,s)}function zg(i,t,e){let n=new Float32Array(hs),s=new O(0,1,0);return new _n({name:"SphericalGaussianBlur",defines:{n:hs,CUBEUV_TEXEL_WIDTH:1/t,CUBEUV_TEXEL_HEIGHT:1/e,CUBEUV_MAX_MIP:`${i}.0`},uniforms:{envMap:{value:null},samples:{value:1},weights:{value:n},latitudinal:{value:!1},dTheta:{value:0},mipInt:{value:0},poleAxis:{value:s}},vertexShader:_c(),fragmentShader:`

			precision mediump float;
			precision mediump int;

			varying vec3 vOutputDirection;

			uniform sampler2D envMap;
			uniform int samples;
			uniform float weights[ n ];
			uniform bool latitudinal;
			uniform float dTheta;
			uniform float mipInt;
			uniform vec3 poleAxis;

			#define ENVMAP_TYPE_CUBE_UV
			#include <cube_uv_reflection_fragment>

			vec3 getSample( float theta, vec3 axis ) {

				float cosTheta = cos( theta );
				// Rodrigues' axis-angle rotation
				vec3 sampleDirection = vOutputDirection * cosTheta
					+ cross( axis, vOutputDirection ) * sin( theta )
					+ axis * dot( axis, vOutputDirection ) * ( 1.0 - cosTheta );

				return bilinearCubeUV( envMap, sampleDirection, mipInt );

			}

			void main() {

				vec3 axis = latitudinal ? poleAxis : cross( poleAxis, vOutputDirection );

				if ( all( equal( axis, vec3( 0.0 ) ) ) ) {

					axis = vec3( vOutputDirection.z, 0.0, - vOutputDirection.x );

				}

				axis = normalize( axis );

				gl_FragColor = vec4( 0.0, 0.0, 0.0, 1.0 );
				gl_FragColor.rgb += weights[ 0 ] * getSample( 0.0, axis );

				for ( int i = 1; i < n; i++ ) {

					if ( i >= samples ) {

						break;

					}

					float theta = dTheta * float( i );
					gl_FragColor.rgb += weights[ i ] * getSample( -1.0 * theta, axis );
					gl_FragColor.rgb += weights[ i ] * getSample( theta, axis );

				}

			}
		`,blending:Gi,depthTest:!1,depthWrite:!1})}function su(){return new _n({name:"EquirectangularToCubeUV",uniforms:{envMap:{value:null}},vertexShader:_c(),fragmentShader:`

			precision mediump float;
			precision mediump int;

			varying vec3 vOutputDirection;

			uniform sampler2D envMap;

			#include <common>

			void main() {

				vec3 outputDirection = normalize( vOutputDirection );
				vec2 uv = equirectUv( outputDirection );

				gl_FragColor = vec4( texture2D ( envMap, uv ).rgb, 1.0 );

			}
		`,blending:Gi,depthTest:!1,depthWrite:!1})}function ru(){return new _n({name:"CubemapToCubeUV",uniforms:{envMap:{value:null},flipEnvMap:{value:-1}},vertexShader:_c(),fragmentShader:`

			precision mediump float;
			precision mediump int;

			uniform float flipEnvMap;

			varying vec3 vOutputDirection;

			uniform samplerCube envMap;

			void main() {

				gl_FragColor = textureCube( envMap, vec3( flipEnvMap * vOutputDirection.x, vOutputDirection.yz ) );

			}
		`,blending:Gi,depthTest:!1,depthWrite:!1})}function _c(){return`

		precision mediump float;
		precision mediump int;

		attribute float faceIndex;

		varying vec3 vOutputDirection;

		// RH coordinate system; PMREM face-indexing convention
		vec3 getDirection( vec2 uv, float face ) {

			uv = 2.0 * uv - 1.0;

			vec3 direction = vec3( uv, 1.0 );

			if ( face == 0.0 ) {

				direction = direction.zyx; // ( 1, v, u ) pos x

			} else if ( face == 1.0 ) {

				direction = direction.xzy;
				direction.xz *= -1.0; // ( -u, 1, -v ) pos y

			} else if ( face == 2.0 ) {

				direction.x *= -1.0; // ( -u, v, 1 ) pos z

			} else if ( face == 3.0 ) {

				direction = direction.zyx;
				direction.xz *= -1.0; // ( -1, v, -u ) neg x

			} else if ( face == 4.0 ) {

				direction = direction.xzy;
				direction.xy *= -1.0; // ( -u, -1, v ) neg y

			} else if ( face == 5.0 ) {

				direction.z *= -1.0; // ( u, v, -1 ) neg z

			}

			return direction;

		}

		void main() {

			vOutputDirection = getDirection( uv, faceIndex );
			gl_Position = vec4( position, 1.0 );

		}
	`}function Hg(i){let t=new WeakMap,e=null;function n(o){if(o&&o.isTexture){let l=o.mapping,c=l===Ml||l===Sl,h=l===Qs||l===tr;if(c||h)if(o.isRenderTargetTexture&&o.needsPMREMUpdate===!0){o.needsPMREMUpdate=!1;let u=t.get(o);return e===null&&(e=new ir(i)),u=c?e.fromEquirectangular(o,u):e.fromCubemap(o,u),t.set(o,u),u.texture}else{if(t.has(o))return t.get(o).texture;{let u=o.image;if(c&&u&&u.height>0||h&&u&&s(u)){e===null&&(e=new ir(i));let d=c?e.fromEquirectangular(o):e.fromCubemap(o);return t.set(o,d),o.addEventListener("dispose",r),d.texture}else return null}}}return o}function s(o){let l=0,c=6;for(let h=0;h<c;h++)o[h]!==void 0&&l++;return l===c}function r(o){let l=o.target;l.removeEventListener("dispose",r);let c=t.get(l);c!==void 0&&(t.delete(l),c.dispose())}function a(){t=new WeakMap,e!==null&&(e.dispose(),e=null)}return{get:n,dispose:a}}function kg(i){let t={};function e(n){if(t[n]!==void 0)return t[n];let s;switch(n){case"WEBGL_depth_texture":s=i.getExtension("WEBGL_depth_texture")||i.getExtension("MOZ_WEBGL_depth_texture")||i.getExtension("WEBKIT_WEBGL_depth_texture");break;case"EXT_texture_filter_anisotropic":s=i.getExtension("EXT_texture_filter_anisotropic")||i.getExtension("MOZ_EXT_texture_filter_anisotropic")||i.getExtension("WEBKIT_EXT_texture_filter_anisotropic");break;case"WEBGL_compressed_texture_s3tc":s=i.getExtension("WEBGL_compressed_texture_s3tc")||i.getExtension("MOZ_WEBGL_compressed_texture_s3tc")||i.getExtension("WEBKIT_WEBGL_compressed_texture_s3tc");break;case"WEBGL_compressed_texture_pvrtc":s=i.getExtension("WEBGL_compressed_texture_pvrtc")||i.getExtension("WEBKIT_WEBGL_compressed_texture_pvrtc");break;default:s=i.getExtension(n)}return t[n]=s,s}return{has:function(n){return e(n)!==null},init:function(n){n.isWebGL2?(e("EXT_color_buffer_float"),e("WEBGL_clip_cull_distance")):(e("WEBGL_depth_texture"),e("OES_texture_float"),e("OES_texture_half_float"),e("OES_texture_half_float_linear"),e("OES_standard_derivatives"),e("OES_element_index_uint"),e("OES_vertex_array_object"),e("ANGLE_instanced_arrays")),e("OES_texture_float_linear"),e("EXT_color_buffer_half_float"),e("WEBGL_multisampled_render_to_texture")},get:function(n){let s=e(n);return s===null&&console.warn("THREE.WebGLRenderer: "+n+" extension not supported."),s}}}function Vg(i,t,e,n){let s={},r=new WeakMap;function a(u){let d=u.target;d.index!==null&&t.remove(d.index);for(let x in d.attributes)t.remove(d.attributes[x]);for(let x in d.morphAttributes){let y=d.morphAttributes[x];for(let g=0,m=y.length;g<m;g++)t.remove(y[g])}d.removeEventListener("dispose",a),delete s[d.id];let p=r.get(d);p&&(t.remove(p),r.delete(d)),n.releaseStatesOfGeometry(d),d.isInstancedBufferGeometry===!0&&delete d._maxInstanceCount,e.memory.geometries--}function o(u,d){return s[d.id]===!0||(d.addEventListener("dispose",a),s[d.id]=!0,e.memory.geometries++),d}function l(u){let d=u.attributes;for(let x in d)t.update(d[x],i.ARRAY_BUFFER);let p=u.morphAttributes;for(let x in p){let y=p[x];for(let g=0,m=y.length;g<m;g++)t.update(y[g],i.ARRAY_BUFFER)}}function c(u){let d=[],p=u.index,x=u.attributes.position,y=0;if(p!==null){let w=p.array;y=p.version;for(let v=0,I=w.length;v<I;v+=3){let H=w[v+0],U=w[v+1],N=w[v+2];d.push(H,U,U,N,N,H)}}else if(x!==void 0){let w=x.array;y=x.version;for(let v=0,I=w.length/3-1;v<I;v+=3){let H=v+0,U=v+1,N=v+2;d.push(H,U,U,N,N,H)}}else return;let g=new(qu(d)?$o:Zo)(d,1);g.version=y;let m=r.get(u);m&&t.remove(m),r.set(u,g)}function h(u){let d=r.get(u);if(d){let p=u.index;p!==null&&d.version<p.version&&c(u)}else c(u);return r.get(u)}return{get:o,update:l,getWireframeAttribute:h}}function Gg(i,t,e,n){let s=n.isWebGL2,r;function a(p){r=p}let o,l;function c(p){o=p.type,l=p.bytesPerElement}function h(p,x){i.drawElements(r,x,o,p*l),e.update(x,r,1)}function u(p,x,y){if(y===0)return;let g,m;if(s)g=i,m="drawElementsInstanced";else if(g=t.get("ANGLE_instanced_arrays"),m="drawElementsInstancedANGLE",g===null){console.error("THREE.WebGLIndexedBufferRenderer: using THREE.InstancedBufferGeometry but hardware does not support extension ANGLE_instanced_arrays.");return}g[m](r,x,o,p*l,y),e.update(x,r,y)}function d(p,x,y){if(y===0)return;let g=t.get("WEBGL_multi_draw");if(g===null)for(let m=0;m<y;m++)this.render(p[m]/l,x[m]);else{g.multiDrawElementsWEBGL(r,x,0,o,p,0,y);let m=0;for(let w=0;w<y;w++)m+=x[w];e.update(m,r,1)}}this.setMode=a,this.setIndex=c,this.render=h,this.renderInstances=u,this.renderMultiDraw=d}function Wg(i){let t={geometries:0,textures:0},e={frame:0,calls:0,triangles:0,points:0,lines:0};function n(r,a,o){switch(e.calls++,a){case i.TRIANGLES:e.triangles+=o*(r/3);break;case i.LINES:e.lines+=o*(r/2);break;case i.LINE_STRIP:e.lines+=o*(r-1);break;case i.LINE_LOOP:e.lines+=o*r;break;case i.POINTS:e.points+=o*r;break;default:console.error("THREE.WebGLInfo: Unknown draw mode:",a);break}}function s(){e.calls=0,e.triangles=0,e.points=0,e.lines=0}return{memory:t,render:e,programs:null,autoReset:!0,reset:s,update:n}}function Xg(i,t){return i[0]-t[0]}function Yg(i,t){return Math.abs(t[1])-Math.abs(i[1])}function qg(i,t,e){let n={},s=new Float32Array(8),r=new WeakMap,a=new Xe,o=[];for(let c=0;c<8;c++)o[c]=[c,0];function l(c,h,u){let d=c.morphTargetInfluences;if(t.isWebGL2===!0){let p=h.morphAttributes.position||h.morphAttributes.normal||h.morphAttributes.color,x=p!==void 0?p.length:0,y=r.get(h);if(y===void 0||y.count!==x){let k=function(){rt.dispose(),r.delete(h),h.removeEventListener("dispose",k)};y!==void 0&&y.texture.dispose();let w=h.morphAttributes.position!==void 0,v=h.morphAttributes.normal!==void 0,I=h.morphAttributes.color!==void 0,H=h.morphAttributes.position||[],U=h.morphAttributes.normal||[],N=h.morphAttributes.color||[],Y=0;w===!0&&(Y=1),v===!0&&(Y=2),I===!0&&(Y=3);let b=h.attributes.position.count*Y,P=1;b>t.maxTextureSize&&(P=Math.ceil(b/t.maxTextureSize),b=t.maxTextureSize);let X=new Float32Array(b*P*4*x),rt=new qo(X,b,P,x);rt.type=Vi,rt.needsUpdate=!0;let _t=Y*4;for(let q=0;q<x;q++){let j=H[q],et=U[q],ut=N[q],tt=b*P*4*q;for(let at=0;at<j.count;at++){let lt=at*_t;w===!0&&(a.fromBufferAttribute(j,at),X[tt+lt+0]=a.x,X[tt+lt+1]=a.y,X[tt+lt+2]=a.z,X[tt+lt+3]=0),v===!0&&(a.fromBufferAttribute(et,at),X[tt+lt+4]=a.x,X[tt+lt+5]=a.y,X[tt+lt+6]=a.z,X[tt+lt+7]=0),I===!0&&(a.fromBufferAttribute(ut,at),X[tt+lt+8]=a.x,X[tt+lt+9]=a.y,X[tt+lt+10]=a.z,X[tt+lt+11]=ut.itemSize===4?a.w:1)}}y={count:x,texture:rt,size:new xt(b,P)},r.set(h,y),h.addEventListener("dispose",k)}let g=0;for(let w=0;w<d.length;w++)g+=d[w];let m=h.morphTargetsRelative?1:1-g;u.getUniforms().setValue(i,"morphTargetBaseInfluence",m),u.getUniforms().setValue(i,"morphTargetInfluences",d),u.getUniforms().setValue(i,"morphTargetsTexture",y.texture,e),u.getUniforms().setValue(i,"morphTargetsTextureSize",y.size)}else{let p=d===void 0?0:d.length,x=n[h.id];if(x===void 0||x.length!==p){x=[];for(let v=0;v<p;v++)x[v]=[v,0];n[h.id]=x}for(let v=0;v<p;v++){let I=x[v];I[0]=v,I[1]=d[v]}x.sort(Yg);for(let v=0;v<8;v++)v<p&&x[v][1]?(o[v][0]=x[v][0],o[v][1]=x[v][1]):(o[v][0]=Number.MAX_SAFE_INTEGER,o[v][1]=0);o.sort(Xg);let y=h.morphAttributes.position,g=h.morphAttributes.normal,m=0;for(let v=0;v<8;v++){let I=o[v],H=I[0],U=I[1];H!==Number.MAX_SAFE_INTEGER&&U?(y&&h.getAttribute("morphTarget"+v)!==y[H]&&h.setAttribute("morphTarget"+v,y[H]),g&&h.getAttribute("morphNormal"+v)!==g[H]&&h.setAttribute("morphNormal"+v,g[H]),s[v]=U,m+=U):(y&&h.hasAttribute("morphTarget"+v)===!0&&h.deleteAttribute("morphTarget"+v),g&&h.hasAttribute("morphNormal"+v)===!0&&h.deleteAttribute("morphNormal"+v),s[v]=0)}let w=h.morphTargetsRelative?1:1-m;u.getUniforms().setValue(i,"morphTargetBaseInfluence",w),u.getUniforms().setValue(i,"morphTargetInfluences",s)}}return{update:l}}function Zg(i,t,e,n){let s=new WeakMap;function r(l){let c=n.render.frame,h=l.geometry,u=t.get(l,h);if(s.get(u)!==c&&(t.update(u),s.set(u,c)),l.isInstancedMesh&&(l.hasEventListener("dispose",o)===!1&&l.addEventListener("dispose",o),s.get(l)!==c&&(e.update(l.instanceMatrix,i.ARRAY_BUFFER),l.instanceColor!==null&&e.update(l.instanceColor,i.ARRAY_BUFFER),s.set(l,c))),l.isSkinnedMesh){let d=l.skeleton;s.get(d)!==c&&(d.update(),s.set(d,c))}return u}function a(){s=new WeakMap}function o(l){let c=l.target;c.removeEventListener("dispose",o),e.remove(c.instanceMatrix),c.instanceColor!==null&&e.remove(c.instanceColor)}return{update:r,dispose:a}}var Qo=class extends Dn{constructor(t,e,n,s,r,a,o,l,c,h){if(h=h!==void 0?h:fs,h!==fs&&h!==er)throw new Error("DepthTexture format must be either THREE.DepthFormat or THREE.DepthStencilFormat");n===void 0&&h===fs&&(n=ki),n===void 0&&h===er&&(n=us),super(null,s,r,a,o,l,h,n,c),this.isDepthTexture=!0,this.image={width:t,height:e},this.magFilter=o!==void 0?o:An,this.minFilter=l!==void 0?l:An,this.flipY=!1,this.generateMipmaps=!1,this.compareFunction=null}copy(t){return super.copy(t),this.compareFunction=t.compareFunction,this}toJSON(t){let e=super.toJSON(t);return this.compareFunction!==null&&(e.compareFunction=this.compareFunction),e}},Ku=new Dn,ju=new Qo(1,1);ju.compareFunction=Yu;var Qu=new qo,tf=new Al,ef=new Ko,ou=[],au=[],lu=new Float32Array(16),cu=new Float32Array(9),hu=new Float32Array(4);function ar(i,t,e){let n=i[0];if(n<=0||n>0)return i;let s=t*e,r=ou[s];if(r===void 0&&(r=new Float32Array(s),ou[s]=r),t!==0){n.toArray(r,0);for(let a=1,o=0;a!==t;++a)o+=e,i[a].toArray(r,o)}return r}function nn(i,t){if(i.length!==t.length)return!1;for(let e=0,n=i.length;e<n;e++)if(i[e]!==t[e])return!1;return!0}function sn(i,t){for(let e=0,n=t.length;e<n;e++)i[e]=t[e]}function xa(i,t){let e=au[t];e===void 0&&(e=new Int32Array(t),au[t]=e);for(let n=0;n!==t;++n)e[n]=i.allocateTextureUnit();return e}function $g(i,t){let e=this.cache;e[0]!==t&&(i.uniform1f(this.addr,t),e[0]=t)}function Jg(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y)&&(i.uniform2f(this.addr,t.x,t.y),e[0]=t.x,e[1]=t.y);else{if(nn(e,t))return;i.uniform2fv(this.addr,t),sn(e,t)}}function Kg(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z)&&(i.uniform3f(this.addr,t.x,t.y,t.z),e[0]=t.x,e[1]=t.y,e[2]=t.z);else if(t.r!==void 0)(e[0]!==t.r||e[1]!==t.g||e[2]!==t.b)&&(i.uniform3f(this.addr,t.r,t.g,t.b),e[0]=t.r,e[1]=t.g,e[2]=t.b);else{if(nn(e,t))return;i.uniform3fv(this.addr,t),sn(e,t)}}function jg(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z||e[3]!==t.w)&&(i.uniform4f(this.addr,t.x,t.y,t.z,t.w),e[0]=t.x,e[1]=t.y,e[2]=t.z,e[3]=t.w);else{if(nn(e,t))return;i.uniform4fv(this.addr,t),sn(e,t)}}function Qg(i,t){let e=this.cache,n=t.elements;if(n===void 0){if(nn(e,t))return;i.uniformMatrix2fv(this.addr,!1,t),sn(e,t)}else{if(nn(e,n))return;hu.set(n),i.uniformMatrix2fv(this.addr,!1,hu),sn(e,n)}}function t0(i,t){let e=this.cache,n=t.elements;if(n===void 0){if(nn(e,t))return;i.uniformMatrix3fv(this.addr,!1,t),sn(e,t)}else{if(nn(e,n))return;cu.set(n),i.uniformMatrix3fv(this.addr,!1,cu),sn(e,n)}}function e0(i,t){let e=this.cache,n=t.elements;if(n===void 0){if(nn(e,t))return;i.uniformMatrix4fv(this.addr,!1,t),sn(e,t)}else{if(nn(e,n))return;lu.set(n),i.uniformMatrix4fv(this.addr,!1,lu),sn(e,n)}}function n0(i,t){let e=this.cache;e[0]!==t&&(i.uniform1i(this.addr,t),e[0]=t)}function i0(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y)&&(i.uniform2i(this.addr,t.x,t.y),e[0]=t.x,e[1]=t.y);else{if(nn(e,t))return;i.uniform2iv(this.addr,t),sn(e,t)}}function s0(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z)&&(i.uniform3i(this.addr,t.x,t.y,t.z),e[0]=t.x,e[1]=t.y,e[2]=t.z);else{if(nn(e,t))return;i.uniform3iv(this.addr,t),sn(e,t)}}function r0(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z||e[3]!==t.w)&&(i.uniform4i(this.addr,t.x,t.y,t.z,t.w),e[0]=t.x,e[1]=t.y,e[2]=t.z,e[3]=t.w);else{if(nn(e,t))return;i.uniform4iv(this.addr,t),sn(e,t)}}function o0(i,t){let e=this.cache;e[0]!==t&&(i.uniform1ui(this.addr,t),e[0]=t)}function a0(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y)&&(i.uniform2ui(this.addr,t.x,t.y),e[0]=t.x,e[1]=t.y);else{if(nn(e,t))return;i.uniform2uiv(this.addr,t),sn(e,t)}}function l0(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z)&&(i.uniform3ui(this.addr,t.x,t.y,t.z),e[0]=t.x,e[1]=t.y,e[2]=t.z);else{if(nn(e,t))return;i.uniform3uiv(this.addr,t),sn(e,t)}}function c0(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z||e[3]!==t.w)&&(i.uniform4ui(this.addr,t.x,t.y,t.z,t.w),e[0]=t.x,e[1]=t.y,e[2]=t.z,e[3]=t.w);else{if(nn(e,t))return;i.uniform4uiv(this.addr,t),sn(e,t)}}function h0(i,t,e){let n=this.cache,s=e.allocateTextureUnit();n[0]!==s&&(i.uniform1i(this.addr,s),n[0]=s);let r=this.type===i.SAMPLER_2D_SHADOW?ju:Ku;e.setTexture2D(t||r,s)}function u0(i,t,e){let n=this.cache,s=e.allocateTextureUnit();n[0]!==s&&(i.uniform1i(this.addr,s),n[0]=s),e.setTexture3D(t||tf,s)}function f0(i,t,e){let n=this.cache,s=e.allocateTextureUnit();n[0]!==s&&(i.uniform1i(this.addr,s),n[0]=s),e.setTextureCube(t||ef,s)}function d0(i,t,e){let n=this.cache,s=e.allocateTextureUnit();n[0]!==s&&(i.uniform1i(this.addr,s),n[0]=s),e.setTexture2DArray(t||Qu,s)}function p0(i){switch(i){case 5126:return $g;case 35664:return Jg;case 35665:return Kg;case 35666:return jg;case 35674:return Qg;case 35675:return t0;case 35676:return e0;case 5124:case 35670:return n0;case 35667:case 35671:return i0;case 35668:case 35672:return s0;case 35669:case 35673:return r0;case 5125:return o0;case 36294:return a0;case 36295:return l0;case 36296:return c0;case 35678:case 36198:case 36298:case 36306:case 35682:return h0;case 35679:case 36299:case 36307:return u0;case 35680:case 36300:case 36308:case 36293:return f0;case 36289:case 36303:case 36311:case 36292:return d0}}function m0(i,t){i.uniform1fv(this.addr,t)}function g0(i,t){let e=ar(t,this.size,2);i.uniform2fv(this.addr,e)}function _0(i,t){let e=ar(t,this.size,3);i.uniform3fv(this.addr,e)}function x0(i,t){let e=ar(t,this.size,4);i.uniform4fv(this.addr,e)}function v0(i,t){let e=ar(t,this.size,4);i.uniformMatrix2fv(this.addr,!1,e)}function y0(i,t){let e=ar(t,this.size,9);i.uniformMatrix3fv(this.addr,!1,e)}function M0(i,t){let e=ar(t,this.size,16);i.uniformMatrix4fv(this.addr,!1,e)}function S0(i,t){i.uniform1iv(this.addr,t)}function b0(i,t){i.uniform2iv(this.addr,t)}function E0(i,t){i.uniform3iv(this.addr,t)}function w0(i,t){i.uniform4iv(this.addr,t)}function T0(i,t){i.uniform1uiv(this.addr,t)}function A0(i,t){i.uniform2uiv(this.addr,t)}function R0(i,t){i.uniform3uiv(this.addr,t)}function C0(i,t){i.uniform4uiv(this.addr,t)}function P0(i,t,e){let n=this.cache,s=t.length,r=xa(e,s);nn(n,r)||(i.uniform1iv(this.addr,r),sn(n,r));for(let a=0;a!==s;++a)e.setTexture2D(t[a]||Ku,r[a])}function I0(i,t,e){let n=this.cache,s=t.length,r=xa(e,s);nn(n,r)||(i.uniform1iv(this.addr,r),sn(n,r));for(let a=0;a!==s;++a)e.setTexture3D(t[a]||tf,r[a])}function L0(i,t,e){let n=this.cache,s=t.length,r=xa(e,s);nn(n,r)||(i.uniform1iv(this.addr,r),sn(n,r));for(let a=0;a!==s;++a)e.setTextureCube(t[a]||ef,r[a])}function U0(i,t,e){let n=this.cache,s=t.length,r=xa(e,s);nn(n,r)||(i.uniform1iv(this.addr,r),sn(n,r));for(let a=0;a!==s;++a)e.setTexture2DArray(t[a]||Qu,r[a])}function D0(i){switch(i){case 5126:return m0;case 35664:return g0;case 35665:return _0;case 35666:return x0;case 35674:return v0;case 35675:return y0;case 35676:return M0;case 5124:case 35670:return S0;case 35667:case 35671:return b0;case 35668:case 35672:return E0;case 35669:case 35673:return w0;case 5125:return T0;case 36294:return A0;case 36295:return R0;case 36296:return C0;case 35678:case 36198:case 36298:case 36306:case 35682:return P0;case 35679:case 36299:case 36307:return I0;case 35680:case 36300:case 36308:case 36293:return L0;case 36289:case 36303:case 36311:case 36292:return U0}}var Pl=class{constructor(t,e,n){this.id=t,this.addr=n,this.cache=[],this.type=e.type,this.setValue=p0(e.type)}},Il=class{constructor(t,e,n){this.id=t,this.addr=n,this.cache=[],this.type=e.type,this.size=e.size,this.setValue=D0(e.type)}},Ll=class{constructor(t){this.id=t,this.seq=[],this.map={}}setValue(t,e,n){let s=this.seq;for(let r=0,a=s.length;r!==a;++r){let o=s[r];o.setValue(t,e[o.id],n)}}},dl=/(\w+)(\])?(\[|\.)?/g;function uu(i,t){i.seq.push(t),i.map[t.id]=t}function N0(i,t,e){let n=i.name,s=n.length;for(dl.lastIndex=0;;){let r=dl.exec(n),a=dl.lastIndex,o=r[1],l=r[2]==="]",c=r[3];if(l&&(o=o|0),c===void 0||c==="["&&a+2===s){uu(e,c===void 0?new Pl(o,i,t):new Il(o,i,t));break}else{let u=e.map[o];u===void 0&&(u=new Ll(o),uu(e,u)),e=u}}}var Ks=class{constructor(t,e){this.seq=[],this.map={};let n=t.getProgramParameter(e,t.ACTIVE_UNIFORMS);for(let s=0;s<n;++s){let r=t.getActiveUniform(e,s),a=t.getUniformLocation(e,r.name);N0(r,a,this)}}setValue(t,e,n,s){let r=this.map[e];r!==void 0&&r.setValue(t,n,s)}setOptional(t,e,n){let s=e[n];s!==void 0&&this.setValue(t,n,s)}static upload(t,e,n,s){for(let r=0,a=e.length;r!==a;++r){let o=e[r],l=n[o.id];l.needsUpdate!==!1&&o.setValue(t,l.value,s)}}static seqWithValue(t,e){let n=[];for(let s=0,r=t.length;s!==r;++s){let a=t[s];a.id in e&&n.push(a)}return n}};function fu(i,t,e){let n=i.createShader(t);return i.shaderSource(n,e),i.compileShader(n),n}var F0=37297,O0=0;function B0(i,t){let e=i.split(`
`),n=[],s=Math.max(t-6,0),r=Math.min(t+6,e.length);for(let a=s;a<r;a++){let o=a+1;n.push(`${o===t?">":" "} ${o}: ${e[a]}`)}return n.join(`
`)}function z0(i){let t=Ue.getPrimaries(Ue.workingColorSpace),e=Ue.getPrimaries(i),n;switch(t===e?n="":t===Vo&&e===ko?n="LinearDisplayP3ToLinearSRGB":t===ko&&e===Vo&&(n="LinearSRGBToLinearDisplayP3"),i){case Ai:case _a:return[n,"LinearTransferOETF"];case Je:case pc:return[n,"sRGBTransferOETF"];default:return console.warn("THREE.WebGLProgram: Unsupported color space:",i),[n,"LinearTransferOETF"]}}function du(i,t,e){let n=i.getShaderParameter(t,i.COMPILE_STATUS),s=i.getShaderInfoLog(t).trim();if(n&&s==="")return"";let r=/ERROR: 0:(\d+)/.exec(s);if(r){let a=parseInt(r[1]);return e.toUpperCase()+`

`+s+`

`+B0(i.getShaderSource(t),a)}else return s}function H0(i,t){let e=z0(t);return`vec4 ${i}( vec4 value ) { return ${e[0]}( ${e[1]}( value ) ); }`}function k0(i,t){let e;switch(t){case $f:e="Linear";break;case Jf:e="Reinhard";break;case Kf:e="OptimizedCineon";break;case uc:e="ACESFilmic";break;case Qf:e="AgX";break;case jf:e="Custom";break;default:console.warn("THREE.WebGLProgram: Unsupported toneMapping:",t),e="Linear"}return"vec3 "+i+"( vec3 color ) { return "+e+"ToneMapping( color ); }"}function V0(i){return[i.extensionDerivatives||i.envMapCubeUVHeight||i.bumpMap||i.normalMapTangentSpace||i.clearcoatNormalMap||i.flatShading||i.shaderID==="physical"?"#extension GL_OES_standard_derivatives : enable":"",(i.extensionFragDepth||i.logarithmicDepthBuffer)&&i.rendererExtensionFragDepth?"#extension GL_EXT_frag_depth : enable":"",i.extensionDrawBuffers&&i.rendererExtensionDrawBuffers?"#extension GL_EXT_draw_buffers : require":"",(i.extensionShaderTextureLOD||i.envMap||i.transmission)&&i.rendererExtensionShaderTextureLod?"#extension GL_EXT_shader_texture_lod : enable":""].filter(Ys).join(`
`)}function G0(i){return[i.extensionClipCullDistance?"#extension GL_ANGLE_clip_cull_distance : require":""].filter(Ys).join(`
`)}function W0(i){let t=[];for(let e in i){let n=i[e];n!==!1&&t.push("#define "+e+" "+n)}return t.join(`
`)}function X0(i,t){let e={},n=i.getProgramParameter(t,i.ACTIVE_ATTRIBUTES);for(let s=0;s<n;s++){let r=i.getActiveAttrib(t,s),a=r.name,o=1;r.type===i.FLOAT_MAT2&&(o=2),r.type===i.FLOAT_MAT3&&(o=3),r.type===i.FLOAT_MAT4&&(o=4),e[a]={type:r.type,location:i.getAttribLocation(t,a),locationSize:o}}return e}function Ys(i){return i!==""}function pu(i,t){let e=t.numSpotLightShadows+t.numSpotLightMaps-t.numSpotLightShadowsWithMaps;return i.replace(/NUM_DIR_LIGHTS/g,t.numDirLights).replace(/NUM_SPOT_LIGHTS/g,t.numSpotLights).replace(/NUM_SPOT_LIGHT_MAPS/g,t.numSpotLightMaps).replace(/NUM_SPOT_LIGHT_COORDS/g,e).replace(/NUM_RECT_AREA_LIGHTS/g,t.numRectAreaLights).replace(/NUM_POINT_LIGHTS/g,t.numPointLights).replace(/NUM_HEMI_LIGHTS/g,t.numHemiLights).replace(/NUM_DIR_LIGHT_SHADOWS/g,t.numDirLightShadows).replace(/NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS/g,t.numSpotLightShadowsWithMaps).replace(/NUM_SPOT_LIGHT_SHADOWS/g,t.numSpotLightShadows).replace(/NUM_POINT_LIGHT_SHADOWS/g,t.numPointLightShadows)}function mu(i,t){return i.replace(/NUM_CLIPPING_PLANES/g,t.numClippingPlanes).replace(/UNION_CLIPPING_PLANES/g,t.numClippingPlanes-t.numClipIntersection)}var Y0=/^[ \t]*#include +<([\w\d./]+)>/gm;function Ul(i){return i.replace(Y0,Z0)}var q0=new Map([["encodings_fragment","colorspace_fragment"],["encodings_pars_fragment","colorspace_pars_fragment"],["output_fragment","opaque_fragment"]]);function Z0(i,t){let e=de[t];if(e===void 0){let n=q0.get(t);if(n!==void 0)e=de[n],console.warn('THREE.WebGLRenderer: Shader chunk "%s" has been deprecated. Use "%s" instead.',t,n);else throw new Error("Can not resolve #include <"+t+">")}return Ul(e)}var $0=/#pragma unroll_loop_start\s+for\s*\(\s*int\s+i\s*=\s*(\d+)\s*;\s*i\s*<\s*(\d+)\s*;\s*i\s*\+\+\s*\)\s*{([\s\S]+?)}\s+#pragma unroll_loop_end/g;function gu(i){return i.replace($0,J0)}function J0(i,t,e,n){let s="";for(let r=parseInt(t);r<parseInt(e);r++)s+=n.replace(/\[\s*i\s*\]/g,"[ "+r+" ]").replace(/UNROLLED_LOOP_INDEX/g,r);return s}function _u(i){let t="precision "+i.precision+` float;
precision `+i.precision+" int;";return i.precision==="highp"?t+=`
#define HIGH_PRECISION`:i.precision==="mediump"?t+=`
#define MEDIUM_PRECISION`:i.precision==="lowp"&&(t+=`
#define LOW_PRECISION`),t}function K0(i){let t="SHADOWMAP_TYPE_BASIC";return i.shadowMapType===Du?t="SHADOWMAP_TYPE_PCF":i.shadowMapType===hc?t="SHADOWMAP_TYPE_PCF_SOFT":i.shadowMapType===Ei&&(t="SHADOWMAP_TYPE_VSM"),t}function j0(i){let t="ENVMAP_TYPE_CUBE";if(i.envMap)switch(i.envMapMode){case Qs:case tr:t="ENVMAP_TYPE_CUBE";break;case ga:t="ENVMAP_TYPE_CUBE_UV";break}return t}function Q0(i){let t="ENVMAP_MODE_REFLECTION";return i.envMap&&i.envMapMode===tr&&(t="ENVMAP_MODE_REFRACTION"),t}function t_(i){let t="ENVMAP_BLENDING_NONE";if(i.envMap)switch(i.combine){case Nu:t="ENVMAP_BLENDING_MULTIPLY";break;case qf:t="ENVMAP_BLENDING_MIX";break;case Zf:t="ENVMAP_BLENDING_ADD";break}return t}function e_(i){let t=i.envMapCubeUVHeight;if(t===null)return null;let e=Math.log2(t)-2,n=1/t;return{texelWidth:1/(3*Math.max(Math.pow(2,e),112)),texelHeight:n,maxMip:e}}function n_(i,t,e,n){let s=i.getContext(),r=e.defines,a=e.vertexShader,o=e.fragmentShader,l=K0(e),c=j0(e),h=Q0(e),u=t_(e),d=e_(e),p=e.isWebGL2?"":V0(e),x=G0(e),y=W0(r),g=s.createProgram(),m,w,v=e.glslVersion?"#version "+e.glslVersion+`
`:"";e.isRawShaderMaterial?(m=["#define SHADER_TYPE "+e.shaderType,"#define SHADER_NAME "+e.shaderName,y].filter(Ys).join(`
`),m.length>0&&(m+=`
`),w=[p,"#define SHADER_TYPE "+e.shaderType,"#define SHADER_NAME "+e.shaderName,y].filter(Ys).join(`
`),w.length>0&&(w+=`
`)):(m=[_u(e),"#define SHADER_TYPE "+e.shaderType,"#define SHADER_NAME "+e.shaderName,y,e.extensionClipCullDistance?"#define USE_CLIP_DISTANCE":"",e.batching?"#define USE_BATCHING":"",e.instancing?"#define USE_INSTANCING":"",e.instancingColor?"#define USE_INSTANCING_COLOR":"",e.useFog&&e.fog?"#define USE_FOG":"",e.useFog&&e.fogExp2?"#define FOG_EXP2":"",e.map?"#define USE_MAP":"",e.envMap?"#define USE_ENVMAP":"",e.envMap?"#define "+h:"",e.lightMap?"#define USE_LIGHTMAP":"",e.aoMap?"#define USE_AOMAP":"",e.bumpMap?"#define USE_BUMPMAP":"",e.normalMap?"#define USE_NORMALMAP":"",e.normalMapObjectSpace?"#define USE_NORMALMAP_OBJECTSPACE":"",e.normalMapTangentSpace?"#define USE_NORMALMAP_TANGENTSPACE":"",e.displacementMap?"#define USE_DISPLACEMENTMAP":"",e.emissiveMap?"#define USE_EMISSIVEMAP":"",e.anisotropy?"#define USE_ANISOTROPY":"",e.anisotropyMap?"#define USE_ANISOTROPYMAP":"",e.clearcoatMap?"#define USE_CLEARCOATMAP":"",e.clearcoatRoughnessMap?"#define USE_CLEARCOAT_ROUGHNESSMAP":"",e.clearcoatNormalMap?"#define USE_CLEARCOAT_NORMALMAP":"",e.iridescenceMap?"#define USE_IRIDESCENCEMAP":"",e.iridescenceThicknessMap?"#define USE_IRIDESCENCE_THICKNESSMAP":"",e.specularMap?"#define USE_SPECULARMAP":"",e.specularColorMap?"#define USE_SPECULAR_COLORMAP":"",e.specularIntensityMap?"#define USE_SPECULAR_INTENSITYMAP":"",e.roughnessMap?"#define USE_ROUGHNESSMAP":"",e.metalnessMap?"#define USE_METALNESSMAP":"",e.alphaMap?"#define USE_ALPHAMAP":"",e.alphaHash?"#define USE_ALPHAHASH":"",e.transmission?"#define USE_TRANSMISSION":"",e.transmissionMap?"#define USE_TRANSMISSIONMAP":"",e.thicknessMap?"#define USE_THICKNESSMAP":"",e.sheenColorMap?"#define USE_SHEEN_COLORMAP":"",e.sheenRoughnessMap?"#define USE_SHEEN_ROUGHNESSMAP":"",e.mapUv?"#define MAP_UV "+e.mapUv:"",e.alphaMapUv?"#define ALPHAMAP_UV "+e.alphaMapUv:"",e.lightMapUv?"#define LIGHTMAP_UV "+e.lightMapUv:"",e.aoMapUv?"#define AOMAP_UV "+e.aoMapUv:"",e.emissiveMapUv?"#define EMISSIVEMAP_UV "+e.emissiveMapUv:"",e.bumpMapUv?"#define BUMPMAP_UV "+e.bumpMapUv:"",e.normalMapUv?"#define NORMALMAP_UV "+e.normalMapUv:"",e.displacementMapUv?"#define DISPLACEMENTMAP_UV "+e.displacementMapUv:"",e.metalnessMapUv?"#define METALNESSMAP_UV "+e.metalnessMapUv:"",e.roughnessMapUv?"#define ROUGHNESSMAP_UV "+e.roughnessMapUv:"",e.anisotropyMapUv?"#define ANISOTROPYMAP_UV "+e.anisotropyMapUv:"",e.clearcoatMapUv?"#define CLEARCOATMAP_UV "+e.clearcoatMapUv:"",e.clearcoatNormalMapUv?"#define CLEARCOAT_NORMALMAP_UV "+e.clearcoatNormalMapUv:"",e.clearcoatRoughnessMapUv?"#define CLEARCOAT_ROUGHNESSMAP_UV "+e.clearcoatRoughnessMapUv:"",e.iridescenceMapUv?"#define IRIDESCENCEMAP_UV "+e.iridescenceMapUv:"",e.iridescenceThicknessMapUv?"#define IRIDESCENCE_THICKNESSMAP_UV "+e.iridescenceThicknessMapUv:"",e.sheenColorMapUv?"#define SHEEN_COLORMAP_UV "+e.sheenColorMapUv:"",e.sheenRoughnessMapUv?"#define SHEEN_ROUGHNESSMAP_UV "+e.sheenRoughnessMapUv:"",e.specularMapUv?"#define SPECULARMAP_UV "+e.specularMapUv:"",e.specularColorMapUv?"#define SPECULAR_COLORMAP_UV "+e.specularColorMapUv:"",e.specularIntensityMapUv?"#define SPECULAR_INTENSITYMAP_UV "+e.specularIntensityMapUv:"",e.transmissionMapUv?"#define TRANSMISSIONMAP_UV "+e.transmissionMapUv:"",e.thicknessMapUv?"#define THICKNESSMAP_UV "+e.thicknessMapUv:"",e.vertexTangents&&e.flatShading===!1?"#define USE_TANGENT":"",e.vertexColors?"#define USE_COLOR":"",e.vertexAlphas?"#define USE_COLOR_ALPHA":"",e.vertexUv1s?"#define USE_UV1":"",e.vertexUv2s?"#define USE_UV2":"",e.vertexUv3s?"#define USE_UV3":"",e.pointsUvs?"#define USE_POINTS_UV":"",e.flatShading?"#define FLAT_SHADED":"",e.skinning?"#define USE_SKINNING":"",e.morphTargets?"#define USE_MORPHTARGETS":"",e.morphNormals&&e.flatShading===!1?"#define USE_MORPHNORMALS":"",e.morphColors&&e.isWebGL2?"#define USE_MORPHCOLORS":"",e.morphTargetsCount>0&&e.isWebGL2?"#define MORPHTARGETS_TEXTURE":"",e.morphTargetsCount>0&&e.isWebGL2?"#define MORPHTARGETS_TEXTURE_STRIDE "+e.morphTextureStride:"",e.morphTargetsCount>0&&e.isWebGL2?"#define MORPHTARGETS_COUNT "+e.morphTargetsCount:"",e.doubleSided?"#define DOUBLE_SIDED":"",e.flipSided?"#define FLIP_SIDED":"",e.shadowMapEnabled?"#define USE_SHADOWMAP":"",e.shadowMapEnabled?"#define "+l:"",e.sizeAttenuation?"#define USE_SIZEATTENUATION":"",e.numLightProbes>0?"#define USE_LIGHT_PROBES":"",e.useLegacyLights?"#define LEGACY_LIGHTS":"",e.logarithmicDepthBuffer?"#define USE_LOGDEPTHBUF":"",e.logarithmicDepthBuffer&&e.rendererExtensionFragDepth?"#define USE_LOGDEPTHBUF_EXT":"","uniform mat4 modelMatrix;","uniform mat4 modelViewMatrix;","uniform mat4 projectionMatrix;","uniform mat4 viewMatrix;","uniform mat3 normalMatrix;","uniform vec3 cameraPosition;","uniform bool isOrthographic;","#ifdef USE_INSTANCING","	attribute mat4 instanceMatrix;","#endif","#ifdef USE_INSTANCING_COLOR","	attribute vec3 instanceColor;","#endif","attribute vec3 position;","attribute vec3 normal;","attribute vec2 uv;","#ifdef USE_UV1","	attribute vec2 uv1;","#endif","#ifdef USE_UV2","	attribute vec2 uv2;","#endif","#ifdef USE_UV3","	attribute vec2 uv3;","#endif","#ifdef USE_TANGENT","	attribute vec4 tangent;","#endif","#if defined( USE_COLOR_ALPHA )","	attribute vec4 color;","#elif defined( USE_COLOR )","	attribute vec3 color;","#endif","#if ( defined( USE_MORPHTARGETS ) && ! defined( MORPHTARGETS_TEXTURE ) )","	attribute vec3 morphTarget0;","	attribute vec3 morphTarget1;","	attribute vec3 morphTarget2;","	attribute vec3 morphTarget3;","	#ifdef USE_MORPHNORMALS","		attribute vec3 morphNormal0;","		attribute vec3 morphNormal1;","		attribute vec3 morphNormal2;","		attribute vec3 morphNormal3;","	#else","		attribute vec3 morphTarget4;","		attribute vec3 morphTarget5;","		attribute vec3 morphTarget6;","		attribute vec3 morphTarget7;","	#endif","#endif","#ifdef USE_SKINNING","	attribute vec4 skinIndex;","	attribute vec4 skinWeight;","#endif",`
`].filter(Ys).join(`
`),w=[p,_u(e),"#define SHADER_TYPE "+e.shaderType,"#define SHADER_NAME "+e.shaderName,y,e.useFog&&e.fog?"#define USE_FOG":"",e.useFog&&e.fogExp2?"#define FOG_EXP2":"",e.map?"#define USE_MAP":"",e.matcap?"#define USE_MATCAP":"",e.envMap?"#define USE_ENVMAP":"",e.envMap?"#define "+c:"",e.envMap?"#define "+h:"",e.envMap?"#define "+u:"",d?"#define CUBEUV_TEXEL_WIDTH "+d.texelWidth:"",d?"#define CUBEUV_TEXEL_HEIGHT "+d.texelHeight:"",d?"#define CUBEUV_MAX_MIP "+d.maxMip+".0":"",e.lightMap?"#define USE_LIGHTMAP":"",e.aoMap?"#define USE_AOMAP":"",e.bumpMap?"#define USE_BUMPMAP":"",e.normalMap?"#define USE_NORMALMAP":"",e.normalMapObjectSpace?"#define USE_NORMALMAP_OBJECTSPACE":"",e.normalMapTangentSpace?"#define USE_NORMALMAP_TANGENTSPACE":"",e.emissiveMap?"#define USE_EMISSIVEMAP":"",e.anisotropy?"#define USE_ANISOTROPY":"",e.anisotropyMap?"#define USE_ANISOTROPYMAP":"",e.clearcoat?"#define USE_CLEARCOAT":"",e.clearcoatMap?"#define USE_CLEARCOATMAP":"",e.clearcoatRoughnessMap?"#define USE_CLEARCOAT_ROUGHNESSMAP":"",e.clearcoatNormalMap?"#define USE_CLEARCOAT_NORMALMAP":"",e.iridescence?"#define USE_IRIDESCENCE":"",e.iridescenceMap?"#define USE_IRIDESCENCEMAP":"",e.iridescenceThicknessMap?"#define USE_IRIDESCENCE_THICKNESSMAP":"",e.specularMap?"#define USE_SPECULARMAP":"",e.specularColorMap?"#define USE_SPECULAR_COLORMAP":"",e.specularIntensityMap?"#define USE_SPECULAR_INTENSITYMAP":"",e.roughnessMap?"#define USE_ROUGHNESSMAP":"",e.metalnessMap?"#define USE_METALNESSMAP":"",e.alphaMap?"#define USE_ALPHAMAP":"",e.alphaTest?"#define USE_ALPHATEST":"",e.alphaHash?"#define USE_ALPHAHASH":"",e.sheen?"#define USE_SHEEN":"",e.sheenColorMap?"#define USE_SHEEN_COLORMAP":"",e.sheenRoughnessMap?"#define USE_SHEEN_ROUGHNESSMAP":"",e.transmission?"#define USE_TRANSMISSION":"",e.transmissionMap?"#define USE_TRANSMISSIONMAP":"",e.thicknessMap?"#define USE_THICKNESSMAP":"",e.vertexTangents&&e.flatShading===!1?"#define USE_TANGENT":"",e.vertexColors||e.instancingColor?"#define USE_COLOR":"",e.vertexAlphas?"#define USE_COLOR_ALPHA":"",e.vertexUv1s?"#define USE_UV1":"",e.vertexUv2s?"#define USE_UV2":"",e.vertexUv3s?"#define USE_UV3":"",e.pointsUvs?"#define USE_POINTS_UV":"",e.gradientMap?"#define USE_GRADIENTMAP":"",e.flatShading?"#define FLAT_SHADED":"",e.doubleSided?"#define DOUBLE_SIDED":"",e.flipSided?"#define FLIP_SIDED":"",e.shadowMapEnabled?"#define USE_SHADOWMAP":"",e.shadowMapEnabled?"#define "+l:"",e.premultipliedAlpha?"#define PREMULTIPLIED_ALPHA":"",e.numLightProbes>0?"#define USE_LIGHT_PROBES":"",e.useLegacyLights?"#define LEGACY_LIGHTS":"",e.decodeVideoTexture?"#define DECODE_VIDEO_TEXTURE":"",e.logarithmicDepthBuffer?"#define USE_LOGDEPTHBUF":"",e.logarithmicDepthBuffer&&e.rendererExtensionFragDepth?"#define USE_LOGDEPTHBUF_EXT":"","uniform mat4 viewMatrix;","uniform vec3 cameraPosition;","uniform bool isOrthographic;",e.toneMapping!==Wi?"#define TONE_MAPPING":"",e.toneMapping!==Wi?de.tonemapping_pars_fragment:"",e.toneMapping!==Wi?k0("toneMapping",e.toneMapping):"",e.dithering?"#define DITHERING":"",e.opaque?"#define OPAQUE":"",de.colorspace_pars_fragment,H0("linearToOutputTexel",e.outputColorSpace),e.useDepthPacking?"#define DEPTH_PACKING "+e.depthPacking:"",`
`].filter(Ys).join(`
`)),a=Ul(a),a=pu(a,e),a=mu(a,e),o=Ul(o),o=pu(o,e),o=mu(o,e),a=gu(a),o=gu(o),e.isWebGL2&&e.isRawShaderMaterial!==!0&&(v=`#version 300 es
`,m=[x,"precision mediump sampler2DArray;","#define attribute in","#define varying out","#define texture2D texture"].join(`
`)+`
`+m,w=["precision mediump sampler2DArray;","#define varying in",e.glslVersion===Fh?"":"layout(location = 0) out highp vec4 pc_fragColor;",e.glslVersion===Fh?"":"#define gl_FragColor pc_fragColor","#define gl_FragDepthEXT gl_FragDepth","#define texture2D texture","#define textureCube texture","#define texture2DProj textureProj","#define texture2DLodEXT textureLod","#define texture2DProjLodEXT textureProjLod","#define textureCubeLodEXT textureLod","#define texture2DGradEXT textureGrad","#define texture2DProjGradEXT textureProjGrad","#define textureCubeGradEXT textureGrad"].join(`
`)+`
`+w);let I=v+m+a,H=v+w+o,U=fu(s,s.VERTEX_SHADER,I),N=fu(s,s.FRAGMENT_SHADER,H);s.attachShader(g,U),s.attachShader(g,N),e.index0AttributeName!==void 0?s.bindAttribLocation(g,0,e.index0AttributeName):e.morphTargets===!0&&s.bindAttribLocation(g,0,"position"),s.linkProgram(g);function Y(rt){if(i.debug.checkShaderErrors){let _t=s.getProgramInfoLog(g).trim(),k=s.getShaderInfoLog(U).trim(),q=s.getShaderInfoLog(N).trim(),j=!0,et=!0;if(s.getProgramParameter(g,s.LINK_STATUS)===!1)if(j=!1,typeof i.debug.onShaderError=="function")i.debug.onShaderError(s,g,U,N);else{let ut=du(s,U,"vertex"),tt=du(s,N,"fragment");console.error("THREE.WebGLProgram: Shader Error "+s.getError()+" - VALIDATE_STATUS "+s.getProgramParameter(g,s.VALIDATE_STATUS)+`

Program Info Log: `+_t+`
`+ut+`
`+tt)}else _t!==""?console.warn("THREE.WebGLProgram: Program Info Log:",_t):(k===""||q==="")&&(et=!1);et&&(rt.diagnostics={runnable:j,programLog:_t,vertexShader:{log:k,prefix:m},fragmentShader:{log:q,prefix:w}})}s.deleteShader(U),s.deleteShader(N),b=new Ks(s,g),P=X0(s,g)}let b;this.getUniforms=function(){return b===void 0&&Y(this),b};let P;this.getAttributes=function(){return P===void 0&&Y(this),P};let X=e.rendererExtensionParallelShaderCompile===!1;return this.isReady=function(){return X===!1&&(X=s.getProgramParameter(g,F0)),X},this.destroy=function(){n.releaseStatesOfProgram(this),s.deleteProgram(g),this.program=void 0},this.type=e.shaderType,this.name=e.shaderName,this.id=O0++,this.cacheKey=t,this.usedTimes=1,this.program=g,this.vertexShader=U,this.fragmentShader=N,this}var i_=0,Dl=class{constructor(){this.shaderCache=new Map,this.materialCache=new Map}update(t){let e=t.vertexShader,n=t.fragmentShader,s=this._getShaderStage(e),r=this._getShaderStage(n),a=this._getShaderCacheForMaterial(t);return a.has(s)===!1&&(a.add(s),s.usedTimes++),a.has(r)===!1&&(a.add(r),r.usedTimes++),this}remove(t){let e=this.materialCache.get(t);for(let n of e)n.usedTimes--,n.usedTimes===0&&this.shaderCache.delete(n.code);return this.materialCache.delete(t),this}getVertexShaderID(t){return this._getShaderStage(t.vertexShader).id}getFragmentShaderID(t){return this._getShaderStage(t.fragmentShader).id}dispose(){this.shaderCache.clear(),this.materialCache.clear()}_getShaderCacheForMaterial(t){let e=this.materialCache,n=e.get(t);return n===void 0&&(n=new Set,e.set(t,n)),n}_getShaderStage(t){let e=this.shaderCache,n=e.get(t);return n===void 0&&(n=new Nl(t),e.set(t,n)),n}},Nl=class{constructor(t){this.id=i_++,this.code=t,this.usedTimes=0}};function s_(i,t,e,n,s,r,a){let o=new Dr,l=new Dl,c=[],h=s.isWebGL2,u=s.logarithmicDepthBuffer,d=s.vertexTextures,p=s.precision,x={MeshDepthMaterial:"depth",MeshDistanceMaterial:"distanceRGBA",MeshNormalMaterial:"normal",MeshBasicMaterial:"basic",MeshLambertMaterial:"lambert",MeshPhongMaterial:"phong",MeshToonMaterial:"toon",MeshStandardMaterial:"physical",MeshPhysicalMaterial:"physical",MeshMatcapMaterial:"matcap",LineBasicMaterial:"basic",LineDashedMaterial:"dashed",PointsMaterial:"points",ShadowMaterial:"shadow",SpriteMaterial:"sprite"};function y(b){return b===0?"uv":`uv${b}`}function g(b,P,X,rt,_t){let k=rt.fog,q=_t.geometry,j=b.isMeshStandardMaterial?rt.environment:null,et=(b.isMeshStandardMaterial?e:t).get(b.envMap||j),ut=et&&et.mapping===ga?et.image.height:null,tt=x[b.type];b.precision!==null&&(p=s.getMaxPrecision(b.precision),p!==b.precision&&console.warn("THREE.WebGLProgram.getParameters:",b.precision,"not supported, using",p,"instead."));let at=q.morphAttributes.position||q.morphAttributes.normal||q.morphAttributes.color,lt=at!==void 0?at.length:0,Ut=0;q.morphAttributes.position!==void 0&&(Ut=1),q.morphAttributes.normal!==void 0&&(Ut=2),q.morphAttributes.color!==void 0&&(Ut=3);let nt,ht,Dt,Bt;if(tt){let un=ui[tt];nt=un.vertexShader,ht=un.fragmentShader}else nt=b.vertexShader,ht=b.fragmentShader,l.update(b),Dt=l.getVertexShaderID(b),Bt=l.getFragmentShaderID(b);let zt=i.getRenderTarget(),ne=_t.isInstancedMesh===!0,Zt=_t.isBatchedMesh===!0,Wt=!!b.map,ae=!!b.matcap,F=!!et,Et=!!b.aoMap,st=!!b.lightMap,vt=!!b.bumpMap,ct=!!b.normalMap,Xt=!!b.displacementMap,Pt=!!b.emissiveMap,T=!!b.metalnessMap,S=!!b.roughnessMap,W=b.anisotropy>0,gt=b.clearcoat>0,pt=b.iridescence>0,mt=b.sheen>0,Vt=b.transmission>0,It=W&&!!b.anisotropyMap,Tt=gt&&!!b.clearcoatMap,jt=gt&&!!b.clearcoatNormalMap,he=gt&&!!b.clearcoatRoughnessMap,ft=pt&&!!b.iridescenceMap,Me=pt&&!!b.iridescenceThicknessMap,xe=mt&&!!b.sheenColorMap,Yt=mt&&!!b.sheenRoughnessMap,$t=!!b.specularMap,Ht=!!b.specularColorMap,re=!!b.specularIntensityMap,Ee=Vt&&!!b.transmissionMap,Ve=Vt&&!!b.thicknessMap,Kt=!!b.gradientMap,St=!!b.alphaMap,B=b.alphaTest>0,At=!!b.alphaHash,Lt=!!b.extensions,ie=!!q.attributes.uv1,Jt=!!q.attributes.uv2,Re=!!q.attributes.uv3,Pe=Wi;return b.toneMapped&&(zt===null||zt.isXRRenderTarget===!0)&&(Pe=i.toneMapping),{isWebGL2:h,shaderID:tt,shaderType:b.type,shaderName:b.name,vertexShader:nt,fragmentShader:ht,defines:b.defines,customVertexShaderID:Dt,customFragmentShaderID:Bt,isRawShaderMaterial:b.isRawShaderMaterial===!0,glslVersion:b.glslVersion,precision:p,batching:Zt,instancing:ne,instancingColor:ne&&_t.instanceColor!==null,supportsVertexTextures:d,outputColorSpace:zt===null?i.outputColorSpace:zt.isXRRenderTarget===!0?zt.texture.colorSpace:Ai,map:Wt,matcap:ae,envMap:F,envMapMode:F&&et.mapping,envMapCubeUVHeight:ut,aoMap:Et,lightMap:st,bumpMap:vt,normalMap:ct,displacementMap:d&&Xt,emissiveMap:Pt,normalMapObjectSpace:ct&&b.normalMapType===dc,normalMapTangentSpace:ct&&b.normalMapType===Xu,metalnessMap:T,roughnessMap:S,anisotropy:W,anisotropyMap:It,clearcoat:gt,clearcoatMap:Tt,clearcoatNormalMap:jt,clearcoatRoughnessMap:he,iridescence:pt,iridescenceMap:ft,iridescenceThicknessMap:Me,sheen:mt,sheenColorMap:xe,sheenRoughnessMap:Yt,specularMap:$t,specularColorMap:Ht,specularIntensityMap:re,transmission:Vt,transmissionMap:Ee,thicknessMap:Ve,gradientMap:Kt,opaque:b.transparent===!1&&b.blending===$s,alphaMap:St,alphaTest:B,alphaHash:At,combine:b.combine,mapUv:Wt&&y(b.map.channel),aoMapUv:Et&&y(b.aoMap.channel),lightMapUv:st&&y(b.lightMap.channel),bumpMapUv:vt&&y(b.bumpMap.channel),normalMapUv:ct&&y(b.normalMap.channel),displacementMapUv:Xt&&y(b.displacementMap.channel),emissiveMapUv:Pt&&y(b.emissiveMap.channel),metalnessMapUv:T&&y(b.metalnessMap.channel),roughnessMapUv:S&&y(b.roughnessMap.channel),anisotropyMapUv:It&&y(b.anisotropyMap.channel),clearcoatMapUv:Tt&&y(b.clearcoatMap.channel),clearcoatNormalMapUv:jt&&y(b.clearcoatNormalMap.channel),clearcoatRoughnessMapUv:he&&y(b.clearcoatRoughnessMap.channel),iridescenceMapUv:ft&&y(b.iridescenceMap.channel),iridescenceThicknessMapUv:Me&&y(b.iridescenceThicknessMap.channel),sheenColorMapUv:xe&&y(b.sheenColorMap.channel),sheenRoughnessMapUv:Yt&&y(b.sheenRoughnessMap.channel),specularMapUv:$t&&y(b.specularMap.channel),specularColorMapUv:Ht&&y(b.specularColorMap.channel),specularIntensityMapUv:re&&y(b.specularIntensityMap.channel),transmissionMapUv:Ee&&y(b.transmissionMap.channel),thicknessMapUv:Ve&&y(b.thicknessMap.channel),alphaMapUv:St&&y(b.alphaMap.channel),vertexTangents:!!q.attributes.tangent&&(ct||W),vertexColors:b.vertexColors,vertexAlphas:b.vertexColors===!0&&!!q.attributes.color&&q.attributes.color.itemSize===4,vertexUv1s:ie,vertexUv2s:Jt,vertexUv3s:Re,pointsUvs:_t.isPoints===!0&&!!q.attributes.uv&&(Wt||St),fog:!!k,useFog:b.fog===!0,fogExp2:k&&k.isFogExp2,flatShading:b.flatShading===!0,sizeAttenuation:b.sizeAttenuation===!0,logarithmicDepthBuffer:u,skinning:_t.isSkinnedMesh===!0,morphTargets:q.morphAttributes.position!==void 0,morphNormals:q.morphAttributes.normal!==void 0,morphColors:q.morphAttributes.color!==void 0,morphTargetsCount:lt,morphTextureStride:Ut,numDirLights:P.directional.length,numPointLights:P.point.length,numSpotLights:P.spot.length,numSpotLightMaps:P.spotLightMap.length,numRectAreaLights:P.rectArea.length,numHemiLights:P.hemi.length,numDirLightShadows:P.directionalShadowMap.length,numPointLightShadows:P.pointShadowMap.length,numSpotLightShadows:P.spotShadowMap.length,numSpotLightShadowsWithMaps:P.numSpotLightShadowsWithMaps,numLightProbes:P.numLightProbes,numClippingPlanes:a.numPlanes,numClipIntersection:a.numIntersection,dithering:b.dithering,shadowMapEnabled:i.shadowMap.enabled&&X.length>0,shadowMapType:i.shadowMap.type,toneMapping:Pe,useLegacyLights:i._useLegacyLights,decodeVideoTexture:Wt&&b.map.isVideoTexture===!0&&Ue.getTransfer(b.map.colorSpace)===ke,premultipliedAlpha:b.premultipliedAlpha,doubleSided:b.side===mn,flipSided:b.side===Sn,useDepthPacking:b.depthPacking>=0,depthPacking:b.depthPacking||0,index0AttributeName:b.index0AttributeName,extensionDerivatives:Lt&&b.extensions.derivatives===!0,extensionFragDepth:Lt&&b.extensions.fragDepth===!0,extensionDrawBuffers:Lt&&b.extensions.drawBuffers===!0,extensionShaderTextureLOD:Lt&&b.extensions.shaderTextureLOD===!0,extensionClipCullDistance:Lt&&b.extensions.clipCullDistance&&n.has("WEBGL_clip_cull_distance"),rendererExtensionFragDepth:h||n.has("EXT_frag_depth"),rendererExtensionDrawBuffers:h||n.has("WEBGL_draw_buffers"),rendererExtensionShaderTextureLod:h||n.has("EXT_shader_texture_lod"),rendererExtensionParallelShaderCompile:n.has("KHR_parallel_shader_compile"),customProgramCacheKey:b.customProgramCacheKey()}}function m(b){let P=[];if(b.shaderID?P.push(b.shaderID):(P.push(b.customVertexShaderID),P.push(b.customFragmentShaderID)),b.defines!==void 0)for(let X in b.defines)P.push(X),P.push(b.defines[X]);return b.isRawShaderMaterial===!1&&(w(P,b),v(P,b),P.push(i.outputColorSpace)),P.push(b.customProgramCacheKey),P.join()}function w(b,P){b.push(P.precision),b.push(P.outputColorSpace),b.push(P.envMapMode),b.push(P.envMapCubeUVHeight),b.push(P.mapUv),b.push(P.alphaMapUv),b.push(P.lightMapUv),b.push(P.aoMapUv),b.push(P.bumpMapUv),b.push(P.normalMapUv),b.push(P.displacementMapUv),b.push(P.emissiveMapUv),b.push(P.metalnessMapUv),b.push(P.roughnessMapUv),b.push(P.anisotropyMapUv),b.push(P.clearcoatMapUv),b.push(P.clearcoatNormalMapUv),b.push(P.clearcoatRoughnessMapUv),b.push(P.iridescenceMapUv),b.push(P.iridescenceThicknessMapUv),b.push(P.sheenColorMapUv),b.push(P.sheenRoughnessMapUv),b.push(P.specularMapUv),b.push(P.specularColorMapUv),b.push(P.specularIntensityMapUv),b.push(P.transmissionMapUv),b.push(P.thicknessMapUv),b.push(P.combine),b.push(P.fogExp2),b.push(P.sizeAttenuation),b.push(P.morphTargetsCount),b.push(P.morphAttributeCount),b.push(P.numDirLights),b.push(P.numPointLights),b.push(P.numSpotLights),b.push(P.numSpotLightMaps),b.push(P.numHemiLights),b.push(P.numRectAreaLights),b.push(P.numDirLightShadows),b.push(P.numPointLightShadows),b.push(P.numSpotLightShadows),b.push(P.numSpotLightShadowsWithMaps),b.push(P.numLightProbes),b.push(P.shadowMapType),b.push(P.toneMapping),b.push(P.numClippingPlanes),b.push(P.numClipIntersection),b.push(P.depthPacking)}function v(b,P){o.disableAll(),P.isWebGL2&&o.enable(0),P.supportsVertexTextures&&o.enable(1),P.instancing&&o.enable(2),P.instancingColor&&o.enable(3),P.matcap&&o.enable(4),P.envMap&&o.enable(5),P.normalMapObjectSpace&&o.enable(6),P.normalMapTangentSpace&&o.enable(7),P.clearcoat&&o.enable(8),P.iridescence&&o.enable(9),P.alphaTest&&o.enable(10),P.vertexColors&&o.enable(11),P.vertexAlphas&&o.enable(12),P.vertexUv1s&&o.enable(13),P.vertexUv2s&&o.enable(14),P.vertexUv3s&&o.enable(15),P.vertexTangents&&o.enable(16),P.anisotropy&&o.enable(17),P.alphaHash&&o.enable(18),P.batching&&o.enable(19),b.push(o.mask),o.disableAll(),P.fog&&o.enable(0),P.useFog&&o.enable(1),P.flatShading&&o.enable(2),P.logarithmicDepthBuffer&&o.enable(3),P.skinning&&o.enable(4),P.morphTargets&&o.enable(5),P.morphNormals&&o.enable(6),P.morphColors&&o.enable(7),P.premultipliedAlpha&&o.enable(8),P.shadowMapEnabled&&o.enable(9),P.useLegacyLights&&o.enable(10),P.doubleSided&&o.enable(11),P.flipSided&&o.enable(12),P.useDepthPacking&&o.enable(13),P.dithering&&o.enable(14),P.transmission&&o.enable(15),P.sheen&&o.enable(16),P.opaque&&o.enable(17),P.pointsUvs&&o.enable(18),P.decodeVideoTexture&&o.enable(19),b.push(o.mask)}function I(b){let P=x[b.type],X;if(P){let rt=ui[P];X=gc.clone(rt.uniforms)}else X=b.uniforms;return X}function H(b,P){let X;for(let rt=0,_t=c.length;rt<_t;rt++){let k=c[rt];if(k.cacheKey===P){X=k,++X.usedTimes;break}}return X===void 0&&(X=new n_(i,P,b,r),c.push(X)),X}function U(b){if(--b.usedTimes===0){let P=c.indexOf(b);c[P]=c[c.length-1],c.pop(),b.destroy()}}function N(b){l.remove(b)}function Y(){l.dispose()}return{getParameters:g,getProgramCacheKey:m,getUniforms:I,acquireProgram:H,releaseProgram:U,releaseShaderCache:N,programs:c,dispose:Y}}function r_(){let i=new WeakMap;function t(r){let a=i.get(r);return a===void 0&&(a={},i.set(r,a)),a}function e(r){i.delete(r)}function n(r,a,o){i.get(r)[a]=o}function s(){i=new WeakMap}return{get:t,remove:e,update:n,dispose:s}}function o_(i,t){return i.groupOrder!==t.groupOrder?i.groupOrder-t.groupOrder:i.renderOrder!==t.renderOrder?i.renderOrder-t.renderOrder:i.material.id!==t.material.id?i.material.id-t.material.id:i.z!==t.z?i.z-t.z:i.id-t.id}function xu(i,t){return i.groupOrder!==t.groupOrder?i.groupOrder-t.groupOrder:i.renderOrder!==t.renderOrder?i.renderOrder-t.renderOrder:i.z!==t.z?t.z-i.z:i.id-t.id}function vu(){let i=[],t=0,e=[],n=[],s=[];function r(){t=0,e.length=0,n.length=0,s.length=0}function a(u,d,p,x,y,g){let m=i[t];return m===void 0?(m={id:u.id,object:u,geometry:d,material:p,groupOrder:x,renderOrder:u.renderOrder,z:y,group:g},i[t]=m):(m.id=u.id,m.object=u,m.geometry=d,m.material=p,m.groupOrder=x,m.renderOrder=u.renderOrder,m.z=y,m.group=g),t++,m}function o(u,d,p,x,y,g){let m=a(u,d,p,x,y,g);p.transmission>0?n.push(m):p.transparent===!0?s.push(m):e.push(m)}function l(u,d,p,x,y,g){let m=a(u,d,p,x,y,g);p.transmission>0?n.unshift(m):p.transparent===!0?s.unshift(m):e.unshift(m)}function c(u,d){e.length>1&&e.sort(u||o_),n.length>1&&n.sort(d||xu),s.length>1&&s.sort(d||xu)}function h(){for(let u=t,d=i.length;u<d;u++){let p=i[u];if(p.id===null)break;p.id=null,p.object=null,p.geometry=null,p.material=null,p.group=null}}return{opaque:e,transmissive:n,transparent:s,init:r,push:o,unshift:l,finish:h,sort:c}}function a_(){let i=new WeakMap;function t(n,s){let r=i.get(n),a;return r===void 0?(a=new vu,i.set(n,[a])):s>=r.length?(a=new vu,r.push(a)):a=r[s],a}function e(){i=new WeakMap}return{get:t,dispose:e}}function l_(){let i={};return{get:function(t){if(i[t.id]!==void 0)return i[t.id];let e;switch(t.type){case"DirectionalLight":e={direction:new O,color:new ge};break;case"SpotLight":e={position:new O,direction:new O,color:new ge,distance:0,coneCos:0,penumbraCos:0,decay:0};break;case"PointLight":e={position:new O,color:new ge,distance:0,decay:0};break;case"HemisphereLight":e={direction:new O,skyColor:new ge,groundColor:new ge};break;case"RectAreaLight":e={color:new ge,position:new O,halfWidth:new O,halfHeight:new O};break}return i[t.id]=e,e}}}function c_(){let i={};return{get:function(t){if(i[t.id]!==void 0)return i[t.id];let e;switch(t.type){case"DirectionalLight":e={shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new xt};break;case"SpotLight":e={shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new xt};break;case"PointLight":e={shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new xt,shadowCameraNear:1,shadowCameraFar:1e3};break}return i[t.id]=e,e}}}var h_=0;function u_(i,t){return(t.castShadow?2:0)-(i.castShadow?2:0)+(t.map?1:0)-(i.map?1:0)}function f_(i,t){let e=new l_,n=c_(),s={version:0,hash:{directionalLength:-1,pointLength:-1,spotLength:-1,rectAreaLength:-1,hemiLength:-1,numDirectionalShadows:-1,numPointShadows:-1,numSpotShadows:-1,numSpotMaps:-1,numLightProbes:-1},ambient:[0,0,0],probe:[],directional:[],directionalShadow:[],directionalShadowMap:[],directionalShadowMatrix:[],spot:[],spotLightMap:[],spotShadow:[],spotShadowMap:[],spotLightMatrix:[],rectArea:[],rectAreaLTC1:null,rectAreaLTC2:null,point:[],pointShadow:[],pointShadowMap:[],pointShadowMatrix:[],hemi:[],numSpotLightShadowsWithMaps:0,numLightProbes:0};for(let h=0;h<9;h++)s.probe.push(new O);let r=new O,a=new De,o=new De;function l(h,u){let d=0,p=0,x=0;for(let rt=0;rt<9;rt++)s.probe[rt].set(0,0,0);let y=0,g=0,m=0,w=0,v=0,I=0,H=0,U=0,N=0,Y=0,b=0;h.sort(u_);let P=u===!0?Math.PI:1;for(let rt=0,_t=h.length;rt<_t;rt++){let k=h[rt],q=k.color,j=k.intensity,et=k.distance,ut=k.shadow&&k.shadow.map?k.shadow.map.texture:null;if(k.isAmbientLight)d+=q.r*j*P,p+=q.g*j*P,x+=q.b*j*P;else if(k.isLightProbe){for(let tt=0;tt<9;tt++)s.probe[tt].addScaledVector(k.sh.coefficients[tt],j);b++}else if(k.isDirectionalLight){let tt=e.get(k);if(tt.color.copy(k.color).multiplyScalar(k.intensity*P),k.castShadow){let at=k.shadow,lt=n.get(k);lt.shadowBias=at.bias,lt.shadowNormalBias=at.normalBias,lt.shadowRadius=at.radius,lt.shadowMapSize=at.mapSize,s.directionalShadow[y]=lt,s.directionalShadowMap[y]=ut,s.directionalShadowMatrix[y]=k.shadow.matrix,I++}s.directional[y]=tt,y++}else if(k.isSpotLight){let tt=e.get(k);tt.position.setFromMatrixPosition(k.matrixWorld),tt.color.copy(q).multiplyScalar(j*P),tt.distance=et,tt.coneCos=Math.cos(k.angle),tt.penumbraCos=Math.cos(k.angle*(1-k.penumbra)),tt.decay=k.decay,s.spot[m]=tt;let at=k.shadow;if(k.map&&(s.spotLightMap[N]=k.map,N++,at.updateMatrices(k),k.castShadow&&Y++),s.spotLightMatrix[m]=at.matrix,k.castShadow){let lt=n.get(k);lt.shadowBias=at.bias,lt.shadowNormalBias=at.normalBias,lt.shadowRadius=at.radius,lt.shadowMapSize=at.mapSize,s.spotShadow[m]=lt,s.spotShadowMap[m]=ut,U++}m++}else if(k.isRectAreaLight){let tt=e.get(k);tt.color.copy(q).multiplyScalar(j),tt.halfWidth.set(k.width*.5,0,0),tt.halfHeight.set(0,k.height*.5,0),s.rectArea[w]=tt,w++}else if(k.isPointLight){let tt=e.get(k);if(tt.color.copy(k.color).multiplyScalar(k.intensity*P),tt.distance=k.distance,tt.decay=k.decay,k.castShadow){let at=k.shadow,lt=n.get(k);lt.shadowBias=at.bias,lt.shadowNormalBias=at.normalBias,lt.shadowRadius=at.radius,lt.shadowMapSize=at.mapSize,lt.shadowCameraNear=at.camera.near,lt.shadowCameraFar=at.camera.far,s.pointShadow[g]=lt,s.pointShadowMap[g]=ut,s.pointShadowMatrix[g]=k.shadow.matrix,H++}s.point[g]=tt,g++}else if(k.isHemisphereLight){let tt=e.get(k);tt.skyColor.copy(k.color).multiplyScalar(j*P),tt.groundColor.copy(k.groundColor).multiplyScalar(j*P),s.hemi[v]=tt,v++}}w>0&&(t.isWebGL2?i.has("OES_texture_float_linear")===!0?(s.rectAreaLTC1=Ct.LTC_FLOAT_1,s.rectAreaLTC2=Ct.LTC_FLOAT_2):(s.rectAreaLTC1=Ct.LTC_HALF_1,s.rectAreaLTC2=Ct.LTC_HALF_2):i.has("OES_texture_float_linear")===!0?(s.rectAreaLTC1=Ct.LTC_FLOAT_1,s.rectAreaLTC2=Ct.LTC_FLOAT_2):i.has("OES_texture_half_float_linear")===!0?(s.rectAreaLTC1=Ct.LTC_HALF_1,s.rectAreaLTC2=Ct.LTC_HALF_2):console.error("THREE.WebGLRenderer: Unable to use RectAreaLight. Missing WebGL extensions.")),s.ambient[0]=d,s.ambient[1]=p,s.ambient[2]=x;let X=s.hash;(X.directionalLength!==y||X.pointLength!==g||X.spotLength!==m||X.rectAreaLength!==w||X.hemiLength!==v||X.numDirectionalShadows!==I||X.numPointShadows!==H||X.numSpotShadows!==U||X.numSpotMaps!==N||X.numLightProbes!==b)&&(s.directional.length=y,s.spot.length=m,s.rectArea.length=w,s.point.length=g,s.hemi.length=v,s.directionalShadow.length=I,s.directionalShadowMap.length=I,s.pointShadow.length=H,s.pointShadowMap.length=H,s.spotShadow.length=U,s.spotShadowMap.length=U,s.directionalShadowMatrix.length=I,s.pointShadowMatrix.length=H,s.spotLightMatrix.length=U+N-Y,s.spotLightMap.length=N,s.numSpotLightShadowsWithMaps=Y,s.numLightProbes=b,X.directionalLength=y,X.pointLength=g,X.spotLength=m,X.rectAreaLength=w,X.hemiLength=v,X.numDirectionalShadows=I,X.numPointShadows=H,X.numSpotShadows=U,X.numSpotMaps=N,X.numLightProbes=b,s.version=h_++)}function c(h,u){let d=0,p=0,x=0,y=0,g=0,m=u.matrixWorldInverse;for(let w=0,v=h.length;w<v;w++){let I=h[w];if(I.isDirectionalLight){let H=s.directional[d];H.direction.setFromMatrixPosition(I.matrixWorld),r.setFromMatrixPosition(I.target.matrixWorld),H.direction.sub(r),H.direction.transformDirection(m),d++}else if(I.isSpotLight){let H=s.spot[x];H.position.setFromMatrixPosition(I.matrixWorld),H.position.applyMatrix4(m),H.direction.setFromMatrixPosition(I.matrixWorld),r.setFromMatrixPosition(I.target.matrixWorld),H.direction.sub(r),H.direction.transformDirection(m),x++}else if(I.isRectAreaLight){let H=s.rectArea[y];H.position.setFromMatrixPosition(I.matrixWorld),H.position.applyMatrix4(m),o.identity(),a.copy(I.matrixWorld),a.premultiply(m),o.extractRotation(a),H.halfWidth.set(I.width*.5,0,0),H.halfHeight.set(0,I.height*.5,0),H.halfWidth.applyMatrix4(o),H.halfHeight.applyMatrix4(o),y++}else if(I.isPointLight){let H=s.point[p];H.position.setFromMatrixPosition(I.matrixWorld),H.position.applyMatrix4(m),p++}else if(I.isHemisphereLight){let H=s.hemi[g];H.direction.setFromMatrixPosition(I.matrixWorld),H.direction.transformDirection(m),g++}}}return{setup:l,setupView:c,state:s}}function yu(i,t){let e=new f_(i,t),n=[],s=[];function r(){n.length=0,s.length=0}function a(u){n.push(u)}function o(u){s.push(u)}function l(u){e.setup(n,u)}function c(u){e.setupView(n,u)}return{init:r,state:{lightsArray:n,shadowsArray:s,lights:e},setupLights:l,setupLightsView:c,pushLight:a,pushShadow:o}}function d_(i,t){let e=new WeakMap;function n(r,a=0){let o=e.get(r),l;return o===void 0?(l=new yu(i,t),e.set(r,[l])):a>=o.length?(l=new yu(i,t),o.push(l)):l=o[a],l}function s(){e=new WeakMap}return{get:n,dispose:s}}var Fl=class extends $i{constructor(t){super(),this.isMeshDepthMaterial=!0,this.type="MeshDepthMaterial",this.depthPacking=cd,this.map=null,this.alphaMap=null,this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.wireframe=!1,this.wireframeLinewidth=1,this.setValues(t)}copy(t){return super.copy(t),this.depthPacking=t.depthPacking,this.map=t.map,this.alphaMap=t.alphaMap,this.displacementMap=t.displacementMap,this.displacementScale=t.displacementScale,this.displacementBias=t.displacementBias,this.wireframe=t.wireframe,this.wireframeLinewidth=t.wireframeLinewidth,this}},Ol=class extends $i{constructor(t){super(),this.isMeshDistanceMaterial=!0,this.type="MeshDistanceMaterial",this.map=null,this.alphaMap=null,this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.setValues(t)}copy(t){return super.copy(t),this.map=t.map,this.alphaMap=t.alphaMap,this.displacementMap=t.displacementMap,this.displacementScale=t.displacementScale,this.displacementBias=t.displacementBias,this}},p_=`void main() {
	gl_Position = vec4( position, 1.0 );
}`,m_=`uniform sampler2D shadow_pass;
uniform vec2 resolution;
uniform float radius;
#include <packing>
void main() {
	const float samples = float( VSM_SAMPLES );
	float mean = 0.0;
	float squared_mean = 0.0;
	float uvStride = samples <= 1.0 ? 0.0 : 2.0 / ( samples - 1.0 );
	float uvStart = samples <= 1.0 ? 0.0 : - 1.0;
	for ( float i = 0.0; i < samples; i ++ ) {
		float uvOffset = uvStart + i * uvStride;
		#ifdef HORIZONTAL_PASS
			vec2 distribution = unpackRGBATo2Half( texture2D( shadow_pass, ( gl_FragCoord.xy + vec2( uvOffset, 0.0 ) * radius ) / resolution ) );
			mean += distribution.x;
			squared_mean += distribution.y * distribution.y + distribution.x * distribution.x;
		#else
			float depth = unpackRGBAToDepth( texture2D( shadow_pass, ( gl_FragCoord.xy + vec2( 0.0, uvOffset ) * radius ) / resolution ) );
			mean += depth;
			squared_mean += depth * depth;
		#endif
	}
	mean = mean / samples;
	squared_mean = squared_mean / samples;
	float std_dev = sqrt( squared_mean - mean * mean );
	gl_FragColor = pack2HalfToRGBA( vec2( mean, std_dev ) );
}`;function g_(i,t,e){let n=new Nr,s=new xt,r=new xt,a=new Xe,o=new Fl({depthPacking:hd}),l=new Ol,c={},h=e.maxTextureSize,u={[Yi]:Sn,[Sn]:Yi,[mn]:mn},d=new _n({defines:{VSM_SAMPLES:8},uniforms:{shadow_pass:{value:null},resolution:{value:new xt},radius:{value:4}},vertexShader:p_,fragmentShader:m_}),p=d.clone();p.defines.HORIZONTAL_PASS=1;let x=new qe;x.setAttribute("position",new gn(new Float32Array([-1,-1,.5,3,-1,.5,-1,3,.5]),3));let y=new Ce(x,d),g=this;this.enabled=!1,this.autoUpdate=!0,this.needsUpdate=!1,this.type=Du;let m=this.type;this.render=function(U,N,Y){if(g.enabled===!1||g.autoUpdate===!1&&g.needsUpdate===!1||U.length===0)return;let b=i.getRenderTarget(),P=i.getActiveCubeFace(),X=i.getActiveMipmapLevel(),rt=i.state;rt.setBlending(Gi),rt.buffers.color.setClear(1,1,1,1),rt.buffers.depth.setTest(!0),rt.setScissorTest(!1);let _t=m!==Ei&&this.type===Ei,k=m===Ei&&this.type!==Ei;for(let q=0,j=U.length;q<j;q++){let et=U[q],ut=et.shadow;if(ut===void 0){console.warn("THREE.WebGLShadowMap:",et,"has no shadow.");continue}if(ut.autoUpdate===!1&&ut.needsUpdate===!1)continue;s.copy(ut.mapSize);let tt=ut.getFrameExtents();if(s.multiply(tt),r.copy(ut.mapSize),(s.x>h||s.y>h)&&(s.x>h&&(r.x=Math.floor(h/tt.x),s.x=r.x*tt.x,ut.mapSize.x=r.x),s.y>h&&(r.y=Math.floor(h/tt.y),s.y=r.y*tt.y,ut.mapSize.y=r.y)),ut.map===null||_t===!0||k===!0){let lt=this.type!==Ei?{minFilter:An,magFilter:An}:{};ut.map!==null&&ut.map.dispose(),ut.map=new Ri(s.x,s.y,lt),ut.map.texture.name=et.name+".shadowMap",ut.camera.updateProjectionMatrix()}i.setRenderTarget(ut.map),i.clear();let at=ut.getViewportCount();for(let lt=0;lt<at;lt++){let Ut=ut.getViewport(lt);a.set(r.x*Ut.x,r.y*Ut.y,r.x*Ut.z,r.y*Ut.w),rt.viewport(a),ut.updateMatrices(et,lt),n=ut.getFrustum(),I(N,Y,ut.camera,et,this.type)}ut.isPointLightShadow!==!0&&this.type===Ei&&w(ut,Y),ut.needsUpdate=!1}m=this.type,g.needsUpdate=!1,i.setRenderTarget(b,P,X)};function w(U,N){let Y=t.update(y);d.defines.VSM_SAMPLES!==U.blurSamples&&(d.defines.VSM_SAMPLES=U.blurSamples,p.defines.VSM_SAMPLES=U.blurSamples,d.needsUpdate=!0,p.needsUpdate=!0),U.mapPass===null&&(U.mapPass=new Ri(s.x,s.y)),d.uniforms.shadow_pass.value=U.map.texture,d.uniforms.resolution.value=U.mapSize,d.uniforms.radius.value=U.radius,i.setRenderTarget(U.mapPass),i.clear(),i.renderBufferDirect(N,null,Y,d,y,null),p.uniforms.shadow_pass.value=U.mapPass.texture,p.uniforms.resolution.value=U.mapSize,p.uniforms.radius.value=U.radius,i.setRenderTarget(U.map),i.clear(),i.renderBufferDirect(N,null,Y,p,y,null)}function v(U,N,Y,b){let P=null,X=Y.isPointLight===!0?U.customDistanceMaterial:U.customDepthMaterial;if(X!==void 0)P=X;else if(P=Y.isPointLight===!0?l:o,i.localClippingEnabled&&N.clipShadows===!0&&Array.isArray(N.clippingPlanes)&&N.clippingPlanes.length!==0||N.displacementMap&&N.displacementScale!==0||N.alphaMap&&N.alphaTest>0||N.map&&N.alphaTest>0){let rt=P.uuid,_t=N.uuid,k=c[rt];k===void 0&&(k={},c[rt]=k);let q=k[_t];q===void 0&&(q=P.clone(),k[_t]=q,N.addEventListener("dispose",H)),P=q}if(P.visible=N.visible,P.wireframe=N.wireframe,b===Ei?P.side=N.shadowSide!==null?N.shadowSide:N.side:P.side=N.shadowSide!==null?N.shadowSide:u[N.side],P.alphaMap=N.alphaMap,P.alphaTest=N.alphaTest,P.map=N.map,P.clipShadows=N.clipShadows,P.clippingPlanes=N.clippingPlanes,P.clipIntersection=N.clipIntersection,P.displacementMap=N.displacementMap,P.displacementScale=N.displacementScale,P.displacementBias=N.displacementBias,P.wireframeLinewidth=N.wireframeLinewidth,P.linewidth=N.linewidth,Y.isPointLight===!0&&P.isMeshDistanceMaterial===!0){let rt=i.properties.get(P);rt.light=Y}return P}function I(U,N,Y,b,P){if(U.visible===!1)return;if(U.layers.test(N.layers)&&(U.isMesh||U.isLine||U.isPoints)&&(U.castShadow||U.receiveShadow&&P===Ei)&&(!U.frustumCulled||n.intersectsObject(U))){U.modelViewMatrix.multiplyMatrices(Y.matrixWorldInverse,U.matrixWorld);let _t=t.update(U),k=U.material;if(Array.isArray(k)){let q=_t.groups;for(let j=0,et=q.length;j<et;j++){let ut=q[j],tt=k[ut.materialIndex];if(tt&&tt.visible){let at=v(U,tt,b,P);U.onBeforeShadow(i,U,N,Y,_t,at,ut),i.renderBufferDirect(Y,null,_t,at,U,ut),U.onAfterShadow(i,U,N,Y,_t,at,ut)}}}else if(k.visible){let q=v(U,k,b,P);U.onBeforeShadow(i,U,N,Y,_t,q,null),i.renderBufferDirect(Y,null,_t,q,U,null),U.onAfterShadow(i,U,N,Y,_t,q,null)}}let rt=U.children;for(let _t=0,k=rt.length;_t<k;_t++)I(rt[_t],N,Y,b,P)}function H(U){U.target.removeEventListener("dispose",H);for(let Y in c){let b=c[Y],P=U.target.uuid;P in b&&(b[P].dispose(),delete b[P])}}}function __(i,t,e){let n=e.isWebGL2;function s(){let B=!1,At=new Xe,Lt=null,ie=new Xe(0,0,0,0);return{setMask:function(Jt){Lt!==Jt&&!B&&(i.colorMask(Jt,Jt,Jt,Jt),Lt=Jt)},setLocked:function(Jt){B=Jt},setClear:function(Jt,Re,Pe,Ke,un){un===!0&&(Jt*=Ke,Re*=Ke,Pe*=Ke),At.set(Jt,Re,Pe,Ke),ie.equals(At)===!1&&(i.clearColor(Jt,Re,Pe,Ke),ie.copy(At))},reset:function(){B=!1,Lt=null,ie.set(-1,0,0,0)}}}function r(){let B=!1,At=null,Lt=null,ie=null;return{setTest:function(Jt){Jt?Zt(i.DEPTH_TEST):Wt(i.DEPTH_TEST)},setMask:function(Jt){At!==Jt&&!B&&(i.depthMask(Jt),At=Jt)},setFunc:function(Jt){if(Lt!==Jt){switch(Jt){case Hf:i.depthFunc(i.NEVER);break;case kf:i.depthFunc(i.ALWAYS);break;case Vf:i.depthFunc(i.LESS);break;case Oo:i.depthFunc(i.LEQUAL);break;case Gf:i.depthFunc(i.EQUAL);break;case Wf:i.depthFunc(i.GEQUAL);break;case Xf:i.depthFunc(i.GREATER);break;case Yf:i.depthFunc(i.NOTEQUAL);break;default:i.depthFunc(i.LEQUAL)}Lt=Jt}},setLocked:function(Jt){B=Jt},setClear:function(Jt){ie!==Jt&&(i.clearDepth(Jt),ie=Jt)},reset:function(){B=!1,At=null,Lt=null,ie=null}}}function a(){let B=!1,At=null,Lt=null,ie=null,Jt=null,Re=null,Pe=null,Ke=null,un=null;return{setTest:function(Se){B||(Se?Zt(i.STENCIL_TEST):Wt(i.STENCIL_TEST))},setMask:function(Se){At!==Se&&!B&&(i.stencilMask(Se),At=Se)},setFunc:function(Se,fn,Nn){(Lt!==Se||ie!==fn||Jt!==Nn)&&(i.stencilFunc(Se,fn,Nn),Lt=Se,ie=fn,Jt=Nn)},setOp:function(Se,fn,Nn){(Re!==Se||Pe!==fn||Ke!==Nn)&&(i.stencilOp(Se,fn,Nn),Re=Se,Pe=fn,Ke=Nn)},setLocked:function(Se){B=Se},setClear:function(Se){un!==Se&&(i.clearStencil(Se),un=Se)},reset:function(){B=!1,At=null,Lt=null,ie=null,Jt=null,Re=null,Pe=null,Ke=null,un=null}}}let o=new s,l=new r,c=new a,h=new WeakMap,u=new WeakMap,d={},p={},x=new WeakMap,y=[],g=null,m=!1,w=null,v=null,I=null,H=null,U=null,N=null,Y=null,b=new ge(0,0,0),P=0,X=!1,rt=null,_t=null,k=null,q=null,j=null,et=i.getParameter(i.MAX_COMBINED_TEXTURE_IMAGE_UNITS),ut=!1,tt=0,at=i.getParameter(i.VERSION);at.indexOf("WebGL")!==-1?(tt=parseFloat(/^WebGL (\d)/.exec(at)[1]),ut=tt>=1):at.indexOf("OpenGL ES")!==-1&&(tt=parseFloat(/^OpenGL ES (\d)/.exec(at)[1]),ut=tt>=2);let lt=null,Ut={},nt=i.getParameter(i.SCISSOR_BOX),ht=i.getParameter(i.VIEWPORT),Dt=new Xe().fromArray(nt),Bt=new Xe().fromArray(ht);function zt(B,At,Lt,ie){let Jt=new Uint8Array(4),Re=i.createTexture();i.bindTexture(B,Re),i.texParameteri(B,i.TEXTURE_MIN_FILTER,i.NEAREST),i.texParameteri(B,i.TEXTURE_MAG_FILTER,i.NEAREST);for(let Pe=0;Pe<Lt;Pe++)n&&(B===i.TEXTURE_3D||B===i.TEXTURE_2D_ARRAY)?i.texImage3D(At,0,i.RGBA,1,1,ie,0,i.RGBA,i.UNSIGNED_BYTE,Jt):i.texImage2D(At+Pe,0,i.RGBA,1,1,0,i.RGBA,i.UNSIGNED_BYTE,Jt);return Re}let ne={};ne[i.TEXTURE_2D]=zt(i.TEXTURE_2D,i.TEXTURE_2D,1),ne[i.TEXTURE_CUBE_MAP]=zt(i.TEXTURE_CUBE_MAP,i.TEXTURE_CUBE_MAP_POSITIVE_X,6),n&&(ne[i.TEXTURE_2D_ARRAY]=zt(i.TEXTURE_2D_ARRAY,i.TEXTURE_2D_ARRAY,1,1),ne[i.TEXTURE_3D]=zt(i.TEXTURE_3D,i.TEXTURE_3D,1,1)),o.setClear(0,0,0,1),l.setClear(1),c.setClear(0),Zt(i.DEPTH_TEST),l.setFunc(Oo),Pt(!1),T(th),Zt(i.CULL_FACE),ct(Gi);function Zt(B){d[B]!==!0&&(i.enable(B),d[B]=!0)}function Wt(B){d[B]!==!1&&(i.disable(B),d[B]=!1)}function ae(B,At){return p[B]!==At?(i.bindFramebuffer(B,At),p[B]=At,n&&(B===i.DRAW_FRAMEBUFFER&&(p[i.FRAMEBUFFER]=At),B===i.FRAMEBUFFER&&(p[i.DRAW_FRAMEBUFFER]=At)),!0):!1}function F(B,At){let Lt=y,ie=!1;if(B)if(Lt=x.get(At),Lt===void 0&&(Lt=[],x.set(At,Lt)),B.isWebGLMultipleRenderTargets){let Jt=B.texture;if(Lt.length!==Jt.length||Lt[0]!==i.COLOR_ATTACHMENT0){for(let Re=0,Pe=Jt.length;Re<Pe;Re++)Lt[Re]=i.COLOR_ATTACHMENT0+Re;Lt.length=Jt.length,ie=!0}}else Lt[0]!==i.COLOR_ATTACHMENT0&&(Lt[0]=i.COLOR_ATTACHMENT0,ie=!0);else Lt[0]!==i.BACK&&(Lt[0]=i.BACK,ie=!0);ie&&(e.isWebGL2?i.drawBuffers(Lt):t.get("WEBGL_draw_buffers").drawBuffersWEBGL(Lt))}function Et(B){return g!==B?(i.useProgram(B),g=B,!0):!1}let st={[cs]:i.FUNC_ADD,[wf]:i.FUNC_SUBTRACT,[Tf]:i.FUNC_REVERSE_SUBTRACT};if(n)st[ih]=i.MIN,st[sh]=i.MAX;else{let B=t.get("EXT_blend_minmax");B!==null&&(st[ih]=B.MIN_EXT,st[sh]=B.MAX_EXT)}let vt={[Af]:i.ZERO,[Rf]:i.ONE,[Cf]:i.SRC_COLOR,[vl]:i.SRC_ALPHA,[Nf]:i.SRC_ALPHA_SATURATE,[Uf]:i.DST_COLOR,[If]:i.DST_ALPHA,[Pf]:i.ONE_MINUS_SRC_COLOR,[yl]:i.ONE_MINUS_SRC_ALPHA,[Df]:i.ONE_MINUS_DST_COLOR,[Lf]:i.ONE_MINUS_DST_ALPHA,[Ff]:i.CONSTANT_COLOR,[Of]:i.ONE_MINUS_CONSTANT_COLOR,[Bf]:i.CONSTANT_ALPHA,[zf]:i.ONE_MINUS_CONSTANT_ALPHA};function ct(B,At,Lt,ie,Jt,Re,Pe,Ke,un,Se){if(B===Gi){m===!0&&(Wt(i.BLEND),m=!1);return}if(m===!1&&(Zt(i.BLEND),m=!0),B!==Ef){if(B!==w||Se!==X){if((v!==cs||U!==cs)&&(i.blendEquation(i.FUNC_ADD),v=cs,U=cs),Se)switch(B){case $s:i.blendFuncSeparate(i.ONE,i.ONE_MINUS_SRC_ALPHA,i.ONE,i.ONE_MINUS_SRC_ALPHA);break;case js:i.blendFunc(i.ONE,i.ONE);break;case eh:i.blendFuncSeparate(i.ZERO,i.ONE_MINUS_SRC_COLOR,i.ZERO,i.ONE);break;case nh:i.blendFuncSeparate(i.ZERO,i.SRC_COLOR,i.ZERO,i.SRC_ALPHA);break;default:console.error("THREE.WebGLState: Invalid blending: ",B);break}else switch(B){case $s:i.blendFuncSeparate(i.SRC_ALPHA,i.ONE_MINUS_SRC_ALPHA,i.ONE,i.ONE_MINUS_SRC_ALPHA);break;case js:i.blendFunc(i.SRC_ALPHA,i.ONE);break;case eh:i.blendFuncSeparate(i.ZERO,i.ONE_MINUS_SRC_COLOR,i.ZERO,i.ONE);break;case nh:i.blendFunc(i.ZERO,i.SRC_COLOR);break;default:console.error("THREE.WebGLState: Invalid blending: ",B);break}I=null,H=null,N=null,Y=null,b.set(0,0,0),P=0,w=B,X=Se}return}Jt=Jt||At,Re=Re||Lt,Pe=Pe||ie,(At!==v||Jt!==U)&&(i.blendEquationSeparate(st[At],st[Jt]),v=At,U=Jt),(Lt!==I||ie!==H||Re!==N||Pe!==Y)&&(i.blendFuncSeparate(vt[Lt],vt[ie],vt[Re],vt[Pe]),I=Lt,H=ie,N=Re,Y=Pe),(Ke.equals(b)===!1||un!==P)&&(i.blendColor(Ke.r,Ke.g,Ke.b,un),b.copy(Ke),P=un),w=B,X=!1}function Xt(B,At){B.side===mn?Wt(i.CULL_FACE):Zt(i.CULL_FACE);let Lt=B.side===Sn;At&&(Lt=!Lt),Pt(Lt),B.blending===$s&&B.transparent===!1?ct(Gi):ct(B.blending,B.blendEquation,B.blendSrc,B.blendDst,B.blendEquationAlpha,B.blendSrcAlpha,B.blendDstAlpha,B.blendColor,B.blendAlpha,B.premultipliedAlpha),l.setFunc(B.depthFunc),l.setTest(B.depthTest),l.setMask(B.depthWrite),o.setMask(B.colorWrite);let ie=B.stencilWrite;c.setTest(ie),ie&&(c.setMask(B.stencilWriteMask),c.setFunc(B.stencilFunc,B.stencilRef,B.stencilFuncMask),c.setOp(B.stencilFail,B.stencilZFail,B.stencilZPass)),W(B.polygonOffset,B.polygonOffsetFactor,B.polygonOffsetUnits),B.alphaToCoverage===!0?Zt(i.SAMPLE_ALPHA_TO_COVERAGE):Wt(i.SAMPLE_ALPHA_TO_COVERAGE)}function Pt(B){rt!==B&&(B?i.frontFace(i.CW):i.frontFace(i.CCW),rt=B)}function T(B){B!==Sf?(Zt(i.CULL_FACE),B!==_t&&(B===th?i.cullFace(i.BACK):B===bf?i.cullFace(i.FRONT):i.cullFace(i.FRONT_AND_BACK))):Wt(i.CULL_FACE),_t=B}function S(B){B!==k&&(ut&&i.lineWidth(B),k=B)}function W(B,At,Lt){B?(Zt(i.POLYGON_OFFSET_FILL),(q!==At||j!==Lt)&&(i.polygonOffset(At,Lt),q=At,j=Lt)):Wt(i.POLYGON_OFFSET_FILL)}function gt(B){B?Zt(i.SCISSOR_TEST):Wt(i.SCISSOR_TEST)}function pt(B){B===void 0&&(B=i.TEXTURE0+et-1),lt!==B&&(i.activeTexture(B),lt=B)}function mt(B,At,Lt){Lt===void 0&&(lt===null?Lt=i.TEXTURE0+et-1:Lt=lt);let ie=Ut[Lt];ie===void 0&&(ie={type:void 0,texture:void 0},Ut[Lt]=ie),(ie.type!==B||ie.texture!==At)&&(lt!==Lt&&(i.activeTexture(Lt),lt=Lt),i.bindTexture(B,At||ne[B]),ie.type=B,ie.texture=At)}function Vt(){let B=Ut[lt];B!==void 0&&B.type!==void 0&&(i.bindTexture(B.type,null),B.type=void 0,B.texture=void 0)}function It(){try{i.compressedTexImage2D.apply(i,arguments)}catch(B){console.error("THREE.WebGLState:",B)}}function Tt(){try{i.compressedTexImage3D.apply(i,arguments)}catch(B){console.error("THREE.WebGLState:",B)}}function jt(){try{i.texSubImage2D.apply(i,arguments)}catch(B){console.error("THREE.WebGLState:",B)}}function he(){try{i.texSubImage3D.apply(i,arguments)}catch(B){console.error("THREE.WebGLState:",B)}}function ft(){try{i.compressedTexSubImage2D.apply(i,arguments)}catch(B){console.error("THREE.WebGLState:",B)}}function Me(){try{i.compressedTexSubImage3D.apply(i,arguments)}catch(B){console.error("THREE.WebGLState:",B)}}function xe(){try{i.texStorage2D.apply(i,arguments)}catch(B){console.error("THREE.WebGLState:",B)}}function Yt(){try{i.texStorage3D.apply(i,arguments)}catch(B){console.error("THREE.WebGLState:",B)}}function $t(){try{i.texImage2D.apply(i,arguments)}catch(B){console.error("THREE.WebGLState:",B)}}function Ht(){try{i.texImage3D.apply(i,arguments)}catch(B){console.error("THREE.WebGLState:",B)}}function re(B){Dt.equals(B)===!1&&(i.scissor(B.x,B.y,B.z,B.w),Dt.copy(B))}function Ee(B){Bt.equals(B)===!1&&(i.viewport(B.x,B.y,B.z,B.w),Bt.copy(B))}function Ve(B,At){let Lt=u.get(At);Lt===void 0&&(Lt=new WeakMap,u.set(At,Lt));let ie=Lt.get(B);ie===void 0&&(ie=i.getUniformBlockIndex(At,B.name),Lt.set(B,ie))}function Kt(B,At){let ie=u.get(At).get(B);h.get(At)!==ie&&(i.uniformBlockBinding(At,ie,B.__bindingPointIndex),h.set(At,ie))}function St(){i.disable(i.BLEND),i.disable(i.CULL_FACE),i.disable(i.DEPTH_TEST),i.disable(i.POLYGON_OFFSET_FILL),i.disable(i.SCISSOR_TEST),i.disable(i.STENCIL_TEST),i.disable(i.SAMPLE_ALPHA_TO_COVERAGE),i.blendEquation(i.FUNC_ADD),i.blendFunc(i.ONE,i.ZERO),i.blendFuncSeparate(i.ONE,i.ZERO,i.ONE,i.ZERO),i.blendColor(0,0,0,0),i.colorMask(!0,!0,!0,!0),i.clearColor(0,0,0,0),i.depthMask(!0),i.depthFunc(i.LESS),i.clearDepth(1),i.stencilMask(4294967295),i.stencilFunc(i.ALWAYS,0,4294967295),i.stencilOp(i.KEEP,i.KEEP,i.KEEP),i.clearStencil(0),i.cullFace(i.BACK),i.frontFace(i.CCW),i.polygonOffset(0,0),i.activeTexture(i.TEXTURE0),i.bindFramebuffer(i.FRAMEBUFFER,null),n===!0&&(i.bindFramebuffer(i.DRAW_FRAMEBUFFER,null),i.bindFramebuffer(i.READ_FRAMEBUFFER,null)),i.useProgram(null),i.lineWidth(1),i.scissor(0,0,i.canvas.width,i.canvas.height),i.viewport(0,0,i.canvas.width,i.canvas.height),d={},lt=null,Ut={},p={},x=new WeakMap,y=[],g=null,m=!1,w=null,v=null,I=null,H=null,U=null,N=null,Y=null,b=new ge(0,0,0),P=0,X=!1,rt=null,_t=null,k=null,q=null,j=null,Dt.set(0,0,i.canvas.width,i.canvas.height),Bt.set(0,0,i.canvas.width,i.canvas.height),o.reset(),l.reset(),c.reset()}return{buffers:{color:o,depth:l,stencil:c},enable:Zt,disable:Wt,bindFramebuffer:ae,drawBuffers:F,useProgram:Et,setBlending:ct,setMaterial:Xt,setFlipSided:Pt,setCullFace:T,setLineWidth:S,setPolygonOffset:W,setScissorTest:gt,activeTexture:pt,bindTexture:mt,unbindTexture:Vt,compressedTexImage2D:It,compressedTexImage3D:Tt,texImage2D:$t,texImage3D:Ht,updateUBOMapping:Ve,uniformBlockBinding:Kt,texStorage2D:xe,texStorage3D:Yt,texSubImage2D:jt,texSubImage3D:he,compressedTexSubImage2D:ft,compressedTexSubImage3D:Me,scissor:re,viewport:Ee,reset:St}}function x_(i,t,e,n,s,r,a){let o=s.isWebGL2,l=t.has("WEBGL_multisampled_render_to_texture")?t.get("WEBGL_multisampled_render_to_texture"):null,c=typeof navigator=="undefined"?!1:/OculusBrowser/g.test(navigator.userAgent),h=new WeakMap,u,d=new WeakMap,p=!1;try{p=typeof OffscreenCanvas!="undefined"&&new OffscreenCanvas(1,1).getContext("2d")!==null}catch{}function x(T,S){return p?new OffscreenCanvas(T,S):Lr("canvas")}function y(T,S,W,gt){let pt=1;if((T.width>gt||T.height>gt)&&(pt=gt/Math.max(T.width,T.height)),pt<1||S===!0)if(typeof HTMLImageElement!="undefined"&&T instanceof HTMLImageElement||typeof HTMLCanvasElement!="undefined"&&T instanceof HTMLCanvasElement||typeof ImageBitmap!="undefined"&&T instanceof ImageBitmap){let mt=S?Wo:Math.floor,Vt=mt(pt*T.width),It=mt(pt*T.height);u===void 0&&(u=x(Vt,It));let Tt=W?x(Vt,It):u;return Tt.width=Vt,Tt.height=It,Tt.getContext("2d").drawImage(T,0,0,Vt,It),console.warn("THREE.WebGLRenderer: Texture has been resized from ("+T.width+"x"+T.height+") to ("+Vt+"x"+It+")."),Tt}else return"data"in T&&console.warn("THREE.WebGLRenderer: Image in DataTexture is too big ("+T.width+"x"+T.height+")."),T;return T}function g(T){return wl(T.width)&&wl(T.height)}function m(T){return o?!1:T.wrapS!==Rn||T.wrapT!==Rn||T.minFilter!==An&&T.minFilter!==kn}function w(T,S){return T.generateMipmaps&&S&&T.minFilter!==An&&T.minFilter!==kn}function v(T){i.generateMipmap(T)}function I(T,S,W,gt,pt=!1){if(o===!1)return S;if(T!==null){if(i[T]!==void 0)return i[T];console.warn("THREE.WebGLRenderer: Attempt to use non-existing WebGL internal format '"+T+"'")}let mt=S;if(S===i.RED&&(W===i.FLOAT&&(mt=i.R32F),W===i.HALF_FLOAT&&(mt=i.R16F),W===i.UNSIGNED_BYTE&&(mt=i.R8)),S===i.RED_INTEGER&&(W===i.UNSIGNED_BYTE&&(mt=i.R8UI),W===i.UNSIGNED_SHORT&&(mt=i.R16UI),W===i.UNSIGNED_INT&&(mt=i.R32UI),W===i.BYTE&&(mt=i.R8I),W===i.SHORT&&(mt=i.R16I),W===i.INT&&(mt=i.R32I)),S===i.RG&&(W===i.FLOAT&&(mt=i.RG32F),W===i.HALF_FLOAT&&(mt=i.RG16F),W===i.UNSIGNED_BYTE&&(mt=i.RG8)),S===i.RGBA){let Vt=pt?Ho:Ue.getTransfer(gt);W===i.FLOAT&&(mt=i.RGBA32F),W===i.HALF_FLOAT&&(mt=i.RGBA16F),W===i.UNSIGNED_BYTE&&(mt=Vt===ke?i.SRGB8_ALPHA8:i.RGBA8),W===i.UNSIGNED_SHORT_4_4_4_4&&(mt=i.RGBA4),W===i.UNSIGNED_SHORT_5_5_5_1&&(mt=i.RGB5_A1)}return(mt===i.R16F||mt===i.R32F||mt===i.RG16F||mt===i.RG32F||mt===i.RGBA16F||mt===i.RGBA32F)&&t.get("EXT_color_buffer_float"),mt}function H(T,S,W){return w(T,W)===!0||T.isFramebufferTexture&&T.minFilter!==An&&T.minFilter!==kn?Math.log2(Math.max(S.width,S.height))+1:T.mipmaps!==void 0&&T.mipmaps.length>0?T.mipmaps.length:T.isCompressedTexture&&Array.isArray(T.image)?S.mipmaps.length:1}function U(T){return T===An||T===rh||T===za?i.NEAREST:i.LINEAR}function N(T){let S=T.target;S.removeEventListener("dispose",N),b(S),S.isVideoTexture&&h.delete(S)}function Y(T){let S=T.target;S.removeEventListener("dispose",Y),X(S)}function b(T){let S=n.get(T);if(S.__webglInit===void 0)return;let W=T.source,gt=d.get(W);if(gt){let pt=gt[S.__cacheKey];pt.usedTimes--,pt.usedTimes===0&&P(T),Object.keys(gt).length===0&&d.delete(W)}n.remove(T)}function P(T){let S=n.get(T);i.deleteTexture(S.__webglTexture);let W=T.source,gt=d.get(W);delete gt[S.__cacheKey],a.memory.textures--}function X(T){let S=T.texture,W=n.get(T),gt=n.get(S);if(gt.__webglTexture!==void 0&&(i.deleteTexture(gt.__webglTexture),a.memory.textures--),T.depthTexture&&T.depthTexture.dispose(),T.isWebGLCubeRenderTarget)for(let pt=0;pt<6;pt++){if(Array.isArray(W.__webglFramebuffer[pt]))for(let mt=0;mt<W.__webglFramebuffer[pt].length;mt++)i.deleteFramebuffer(W.__webglFramebuffer[pt][mt]);else i.deleteFramebuffer(W.__webglFramebuffer[pt]);W.__webglDepthbuffer&&i.deleteRenderbuffer(W.__webglDepthbuffer[pt])}else{if(Array.isArray(W.__webglFramebuffer))for(let pt=0;pt<W.__webglFramebuffer.length;pt++)i.deleteFramebuffer(W.__webglFramebuffer[pt]);else i.deleteFramebuffer(W.__webglFramebuffer);if(W.__webglDepthbuffer&&i.deleteRenderbuffer(W.__webglDepthbuffer),W.__webglMultisampledFramebuffer&&i.deleteFramebuffer(W.__webglMultisampledFramebuffer),W.__webglColorRenderbuffer)for(let pt=0;pt<W.__webglColorRenderbuffer.length;pt++)W.__webglColorRenderbuffer[pt]&&i.deleteRenderbuffer(W.__webglColorRenderbuffer[pt]);W.__webglDepthRenderbuffer&&i.deleteRenderbuffer(W.__webglDepthRenderbuffer)}if(T.isWebGLMultipleRenderTargets)for(let pt=0,mt=S.length;pt<mt;pt++){let Vt=n.get(S[pt]);Vt.__webglTexture&&(i.deleteTexture(Vt.__webglTexture),a.memory.textures--),n.remove(S[pt])}n.remove(S),n.remove(T)}let rt=0;function _t(){rt=0}function k(){let T=rt;return T>=s.maxTextures&&console.warn("THREE.WebGLTextures: Trying to use "+T+" texture units while this GPU supports only "+s.maxTextures),rt+=1,T}function q(T){let S=[];return S.push(T.wrapS),S.push(T.wrapT),S.push(T.wrapR||0),S.push(T.magFilter),S.push(T.minFilter),S.push(T.anisotropy),S.push(T.internalFormat),S.push(T.format),S.push(T.type),S.push(T.generateMipmaps),S.push(T.premultiplyAlpha),S.push(T.flipY),S.push(T.unpackAlignment),S.push(T.colorSpace),S.join()}function j(T,S){let W=n.get(T);if(T.isVideoTexture&&Xt(T),T.isRenderTargetTexture===!1&&T.version>0&&W.__version!==T.version){let gt=T.image;if(gt===null)console.warn("THREE.WebGLRenderer: Texture marked for update but no image data found.");else if(gt.complete===!1)console.warn("THREE.WebGLRenderer: Texture marked for update but image is incomplete");else{Dt(W,T,S);return}}e.bindTexture(i.TEXTURE_2D,W.__webglTexture,i.TEXTURE0+S)}function et(T,S){let W=n.get(T);if(T.version>0&&W.__version!==T.version){Dt(W,T,S);return}e.bindTexture(i.TEXTURE_2D_ARRAY,W.__webglTexture,i.TEXTURE0+S)}function ut(T,S){let W=n.get(T);if(T.version>0&&W.__version!==T.version){Dt(W,T,S);return}e.bindTexture(i.TEXTURE_3D,W.__webglTexture,i.TEXTURE0+S)}function tt(T,S){let W=n.get(T);if(T.version>0&&W.__version!==T.version){Bt(W,T,S);return}e.bindTexture(i.TEXTURE_CUBE_MAP,W.__webglTexture,i.TEXTURE0+S)}let at={[ps]:i.REPEAT,[Rn]:i.CLAMP_TO_EDGE,[bl]:i.MIRRORED_REPEAT},lt={[An]:i.NEAREST,[rh]:i.NEAREST_MIPMAP_NEAREST,[za]:i.NEAREST_MIPMAP_LINEAR,[kn]:i.LINEAR,[td]:i.LINEAR_MIPMAP_NEAREST,[Cr]:i.LINEAR_MIPMAP_LINEAR},Ut={[ud]:i.NEVER,[_d]:i.ALWAYS,[fd]:i.LESS,[Yu]:i.LEQUAL,[dd]:i.EQUAL,[gd]:i.GEQUAL,[pd]:i.GREATER,[md]:i.NOTEQUAL};function nt(T,S,W){if(W?(i.texParameteri(T,i.TEXTURE_WRAP_S,at[S.wrapS]),i.texParameteri(T,i.TEXTURE_WRAP_T,at[S.wrapT]),(T===i.TEXTURE_3D||T===i.TEXTURE_2D_ARRAY)&&i.texParameteri(T,i.TEXTURE_WRAP_R,at[S.wrapR]),i.texParameteri(T,i.TEXTURE_MAG_FILTER,lt[S.magFilter]),i.texParameteri(T,i.TEXTURE_MIN_FILTER,lt[S.minFilter])):(i.texParameteri(T,i.TEXTURE_WRAP_S,i.CLAMP_TO_EDGE),i.texParameteri(T,i.TEXTURE_WRAP_T,i.CLAMP_TO_EDGE),(T===i.TEXTURE_3D||T===i.TEXTURE_2D_ARRAY)&&i.texParameteri(T,i.TEXTURE_WRAP_R,i.CLAMP_TO_EDGE),(S.wrapS!==Rn||S.wrapT!==Rn)&&console.warn("THREE.WebGLRenderer: Texture is not power of two. Texture.wrapS and Texture.wrapT should be set to THREE.ClampToEdgeWrapping."),i.texParameteri(T,i.TEXTURE_MAG_FILTER,U(S.magFilter)),i.texParameteri(T,i.TEXTURE_MIN_FILTER,U(S.minFilter)),S.minFilter!==An&&S.minFilter!==kn&&console.warn("THREE.WebGLRenderer: Texture is not power of two. Texture.minFilter should be set to THREE.NearestFilter or THREE.LinearFilter.")),S.compareFunction&&(i.texParameteri(T,i.TEXTURE_COMPARE_MODE,i.COMPARE_REF_TO_TEXTURE),i.texParameteri(T,i.TEXTURE_COMPARE_FUNC,Ut[S.compareFunction])),t.has("EXT_texture_filter_anisotropic")===!0){let gt=t.get("EXT_texture_filter_anisotropic");if(S.magFilter===An||S.minFilter!==za&&S.minFilter!==Cr||S.type===Vi&&t.has("OES_texture_float_linear")===!1||o===!1&&S.type===Pr&&t.has("OES_texture_half_float_linear")===!1)return;(S.anisotropy>1||n.get(S).__currentAnisotropy)&&(i.texParameterf(T,gt.TEXTURE_MAX_ANISOTROPY_EXT,Math.min(S.anisotropy,s.getMaxAnisotropy())),n.get(S).__currentAnisotropy=S.anisotropy)}}function ht(T,S){let W=!1;T.__webglInit===void 0&&(T.__webglInit=!0,S.addEventListener("dispose",N));let gt=S.source,pt=d.get(gt);pt===void 0&&(pt={},d.set(gt,pt));let mt=q(S);if(mt!==T.__cacheKey){pt[mt]===void 0&&(pt[mt]={texture:i.createTexture(),usedTimes:0},a.memory.textures++,W=!0),pt[mt].usedTimes++;let Vt=pt[T.__cacheKey];Vt!==void 0&&(pt[T.__cacheKey].usedTimes--,Vt.usedTimes===0&&P(S)),T.__cacheKey=mt,T.__webglTexture=pt[mt].texture}return W}function Dt(T,S,W){let gt=i.TEXTURE_2D;(S.isDataArrayTexture||S.isCompressedArrayTexture)&&(gt=i.TEXTURE_2D_ARRAY),S.isData3DTexture&&(gt=i.TEXTURE_3D);let pt=ht(T,S),mt=S.source;e.bindTexture(gt,T.__webglTexture,i.TEXTURE0+W);let Vt=n.get(mt);if(mt.version!==Vt.__version||pt===!0){e.activeTexture(i.TEXTURE0+W);let It=Ue.getPrimaries(Ue.workingColorSpace),Tt=S.colorSpace===Vn?null:Ue.getPrimaries(S.colorSpace),jt=S.colorSpace===Vn||It===Tt?i.NONE:i.BROWSER_DEFAULT_WEBGL;i.pixelStorei(i.UNPACK_FLIP_Y_WEBGL,S.flipY),i.pixelStorei(i.UNPACK_PREMULTIPLY_ALPHA_WEBGL,S.premultiplyAlpha),i.pixelStorei(i.UNPACK_ALIGNMENT,S.unpackAlignment),i.pixelStorei(i.UNPACK_COLORSPACE_CONVERSION_WEBGL,jt);let he=m(S)&&g(S.image)===!1,ft=y(S.image,he,!1,s.maxTextureSize);ft=Pt(S,ft);let Me=g(ft)||o,xe=r.convert(S.format,S.colorSpace),Yt=r.convert(S.type),$t=I(S.internalFormat,xe,Yt,S.colorSpace,S.isVideoTexture);nt(gt,S,Me);let Ht,re=S.mipmaps,Ee=o&&S.isVideoTexture!==!0&&$t!==Gu,Ve=Vt.__version===void 0||pt===!0,Kt=H(S,ft,Me);if(S.isDepthTexture)$t=i.DEPTH_COMPONENT,o?S.type===Vi?$t=i.DEPTH_COMPONENT32F:S.type===ki?$t=i.DEPTH_COMPONENT24:S.type===us?$t=i.DEPTH24_STENCIL8:$t=i.DEPTH_COMPONENT16:S.type===Vi&&console.error("WebGLRenderer: Floating point depth texture requires WebGL2."),S.format===fs&&$t===i.DEPTH_COMPONENT&&S.type!==fc&&S.type!==ki&&(console.warn("THREE.WebGLRenderer: Use UnsignedShortType or UnsignedIntType for DepthFormat DepthTexture."),S.type=ki,Yt=r.convert(S.type)),S.format===er&&$t===i.DEPTH_COMPONENT&&($t=i.DEPTH_STENCIL,S.type!==us&&(console.warn("THREE.WebGLRenderer: Use UnsignedInt248Type for DepthStencilFormat DepthTexture."),S.type=us,Yt=r.convert(S.type))),Ve&&(Ee?e.texStorage2D(i.TEXTURE_2D,1,$t,ft.width,ft.height):e.texImage2D(i.TEXTURE_2D,0,$t,ft.width,ft.height,0,xe,Yt,null));else if(S.isDataTexture)if(re.length>0&&Me){Ee&&Ve&&e.texStorage2D(i.TEXTURE_2D,Kt,$t,re[0].width,re[0].height);for(let St=0,B=re.length;St<B;St++)Ht=re[St],Ee?e.texSubImage2D(i.TEXTURE_2D,St,0,0,Ht.width,Ht.height,xe,Yt,Ht.data):e.texImage2D(i.TEXTURE_2D,St,$t,Ht.width,Ht.height,0,xe,Yt,Ht.data);S.generateMipmaps=!1}else Ee?(Ve&&e.texStorage2D(i.TEXTURE_2D,Kt,$t,ft.width,ft.height),e.texSubImage2D(i.TEXTURE_2D,0,0,0,ft.width,ft.height,xe,Yt,ft.data)):e.texImage2D(i.TEXTURE_2D,0,$t,ft.width,ft.height,0,xe,Yt,ft.data);else if(S.isCompressedTexture)if(S.isCompressedArrayTexture){Ee&&Ve&&e.texStorage3D(i.TEXTURE_2D_ARRAY,Kt,$t,re[0].width,re[0].height,ft.depth);for(let St=0,B=re.length;St<B;St++)Ht=re[St],S.format!==Qn?xe!==null?Ee?e.compressedTexSubImage3D(i.TEXTURE_2D_ARRAY,St,0,0,0,Ht.width,Ht.height,ft.depth,xe,Ht.data,0,0):e.compressedTexImage3D(i.TEXTURE_2D_ARRAY,St,$t,Ht.width,Ht.height,ft.depth,0,Ht.data,0,0):console.warn("THREE.WebGLRenderer: Attempt to load unsupported compressed texture format in .uploadTexture()"):Ee?e.texSubImage3D(i.TEXTURE_2D_ARRAY,St,0,0,0,Ht.width,Ht.height,ft.depth,xe,Yt,Ht.data):e.texImage3D(i.TEXTURE_2D_ARRAY,St,$t,Ht.width,Ht.height,ft.depth,0,xe,Yt,Ht.data)}else{Ee&&Ve&&e.texStorage2D(i.TEXTURE_2D,Kt,$t,re[0].width,re[0].height);for(let St=0,B=re.length;St<B;St++)Ht=re[St],S.format!==Qn?xe!==null?Ee?e.compressedTexSubImage2D(i.TEXTURE_2D,St,0,0,Ht.width,Ht.height,xe,Ht.data):e.compressedTexImage2D(i.TEXTURE_2D,St,$t,Ht.width,Ht.height,0,Ht.data):console.warn("THREE.WebGLRenderer: Attempt to load unsupported compressed texture format in .uploadTexture()"):Ee?e.texSubImage2D(i.TEXTURE_2D,St,0,0,Ht.width,Ht.height,xe,Yt,Ht.data):e.texImage2D(i.TEXTURE_2D,St,$t,Ht.width,Ht.height,0,xe,Yt,Ht.data)}else if(S.isDataArrayTexture)Ee?(Ve&&e.texStorage3D(i.TEXTURE_2D_ARRAY,Kt,$t,ft.width,ft.height,ft.depth),e.texSubImage3D(i.TEXTURE_2D_ARRAY,0,0,0,0,ft.width,ft.height,ft.depth,xe,Yt,ft.data)):e.texImage3D(i.TEXTURE_2D_ARRAY,0,$t,ft.width,ft.height,ft.depth,0,xe,Yt,ft.data);else if(S.isData3DTexture)Ee?(Ve&&e.texStorage3D(i.TEXTURE_3D,Kt,$t,ft.width,ft.height,ft.depth),e.texSubImage3D(i.TEXTURE_3D,0,0,0,0,ft.width,ft.height,ft.depth,xe,Yt,ft.data)):e.texImage3D(i.TEXTURE_3D,0,$t,ft.width,ft.height,ft.depth,0,xe,Yt,ft.data);else if(S.isFramebufferTexture){if(Ve)if(Ee)e.texStorage2D(i.TEXTURE_2D,Kt,$t,ft.width,ft.height);else{let St=ft.width,B=ft.height;for(let At=0;At<Kt;At++)e.texImage2D(i.TEXTURE_2D,At,$t,St,B,0,xe,Yt,null),St>>=1,B>>=1}}else if(re.length>0&&Me){Ee&&Ve&&e.texStorage2D(i.TEXTURE_2D,Kt,$t,re[0].width,re[0].height);for(let St=0,B=re.length;St<B;St++)Ht=re[St],Ee?e.texSubImage2D(i.TEXTURE_2D,St,0,0,xe,Yt,Ht):e.texImage2D(i.TEXTURE_2D,St,$t,xe,Yt,Ht);S.generateMipmaps=!1}else Ee?(Ve&&e.texStorage2D(i.TEXTURE_2D,Kt,$t,ft.width,ft.height),e.texSubImage2D(i.TEXTURE_2D,0,0,0,xe,Yt,ft)):e.texImage2D(i.TEXTURE_2D,0,$t,xe,Yt,ft);w(S,Me)&&v(gt),Vt.__version=mt.version,S.onUpdate&&S.onUpdate(S)}T.__version=S.version}function Bt(T,S,W){if(S.image.length!==6)return;let gt=ht(T,S),pt=S.source;e.bindTexture(i.TEXTURE_CUBE_MAP,T.__webglTexture,i.TEXTURE0+W);let mt=n.get(pt);if(pt.version!==mt.__version||gt===!0){e.activeTexture(i.TEXTURE0+W);let Vt=Ue.getPrimaries(Ue.workingColorSpace),It=S.colorSpace===Vn?null:Ue.getPrimaries(S.colorSpace),Tt=S.colorSpace===Vn||Vt===It?i.NONE:i.BROWSER_DEFAULT_WEBGL;i.pixelStorei(i.UNPACK_FLIP_Y_WEBGL,S.flipY),i.pixelStorei(i.UNPACK_PREMULTIPLY_ALPHA_WEBGL,S.premultiplyAlpha),i.pixelStorei(i.UNPACK_ALIGNMENT,S.unpackAlignment),i.pixelStorei(i.UNPACK_COLORSPACE_CONVERSION_WEBGL,Tt);let jt=S.isCompressedTexture||S.image[0].isCompressedTexture,he=S.image[0]&&S.image[0].isDataTexture,ft=[];for(let St=0;St<6;St++)!jt&&!he?ft[St]=y(S.image[St],!1,!0,s.maxCubemapSize):ft[St]=he?S.image[St].image:S.image[St],ft[St]=Pt(S,ft[St]);let Me=ft[0],xe=g(Me)||o,Yt=r.convert(S.format,S.colorSpace),$t=r.convert(S.type),Ht=I(S.internalFormat,Yt,$t,S.colorSpace),re=o&&S.isVideoTexture!==!0,Ee=mt.__version===void 0||gt===!0,Ve=H(S,Me,xe);nt(i.TEXTURE_CUBE_MAP,S,xe);let Kt;if(jt){re&&Ee&&e.texStorage2D(i.TEXTURE_CUBE_MAP,Ve,Ht,Me.width,Me.height);for(let St=0;St<6;St++){Kt=ft[St].mipmaps;for(let B=0;B<Kt.length;B++){let At=Kt[B];S.format!==Qn?Yt!==null?re?e.compressedTexSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+St,B,0,0,At.width,At.height,Yt,At.data):e.compressedTexImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+St,B,Ht,At.width,At.height,0,At.data):console.warn("THREE.WebGLRenderer: Attempt to load unsupported compressed texture format in .setTextureCube()"):re?e.texSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+St,B,0,0,At.width,At.height,Yt,$t,At.data):e.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+St,B,Ht,At.width,At.height,0,Yt,$t,At.data)}}}else{Kt=S.mipmaps,re&&Ee&&(Kt.length>0&&Ve++,e.texStorage2D(i.TEXTURE_CUBE_MAP,Ve,Ht,ft[0].width,ft[0].height));for(let St=0;St<6;St++)if(he){re?e.texSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+St,0,0,0,ft[St].width,ft[St].height,Yt,$t,ft[St].data):e.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+St,0,Ht,ft[St].width,ft[St].height,0,Yt,$t,ft[St].data);for(let B=0;B<Kt.length;B++){let Lt=Kt[B].image[St].image;re?e.texSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+St,B+1,0,0,Lt.width,Lt.height,Yt,$t,Lt.data):e.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+St,B+1,Ht,Lt.width,Lt.height,0,Yt,$t,Lt.data)}}else{re?e.texSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+St,0,0,0,Yt,$t,ft[St]):e.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+St,0,Ht,Yt,$t,ft[St]);for(let B=0;B<Kt.length;B++){let At=Kt[B];re?e.texSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+St,B+1,0,0,Yt,$t,At.image[St]):e.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+St,B+1,Ht,Yt,$t,At.image[St])}}}w(S,xe)&&v(i.TEXTURE_CUBE_MAP),mt.__version=pt.version,S.onUpdate&&S.onUpdate(S)}T.__version=S.version}function zt(T,S,W,gt,pt,mt){let Vt=r.convert(W.format,W.colorSpace),It=r.convert(W.type),Tt=I(W.internalFormat,Vt,It,W.colorSpace);if(!n.get(S).__hasExternalTextures){let he=Math.max(1,S.width>>mt),ft=Math.max(1,S.height>>mt);pt===i.TEXTURE_3D||pt===i.TEXTURE_2D_ARRAY?e.texImage3D(pt,mt,Tt,he,ft,S.depth,0,Vt,It,null):e.texImage2D(pt,mt,Tt,he,ft,0,Vt,It,null)}e.bindFramebuffer(i.FRAMEBUFFER,T),ct(S)?l.framebufferTexture2DMultisampleEXT(i.FRAMEBUFFER,gt,pt,n.get(W).__webglTexture,0,vt(S)):(pt===i.TEXTURE_2D||pt>=i.TEXTURE_CUBE_MAP_POSITIVE_X&&pt<=i.TEXTURE_CUBE_MAP_NEGATIVE_Z)&&i.framebufferTexture2D(i.FRAMEBUFFER,gt,pt,n.get(W).__webglTexture,mt),e.bindFramebuffer(i.FRAMEBUFFER,null)}function ne(T,S,W){if(i.bindRenderbuffer(i.RENDERBUFFER,T),S.depthBuffer&&!S.stencilBuffer){let gt=o===!0?i.DEPTH_COMPONENT24:i.DEPTH_COMPONENT16;if(W||ct(S)){let pt=S.depthTexture;pt&&pt.isDepthTexture&&(pt.type===Vi?gt=i.DEPTH_COMPONENT32F:pt.type===ki&&(gt=i.DEPTH_COMPONENT24));let mt=vt(S);ct(S)?l.renderbufferStorageMultisampleEXT(i.RENDERBUFFER,mt,gt,S.width,S.height):i.renderbufferStorageMultisample(i.RENDERBUFFER,mt,gt,S.width,S.height)}else i.renderbufferStorage(i.RENDERBUFFER,gt,S.width,S.height);i.framebufferRenderbuffer(i.FRAMEBUFFER,i.DEPTH_ATTACHMENT,i.RENDERBUFFER,T)}else if(S.depthBuffer&&S.stencilBuffer){let gt=vt(S);W&&ct(S)===!1?i.renderbufferStorageMultisample(i.RENDERBUFFER,gt,i.DEPTH24_STENCIL8,S.width,S.height):ct(S)?l.renderbufferStorageMultisampleEXT(i.RENDERBUFFER,gt,i.DEPTH24_STENCIL8,S.width,S.height):i.renderbufferStorage(i.RENDERBUFFER,i.DEPTH_STENCIL,S.width,S.height),i.framebufferRenderbuffer(i.FRAMEBUFFER,i.DEPTH_STENCIL_ATTACHMENT,i.RENDERBUFFER,T)}else{let gt=S.isWebGLMultipleRenderTargets===!0?S.texture:[S.texture];for(let pt=0;pt<gt.length;pt++){let mt=gt[pt],Vt=r.convert(mt.format,mt.colorSpace),It=r.convert(mt.type),Tt=I(mt.internalFormat,Vt,It,mt.colorSpace),jt=vt(S);W&&ct(S)===!1?i.renderbufferStorageMultisample(i.RENDERBUFFER,jt,Tt,S.width,S.height):ct(S)?l.renderbufferStorageMultisampleEXT(i.RENDERBUFFER,jt,Tt,S.width,S.height):i.renderbufferStorage(i.RENDERBUFFER,Tt,S.width,S.height)}}i.bindRenderbuffer(i.RENDERBUFFER,null)}function Zt(T,S){if(S&&S.isWebGLCubeRenderTarget)throw new Error("Depth Texture with cube render targets is not supported");if(e.bindFramebuffer(i.FRAMEBUFFER,T),!(S.depthTexture&&S.depthTexture.isDepthTexture))throw new Error("renderTarget.depthTexture must be an instance of THREE.DepthTexture");(!n.get(S.depthTexture).__webglTexture||S.depthTexture.image.width!==S.width||S.depthTexture.image.height!==S.height)&&(S.depthTexture.image.width=S.width,S.depthTexture.image.height=S.height,S.depthTexture.needsUpdate=!0),j(S.depthTexture,0);let gt=n.get(S.depthTexture).__webglTexture,pt=vt(S);if(S.depthTexture.format===fs)ct(S)?l.framebufferTexture2DMultisampleEXT(i.FRAMEBUFFER,i.DEPTH_ATTACHMENT,i.TEXTURE_2D,gt,0,pt):i.framebufferTexture2D(i.FRAMEBUFFER,i.DEPTH_ATTACHMENT,i.TEXTURE_2D,gt,0);else if(S.depthTexture.format===er)ct(S)?l.framebufferTexture2DMultisampleEXT(i.FRAMEBUFFER,i.DEPTH_STENCIL_ATTACHMENT,i.TEXTURE_2D,gt,0,pt):i.framebufferTexture2D(i.FRAMEBUFFER,i.DEPTH_STENCIL_ATTACHMENT,i.TEXTURE_2D,gt,0);else throw new Error("Unknown depthTexture format")}function Wt(T){let S=n.get(T),W=T.isWebGLCubeRenderTarget===!0;if(T.depthTexture&&!S.__autoAllocateDepthBuffer){if(W)throw new Error("target.depthTexture not supported in Cube render targets");Zt(S.__webglFramebuffer,T)}else if(W){S.__webglDepthbuffer=[];for(let gt=0;gt<6;gt++)e.bindFramebuffer(i.FRAMEBUFFER,S.__webglFramebuffer[gt]),S.__webglDepthbuffer[gt]=i.createRenderbuffer(),ne(S.__webglDepthbuffer[gt],T,!1)}else e.bindFramebuffer(i.FRAMEBUFFER,S.__webglFramebuffer),S.__webglDepthbuffer=i.createRenderbuffer(),ne(S.__webglDepthbuffer,T,!1);e.bindFramebuffer(i.FRAMEBUFFER,null)}function ae(T,S,W){let gt=n.get(T);S!==void 0&&zt(gt.__webglFramebuffer,T,T.texture,i.COLOR_ATTACHMENT0,i.TEXTURE_2D,0),W!==void 0&&Wt(T)}function F(T){let S=T.texture,W=n.get(T),gt=n.get(S);T.addEventListener("dispose",Y),T.isWebGLMultipleRenderTargets!==!0&&(gt.__webglTexture===void 0&&(gt.__webglTexture=i.createTexture()),gt.__version=S.version,a.memory.textures++);let pt=T.isWebGLCubeRenderTarget===!0,mt=T.isWebGLMultipleRenderTargets===!0,Vt=g(T)||o;if(pt){W.__webglFramebuffer=[];for(let It=0;It<6;It++)if(o&&S.mipmaps&&S.mipmaps.length>0){W.__webglFramebuffer[It]=[];for(let Tt=0;Tt<S.mipmaps.length;Tt++)W.__webglFramebuffer[It][Tt]=i.createFramebuffer()}else W.__webglFramebuffer[It]=i.createFramebuffer()}else{if(o&&S.mipmaps&&S.mipmaps.length>0){W.__webglFramebuffer=[];for(let It=0;It<S.mipmaps.length;It++)W.__webglFramebuffer[It]=i.createFramebuffer()}else W.__webglFramebuffer=i.createFramebuffer();if(mt)if(s.drawBuffers){let It=T.texture;for(let Tt=0,jt=It.length;Tt<jt;Tt++){let he=n.get(It[Tt]);he.__webglTexture===void 0&&(he.__webglTexture=i.createTexture(),a.memory.textures++)}}else console.warn("THREE.WebGLRenderer: WebGLMultipleRenderTargets can only be used with WebGL2 or WEBGL_draw_buffers extension.");if(o&&T.samples>0&&ct(T)===!1){let It=mt?S:[S];W.__webglMultisampledFramebuffer=i.createFramebuffer(),W.__webglColorRenderbuffer=[],e.bindFramebuffer(i.FRAMEBUFFER,W.__webglMultisampledFramebuffer);for(let Tt=0;Tt<It.length;Tt++){let jt=It[Tt];W.__webglColorRenderbuffer[Tt]=i.createRenderbuffer(),i.bindRenderbuffer(i.RENDERBUFFER,W.__webglColorRenderbuffer[Tt]);let he=r.convert(jt.format,jt.colorSpace),ft=r.convert(jt.type),Me=I(jt.internalFormat,he,ft,jt.colorSpace,T.isXRRenderTarget===!0),xe=vt(T);i.renderbufferStorageMultisample(i.RENDERBUFFER,xe,Me,T.width,T.height),i.framebufferRenderbuffer(i.FRAMEBUFFER,i.COLOR_ATTACHMENT0+Tt,i.RENDERBUFFER,W.__webglColorRenderbuffer[Tt])}i.bindRenderbuffer(i.RENDERBUFFER,null),T.depthBuffer&&(W.__webglDepthRenderbuffer=i.createRenderbuffer(),ne(W.__webglDepthRenderbuffer,T,!0)),e.bindFramebuffer(i.FRAMEBUFFER,null)}}if(pt){e.bindTexture(i.TEXTURE_CUBE_MAP,gt.__webglTexture),nt(i.TEXTURE_CUBE_MAP,S,Vt);for(let It=0;It<6;It++)if(o&&S.mipmaps&&S.mipmaps.length>0)for(let Tt=0;Tt<S.mipmaps.length;Tt++)zt(W.__webglFramebuffer[It][Tt],T,S,i.COLOR_ATTACHMENT0,i.TEXTURE_CUBE_MAP_POSITIVE_X+It,Tt);else zt(W.__webglFramebuffer[It],T,S,i.COLOR_ATTACHMENT0,i.TEXTURE_CUBE_MAP_POSITIVE_X+It,0);w(S,Vt)&&v(i.TEXTURE_CUBE_MAP),e.unbindTexture()}else if(mt){let It=T.texture;for(let Tt=0,jt=It.length;Tt<jt;Tt++){let he=It[Tt],ft=n.get(he);e.bindTexture(i.TEXTURE_2D,ft.__webglTexture),nt(i.TEXTURE_2D,he,Vt),zt(W.__webglFramebuffer,T,he,i.COLOR_ATTACHMENT0+Tt,i.TEXTURE_2D,0),w(he,Vt)&&v(i.TEXTURE_2D)}e.unbindTexture()}else{let It=i.TEXTURE_2D;if((T.isWebGL3DRenderTarget||T.isWebGLArrayRenderTarget)&&(o?It=T.isWebGL3DRenderTarget?i.TEXTURE_3D:i.TEXTURE_2D_ARRAY:console.error("THREE.WebGLTextures: THREE.Data3DTexture and THREE.DataArrayTexture only supported with WebGL2.")),e.bindTexture(It,gt.__webglTexture),nt(It,S,Vt),o&&S.mipmaps&&S.mipmaps.length>0)for(let Tt=0;Tt<S.mipmaps.length;Tt++)zt(W.__webglFramebuffer[Tt],T,S,i.COLOR_ATTACHMENT0,It,Tt);else zt(W.__webglFramebuffer,T,S,i.COLOR_ATTACHMENT0,It,0);w(S,Vt)&&v(It),e.unbindTexture()}T.depthBuffer&&Wt(T)}function Et(T){let S=g(T)||o,W=T.isWebGLMultipleRenderTargets===!0?T.texture:[T.texture];for(let gt=0,pt=W.length;gt<pt;gt++){let mt=W[gt];if(w(mt,S)){let Vt=T.isWebGLCubeRenderTarget?i.TEXTURE_CUBE_MAP:i.TEXTURE_2D,It=n.get(mt).__webglTexture;e.bindTexture(Vt,It),v(Vt),e.unbindTexture()}}}function st(T){if(o&&T.samples>0&&ct(T)===!1){let S=T.isWebGLMultipleRenderTargets?T.texture:[T.texture],W=T.width,gt=T.height,pt=i.COLOR_BUFFER_BIT,mt=[],Vt=T.stencilBuffer?i.DEPTH_STENCIL_ATTACHMENT:i.DEPTH_ATTACHMENT,It=n.get(T),Tt=T.isWebGLMultipleRenderTargets===!0;if(Tt)for(let jt=0;jt<S.length;jt++)e.bindFramebuffer(i.FRAMEBUFFER,It.__webglMultisampledFramebuffer),i.framebufferRenderbuffer(i.FRAMEBUFFER,i.COLOR_ATTACHMENT0+jt,i.RENDERBUFFER,null),e.bindFramebuffer(i.FRAMEBUFFER,It.__webglFramebuffer),i.framebufferTexture2D(i.DRAW_FRAMEBUFFER,i.COLOR_ATTACHMENT0+jt,i.TEXTURE_2D,null,0);e.bindFramebuffer(i.READ_FRAMEBUFFER,It.__webglMultisampledFramebuffer),e.bindFramebuffer(i.DRAW_FRAMEBUFFER,It.__webglFramebuffer);for(let jt=0;jt<S.length;jt++){mt.push(i.COLOR_ATTACHMENT0+jt),T.depthBuffer&&mt.push(Vt);let he=It.__ignoreDepthValues!==void 0?It.__ignoreDepthValues:!1;if(he===!1&&(T.depthBuffer&&(pt|=i.DEPTH_BUFFER_BIT),T.stencilBuffer&&(pt|=i.STENCIL_BUFFER_BIT)),Tt&&i.framebufferRenderbuffer(i.READ_FRAMEBUFFER,i.COLOR_ATTACHMENT0,i.RENDERBUFFER,It.__webglColorRenderbuffer[jt]),he===!0&&(i.invalidateFramebuffer(i.READ_FRAMEBUFFER,[Vt]),i.invalidateFramebuffer(i.DRAW_FRAMEBUFFER,[Vt])),Tt){let ft=n.get(S[jt]).__webglTexture;i.framebufferTexture2D(i.DRAW_FRAMEBUFFER,i.COLOR_ATTACHMENT0,i.TEXTURE_2D,ft,0)}i.blitFramebuffer(0,0,W,gt,0,0,W,gt,pt,i.NEAREST),c&&i.invalidateFramebuffer(i.READ_FRAMEBUFFER,mt)}if(e.bindFramebuffer(i.READ_FRAMEBUFFER,null),e.bindFramebuffer(i.DRAW_FRAMEBUFFER,null),Tt)for(let jt=0;jt<S.length;jt++){e.bindFramebuffer(i.FRAMEBUFFER,It.__webglMultisampledFramebuffer),i.framebufferRenderbuffer(i.FRAMEBUFFER,i.COLOR_ATTACHMENT0+jt,i.RENDERBUFFER,It.__webglColorRenderbuffer[jt]);let he=n.get(S[jt]).__webglTexture;e.bindFramebuffer(i.FRAMEBUFFER,It.__webglFramebuffer),i.framebufferTexture2D(i.DRAW_FRAMEBUFFER,i.COLOR_ATTACHMENT0+jt,i.TEXTURE_2D,he,0)}e.bindFramebuffer(i.DRAW_FRAMEBUFFER,It.__webglMultisampledFramebuffer)}}function vt(T){return Math.min(s.maxSamples,T.samples)}function ct(T){let S=n.get(T);return o&&T.samples>0&&t.has("WEBGL_multisampled_render_to_texture")===!0&&S.__useRenderToTexture!==!1}function Xt(T){let S=a.render.frame;h.get(T)!==S&&(h.set(T,S),T.update())}function Pt(T,S){let W=T.colorSpace,gt=T.format,pt=T.type;return T.isCompressedTexture===!0||T.isVideoTexture===!0||T.format===El||W!==Ai&&W!==Vn&&(Ue.getTransfer(W)===ke?o===!1?t.has("EXT_sRGB")===!0&&gt===Qn?(T.format=El,T.minFilter=kn,T.generateMipmaps=!1):S=Xo.sRGBToLinear(S):(gt!==Qn||pt!==Xi)&&console.warn("THREE.WebGLTextures: sRGB encoded textures have to use RGBAFormat and UnsignedByteType."):console.error("THREE.WebGLTextures: Unsupported texture color space:",W)),S}this.allocateTextureUnit=k,this.resetTextureUnits=_t,this.setTexture2D=j,this.setTexture2DArray=et,this.setTexture3D=ut,this.setTextureCube=tt,this.rebindTextures=ae,this.setupRenderTarget=F,this.updateRenderTargetMipmap=Et,this.updateMultisampleRenderTarget=st,this.setupDepthRenderbuffer=Wt,this.setupFrameBufferTexture=zt,this.useMultisampledRTT=ct}function v_(i,t,e){let n=e.isWebGL2;function s(r,a=Vn){let o,l=Ue.getTransfer(a);if(r===Xi)return i.UNSIGNED_BYTE;if(r===Bu)return i.UNSIGNED_SHORT_4_4_4_4;if(r===zu)return i.UNSIGNED_SHORT_5_5_5_1;if(r===ed)return i.BYTE;if(r===nd)return i.SHORT;if(r===fc)return i.UNSIGNED_SHORT;if(r===Ou)return i.INT;if(r===ki)return i.UNSIGNED_INT;if(r===Vi)return i.FLOAT;if(r===Pr)return n?i.HALF_FLOAT:(o=t.get("OES_texture_half_float"),o!==null?o.HALF_FLOAT_OES:null);if(r===id)return i.ALPHA;if(r===Qn)return i.RGBA;if(r===sd)return i.LUMINANCE;if(r===rd)return i.LUMINANCE_ALPHA;if(r===fs)return i.DEPTH_COMPONENT;if(r===er)return i.DEPTH_STENCIL;if(r===El)return o=t.get("EXT_sRGB"),o!==null?o.SRGB_ALPHA_EXT:null;if(r===od)return i.RED;if(r===Hu)return i.RED_INTEGER;if(r===ad)return i.RG;if(r===ku)return i.RG_INTEGER;if(r===Vu)return i.RGBA_INTEGER;if(r===Ha||r===ka||r===Va||r===Ga)if(l===ke)if(o=t.get("WEBGL_compressed_texture_s3tc_srgb"),o!==null){if(r===Ha)return o.COMPRESSED_SRGB_S3TC_DXT1_EXT;if(r===ka)return o.COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT;if(r===Va)return o.COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT;if(r===Ga)return o.COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT}else return null;else if(o=t.get("WEBGL_compressed_texture_s3tc"),o!==null){if(r===Ha)return o.COMPRESSED_RGB_S3TC_DXT1_EXT;if(r===ka)return o.COMPRESSED_RGBA_S3TC_DXT1_EXT;if(r===Va)return o.COMPRESSED_RGBA_S3TC_DXT3_EXT;if(r===Ga)return o.COMPRESSED_RGBA_S3TC_DXT5_EXT}else return null;if(r===oh||r===ah||r===lh||r===ch)if(o=t.get("WEBGL_compressed_texture_pvrtc"),o!==null){if(r===oh)return o.COMPRESSED_RGB_PVRTC_4BPPV1_IMG;if(r===ah)return o.COMPRESSED_RGB_PVRTC_2BPPV1_IMG;if(r===lh)return o.COMPRESSED_RGBA_PVRTC_4BPPV1_IMG;if(r===ch)return o.COMPRESSED_RGBA_PVRTC_2BPPV1_IMG}else return null;if(r===Gu)return o=t.get("WEBGL_compressed_texture_etc1"),o!==null?o.COMPRESSED_RGB_ETC1_WEBGL:null;if(r===hh||r===uh)if(o=t.get("WEBGL_compressed_texture_etc"),o!==null){if(r===hh)return l===ke?o.COMPRESSED_SRGB8_ETC2:o.COMPRESSED_RGB8_ETC2;if(r===uh)return l===ke?o.COMPRESSED_SRGB8_ALPHA8_ETC2_EAC:o.COMPRESSED_RGBA8_ETC2_EAC}else return null;if(r===fh||r===dh||r===ph||r===mh||r===gh||r===_h||r===xh||r===vh||r===yh||r===Mh||r===Sh||r===bh||r===Eh||r===wh)if(o=t.get("WEBGL_compressed_texture_astc"),o!==null){if(r===fh)return l===ke?o.COMPRESSED_SRGB8_ALPHA8_ASTC_4x4_KHR:o.COMPRESSED_RGBA_ASTC_4x4_KHR;if(r===dh)return l===ke?o.COMPRESSED_SRGB8_ALPHA8_ASTC_5x4_KHR:o.COMPRESSED_RGBA_ASTC_5x4_KHR;if(r===ph)return l===ke?o.COMPRESSED_SRGB8_ALPHA8_ASTC_5x5_KHR:o.COMPRESSED_RGBA_ASTC_5x5_KHR;if(r===mh)return l===ke?o.COMPRESSED_SRGB8_ALPHA8_ASTC_6x5_KHR:o.COMPRESSED_RGBA_ASTC_6x5_KHR;if(r===gh)return l===ke?o.COMPRESSED_SRGB8_ALPHA8_ASTC_6x6_KHR:o.COMPRESSED_RGBA_ASTC_6x6_KHR;if(r===_h)return l===ke?o.COMPRESSED_SRGB8_ALPHA8_ASTC_8x5_KHR:o.COMPRESSED_RGBA_ASTC_8x5_KHR;if(r===xh)return l===ke?o.COMPRESSED_SRGB8_ALPHA8_ASTC_8x6_KHR:o.COMPRESSED_RGBA_ASTC_8x6_KHR;if(r===vh)return l===ke?o.COMPRESSED_SRGB8_ALPHA8_ASTC_8x8_KHR:o.COMPRESSED_RGBA_ASTC_8x8_KHR;if(r===yh)return l===ke?o.COMPRESSED_SRGB8_ALPHA8_ASTC_10x5_KHR:o.COMPRESSED_RGBA_ASTC_10x5_KHR;if(r===Mh)return l===ke?o.COMPRESSED_SRGB8_ALPHA8_ASTC_10x6_KHR:o.COMPRESSED_RGBA_ASTC_10x6_KHR;if(r===Sh)return l===ke?o.COMPRESSED_SRGB8_ALPHA8_ASTC_10x8_KHR:o.COMPRESSED_RGBA_ASTC_10x8_KHR;if(r===bh)return l===ke?o.COMPRESSED_SRGB8_ALPHA8_ASTC_10x10_KHR:o.COMPRESSED_RGBA_ASTC_10x10_KHR;if(r===Eh)return l===ke?o.COMPRESSED_SRGB8_ALPHA8_ASTC_12x10_KHR:o.COMPRESSED_RGBA_ASTC_12x10_KHR;if(r===wh)return l===ke?o.COMPRESSED_SRGB8_ALPHA8_ASTC_12x12_KHR:o.COMPRESSED_RGBA_ASTC_12x12_KHR}else return null;if(r===Wa||r===Th||r===Ah)if(o=t.get("EXT_texture_compression_bptc"),o!==null){if(r===Wa)return l===ke?o.COMPRESSED_SRGB_ALPHA_BPTC_UNORM_EXT:o.COMPRESSED_RGBA_BPTC_UNORM_EXT;if(r===Th)return o.COMPRESSED_RGB_BPTC_SIGNED_FLOAT_EXT;if(r===Ah)return o.COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_EXT}else return null;if(r===ld||r===Rh||r===Ch||r===Ph)if(o=t.get("EXT_texture_compression_rgtc"),o!==null){if(r===Wa)return o.COMPRESSED_RED_RGTC1_EXT;if(r===Rh)return o.COMPRESSED_SIGNED_RED_RGTC1_EXT;if(r===Ch)return o.COMPRESSED_RED_GREEN_RGTC2_EXT;if(r===Ph)return o.COMPRESSED_SIGNED_RED_GREEN_RGTC2_EXT}else return null;return r===us?n?i.UNSIGNED_INT_24_8:(o=t.get("WEBGL_depth_texture"),o!==null?o.UNSIGNED_INT_24_8_WEBGL:null):i[r]!==void 0?i[r]:null}return{convert:s}}var Bl=class extends Mn{constructor(t=[]){super(),this.isArrayCamera=!0,this.cameras=t}},qs=class extends bn{constructor(){super(),this.isGroup=!0,this.type="Group"}},y_={type:"move"},wr=class{constructor(){this._targetRay=null,this._grip=null,this._hand=null}getHandSpace(){return this._hand===null&&(this._hand=new qs,this._hand.matrixAutoUpdate=!1,this._hand.visible=!1,this._hand.joints={},this._hand.inputState={pinching:!1}),this._hand}getTargetRaySpace(){return this._targetRay===null&&(this._targetRay=new qs,this._targetRay.matrixAutoUpdate=!1,this._targetRay.visible=!1,this._targetRay.hasLinearVelocity=!1,this._targetRay.linearVelocity=new O,this._targetRay.hasAngularVelocity=!1,this._targetRay.angularVelocity=new O),this._targetRay}getGripSpace(){return this._grip===null&&(this._grip=new qs,this._grip.matrixAutoUpdate=!1,this._grip.visible=!1,this._grip.hasLinearVelocity=!1,this._grip.linearVelocity=new O,this._grip.hasAngularVelocity=!1,this._grip.angularVelocity=new O),this._grip}dispatchEvent(t){return this._targetRay!==null&&this._targetRay.dispatchEvent(t),this._grip!==null&&this._grip.dispatchEvent(t),this._hand!==null&&this._hand.dispatchEvent(t),this}connect(t){if(t&&t.hand){let e=this._hand;if(e)for(let n of t.hand.values())this._getHandJoint(e,n)}return this.dispatchEvent({type:"connected",data:t}),this}disconnect(t){return this.dispatchEvent({type:"disconnected",data:t}),this._targetRay!==null&&(this._targetRay.visible=!1),this._grip!==null&&(this._grip.visible=!1),this._hand!==null&&(this._hand.visible=!1),this}update(t,e,n){let s=null,r=null,a=null,o=this._targetRay,l=this._grip,c=this._hand;if(t&&e.session.visibilityState!=="visible-blurred"){if(c&&t.hand){a=!0;for(let y of t.hand.values()){let g=e.getJointPose(y,n),m=this._getHandJoint(c,y);g!==null&&(m.matrix.fromArray(g.transform.matrix),m.matrix.decompose(m.position,m.rotation,m.scale),m.matrixWorldNeedsUpdate=!0,m.jointRadius=g.radius),m.visible=g!==null}let h=c.joints["index-finger-tip"],u=c.joints["thumb-tip"],d=h.position.distanceTo(u.position),p=.02,x=.005;c.inputState.pinching&&d>p+x?(c.inputState.pinching=!1,this.dispatchEvent({type:"pinchend",handedness:t.handedness,target:this})):!c.inputState.pinching&&d<=p-x&&(c.inputState.pinching=!0,this.dispatchEvent({type:"pinchstart",handedness:t.handedness,target:this}))}else l!==null&&t.gripSpace&&(r=e.getPose(t.gripSpace,n),r!==null&&(l.matrix.fromArray(r.transform.matrix),l.matrix.decompose(l.position,l.rotation,l.scale),l.matrixWorldNeedsUpdate=!0,r.linearVelocity?(l.hasLinearVelocity=!0,l.linearVelocity.copy(r.linearVelocity)):l.hasLinearVelocity=!1,r.angularVelocity?(l.hasAngularVelocity=!0,l.angularVelocity.copy(r.angularVelocity)):l.hasAngularVelocity=!1));o!==null&&(s=e.getPose(t.targetRaySpace,n),s===null&&r!==null&&(s=r),s!==null&&(o.matrix.fromArray(s.transform.matrix),o.matrix.decompose(o.position,o.rotation,o.scale),o.matrixWorldNeedsUpdate=!0,s.linearVelocity?(o.hasLinearVelocity=!0,o.linearVelocity.copy(s.linearVelocity)):o.hasLinearVelocity=!1,s.angularVelocity?(o.hasAngularVelocity=!0,o.angularVelocity.copy(s.angularVelocity)):o.hasAngularVelocity=!1,this.dispatchEvent(y_)))}return o!==null&&(o.visible=s!==null),l!==null&&(l.visible=r!==null),c!==null&&(c.visible=a!==null),this}_getHandJoint(t,e){if(t.joints[e.jointName]===void 0){let n=new qs;n.matrixAutoUpdate=!1,n.visible=!1,t.joints[e.jointName]=n,t.add(n)}return t.joints[e.jointName]}},zl=class extends qi{constructor(t,e){super();let n=this,s=null,r=1,a=null,o="local-floor",l=1,c=null,h=null,u=null,d=null,p=null,x=null,y=e.getContextAttributes(),g=null,m=null,w=[],v=[],I=new xt,H=null,U=new Mn;U.layers.enable(1),U.viewport=new Xe;let N=new Mn;N.layers.enable(2),N.viewport=new Xe;let Y=[U,N],b=new Bl;b.layers.enable(1),b.layers.enable(2);let P=null,X=null;this.cameraAutoUpdate=!0,this.enabled=!1,this.isPresenting=!1,this.getController=function(nt){let ht=w[nt];return ht===void 0&&(ht=new wr,w[nt]=ht),ht.getTargetRaySpace()},this.getControllerGrip=function(nt){let ht=w[nt];return ht===void 0&&(ht=new wr,w[nt]=ht),ht.getGripSpace()},this.getHand=function(nt){let ht=w[nt];return ht===void 0&&(ht=new wr,w[nt]=ht),ht.getHandSpace()};function rt(nt){let ht=v.indexOf(nt.inputSource);if(ht===-1)return;let Dt=w[ht];Dt!==void 0&&(Dt.update(nt.inputSource,nt.frame,c||a),Dt.dispatchEvent({type:nt.type,data:nt.inputSource}))}function _t(){s.removeEventListener("select",rt),s.removeEventListener("selectstart",rt),s.removeEventListener("selectend",rt),s.removeEventListener("squeeze",rt),s.removeEventListener("squeezestart",rt),s.removeEventListener("squeezeend",rt),s.removeEventListener("end",_t),s.removeEventListener("inputsourceschange",k);for(let nt=0;nt<w.length;nt++){let ht=v[nt];ht!==null&&(v[nt]=null,w[nt].disconnect(ht))}P=null,X=null,t.setRenderTarget(g),p=null,d=null,u=null,s=null,m=null,Ut.stop(),n.isPresenting=!1,t.setPixelRatio(H),t.setSize(I.width,I.height,!1),n.dispatchEvent({type:"sessionend"})}this.setFramebufferScaleFactor=function(nt){r=nt,n.isPresenting===!0&&console.warn("THREE.WebXRManager: Cannot change framebuffer scale while presenting.")},this.setReferenceSpaceType=function(nt){o=nt,n.isPresenting===!0&&console.warn("THREE.WebXRManager: Cannot change reference space type while presenting.")},this.getReferenceSpace=function(){return c||a},this.setReferenceSpace=function(nt){c=nt},this.getBaseLayer=function(){return d!==null?d:p},this.getBinding=function(){return u},this.getFrame=function(){return x},this.getSession=function(){return s},this.setSession=async function(nt){if(s=nt,s!==null){if(g=t.getRenderTarget(),s.addEventListener("select",rt),s.addEventListener("selectstart",rt),s.addEventListener("selectend",rt),s.addEventListener("squeeze",rt),s.addEventListener("squeezestart",rt),s.addEventListener("squeezeend",rt),s.addEventListener("end",_t),s.addEventListener("inputsourceschange",k),y.xrCompatible!==!0&&await e.makeXRCompatible(),H=t.getPixelRatio(),t.getSize(I),s.renderState.layers===void 0||t.capabilities.isWebGL2===!1){let ht={antialias:s.renderState.layers===void 0?y.antialias:!0,alpha:!0,depth:y.depth,stencil:y.stencil,framebufferScaleFactor:r};p=new XRWebGLLayer(s,e,ht),s.updateRenderState({baseLayer:p}),t.setPixelRatio(1),t.setSize(p.framebufferWidth,p.framebufferHeight,!1),m=new Ri(p.framebufferWidth,p.framebufferHeight,{format:Qn,type:Xi,colorSpace:t.outputColorSpace,stencilBuffer:y.stencil})}else{let ht=null,Dt=null,Bt=null;y.depth&&(Bt=y.stencil?e.DEPTH24_STENCIL8:e.DEPTH_COMPONENT24,ht=y.stencil?er:fs,Dt=y.stencil?us:ki);let zt={colorFormat:e.RGBA8,depthFormat:Bt,scaleFactor:r};u=new XRWebGLBinding(s,e),d=u.createProjectionLayer(zt),s.updateRenderState({layers:[d]}),t.setPixelRatio(1),t.setSize(d.textureWidth,d.textureHeight,!1),m=new Ri(d.textureWidth,d.textureHeight,{format:Qn,type:Xi,depthTexture:new Qo(d.textureWidth,d.textureHeight,Dt,void 0,void 0,void 0,void 0,void 0,void 0,ht),stencilBuffer:y.stencil,colorSpace:t.outputColorSpace,samples:y.antialias?4:0});let ne=t.properties.get(m);ne.__ignoreDepthValues=d.ignoreDepthValues}m.isXRRenderTarget=!0,this.setFoveation(l),c=null,a=await s.requestReferenceSpace(o),Ut.setContext(s),Ut.start(),n.isPresenting=!0,n.dispatchEvent({type:"sessionstart"})}},this.getEnvironmentBlendMode=function(){if(s!==null)return s.environmentBlendMode};function k(nt){for(let ht=0;ht<nt.removed.length;ht++){let Dt=nt.removed[ht],Bt=v.indexOf(Dt);Bt>=0&&(v[Bt]=null,w[Bt].disconnect(Dt))}for(let ht=0;ht<nt.added.length;ht++){let Dt=nt.added[ht],Bt=v.indexOf(Dt);if(Bt===-1){for(let ne=0;ne<w.length;ne++)if(ne>=v.length){v.push(Dt),Bt=ne;break}else if(v[ne]===null){v[ne]=Dt,Bt=ne;break}if(Bt===-1)break}let zt=w[Bt];zt&&zt.connect(Dt)}}let q=new O,j=new O;function et(nt,ht,Dt){q.setFromMatrixPosition(ht.matrixWorld),j.setFromMatrixPosition(Dt.matrixWorld);let Bt=q.distanceTo(j),zt=ht.projectionMatrix.elements,ne=Dt.projectionMatrix.elements,Zt=zt[14]/(zt[10]-1),Wt=zt[14]/(zt[10]+1),ae=(zt[9]+1)/zt[5],F=(zt[9]-1)/zt[5],Et=(zt[8]-1)/zt[0],st=(ne[8]+1)/ne[0],vt=Zt*Et,ct=Zt*st,Xt=Bt/(-Et+st),Pt=Xt*-Et;ht.matrixWorld.decompose(nt.position,nt.quaternion,nt.scale),nt.translateX(Pt),nt.translateZ(Xt),nt.matrixWorld.compose(nt.position,nt.quaternion,nt.scale),nt.matrixWorldInverse.copy(nt.matrixWorld).invert();let T=Zt+Xt,S=Wt+Xt,W=vt-Pt,gt=ct+(Bt-Pt),pt=ae*Wt/S*T,mt=F*Wt/S*T;nt.projectionMatrix.makePerspective(W,gt,pt,mt,T,S),nt.projectionMatrixInverse.copy(nt.projectionMatrix).invert()}function ut(nt,ht){ht===null?nt.matrixWorld.copy(nt.matrix):nt.matrixWorld.multiplyMatrices(ht.matrixWorld,nt.matrix),nt.matrixWorldInverse.copy(nt.matrixWorld).invert()}this.updateCamera=function(nt){if(s===null)return;b.near=N.near=U.near=nt.near,b.far=N.far=U.far=nt.far,(P!==b.near||X!==b.far)&&(s.updateRenderState({depthNear:b.near,depthFar:b.far}),P=b.near,X=b.far);let ht=nt.parent,Dt=b.cameras;ut(b,ht);for(let Bt=0;Bt<Dt.length;Bt++)ut(Dt[Bt],ht);Dt.length===2?et(b,U,N):b.projectionMatrix.copy(U.projectionMatrix),tt(nt,b,ht)};function tt(nt,ht,Dt){Dt===null?nt.matrix.copy(ht.matrixWorld):(nt.matrix.copy(Dt.matrixWorld),nt.matrix.invert(),nt.matrix.multiply(ht.matrixWorld)),nt.matrix.decompose(nt.position,nt.quaternion,nt.scale),nt.updateMatrixWorld(!0),nt.projectionMatrix.copy(ht.projectionMatrix),nt.projectionMatrixInverse.copy(ht.projectionMatrixInverse),nt.isPerspectiveCamera&&(nt.fov=Ir*2*Math.atan(1/nt.projectionMatrix.elements[5]),nt.zoom=1)}this.getCamera=function(){return b},this.getFoveation=function(){if(!(d===null&&p===null))return l},this.setFoveation=function(nt){l=nt,d!==null&&(d.fixedFoveation=nt),p!==null&&p.fixedFoveation!==void 0&&(p.fixedFoveation=nt)};let at=null;function lt(nt,ht){if(h=ht.getViewerPose(c||a),x=ht,h!==null){let Dt=h.views;p!==null&&(t.setRenderTargetFramebuffer(m,p.framebuffer),t.setRenderTarget(m));let Bt=!1;Dt.length!==b.cameras.length&&(b.cameras.length=0,Bt=!0);for(let zt=0;zt<Dt.length;zt++){let ne=Dt[zt],Zt=null;if(p!==null)Zt=p.getViewport(ne);else{let ae=u.getViewSubImage(d,ne);Zt=ae.viewport,zt===0&&(t.setRenderTargetTextures(m,ae.colorTexture,d.ignoreDepthValues?void 0:ae.depthStencilTexture),t.setRenderTarget(m))}let Wt=Y[zt];Wt===void 0&&(Wt=new Mn,Wt.layers.enable(zt),Wt.viewport=new Xe,Y[zt]=Wt),Wt.matrix.fromArray(ne.transform.matrix),Wt.matrix.decompose(Wt.position,Wt.quaternion,Wt.scale),Wt.projectionMatrix.fromArray(ne.projectionMatrix),Wt.projectionMatrixInverse.copy(Wt.projectionMatrix).invert(),Wt.viewport.set(Zt.x,Zt.y,Zt.width,Zt.height),zt===0&&(b.matrix.copy(Wt.matrix),b.matrix.decompose(b.position,b.quaternion,b.scale)),Bt===!0&&b.cameras.push(Wt)}}for(let Dt=0;Dt<w.length;Dt++){let Bt=v[Dt],zt=w[Dt];Bt!==null&&zt!==void 0&&zt.update(Bt,ht,c||a)}at&&at(nt,ht),ht.detectedPlanes&&n.dispatchEvent({type:"planesdetected",data:ht}),x=null}let Ut=new Ju;Ut.setAnimationLoop(lt),this.setAnimationLoop=function(nt){at=nt},this.dispose=function(){}}};function M_(i,t){function e(g,m){g.matrixAutoUpdate===!0&&g.updateMatrix(),m.value.copy(g.matrix)}function n(g,m){m.color.getRGB(g.fogColor.value,$u(i)),m.isFog?(g.fogNear.value=m.near,g.fogFar.value=m.far):m.isFogExp2&&(g.fogDensity.value=m.density)}function s(g,m,w,v,I){m.isMeshBasicMaterial||m.isMeshLambertMaterial?r(g,m):m.isMeshToonMaterial?(r(g,m),u(g,m)):m.isMeshPhongMaterial?(r(g,m),h(g,m)):m.isMeshStandardMaterial?(r(g,m),d(g,m),m.isMeshPhysicalMaterial&&p(g,m,I)):m.isMeshMatcapMaterial?(r(g,m),x(g,m)):m.isMeshDepthMaterial?r(g,m):m.isMeshDistanceMaterial?(r(g,m),y(g,m)):m.isMeshNormalMaterial?r(g,m):m.isLineBasicMaterial?(a(g,m),m.isLineDashedMaterial&&o(g,m)):m.isPointsMaterial?l(g,m,w,v):m.isSpriteMaterial?c(g,m):m.isShadowMaterial?(g.color.value.copy(m.color),g.opacity.value=m.opacity):m.isShaderMaterial&&(m.uniformsNeedUpdate=!1)}function r(g,m){g.opacity.value=m.opacity,m.color&&g.diffuse.value.copy(m.color),m.emissive&&g.emissive.value.copy(m.emissive).multiplyScalar(m.emissiveIntensity),m.map&&(g.map.value=m.map,e(m.map,g.mapTransform)),m.alphaMap&&(g.alphaMap.value=m.alphaMap,e(m.alphaMap,g.alphaMapTransform)),m.bumpMap&&(g.bumpMap.value=m.bumpMap,e(m.bumpMap,g.bumpMapTransform),g.bumpScale.value=m.bumpScale,m.side===Sn&&(g.bumpScale.value*=-1)),m.normalMap&&(g.normalMap.value=m.normalMap,e(m.normalMap,g.normalMapTransform),g.normalScale.value.copy(m.normalScale),m.side===Sn&&g.normalScale.value.negate()),m.displacementMap&&(g.displacementMap.value=m.displacementMap,e(m.displacementMap,g.displacementMapTransform),g.displacementScale.value=m.displacementScale,g.displacementBias.value=m.displacementBias),m.emissiveMap&&(g.emissiveMap.value=m.emissiveMap,e(m.emissiveMap,g.emissiveMapTransform)),m.specularMap&&(g.specularMap.value=m.specularMap,e(m.specularMap,g.specularMapTransform)),m.alphaTest>0&&(g.alphaTest.value=m.alphaTest);let w=t.get(m).envMap;if(w&&(g.envMap.value=w,g.flipEnvMap.value=w.isCubeTexture&&w.isRenderTargetTexture===!1?-1:1,g.reflectivity.value=m.reflectivity,g.ior.value=m.ior,g.refractionRatio.value=m.refractionRatio),m.lightMap){g.lightMap.value=m.lightMap;let v=i._useLegacyLights===!0?Math.PI:1;g.lightMapIntensity.value=m.lightMapIntensity*v,e(m.lightMap,g.lightMapTransform)}m.aoMap&&(g.aoMap.value=m.aoMap,g.aoMapIntensity.value=m.aoMapIntensity,e(m.aoMap,g.aoMapTransform))}function a(g,m){g.diffuse.value.copy(m.color),g.opacity.value=m.opacity,m.map&&(g.map.value=m.map,e(m.map,g.mapTransform))}function o(g,m){g.dashSize.value=m.dashSize,g.totalSize.value=m.dashSize+m.gapSize,g.scale.value=m.scale}function l(g,m,w,v){g.diffuse.value.copy(m.color),g.opacity.value=m.opacity,g.size.value=m.size*w,g.scale.value=v*.5,m.map&&(g.map.value=m.map,e(m.map,g.uvTransform)),m.alphaMap&&(g.alphaMap.value=m.alphaMap,e(m.alphaMap,g.alphaMapTransform)),m.alphaTest>0&&(g.alphaTest.value=m.alphaTest)}function c(g,m){g.diffuse.value.copy(m.color),g.opacity.value=m.opacity,g.rotation.value=m.rotation,m.map&&(g.map.value=m.map,e(m.map,g.mapTransform)),m.alphaMap&&(g.alphaMap.value=m.alphaMap,e(m.alphaMap,g.alphaMapTransform)),m.alphaTest>0&&(g.alphaTest.value=m.alphaTest)}function h(g,m){g.specular.value.copy(m.specular),g.shininess.value=Math.max(m.shininess,1e-4)}function u(g,m){m.gradientMap&&(g.gradientMap.value=m.gradientMap)}function d(g,m){g.metalness.value=m.metalness,m.metalnessMap&&(g.metalnessMap.value=m.metalnessMap,e(m.metalnessMap,g.metalnessMapTransform)),g.roughness.value=m.roughness,m.roughnessMap&&(g.roughnessMap.value=m.roughnessMap,e(m.roughnessMap,g.roughnessMapTransform)),t.get(m).envMap&&(g.envMapIntensity.value=m.envMapIntensity)}function p(g,m,w){g.ior.value=m.ior,m.sheen>0&&(g.sheenColor.value.copy(m.sheenColor).multiplyScalar(m.sheen),g.sheenRoughness.value=m.sheenRoughness,m.sheenColorMap&&(g.sheenColorMap.value=m.sheenColorMap,e(m.sheenColorMap,g.sheenColorMapTransform)),m.sheenRoughnessMap&&(g.sheenRoughnessMap.value=m.sheenRoughnessMap,e(m.sheenRoughnessMap,g.sheenRoughnessMapTransform))),m.clearcoat>0&&(g.clearcoat.value=m.clearcoat,g.clearcoatRoughness.value=m.clearcoatRoughness,m.clearcoatMap&&(g.clearcoatMap.value=m.clearcoatMap,e(m.clearcoatMap,g.clearcoatMapTransform)),m.clearcoatRoughnessMap&&(g.clearcoatRoughnessMap.value=m.clearcoatRoughnessMap,e(m.clearcoatRoughnessMap,g.clearcoatRoughnessMapTransform)),m.clearcoatNormalMap&&(g.clearcoatNormalMap.value=m.clearcoatNormalMap,e(m.clearcoatNormalMap,g.clearcoatNormalMapTransform),g.clearcoatNormalScale.value.copy(m.clearcoatNormalScale),m.side===Sn&&g.clearcoatNormalScale.value.negate())),m.iridescence>0&&(g.iridescence.value=m.iridescence,g.iridescenceIOR.value=m.iridescenceIOR,g.iridescenceThicknessMinimum.value=m.iridescenceThicknessRange[0],g.iridescenceThicknessMaximum.value=m.iridescenceThicknessRange[1],m.iridescenceMap&&(g.iridescenceMap.value=m.iridescenceMap,e(m.iridescenceMap,g.iridescenceMapTransform)),m.iridescenceThicknessMap&&(g.iridescenceThicknessMap.value=m.iridescenceThicknessMap,e(m.iridescenceThicknessMap,g.iridescenceThicknessMapTransform))),m.transmission>0&&(g.transmission.value=m.transmission,g.transmissionSamplerMap.value=w.texture,g.transmissionSamplerSize.value.set(w.width,w.height),m.transmissionMap&&(g.transmissionMap.value=m.transmissionMap,e(m.transmissionMap,g.transmissionMapTransform)),g.thickness.value=m.thickness,m.thicknessMap&&(g.thicknessMap.value=m.thicknessMap,e(m.thicknessMap,g.thicknessMapTransform)),g.attenuationDistance.value=m.attenuationDistance,g.attenuationColor.value.copy(m.attenuationColor)),m.anisotropy>0&&(g.anisotropyVector.value.set(m.anisotropy*Math.cos(m.anisotropyRotation),m.anisotropy*Math.sin(m.anisotropyRotation)),m.anisotropyMap&&(g.anisotropyMap.value=m.anisotropyMap,e(m.anisotropyMap,g.anisotropyMapTransform))),g.specularIntensity.value=m.specularIntensity,g.specularColor.value.copy(m.specularColor),m.specularColorMap&&(g.specularColorMap.value=m.specularColorMap,e(m.specularColorMap,g.specularColorMapTransform)),m.specularIntensityMap&&(g.specularIntensityMap.value=m.specularIntensityMap,e(m.specularIntensityMap,g.specularIntensityMapTransform))}function x(g,m){m.matcap&&(g.matcap.value=m.matcap)}function y(g,m){let w=t.get(m).light;g.referencePosition.value.setFromMatrixPosition(w.matrixWorld),g.nearDistance.value=w.shadow.camera.near,g.farDistance.value=w.shadow.camera.far}return{refreshFogUniforms:n,refreshMaterialUniforms:s}}function S_(i,t,e,n){let s={},r={},a=[],o=e.isWebGL2?i.getParameter(i.MAX_UNIFORM_BUFFER_BINDINGS):0;function l(w,v){let I=v.program;n.uniformBlockBinding(w,I)}function c(w,v){let I=s[w.id];I===void 0&&(x(w),I=h(w),s[w.id]=I,w.addEventListener("dispose",g));let H=v.program;n.updateUBOMapping(w,H);let U=t.render.frame;r[w.id]!==U&&(d(w),r[w.id]=U)}function h(w){let v=u();w.__bindingPointIndex=v;let I=i.createBuffer(),H=w.__size,U=w.usage;return i.bindBuffer(i.UNIFORM_BUFFER,I),i.bufferData(i.UNIFORM_BUFFER,H,U),i.bindBuffer(i.UNIFORM_BUFFER,null),i.bindBufferBase(i.UNIFORM_BUFFER,v,I),I}function u(){for(let w=0;w<o;w++)if(a.indexOf(w)===-1)return a.push(w),w;return console.error("THREE.WebGLRenderer: Maximum number of simultaneously usable uniforms groups reached."),0}function d(w){let v=s[w.id],I=w.uniforms,H=w.__cache;i.bindBuffer(i.UNIFORM_BUFFER,v);for(let U=0,N=I.length;U<N;U++){let Y=Array.isArray(I[U])?I[U]:[I[U]];for(let b=0,P=Y.length;b<P;b++){let X=Y[b];if(p(X,U,b,H)===!0){let rt=X.__offset,_t=Array.isArray(X.value)?X.value:[X.value],k=0;for(let q=0;q<_t.length;q++){let j=_t[q],et=y(j);typeof j=="number"||typeof j=="boolean"?(X.__data[0]=j,i.bufferSubData(i.UNIFORM_BUFFER,rt+k,X.__data)):j.isMatrix3?(X.__data[0]=j.elements[0],X.__data[1]=j.elements[1],X.__data[2]=j.elements[2],X.__data[3]=0,X.__data[4]=j.elements[3],X.__data[5]=j.elements[4],X.__data[6]=j.elements[5],X.__data[7]=0,X.__data[8]=j.elements[6],X.__data[9]=j.elements[7],X.__data[10]=j.elements[8],X.__data[11]=0):(j.toArray(X.__data,k),k+=et.storage/Float32Array.BYTES_PER_ELEMENT)}i.bufferSubData(i.UNIFORM_BUFFER,rt,X.__data)}}}i.bindBuffer(i.UNIFORM_BUFFER,null)}function p(w,v,I,H){let U=w.value,N=v+"_"+I;if(H[N]===void 0)return typeof U=="number"||typeof U=="boolean"?H[N]=U:H[N]=U.clone(),!0;{let Y=H[N];if(typeof U=="number"||typeof U=="boolean"){if(Y!==U)return H[N]=U,!0}else if(Y.equals(U)===!1)return Y.copy(U),!0}return!1}function x(w){let v=w.uniforms,I=0,H=16;for(let N=0,Y=v.length;N<Y;N++){let b=Array.isArray(v[N])?v[N]:[v[N]];for(let P=0,X=b.length;P<X;P++){let rt=b[P],_t=Array.isArray(rt.value)?rt.value:[rt.value];for(let k=0,q=_t.length;k<q;k++){let j=_t[k],et=y(j),ut=I%H;ut!==0&&H-ut<et.boundary&&(I+=H-ut),rt.__data=new Float32Array(et.storage/Float32Array.BYTES_PER_ELEMENT),rt.__offset=I,I+=et.storage}}}let U=I%H;return U>0&&(I+=H-U),w.__size=I,w.__cache={},this}function y(w){let v={boundary:0,storage:0};return typeof w=="number"||typeof w=="boolean"?(v.boundary=4,v.storage=4):w.isVector2?(v.boundary=8,v.storage=8):w.isVector3||w.isColor?(v.boundary=16,v.storage=12):w.isVector4?(v.boundary=16,v.storage=16):w.isMatrix3?(v.boundary=48,v.storage=48):w.isMatrix4?(v.boundary=64,v.storage=64):w.isTexture?console.warn("THREE.WebGLRenderer: Texture samplers can not be part of an uniforms group."):console.warn("THREE.WebGLRenderer: Unsupported uniform value type.",w),v}function g(w){let v=w.target;v.removeEventListener("dispose",g);let I=a.indexOf(v.__bindingPointIndex);a.splice(I,1),i.deleteBuffer(s[v.id]),delete s[v.id],delete r[v.id]}function m(){for(let w in s)i.deleteBuffer(s[w]);a=[],s={},r={}}return{bind:l,update:c,dispose:m}}var Fr=class{constructor(t={}){let{canvas:e=Ld(),context:n=null,depth:s=!0,stencil:r=!0,alpha:a=!1,antialias:o=!1,premultipliedAlpha:l=!0,preserveDrawingBuffer:c=!1,powerPreference:h="default",failIfMajorPerformanceCaveat:u=!1}=t;this.isWebGLRenderer=!0;let d;n!==null?d=n.getContextAttributes().alpha:d=a;let p=new Uint32Array(4),x=new Int32Array(4),y=null,g=null,m=[],w=[];this.domElement=e,this.debug={checkShaderErrors:!0,onShaderError:null},this.autoClear=!0,this.autoClearColor=!0,this.autoClearDepth=!0,this.autoClearStencil=!0,this.sortObjects=!0,this.clippingPlanes=[],this.localClippingEnabled=!1,this._outputColorSpace=Je,this._useLegacyLights=!1,this.toneMapping=Wi,this.toneMappingExposure=1;let v=this,I=!1,H=0,U=0,N=null,Y=-1,b=null,P=new Xe,X=new Xe,rt=null,_t=new ge(0),k=0,q=e.width,j=e.height,et=1,ut=null,tt=null,at=new Xe(0,0,q,j),lt=new Xe(0,0,q,j),Ut=!1,nt=new Nr,ht=!1,Dt=!1,Bt=null,zt=new De,ne=new xt,Zt=new O,Wt={background:null,fog:null,environment:null,overrideMaterial:null,isScene:!0};function ae(){return N===null?et:1}let F=n;function Et(A,V){for(let R=0;R<A.length;R++){let Q=A[R],J=e.getContext(Q,V);if(J!==null)return J}return null}try{let A={alpha:!0,depth:s,stencil:r,antialias:o,premultipliedAlpha:l,preserveDrawingBuffer:c,powerPreference:h,failIfMajorPerformanceCaveat:u};if("setAttribute"in e&&e.setAttribute("data-engine","three.js r160"),e.addEventListener("webglcontextlost",St,!1),e.addEventListener("webglcontextrestored",B,!1),e.addEventListener("webglcontextcreationerror",At,!1),F===null){let V=["webgl2","webgl","experimental-webgl"];if(v.isWebGL1Renderer===!0&&V.shift(),F=Et(V,A),F===null)throw Et(V)?new Error("Error creating WebGL context with your selected attributes."):new Error("Error creating WebGL context.")}typeof WebGLRenderingContext!="undefined"&&F instanceof WebGLRenderingContext&&console.warn("THREE.WebGLRenderer: WebGL 1 support was deprecated in r153 and will be removed in r163."),F.getShaderPrecisionFormat===void 0&&(F.getShaderPrecisionFormat=function(){return{rangeMin:1,rangeMax:1,precision:1}})}catch(A){throw console.error("THREE.WebGLRenderer: "+A.message),A}let st,vt,ct,Xt,Pt,T,S,W,gt,pt,mt,Vt,It,Tt,jt,he,ft,Me,xe,Yt,$t,Ht,re,Ee;function Ve(){st=new kg(F),vt=new Ng(F,st,t),st.init(vt),Ht=new v_(F,st,vt),ct=new __(F,st,vt),Xt=new Wg(F),Pt=new r_,T=new x_(F,st,ct,Pt,vt,Ht,Xt),S=new Og(v),W=new Hg(v),gt=new jd(F,vt),re=new Ug(F,st,gt,vt),pt=new Vg(F,gt,Xt,re),mt=new Zg(F,pt,gt,Xt),xe=new qg(F,vt,T),he=new Fg(Pt),Vt=new s_(v,S,W,st,vt,re,he),It=new M_(v,Pt),Tt=new a_,jt=new d_(st,vt),Me=new Lg(v,S,W,ct,mt,d,l),ft=new g_(v,mt,vt),Ee=new S_(F,Xt,vt,ct),Yt=new Dg(F,st,Xt,vt),$t=new Gg(F,st,Xt,vt),Xt.programs=Vt.programs,v.capabilities=vt,v.extensions=st,v.properties=Pt,v.renderLists=Tt,v.shadowMap=ft,v.state=ct,v.info=Xt}Ve();let Kt=new zl(v,F);this.xr=Kt,this.getContext=function(){return F},this.getContextAttributes=function(){return F.getContextAttributes()},this.forceContextLoss=function(){let A=st.get("WEBGL_lose_context");A&&A.loseContext()},this.forceContextRestore=function(){let A=st.get("WEBGL_lose_context");A&&A.restoreContext()},this.getPixelRatio=function(){return et},this.setPixelRatio=function(A){A!==void 0&&(et=A,this.setSize(q,j,!1))},this.getSize=function(A){return A.set(q,j)},this.setSize=function(A,V,R=!0){if(Kt.isPresenting){console.warn("THREE.WebGLRenderer: Can't change size while VR device is presenting.");return}q=A,j=V,e.width=Math.floor(A*et),e.height=Math.floor(V*et),R===!0&&(e.style.width=A+"px",e.style.height=V+"px"),this.setViewport(0,0,A,V)},this.getDrawingBufferSize=function(A){return A.set(q*et,j*et).floor()},this.setDrawingBufferSize=function(A,V,R){q=A,j=V,et=R,e.width=Math.floor(A*R),e.height=Math.floor(V*R),this.setViewport(0,0,A,V)},this.getCurrentViewport=function(A){return A.copy(P)},this.getViewport=function(A){return A.copy(at)},this.setViewport=function(A,V,R,Q){A.isVector4?at.set(A.x,A.y,A.z,A.w):at.set(A,V,R,Q),ct.viewport(P.copy(at).multiplyScalar(et).floor())},this.getScissor=function(A){return A.copy(lt)},this.setScissor=function(A,V,R,Q){A.isVector4?lt.set(A.x,A.y,A.z,A.w):lt.set(A,V,R,Q),ct.scissor(X.copy(lt).multiplyScalar(et).floor())},this.getScissorTest=function(){return Ut},this.setScissorTest=function(A){ct.setScissorTest(Ut=A)},this.setOpaqueSort=function(A){ut=A},this.setTransparentSort=function(A){tt=A},this.getClearColor=function(A){return A.copy(Me.getClearColor())},this.setClearColor=function(){Me.setClearColor.apply(Me,arguments)},this.getClearAlpha=function(){return Me.getClearAlpha()},this.setClearAlpha=function(){Me.setClearAlpha.apply(Me,arguments)},this.clear=function(A=!0,V=!0,R=!0){let Q=0;if(A){let J=!1;if(N!==null){let Ft=N.texture.format;J=Ft===Vu||Ft===ku||Ft===Hu}if(J){let Ft=N.texture.type,Gt=Ft===Xi||Ft===ki||Ft===fc||Ft===us||Ft===Bu||Ft===zu,Qt=Me.getClearColor(),oe=Me.getClearAlpha(),dt=Qt.r,yt=Qt.g,Mt=Qt.b;Gt?(p[0]=dt,p[1]=yt,p[2]=Mt,p[3]=oe,F.clearBufferuiv(F.COLOR,0,p)):(x[0]=dt,x[1]=yt,x[2]=Mt,x[3]=oe,F.clearBufferiv(F.COLOR,0,x))}else Q|=F.COLOR_BUFFER_BIT}V&&(Q|=F.DEPTH_BUFFER_BIT),R&&(Q|=F.STENCIL_BUFFER_BIT,this.state.buffers.stencil.setMask(4294967295)),F.clear(Q)},this.clearColor=function(){this.clear(!0,!1,!1)},this.clearDepth=function(){this.clear(!1,!0,!1)},this.clearStencil=function(){this.clear(!1,!1,!0)},this.dispose=function(){e.removeEventListener("webglcontextlost",St,!1),e.removeEventListener("webglcontextrestored",B,!1),e.removeEventListener("webglcontextcreationerror",At,!1),Tt.dispose(),jt.dispose(),Pt.dispose(),S.dispose(),W.dispose(),mt.dispose(),re.dispose(),Ee.dispose(),Vt.dispose(),Kt.dispose(),Kt.removeEventListener("sessionstart",un),Kt.removeEventListener("sessionend",Se),Bt&&(Bt.dispose(),Bt=null),fn.stop()};function St(A){A.preventDefault(),console.log("THREE.WebGLRenderer: Context Lost."),I=!0}function B(){console.log("THREE.WebGLRenderer: Context Restored."),I=!1;let A=Xt.autoReset,V=ft.enabled,R=ft.autoUpdate,Q=ft.needsUpdate,J=ft.type;Ve(),Xt.autoReset=A,ft.enabled=V,ft.autoUpdate=R,ft.needsUpdate=Q,ft.type=J}function At(A){console.error("THREE.WebGLRenderer: A WebGL context could not be created. Reason: ",A.statusMessage)}function Lt(A){let V=A.target;V.removeEventListener("dispose",Lt),ie(V)}function ie(A){Jt(A),Pt.remove(A)}function Jt(A){let V=Pt.get(A).programs;V!==void 0&&(V.forEach(function(R){Vt.releaseProgram(R)}),A.isShaderMaterial&&Vt.releaseShaderCache(A))}this.renderBufferDirect=function(A,V,R,Q,J,Ft){V===null&&(V=Wt);let Gt=J.isMesh&&J.matrixWorld.determinant()<0,Qt=Fe(A,V,R,Q,J);ct.setMaterial(Q,Gt);let oe=R.index,dt=1;if(Q.wireframe===!0){if(oe=pt.getWireframeAttribute(R),oe===void 0)return;dt=2}let yt=R.drawRange,Mt=R.attributes.position,be=yt.start*dt,xn=(yt.start+yt.count)*dt;Ft!==null&&(be=Math.max(be,Ft.start*dt),xn=Math.min(xn,(Ft.start+Ft.count)*dt)),oe!==null?(be=Math.max(be,0),xn=Math.min(xn,oe.count)):Mt!=null&&(be=Math.max(be,0),xn=Math.min(xn,Mt.count));let Ne=xn-be;if(Ne<0||Ne===1/0)return;re.setup(J,Q,Qt,R,oe);let Ze,we=Yt;if(oe!==null&&(Ze=gt.get(oe),we=$t,we.setIndex(Ze)),J.isMesh)Q.wireframe===!0?(ct.setLineWidth(Q.wireframeLinewidth*ae()),we.setMode(F.LINES)):we.setMode(F.TRIANGLES);else if(J.isLine){let pe=Q.linewidth;pe===void 0&&(pe=1),ct.setLineWidth(pe*ae()),J.isLineSegments?we.setMode(F.LINES):J.isLineLoop?we.setMode(F.LINE_LOOP):we.setMode(F.LINE_STRIP)}else J.isPoints?we.setMode(F.POINTS):J.isSprite&&we.setMode(F.TRIANGLES);if(J.isBatchedMesh)we.renderMultiDraw(J._multiDrawStarts,J._multiDrawCounts,J._multiDrawCount);else if(J.isInstancedMesh)we.renderInstances(be,Ne,J.count);else if(R.isInstancedBufferGeometry){let pe=R._maxInstanceCount!==void 0?R._maxInstanceCount:1/0,mi=Math.min(R.instanceCount,pe);we.renderInstances(be,Ne,mi)}else we.render(be,Ne)};function Re(A,V,R){A.transparent===!0&&A.side===mn&&A.forceSinglePass===!1?(A.side=Sn,A.needsUpdate=!0,bs(A,V,R),A.side=Yi,A.needsUpdate=!0,bs(A,V,R),A.side=mn):bs(A,V,R)}this.compile=function(A,V,R=null){R===null&&(R=A),g=jt.get(R),g.init(),w.push(g),R.traverseVisible(function(J){J.isLight&&J.layers.test(V.layers)&&(g.pushLight(J),J.castShadow&&g.pushShadow(J))}),A!==R&&A.traverseVisible(function(J){J.isLight&&J.layers.test(V.layers)&&(g.pushLight(J),J.castShadow&&g.pushShadow(J))}),g.setupLights(v._useLegacyLights);let Q=new Set;return A.traverse(function(J){let Ft=J.material;if(Ft)if(Array.isArray(Ft))for(let Gt=0;Gt<Ft.length;Gt++){let Qt=Ft[Gt];Re(Qt,R,J),Q.add(Qt)}else Re(Ft,R,J),Q.add(Ft)}),w.pop(),g=null,Q},this.compileAsync=function(A,V,R=null){let Q=this.compile(A,V,R);return new Promise(J=>{function Ft(){if(Q.forEach(function(Gt){Pt.get(Gt).currentProgram.isReady()&&Q.delete(Gt)}),Q.size===0){J(A);return}setTimeout(Ft,10)}st.get("KHR_parallel_shader_compile")!==null?Ft():setTimeout(Ft,10)})};let Pe=null;function Ke(A){Pe&&Pe(A)}function un(){fn.stop()}function Se(){fn.start()}let fn=new Ju;fn.setAnimationLoop(Ke),typeof self!="undefined"&&fn.setContext(self),this.setAnimationLoop=function(A){Pe=A,Kt.setAnimationLoop(A),A===null?fn.stop():fn.start()},Kt.addEventListener("sessionstart",un),Kt.addEventListener("sessionend",Se),this.render=function(A,V){if(V!==void 0&&V.isCamera!==!0){console.error("THREE.WebGLRenderer.render: camera is not an instance of THREE.Camera.");return}if(I===!0)return;A.matrixWorldAutoUpdate===!0&&A.updateMatrixWorld(),V.parent===null&&V.matrixWorldAutoUpdate===!0&&V.updateMatrixWorld(),Kt.enabled===!0&&Kt.isPresenting===!0&&(Kt.cameraAutoUpdate===!0&&Kt.updateCamera(V),V=Kt.getCamera()),A.isScene===!0&&A.onBeforeRender(v,A,V,N),g=jt.get(A,w.length),g.init(),w.push(g),zt.multiplyMatrices(V.projectionMatrix,V.matrixWorldInverse),nt.setFromProjectionMatrix(zt),Dt=this.localClippingEnabled,ht=he.init(this.clippingPlanes,Dt),y=Tt.get(A,m.length),y.init(),m.push(y),Nn(A,V,0,v.sortObjects),y.finish(),v.sortObjects===!0&&y.sort(ut,tt),this.info.render.frame++,ht===!0&&he.beginShadows();let R=g.state.shadowsArray;if(ft.render(R,A,V),ht===!0&&he.endShadows(),this.info.autoReset===!0&&this.info.reset(),Me.render(y,A),g.setupLights(v._useLegacyLights),V.isArrayCamera){let Q=V.cameras;for(let J=0,Ft=Q.length;J<Ft;J++){let Gt=Q[J];ji(y,A,Gt,Gt.viewport)}}else ji(y,A,V);N!==null&&(T.updateMultisampleRenderTarget(N),T.updateRenderTargetMipmap(N)),A.isScene===!0&&A.onAfterRender(v,A,V),re.resetDefaultState(),Y=-1,b=null,w.pop(),w.length>0?g=w[w.length-1]:g=null,m.pop(),m.length>0?y=m[m.length-1]:y=null};function Nn(A,V,R,Q){if(A.visible===!1)return;if(A.layers.test(V.layers)){if(A.isGroup)R=A.renderOrder;else if(A.isLOD)A.autoUpdate===!0&&A.update(V);else if(A.isLight)g.pushLight(A),A.castShadow&&g.pushShadow(A);else if(A.isSprite){if(!A.frustumCulled||nt.intersectsSprite(A)){Q&&Zt.setFromMatrixPosition(A.matrixWorld).applyMatrix4(zt);let Gt=mt.update(A),Qt=A.material;Qt.visible&&y.push(A,Gt,Qt,R,Zt.z,null)}}else if((A.isMesh||A.isLine||A.isPoints)&&(!A.frustumCulled||nt.intersectsObject(A))){let Gt=mt.update(A),Qt=A.material;if(Q&&(A.boundingSphere!==void 0?(A.boundingSphere===null&&A.computeBoundingSphere(),Zt.copy(A.boundingSphere.center)):(Gt.boundingSphere===null&&Gt.computeBoundingSphere(),Zt.copy(Gt.boundingSphere.center)),Zt.applyMatrix4(A.matrixWorld).applyMatrix4(zt)),Array.isArray(Qt)){let oe=Gt.groups;for(let dt=0,yt=oe.length;dt<yt;dt++){let Mt=oe[dt],be=Qt[Mt.materialIndex];be&&be.visible&&y.push(A,Gt,be,R,Zt.z,Mt)}}else Qt.visible&&y.push(A,Gt,Qt,R,Zt.z,null)}}let Ft=A.children;for(let Gt=0,Qt=Ft.length;Gt<Qt;Gt++)Nn(Ft[Gt],V,R,Q)}function ji(A,V,R,Q){let J=A.opaque,Ft=A.transmissive,Gt=A.transparent;g.setupLightsView(R),ht===!0&&he.setGlobalState(v.clippingPlanes,R),Ft.length>0&&Ma(J,Ft,V,R),Q&&ct.viewport(P.copy(Q)),J.length>0&&di(J,V,R),Ft.length>0&&di(Ft,V,R),Gt.length>0&&di(Gt,V,R),ct.buffers.depth.setTest(!0),ct.buffers.depth.setMask(!0),ct.buffers.color.setMask(!0),ct.setPolygonOffset(!1)}function Ma(A,V,R,Q){if((R.isScene===!0?R.overrideMaterial:null)!==null)return;let Ft=vt.isWebGL2;Bt===null&&(Bt=new Ri(1,1,{generateMipmaps:!0,type:st.has("EXT_color_buffer_half_float")?Pr:Xi,minFilter:Cr,samples:Ft?4:0})),v.getDrawingBufferSize(ne),Ft?Bt.setSize(ne.x,ne.y):Bt.setSize(Wo(ne.x),Wo(ne.y));let Gt=v.getRenderTarget();v.setRenderTarget(Bt),v.getClearColor(_t),k=v.getClearAlpha(),k<1&&v.setClearColor(16777215,.5),v.clear();let Qt=v.toneMapping;v.toneMapping=Wi,di(A,R,Q),T.updateMultisampleRenderTarget(Bt),T.updateRenderTargetMipmap(Bt);let oe=!1;for(let dt=0,yt=V.length;dt<yt;dt++){let Mt=V[dt],be=Mt.object,xn=Mt.geometry,Ne=Mt.material,Ze=Mt.group;if(Ne.side===mn&&be.layers.test(Q.layers)){let we=Ne.side;Ne.side=Sn,Ne.needsUpdate=!0,Qi(be,R,Q,xn,Ne,Ze),Ne.side=we,Ne.needsUpdate=!0,oe=!0}}oe===!0&&(T.updateMultisampleRenderTarget(Bt),T.updateRenderTargetMipmap(Bt)),v.setRenderTarget(Gt),v.setClearColor(_t,k),v.toneMapping=Qt}function di(A,V,R){let Q=V.isScene===!0?V.overrideMaterial:null;for(let J=0,Ft=A.length;J<Ft;J++){let Gt=A[J],Qt=Gt.object,oe=Gt.geometry,dt=Q===null?Gt.material:Q,yt=Gt.group;Qt.layers.test(R.layers)&&Qi(Qt,V,R,oe,dt,yt)}}function Qi(A,V,R,Q,J,Ft){A.onBeforeRender(v,V,R,Q,J,Ft),A.modelViewMatrix.multiplyMatrices(R.matrixWorldInverse,A.matrixWorld),A.normalMatrix.getNormalMatrix(A.modelViewMatrix),J.onBeforeRender(v,V,R,Q,A,Ft),J.transparent===!0&&J.side===mn&&J.forceSinglePass===!1?(J.side=Sn,J.needsUpdate=!0,v.renderBufferDirect(R,V,Q,J,A,Ft),J.side=Yi,J.needsUpdate=!0,v.renderBufferDirect(R,V,Q,J,A,Ft),J.side=mn):v.renderBufferDirect(R,V,Q,J,A,Ft),A.onAfterRender(v,V,R,Q,J,Ft)}function bs(A,V,R){V.isScene!==!0&&(V=Wt);let Q=Pt.get(A),J=g.state.lights,Ft=g.state.shadowsArray,Gt=J.state.version,Qt=Vt.getParameters(A,J.state,Ft,V,R),oe=Vt.getProgramCacheKey(Qt),dt=Q.programs;Q.environment=A.isMeshStandardMaterial?V.environment:null,Q.fog=V.fog,Q.envMap=(A.isMeshStandardMaterial?W:S).get(A.envMap||Q.environment),dt===void 0&&(A.addEventListener("dispose",Lt),dt=new Map,Q.programs=dt);let yt=dt.get(oe);if(yt!==void 0){if(Q.currentProgram===yt&&Q.lightsStateVersion===Gt)return Kr(A,Qt),yt}else Qt.uniforms=Vt.getUniforms(A),A.onBuild(R,Qt,v),A.onBeforeCompile(Qt,v),yt=Vt.acquireProgram(Qt,oe),dt.set(oe,yt),Q.uniforms=Qt.uniforms;let Mt=Q.uniforms;return(!A.isShaderMaterial&&!A.isRawShaderMaterial||A.clipping===!0)&&(Mt.clippingPlanes=he.uniform),Kr(A,Qt),Q.needsLights=jr(A),Q.lightsStateVersion=Gt,Q.needsLights&&(Mt.ambientLightColor.value=J.state.ambient,Mt.lightProbe.value=J.state.probe,Mt.directionalLights.value=J.state.directional,Mt.directionalLightShadows.value=J.state.directionalShadow,Mt.spotLights.value=J.state.spot,Mt.spotLightShadows.value=J.state.spotShadow,Mt.rectAreaLights.value=J.state.rectArea,Mt.ltc_1.value=J.state.rectAreaLTC1,Mt.ltc_2.value=J.state.rectAreaLTC2,Mt.pointLights.value=J.state.point,Mt.pointLightShadows.value=J.state.pointShadow,Mt.hemisphereLights.value=J.state.hemi,Mt.directionalShadowMap.value=J.state.directionalShadowMap,Mt.directionalShadowMatrix.value=J.state.directionalShadowMatrix,Mt.spotShadowMap.value=J.state.spotShadowMap,Mt.spotLightMatrix.value=J.state.spotLightMatrix,Mt.spotLightMap.value=J.state.spotLightMap,Mt.pointShadowMap.value=J.state.pointShadowMap,Mt.pointShadowMatrix.value=J.state.pointShadowMatrix),Q.currentProgram=yt,Q.uniformsList=null,yt}function pi(A){if(A.uniformsList===null){let V=A.currentProgram.getUniforms();A.uniformsList=Ks.seqWithValue(V.seq,A.uniforms)}return A.uniformsList}function Kr(A,V){let R=Pt.get(A);R.outputColorSpace=V.outputColorSpace,R.batching=V.batching,R.instancing=V.instancing,R.instancingColor=V.instancingColor,R.skinning=V.skinning,R.morphTargets=V.morphTargets,R.morphNormals=V.morphNormals,R.morphColors=V.morphColors,R.morphTargetsCount=V.morphTargetsCount,R.numClippingPlanes=V.numClippingPlanes,R.numIntersection=V.numClipIntersection,R.vertexAlphas=V.vertexAlphas,R.vertexTangents=V.vertexTangents,R.toneMapping=V.toneMapping}function Fe(A,V,R,Q,J){V.isScene!==!0&&(V=Wt),T.resetTextureUnits();let Ft=V.fog,Gt=Q.isMeshStandardMaterial?V.environment:null,Qt=N===null?v.outputColorSpace:N.isXRRenderTarget===!0?N.texture.colorSpace:Ai,oe=(Q.isMeshStandardMaterial?W:S).get(Q.envMap||Gt),dt=Q.vertexColors===!0&&!!R.attributes.color&&R.attributes.color.itemSize===4,yt=!!R.attributes.tangent&&(!!Q.normalMap||Q.anisotropy>0),Mt=!!R.morphAttributes.position,be=!!R.morphAttributes.normal,xn=!!R.morphAttributes.color,Ne=Wi;Q.toneMapped&&(N===null||N.isXRRenderTarget===!0)&&(Ne=v.toneMapping);let Ze=R.morphAttributes.position||R.morphAttributes.normal||R.morphAttributes.color,we=Ze!==void 0?Ze.length:0,pe=Pt.get(Q),mi=g.state.lights;if(ht===!0&&(Dt===!0||A!==b)){let on=A===b&&Q.id===Y;he.setState(Q,A,on)}let Oe=!1;Q.version===pe.__version?(pe.needsLights&&pe.lightsStateVersion!==mi.state.version||pe.outputColorSpace!==Qt||J.isBatchedMesh&&pe.batching===!1||!J.isBatchedMesh&&pe.batching===!0||J.isInstancedMesh&&pe.instancing===!1||!J.isInstancedMesh&&pe.instancing===!0||J.isSkinnedMesh&&pe.skinning===!1||!J.isSkinnedMesh&&pe.skinning===!0||J.isInstancedMesh&&pe.instancingColor===!0&&J.instanceColor===null||J.isInstancedMesh&&pe.instancingColor===!1&&J.instanceColor!==null||pe.envMap!==oe||Q.fog===!0&&pe.fog!==Ft||pe.numClippingPlanes!==void 0&&(pe.numClippingPlanes!==he.numPlanes||pe.numIntersection!==he.numIntersection)||pe.vertexAlphas!==dt||pe.vertexTangents!==yt||pe.morphTargets!==Mt||pe.morphNormals!==be||pe.morphColors!==xn||pe.toneMapping!==Ne||vt.isWebGL2===!0&&pe.morphTargetsCount!==we)&&(Oe=!0):(Oe=!0,pe.__version=Q.version);let ii=pe.currentProgram;Oe===!0&&(ii=bs(Q,V,J));let si=!1,gi=!1,Ni=!1,$e=ii.getUniforms(),Te=pe.uniforms;if(ct.useProgram(ii.program)&&(si=!0,gi=!0,Ni=!0),Q.id!==Y&&(Y=Q.id,gi=!0),si||b!==A){$e.setValue(F,"projectionMatrix",A.projectionMatrix),$e.setValue(F,"viewMatrix",A.matrixWorldInverse);let on=$e.map.cameraPosition;on!==void 0&&on.setValue(F,Zt.setFromMatrixPosition(A.matrixWorld)),vt.logarithmicDepthBuffer&&$e.setValue(F,"logDepthBufFC",2/(Math.log(A.far+1)/Math.LN2)),(Q.isMeshPhongMaterial||Q.isMeshToonMaterial||Q.isMeshLambertMaterial||Q.isMeshBasicMaterial||Q.isMeshStandardMaterial||Q.isShaderMaterial)&&$e.setValue(F,"isOrthographic",A.isOrthographicCamera===!0),b!==A&&(b=A,gi=!0,Ni=!0)}if(J.isSkinnedMesh){$e.setOptional(F,J,"bindMatrix"),$e.setOptional(F,J,"bindMatrixInverse");let on=J.skeleton;on&&(vt.floatVertexTextures?(on.boneTexture===null&&on.computeBoneTexture(),$e.setValue(F,"boneTexture",on.boneTexture,T)):console.warn("THREE.WebGLRenderer: SkinnedMesh can only be used with WebGL 2. With WebGL 1 OES_texture_float and vertex textures support is required."))}J.isBatchedMesh&&($e.setOptional(F,J,"batchingTexture"),$e.setValue(F,"batchingTexture",J._matricesTexture,T));let In=R.morphAttributes;if((In.position!==void 0||In.normal!==void 0||In.color!==void 0&&vt.isWebGL2===!0)&&xe.update(J,R,ii),(gi||pe.receiveShadow!==J.receiveShadow)&&(pe.receiveShadow=J.receiveShadow,$e.setValue(F,"receiveShadow",J.receiveShadow)),Q.isMeshGouraudMaterial&&Q.envMap!==null&&(Te.envMap.value=oe,Te.flipEnvMap.value=oe.isCubeTexture&&oe.isRenderTargetTexture===!1?-1:1),gi&&($e.setValue(F,"toneMappingExposure",v.toneMappingExposure),pe.needsLights&&Fn(Te,Ni),Ft&&Q.fog===!0&&It.refreshFogUniforms(Te,Ft),It.refreshMaterialUniforms(Te,Q,et,j,Bt),Ks.upload(F,pi(pe),Te,T)),Q.isShaderMaterial&&Q.uniformsNeedUpdate===!0&&(Ks.upload(F,pi(pe),Te,T),Q.uniformsNeedUpdate=!1),Q.isSpriteMaterial&&$e.setValue(F,"center",J.center),$e.setValue(F,"modelViewMatrix",J.modelViewMatrix),$e.setValue(F,"normalMatrix",J.normalMatrix),$e.setValue(F,"modelMatrix",J.matrixWorld),Q.isShaderMaterial||Q.isRawShaderMaterial){let on=Q.uniformsGroups;for(let an=0,hr=on.length;an<hr;an++)if(vt.isWebGL2){let ce=on[an];Ee.update(ce,ii),Ee.bind(ce,ii)}else console.warn("THREE.WebGLRenderer: Uniform Buffer Objects can only be used with WebGL 2.")}return ii}function Fn(A,V){A.ambientLightColor.needsUpdate=V,A.lightProbe.needsUpdate=V,A.directionalLights.needsUpdate=V,A.directionalLightShadows.needsUpdate=V,A.pointLights.needsUpdate=V,A.pointLightShadows.needsUpdate=V,A.spotLights.needsUpdate=V,A.spotLightShadows.needsUpdate=V,A.rectAreaLights.needsUpdate=V,A.hemisphereLights.needsUpdate=V}function jr(A){return A.isMeshLambertMaterial||A.isMeshToonMaterial||A.isMeshPhongMaterial||A.isMeshStandardMaterial||A.isShadowMaterial||A.isShaderMaterial&&A.lights===!0}this.getActiveCubeFace=function(){return H},this.getActiveMipmapLevel=function(){return U},this.getRenderTarget=function(){return N},this.setRenderTargetTextures=function(A,V,R){Pt.get(A.texture).__webglTexture=V,Pt.get(A.depthTexture).__webglTexture=R;let Q=Pt.get(A);Q.__hasExternalTextures=!0,Q.__hasExternalTextures&&(Q.__autoAllocateDepthBuffer=R===void 0,Q.__autoAllocateDepthBuffer||st.has("WEBGL_multisampled_render_to_texture")===!0&&(console.warn("THREE.WebGLRenderer: Render-to-texture extension was disabled because an external texture was provided"),Q.__useRenderToTexture=!1))},this.setRenderTargetFramebuffer=function(A,V){let R=Pt.get(A);R.__webglFramebuffer=V,R.__useDefaultFramebuffer=V===void 0},this.setRenderTarget=function(A,V=0,R=0){N=A,H=V,U=R;let Q=!0,J=null,Ft=!1,Gt=!1;if(A){let oe=Pt.get(A);oe.__useDefaultFramebuffer!==void 0?(ct.bindFramebuffer(F.FRAMEBUFFER,null),Q=!1):oe.__webglFramebuffer===void 0?T.setupRenderTarget(A):oe.__hasExternalTextures&&T.rebindTextures(A,Pt.get(A.texture).__webglTexture,Pt.get(A.depthTexture).__webglTexture);let dt=A.texture;(dt.isData3DTexture||dt.isDataArrayTexture||dt.isCompressedArrayTexture)&&(Gt=!0);let yt=Pt.get(A).__webglFramebuffer;A.isWebGLCubeRenderTarget?(Array.isArray(yt[V])?J=yt[V][R]:J=yt[V],Ft=!0):vt.isWebGL2&&A.samples>0&&T.useMultisampledRTT(A)===!1?J=Pt.get(A).__webglMultisampledFramebuffer:Array.isArray(yt)?J=yt[R]:J=yt,P.copy(A.viewport),X.copy(A.scissor),rt=A.scissorTest}else P.copy(at).multiplyScalar(et).floor(),X.copy(lt).multiplyScalar(et).floor(),rt=Ut;if(ct.bindFramebuffer(F.FRAMEBUFFER,J)&&vt.drawBuffers&&Q&&ct.drawBuffers(A,J),ct.viewport(P),ct.scissor(X),ct.setScissorTest(rt),Ft){let oe=Pt.get(A.texture);F.framebufferTexture2D(F.FRAMEBUFFER,F.COLOR_ATTACHMENT0,F.TEXTURE_CUBE_MAP_POSITIVE_X+V,oe.__webglTexture,R)}else if(Gt){let oe=Pt.get(A.texture),dt=V||0;F.framebufferTextureLayer(F.FRAMEBUFFER,F.COLOR_ATTACHMENT0,oe.__webglTexture,R||0,dt)}Y=-1},this.readRenderTargetPixels=function(A,V,R,Q,J,Ft,Gt){if(!(A&&A.isWebGLRenderTarget)){console.error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not THREE.WebGLRenderTarget.");return}let Qt=Pt.get(A).__webglFramebuffer;if(A.isWebGLCubeRenderTarget&&Gt!==void 0&&(Qt=Qt[Gt]),Qt){ct.bindFramebuffer(F.FRAMEBUFFER,Qt);try{let oe=A.texture,dt=oe.format,yt=oe.type;if(dt!==Qn&&Ht.convert(dt)!==F.getParameter(F.IMPLEMENTATION_COLOR_READ_FORMAT)){console.error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not in RGBA or implementation defined format.");return}let Mt=yt===Pr&&(st.has("EXT_color_buffer_half_float")||vt.isWebGL2&&st.has("EXT_color_buffer_float"));if(yt!==Xi&&Ht.convert(yt)!==F.getParameter(F.IMPLEMENTATION_COLOR_READ_TYPE)&&!(yt===Vi&&(vt.isWebGL2||st.has("OES_texture_float")||st.has("WEBGL_color_buffer_float")))&&!Mt){console.error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not in UnsignedByteType or implementation defined type.");return}V>=0&&V<=A.width-Q&&R>=0&&R<=A.height-J&&F.readPixels(V,R,Q,J,Ht.convert(dt),Ht.convert(yt),Ft)}finally{let oe=N!==null?Pt.get(N).__webglFramebuffer:null;ct.bindFramebuffer(F.FRAMEBUFFER,oe)}}},this.copyFramebufferToTexture=function(A,V,R=0){let Q=Math.pow(2,-R),J=Math.floor(V.image.width*Q),Ft=Math.floor(V.image.height*Q);T.setTexture2D(V,0),F.copyTexSubImage2D(F.TEXTURE_2D,R,0,0,A.x,A.y,J,Ft),ct.unbindTexture()},this.copyTextureToTexture=function(A,V,R,Q=0){let J=V.image.width,Ft=V.image.height,Gt=Ht.convert(R.format),Qt=Ht.convert(R.type);T.setTexture2D(R,0),F.pixelStorei(F.UNPACK_FLIP_Y_WEBGL,R.flipY),F.pixelStorei(F.UNPACK_PREMULTIPLY_ALPHA_WEBGL,R.premultiplyAlpha),F.pixelStorei(F.UNPACK_ALIGNMENT,R.unpackAlignment),V.isDataTexture?F.texSubImage2D(F.TEXTURE_2D,Q,A.x,A.y,J,Ft,Gt,Qt,V.image.data):V.isCompressedTexture?F.compressedTexSubImage2D(F.TEXTURE_2D,Q,A.x,A.y,V.mipmaps[0].width,V.mipmaps[0].height,Gt,V.mipmaps[0].data):F.texSubImage2D(F.TEXTURE_2D,Q,A.x,A.y,Gt,Qt,V.image),Q===0&&R.generateMipmaps&&F.generateMipmap(F.TEXTURE_2D),ct.unbindTexture()},this.copyTextureToTexture3D=function(A,V,R,Q,J=0){if(v.isWebGL1Renderer){console.warn("THREE.WebGLRenderer.copyTextureToTexture3D: can only be used with WebGL2.");return}let Ft=A.max.x-A.min.x+1,Gt=A.max.y-A.min.y+1,Qt=A.max.z-A.min.z+1,oe=Ht.convert(Q.format),dt=Ht.convert(Q.type),yt;if(Q.isData3DTexture)T.setTexture3D(Q,0),yt=F.TEXTURE_3D;else if(Q.isDataArrayTexture||Q.isCompressedArrayTexture)T.setTexture2DArray(Q,0),yt=F.TEXTURE_2D_ARRAY;else{console.warn("THREE.WebGLRenderer.copyTextureToTexture3D: only supports THREE.DataTexture3D and THREE.DataTexture2DArray.");return}F.pixelStorei(F.UNPACK_FLIP_Y_WEBGL,Q.flipY),F.pixelStorei(F.UNPACK_PREMULTIPLY_ALPHA_WEBGL,Q.premultiplyAlpha),F.pixelStorei(F.UNPACK_ALIGNMENT,Q.unpackAlignment);let Mt=F.getParameter(F.UNPACK_ROW_LENGTH),be=F.getParameter(F.UNPACK_IMAGE_HEIGHT),xn=F.getParameter(F.UNPACK_SKIP_PIXELS),Ne=F.getParameter(F.UNPACK_SKIP_ROWS),Ze=F.getParameter(F.UNPACK_SKIP_IMAGES),we=R.isCompressedTexture?R.mipmaps[J]:R.image;F.pixelStorei(F.UNPACK_ROW_LENGTH,we.width),F.pixelStorei(F.UNPACK_IMAGE_HEIGHT,we.height),F.pixelStorei(F.UNPACK_SKIP_PIXELS,A.min.x),F.pixelStorei(F.UNPACK_SKIP_ROWS,A.min.y),F.pixelStorei(F.UNPACK_SKIP_IMAGES,A.min.z),R.isDataTexture||R.isData3DTexture?F.texSubImage3D(yt,J,V.x,V.y,V.z,Ft,Gt,Qt,oe,dt,we.data):R.isCompressedArrayTexture?(console.warn("THREE.WebGLRenderer.copyTextureToTexture3D: untested support for compressed srcTexture."),F.compressedTexSubImage3D(yt,J,V.x,V.y,V.z,Ft,Gt,Qt,oe,we.data)):F.texSubImage3D(yt,J,V.x,V.y,V.z,Ft,Gt,Qt,oe,dt,we),F.pixelStorei(F.UNPACK_ROW_LENGTH,Mt),F.pixelStorei(F.UNPACK_IMAGE_HEIGHT,be),F.pixelStorei(F.UNPACK_SKIP_PIXELS,xn),F.pixelStorei(F.UNPACK_SKIP_ROWS,Ne),F.pixelStorei(F.UNPACK_SKIP_IMAGES,Ze),J===0&&Q.generateMipmaps&&F.generateMipmap(yt),ct.unbindTexture()},this.initTexture=function(A){A.isCubeTexture?T.setTextureCube(A,0):A.isData3DTexture?T.setTexture3D(A,0):A.isDataArrayTexture||A.isCompressedArrayTexture?T.setTexture2DArray(A,0):T.setTexture2D(A,0),ct.unbindTexture()},this.resetState=function(){H=0,U=0,N=null,ct.reset(),re.reset()},typeof __THREE_DEVTOOLS__!="undefined"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("observe",{detail:this}))}get coordinateSystem(){return Ti}get outputColorSpace(){return this._outputColorSpace}set outputColorSpace(t){this._outputColorSpace=t;let e=this.getContext();e.drawingBufferColorSpace=t===pc?"display-p3":"srgb",e.unpackColorSpace=Ue.workingColorSpace===_a?"display-p3":"srgb"}get outputEncoding(){return console.warn("THREE.WebGLRenderer: Property .outputEncoding has been removed. Use .outputColorSpace instead."),this.outputColorSpace===Je?ds:Wu}set outputEncoding(t){console.warn("THREE.WebGLRenderer: Property .outputEncoding has been removed. Use .outputColorSpace instead."),this.outputColorSpace=t===ds?Je:Ai}get useLegacyLights(){return console.warn("THREE.WebGLRenderer: The property .useLegacyLights has been deprecated. Migrate your lighting according to the following guide: https://discourse.threejs.org/t/updates-to-lighting-in-three-js-r155/53733."),this._useLegacyLights}set useLegacyLights(t){console.warn("THREE.WebGLRenderer: The property .useLegacyLights has been deprecated. Migrate your lighting according to the following guide: https://discourse.threejs.org/t/updates-to-lighting-in-three-js-r155/53733."),this._useLegacyLights=t}},Hl=class extends Fr{};Hl.prototype.isWebGL1Renderer=!0;var ta=class i{constructor(t,e=25e-5){this.isFogExp2=!0,this.name="",this.color=new ge(t),this.density=e}clone(){return new i(this.color,this.density)}toJSON(){return{type:"FogExp2",name:this.name,color:this.color.getHex(),density:this.density}}};var Or=class extends bn{constructor(){super(),this.isScene=!0,this.type="Scene",this.background=null,this.environment=null,this.fog=null,this.backgroundBlurriness=0,this.backgroundIntensity=1,this.overrideMaterial=null,typeof __THREE_DEVTOOLS__!="undefined"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("observe",{detail:this}))}copy(t,e){return super.copy(t,e),t.background!==null&&(this.background=t.background.clone()),t.environment!==null&&(this.environment=t.environment.clone()),t.fog!==null&&(this.fog=t.fog.clone()),this.backgroundBlurriness=t.backgroundBlurriness,this.backgroundIntensity=t.backgroundIntensity,t.overrideMaterial!==null&&(this.overrideMaterial=t.overrideMaterial.clone()),this.matrixAutoUpdate=t.matrixAutoUpdate,this}toJSON(t){let e=super.toJSON(t);return this.fog!==null&&(e.object.fog=this.fog.toJSON()),this.backgroundBlurriness>0&&(e.object.backgroundBlurriness=this.backgroundBlurriness),this.backgroundIntensity!==1&&(e.object.backgroundIntensity=this.backgroundIntensity),e}};var Pi=class extends gn{constructor(t,e,n,s=1){super(t,e,n),this.isInstancedBufferAttribute=!0,this.meshPerAttribute=s}copy(t){return super.copy(t),this.meshPerAttribute=t.meshPerAttribute,this}toJSON(){let t=super.toJSON();return t.meshPerAttribute=this.meshPerAttribute,t.isInstancedBufferAttribute=!0,t}},Vs=new De,Mu=new De,Po=[],Su=new Ci,b_=new De,vr=new Ce,yr=new Zi,ea=class extends Ce{constructor(t,e,n){super(t,e),this.isInstancedMesh=!0,this.instanceMatrix=new Pi(new Float32Array(n*16),16),this.instanceColor=null,this.count=n,this.boundingBox=null,this.boundingSphere=null;for(let s=0;s<n;s++)this.setMatrixAt(s,b_)}computeBoundingBox(){let t=this.geometry,e=this.count;this.boundingBox===null&&(this.boundingBox=new Ci),t.boundingBox===null&&t.computeBoundingBox(),this.boundingBox.makeEmpty();for(let n=0;n<e;n++)this.getMatrixAt(n,Vs),Su.copy(t.boundingBox).applyMatrix4(Vs),this.boundingBox.union(Su)}computeBoundingSphere(){let t=this.geometry,e=this.count;this.boundingSphere===null&&(this.boundingSphere=new Zi),t.boundingSphere===null&&t.computeBoundingSphere(),this.boundingSphere.makeEmpty();for(let n=0;n<e;n++)this.getMatrixAt(n,Vs),yr.copy(t.boundingSphere).applyMatrix4(Vs),this.boundingSphere.union(yr)}copy(t,e){return super.copy(t,e),this.instanceMatrix.copy(t.instanceMatrix),t.instanceColor!==null&&(this.instanceColor=t.instanceColor.clone()),this.count=t.count,t.boundingBox!==null&&(this.boundingBox=t.boundingBox.clone()),t.boundingSphere!==null&&(this.boundingSphere=t.boundingSphere.clone()),this}getColorAt(t,e){e.fromArray(this.instanceColor.array,t*3)}getMatrixAt(t,e){e.fromArray(this.instanceMatrix.array,t*16)}raycast(t,e){let n=this.matrixWorld,s=this.count;if(vr.geometry=this.geometry,vr.material=this.material,vr.material!==void 0&&(this.boundingSphere===null&&this.computeBoundingSphere(),yr.copy(this.boundingSphere),yr.applyMatrix4(n),t.ray.intersectsSphere(yr)!==!1))for(let r=0;r<s;r++){this.getMatrixAt(r,Vs),Mu.multiplyMatrices(n,Vs),vr.matrixWorld=Mu,vr.raycast(t,Po);for(let a=0,o=Po.length;a<o;a++){let l=Po[a];l.instanceId=r,l.object=this,e.push(l)}Po.length=0}}setColorAt(t,e){this.instanceColor===null&&(this.instanceColor=new Pi(new Float32Array(this.instanceMatrix.count*3),3)),e.toArray(this.instanceColor.array,t*3)}setMatrixAt(t,e){e.toArray(this.instanceMatrix.array,t*16)}updateMorphTargets(){}dispose(){this.dispatchEvent({type:"dispose"})}};var Br=class extends $i{constructor(t){super(),this.isPointsMaterial=!0,this.type="PointsMaterial",this.color=new ge(16777215),this.map=null,this.alphaMap=null,this.size=1,this.sizeAttenuation=!0,this.fog=!0,this.setValues(t)}copy(t){return super.copy(t),this.color.copy(t.color),this.map=t.map,this.alphaMap=t.alphaMap,this.size=t.size,this.sizeAttenuation=t.sizeAttenuation,this.fog=t.fog,this}},bu=new De,kl=new Ur,Io=new Zi,Lo=new O,na=class extends bn{constructor(t=new qe,e=new Br){super(),this.isPoints=!0,this.type="Points",this.geometry=t,this.material=e,this.updateMorphTargets()}copy(t,e){return super.copy(t,e),this.material=Array.isArray(t.material)?t.material.slice():t.material,this.geometry=t.geometry,this}raycast(t,e){let n=this.geometry,s=this.matrixWorld,r=t.params.Points.threshold,a=n.drawRange;if(n.boundingSphere===null&&n.computeBoundingSphere(),Io.copy(n.boundingSphere),Io.applyMatrix4(s),Io.radius+=r,t.ray.intersectsSphere(Io)===!1)return;bu.copy(s).invert(),kl.copy(t.ray).applyMatrix4(bu);let o=r/((this.scale.x+this.scale.y+this.scale.z)/3),l=o*o,c=n.index,u=n.attributes.position;if(c!==null){let d=Math.max(0,a.start),p=Math.min(c.count,a.start+a.count);for(let x=d,y=p;x<y;x++){let g=c.getX(x);Lo.fromBufferAttribute(u,g),Eu(Lo,g,l,s,t,e,this)}}else{let d=Math.max(0,a.start),p=Math.min(u.count,a.start+a.count);for(let x=d,y=p;x<y;x++)Lo.fromBufferAttribute(u,x),Eu(Lo,x,l,s,t,e,this)}}updateMorphTargets(){let e=this.geometry.morphAttributes,n=Object.keys(e);if(n.length>0){let s=e[n[0]];if(s!==void 0){this.morphTargetInfluences=[],this.morphTargetDictionary={};for(let r=0,a=s.length;r<a;r++){let o=s[r].name||String(r);this.morphTargetInfluences.push(0),this.morphTargetDictionary[o]=r}}}}};function Eu(i,t,e,n,s,r,a){let o=kl.distanceSqToPoint(i);if(o<e){let l=new O;kl.closestPointToPoint(i,l),l.applyMatrix4(n);let c=s.ray.origin.distanceTo(l);if(c<s.near||c>s.far)return;r.push({distance:c,distanceToRay:Math.sqrt(o),point:l,index:t,face:null,object:a})}}var ia=class extends Dn{constructor(t,e,n,s,r,a,o,l,c){super(t,e,n,s,r,a,o,l,c),this.isCanvasTexture=!0,this.needsUpdate=!0}},Gn=class{constructor(){this.type="Curve",this.arcLengthDivisions=200}getPoint(){return console.warn("THREE.Curve: .getPoint() not implemented."),null}getPointAt(t,e){let n=this.getUtoTmapping(t);return this.getPoint(n,e)}getPoints(t=5){let e=[];for(let n=0;n<=t;n++)e.push(this.getPoint(n/t));return e}getSpacedPoints(t=5){let e=[];for(let n=0;n<=t;n++)e.push(this.getPointAt(n/t));return e}getLength(){let t=this.getLengths();return t[t.length-1]}getLengths(t=this.arcLengthDivisions){if(this.cacheArcLengths&&this.cacheArcLengths.length===t+1&&!this.needsUpdate)return this.cacheArcLengths;this.needsUpdate=!1;let e=[],n,s=this.getPoint(0),r=0;e.push(0);for(let a=1;a<=t;a++)n=this.getPoint(a/t),r+=n.distanceTo(s),e.push(r),s=n;return this.cacheArcLengths=e,e}updateArcLengths(){this.needsUpdate=!0,this.getLengths()}getUtoTmapping(t,e){let n=this.getLengths(),s=0,r=n.length,a;e?a=e:a=t*n[r-1];let o=0,l=r-1,c;for(;o<=l;)if(s=Math.floor(o+(l-o)/2),c=n[s]-a,c<0)o=s+1;else if(c>0)l=s-1;else{l=s;break}if(s=l,n[s]===a)return s/(r-1);let h=n[s],d=n[s+1]-h,p=(a-h)/d;return(s+p)/(r-1)}getTangent(t,e){let s=t-1e-4,r=t+1e-4;s<0&&(s=0),r>1&&(r=1);let a=this.getPoint(s),o=this.getPoint(r),l=e||(a.isVector2?new xt:new O);return l.copy(o).sub(a).normalize(),l}getTangentAt(t,e){let n=this.getUtoTmapping(t);return this.getTangent(n,e)}computeFrenetFrames(t,e){let n=new O,s=[],r=[],a=[],o=new O,l=new De;for(let p=0;p<=t;p++){let x=p/t;s[p]=this.getTangentAt(x,new O)}r[0]=new O,a[0]=new O;let c=Number.MAX_VALUE,h=Math.abs(s[0].x),u=Math.abs(s[0].y),d=Math.abs(s[0].z);h<=c&&(c=h,n.set(1,0,0)),u<=c&&(c=u,n.set(0,1,0)),d<=c&&n.set(0,0,1),o.crossVectors(s[0],n).normalize(),r[0].crossVectors(s[0],o),a[0].crossVectors(s[0],r[0]);for(let p=1;p<=t;p++){if(r[p]=r[p-1].clone(),a[p]=a[p-1].clone(),o.crossVectors(s[p-1],s[p]),o.length()>Number.EPSILON){o.normalize();let x=Math.acos(cn(s[p-1].dot(s[p]),-1,1));r[p].applyMatrix4(l.makeRotationAxis(o,x))}a[p].crossVectors(s[p],r[p])}if(e===!0){let p=Math.acos(cn(r[0].dot(r[t]),-1,1));p/=t,s[0].dot(o.crossVectors(r[0],r[t]))>0&&(p=-p);for(let x=1;x<=t;x++)r[x].applyMatrix4(l.makeRotationAxis(s[x],p*x)),a[x].crossVectors(s[x],r[x])}return{tangents:s,normals:r,binormals:a}}clone(){return new this.constructor().copy(this)}copy(t){return this.arcLengthDivisions=t.arcLengthDivisions,this}toJSON(){let t={metadata:{version:4.6,type:"Curve",generator:"Curve.toJSON"}};return t.arcLengthDivisions=this.arcLengthDivisions,t.type=this.type,t}fromJSON(t){return this.arcLengthDivisions=t.arcLengthDivisions,this}},zr=class extends Gn{constructor(t=0,e=0,n=1,s=1,r=0,a=Math.PI*2,o=!1,l=0){super(),this.isEllipseCurve=!0,this.type="EllipseCurve",this.aX=t,this.aY=e,this.xRadius=n,this.yRadius=s,this.aStartAngle=r,this.aEndAngle=a,this.aClockwise=o,this.aRotation=l}getPoint(t,e){let n=e||new xt,s=Math.PI*2,r=this.aEndAngle-this.aStartAngle,a=Math.abs(r)<Number.EPSILON;for(;r<0;)r+=s;for(;r>s;)r-=s;r<Number.EPSILON&&(a?r=0:r=s),this.aClockwise===!0&&!a&&(r===s?r=-s:r=r-s);let o=this.aStartAngle+t*r,l=this.aX+this.xRadius*Math.cos(o),c=this.aY+this.yRadius*Math.sin(o);if(this.aRotation!==0){let h=Math.cos(this.aRotation),u=Math.sin(this.aRotation),d=l-this.aX,p=c-this.aY;l=d*h-p*u+this.aX,c=d*u+p*h+this.aY}return n.set(l,c)}copy(t){return super.copy(t),this.aX=t.aX,this.aY=t.aY,this.xRadius=t.xRadius,this.yRadius=t.yRadius,this.aStartAngle=t.aStartAngle,this.aEndAngle=t.aEndAngle,this.aClockwise=t.aClockwise,this.aRotation=t.aRotation,this}toJSON(){let t=super.toJSON();return t.aX=this.aX,t.aY=this.aY,t.xRadius=this.xRadius,t.yRadius=this.yRadius,t.aStartAngle=this.aStartAngle,t.aEndAngle=this.aEndAngle,t.aClockwise=this.aClockwise,t.aRotation=this.aRotation,t}fromJSON(t){return super.fromJSON(t),this.aX=t.aX,this.aY=t.aY,this.xRadius=t.xRadius,this.yRadius=t.yRadius,this.aStartAngle=t.aStartAngle,this.aEndAngle=t.aEndAngle,this.aClockwise=t.aClockwise,this.aRotation=t.aRotation,this}},Vl=class extends zr{constructor(t,e,n,s,r,a){super(t,e,n,n,s,r,a),this.isArcCurve=!0,this.type="ArcCurve"}};function xc(){let i=0,t=0,e=0,n=0;function s(r,a,o,l){i=r,t=o,e=-3*r+3*a-2*o-l,n=2*r-2*a+o+l}return{initCatmullRom:function(r,a,o,l,c){s(a,o,c*(o-r),c*(l-a))},initNonuniformCatmullRom:function(r,a,o,l,c,h,u){let d=(a-r)/c-(o-r)/(c+h)+(o-a)/h,p=(o-a)/h-(l-a)/(h+u)+(l-o)/u;d*=h,p*=h,s(a,o,d,p)},calc:function(r){let a=r*r,o=a*r;return i+t*r+e*a+n*o}}}var Uo=new O,pl=new xc,ml=new xc,gl=new xc,Gl=class extends Gn{constructor(t=[],e=!1,n="centripetal",s=.5){super(),this.isCatmullRomCurve3=!0,this.type="CatmullRomCurve3",this.points=t,this.closed=e,this.curveType=n,this.tension=s}getPoint(t,e=new O){let n=e,s=this.points,r=s.length,a=(r-(this.closed?0:1))*t,o=Math.floor(a),l=a-o;this.closed?o+=o>0?0:(Math.floor(Math.abs(o)/r)+1)*r:l===0&&o===r-1&&(o=r-2,l=1);let c,h;this.closed||o>0?c=s[(o-1)%r]:(Uo.subVectors(s[0],s[1]).add(s[0]),c=Uo);let u=s[o%r],d=s[(o+1)%r];if(this.closed||o+2<r?h=s[(o+2)%r]:(Uo.subVectors(s[r-1],s[r-2]).add(s[r-1]),h=Uo),this.curveType==="centripetal"||this.curveType==="chordal"){let p=this.curveType==="chordal"?.5:.25,x=Math.pow(c.distanceToSquared(u),p),y=Math.pow(u.distanceToSquared(d),p),g=Math.pow(d.distanceToSquared(h),p);y<1e-4&&(y=1),x<1e-4&&(x=y),g<1e-4&&(g=y),pl.initNonuniformCatmullRom(c.x,u.x,d.x,h.x,x,y,g),ml.initNonuniformCatmullRom(c.y,u.y,d.y,h.y,x,y,g),gl.initNonuniformCatmullRom(c.z,u.z,d.z,h.z,x,y,g)}else this.curveType==="catmullrom"&&(pl.initCatmullRom(c.x,u.x,d.x,h.x,this.tension),ml.initCatmullRom(c.y,u.y,d.y,h.y,this.tension),gl.initCatmullRom(c.z,u.z,d.z,h.z,this.tension));return n.set(pl.calc(l),ml.calc(l),gl.calc(l)),n}copy(t){super.copy(t),this.points=[];for(let e=0,n=t.points.length;e<n;e++){let s=t.points[e];this.points.push(s.clone())}return this.closed=t.closed,this.curveType=t.curveType,this.tension=t.tension,this}toJSON(){let t=super.toJSON();t.points=[];for(let e=0,n=this.points.length;e<n;e++){let s=this.points[e];t.points.push(s.toArray())}return t.closed=this.closed,t.curveType=this.curveType,t.tension=this.tension,t}fromJSON(t){super.fromJSON(t),this.points=[];for(let e=0,n=t.points.length;e<n;e++){let s=t.points[e];this.points.push(new O().fromArray(s))}return this.closed=t.closed,this.curveType=t.curveType,this.tension=t.tension,this}};function wu(i,t,e,n,s){let r=(n-t)*.5,a=(s-e)*.5,o=i*i,l=i*o;return(2*e-2*n+r+a)*l+(-3*e+3*n-2*r-a)*o+r*i+e}function E_(i,t){let e=1-i;return e*e*t}function w_(i,t){return 2*(1-i)*i*t}function T_(i,t){return i*i*t}function Tr(i,t,e,n){return E_(i,t)+w_(i,e)+T_(i,n)}function A_(i,t){let e=1-i;return e*e*e*t}function R_(i,t){let e=1-i;return 3*e*e*i*t}function C_(i,t){return 3*(1-i)*i*i*t}function P_(i,t){return i*i*i*t}function Ar(i,t,e,n,s){return A_(i,t)+R_(i,e)+C_(i,n)+P_(i,s)}var sa=class extends Gn{constructor(t=new xt,e=new xt,n=new xt,s=new xt){super(),this.isCubicBezierCurve=!0,this.type="CubicBezierCurve",this.v0=t,this.v1=e,this.v2=n,this.v3=s}getPoint(t,e=new xt){let n=e,s=this.v0,r=this.v1,a=this.v2,o=this.v3;return n.set(Ar(t,s.x,r.x,a.x,o.x),Ar(t,s.y,r.y,a.y,o.y)),n}copy(t){return super.copy(t),this.v0.copy(t.v0),this.v1.copy(t.v1),this.v2.copy(t.v2),this.v3.copy(t.v3),this}toJSON(){let t=super.toJSON();return t.v0=this.v0.toArray(),t.v1=this.v1.toArray(),t.v2=this.v2.toArray(),t.v3=this.v3.toArray(),t}fromJSON(t){return super.fromJSON(t),this.v0.fromArray(t.v0),this.v1.fromArray(t.v1),this.v2.fromArray(t.v2),this.v3.fromArray(t.v3),this}},Wl=class extends Gn{constructor(t=new O,e=new O,n=new O,s=new O){super(),this.isCubicBezierCurve3=!0,this.type="CubicBezierCurve3",this.v0=t,this.v1=e,this.v2=n,this.v3=s}getPoint(t,e=new O){let n=e,s=this.v0,r=this.v1,a=this.v2,o=this.v3;return n.set(Ar(t,s.x,r.x,a.x,o.x),Ar(t,s.y,r.y,a.y,o.y),Ar(t,s.z,r.z,a.z,o.z)),n}copy(t){return super.copy(t),this.v0.copy(t.v0),this.v1.copy(t.v1),this.v2.copy(t.v2),this.v3.copy(t.v3),this}toJSON(){let t=super.toJSON();return t.v0=this.v0.toArray(),t.v1=this.v1.toArray(),t.v2=this.v2.toArray(),t.v3=this.v3.toArray(),t}fromJSON(t){return super.fromJSON(t),this.v0.fromArray(t.v0),this.v1.fromArray(t.v1),this.v2.fromArray(t.v2),this.v3.fromArray(t.v3),this}},ra=class extends Gn{constructor(t=new xt,e=new xt){super(),this.isLineCurve=!0,this.type="LineCurve",this.v1=t,this.v2=e}getPoint(t,e=new xt){let n=e;return t===1?n.copy(this.v2):(n.copy(this.v2).sub(this.v1),n.multiplyScalar(t).add(this.v1)),n}getPointAt(t,e){return this.getPoint(t,e)}getTangent(t,e=new xt){return e.subVectors(this.v2,this.v1).normalize()}getTangentAt(t,e){return this.getTangent(t,e)}copy(t){return super.copy(t),this.v1.copy(t.v1),this.v2.copy(t.v2),this}toJSON(){let t=super.toJSON();return t.v1=this.v1.toArray(),t.v2=this.v2.toArray(),t}fromJSON(t){return super.fromJSON(t),this.v1.fromArray(t.v1),this.v2.fromArray(t.v2),this}},Xl=class extends Gn{constructor(t=new O,e=new O){super(),this.isLineCurve3=!0,this.type="LineCurve3",this.v1=t,this.v2=e}getPoint(t,e=new O){let n=e;return t===1?n.copy(this.v2):(n.copy(this.v2).sub(this.v1),n.multiplyScalar(t).add(this.v1)),n}getPointAt(t,e){return this.getPoint(t,e)}getTangent(t,e=new O){return e.subVectors(this.v2,this.v1).normalize()}getTangentAt(t,e){return this.getTangent(t,e)}copy(t){return super.copy(t),this.v1.copy(t.v1),this.v2.copy(t.v2),this}toJSON(){let t=super.toJSON();return t.v1=this.v1.toArray(),t.v2=this.v2.toArray(),t}fromJSON(t){return super.fromJSON(t),this.v1.fromArray(t.v1),this.v2.fromArray(t.v2),this}},oa=class extends Gn{constructor(t=new xt,e=new xt,n=new xt){super(),this.isQuadraticBezierCurve=!0,this.type="QuadraticBezierCurve",this.v0=t,this.v1=e,this.v2=n}getPoint(t,e=new xt){let n=e,s=this.v0,r=this.v1,a=this.v2;return n.set(Tr(t,s.x,r.x,a.x),Tr(t,s.y,r.y,a.y)),n}copy(t){return super.copy(t),this.v0.copy(t.v0),this.v1.copy(t.v1),this.v2.copy(t.v2),this}toJSON(){let t=super.toJSON();return t.v0=this.v0.toArray(),t.v1=this.v1.toArray(),t.v2=this.v2.toArray(),t}fromJSON(t){return super.fromJSON(t),this.v0.fromArray(t.v0),this.v1.fromArray(t.v1),this.v2.fromArray(t.v2),this}},Yl=class extends Gn{constructor(t=new O,e=new O,n=new O){super(),this.isQuadraticBezierCurve3=!0,this.type="QuadraticBezierCurve3",this.v0=t,this.v1=e,this.v2=n}getPoint(t,e=new O){let n=e,s=this.v0,r=this.v1,a=this.v2;return n.set(Tr(t,s.x,r.x,a.x),Tr(t,s.y,r.y,a.y),Tr(t,s.z,r.z,a.z)),n}copy(t){return super.copy(t),this.v0.copy(t.v0),this.v1.copy(t.v1),this.v2.copy(t.v2),this}toJSON(){let t=super.toJSON();return t.v0=this.v0.toArray(),t.v1=this.v1.toArray(),t.v2=this.v2.toArray(),t}fromJSON(t){return super.fromJSON(t),this.v0.fromArray(t.v0),this.v1.fromArray(t.v1),this.v2.fromArray(t.v2),this}},aa=class extends Gn{constructor(t=[]){super(),this.isSplineCurve=!0,this.type="SplineCurve",this.points=t}getPoint(t,e=new xt){let n=e,s=this.points,r=(s.length-1)*t,a=Math.floor(r),o=r-a,l=s[a===0?a:a-1],c=s[a],h=s[a>s.length-2?s.length-1:a+1],u=s[a>s.length-3?s.length-1:a+2];return n.set(wu(o,l.x,c.x,h.x,u.x),wu(o,l.y,c.y,h.y,u.y)),n}copy(t){super.copy(t),this.points=[];for(let e=0,n=t.points.length;e<n;e++){let s=t.points[e];this.points.push(s.clone())}return this}toJSON(){let t=super.toJSON();t.points=[];for(let e=0,n=this.points.length;e<n;e++){let s=this.points[e];t.points.push(s.toArray())}return t}fromJSON(t){super.fromJSON(t),this.points=[];for(let e=0,n=t.points.length;e<n;e++){let s=t.points[e];this.points.push(new xt().fromArray(s))}return this}},ql=Object.freeze({__proto__:null,ArcCurve:Vl,CatmullRomCurve3:Gl,CubicBezierCurve:sa,CubicBezierCurve3:Wl,EllipseCurve:zr,LineCurve:ra,LineCurve3:Xl,QuadraticBezierCurve:oa,QuadraticBezierCurve3:Yl,SplineCurve:aa}),Zl=class extends Gn{constructor(){super(),this.type="CurvePath",this.curves=[],this.autoClose=!1}add(t){this.curves.push(t)}closePath(){let t=this.curves[0].getPoint(0),e=this.curves[this.curves.length-1].getPoint(1);if(!t.equals(e)){let n=t.isVector2===!0?"LineCurve":"LineCurve3";this.curves.push(new ql[n](e,t))}return this}getPoint(t,e){let n=t*this.getLength(),s=this.getCurveLengths(),r=0;for(;r<s.length;){if(s[r]>=n){let a=s[r]-n,o=this.curves[r],l=o.getLength(),c=l===0?0:1-a/l;return o.getPointAt(c,e)}r++}return null}getLength(){let t=this.getCurveLengths();return t[t.length-1]}updateArcLengths(){this.needsUpdate=!0,this.cacheLengths=null,this.getCurveLengths()}getCurveLengths(){if(this.cacheLengths&&this.cacheLengths.length===this.curves.length)return this.cacheLengths;let t=[],e=0;for(let n=0,s=this.curves.length;n<s;n++)e+=this.curves[n].getLength(),t.push(e);return this.cacheLengths=t,t}getSpacedPoints(t=40){let e=[];for(let n=0;n<=t;n++)e.push(this.getPoint(n/t));return this.autoClose&&e.push(e[0]),e}getPoints(t=12){let e=[],n;for(let s=0,r=this.curves;s<r.length;s++){let a=r[s],o=a.isEllipseCurve?t*2:a.isLineCurve||a.isLineCurve3?1:a.isSplineCurve?t*a.points.length:t,l=a.getPoints(o);for(let c=0;c<l.length;c++){let h=l[c];n&&n.equals(h)||(e.push(h),n=h)}}return this.autoClose&&e.length>1&&!e[e.length-1].equals(e[0])&&e.push(e[0]),e}copy(t){super.copy(t),this.curves=[];for(let e=0,n=t.curves.length;e<n;e++){let s=t.curves[e];this.curves.push(s.clone())}return this.autoClose=t.autoClose,this}toJSON(){let t=super.toJSON();t.autoClose=this.autoClose,t.curves=[];for(let e=0,n=this.curves.length;e<n;e++){let s=this.curves[e];t.curves.push(s.toJSON())}return t}fromJSON(t){super.fromJSON(t),this.autoClose=t.autoClose,this.curves=[];for(let e=0,n=t.curves.length;e<n;e++){let s=t.curves[e];this.curves.push(new ql[s.type]().fromJSON(s))}return this}},sr=class extends Zl{constructor(t){super(),this.type="Path",this.currentPoint=new xt,t&&this.setFromPoints(t)}setFromPoints(t){this.moveTo(t[0].x,t[0].y);for(let e=1,n=t.length;e<n;e++)this.lineTo(t[e].x,t[e].y);return this}moveTo(t,e){return this.currentPoint.set(t,e),this}lineTo(t,e){let n=new ra(this.currentPoint.clone(),new xt(t,e));return this.curves.push(n),this.currentPoint.set(t,e),this}quadraticCurveTo(t,e,n,s){let r=new oa(this.currentPoint.clone(),new xt(t,e),new xt(n,s));return this.curves.push(r),this.currentPoint.set(n,s),this}bezierCurveTo(t,e,n,s,r,a){let o=new sa(this.currentPoint.clone(),new xt(t,e),new xt(n,s),new xt(r,a));return this.curves.push(o),this.currentPoint.set(r,a),this}splineThru(t){let e=[this.currentPoint.clone()].concat(t),n=new aa(e);return this.curves.push(n),this.currentPoint.copy(t[t.length-1]),this}arc(t,e,n,s,r,a){let o=this.currentPoint.x,l=this.currentPoint.y;return this.absarc(t+o,e+l,n,s,r,a),this}absarc(t,e,n,s,r,a){return this.absellipse(t,e,n,n,s,r,a),this}ellipse(t,e,n,s,r,a,o,l){let c=this.currentPoint.x,h=this.currentPoint.y;return this.absellipse(t+c,e+h,n,s,r,a,o,l),this}absellipse(t,e,n,s,r,a,o,l){let c=new zr(t,e,n,s,r,a,o,l);if(this.curves.length>0){let u=c.getPoint(0);u.equals(this.currentPoint)||this.lineTo(u.x,u.y)}this.curves.push(c);let h=c.getPoint(1);return this.currentPoint.copy(h),this}copy(t){return super.copy(t),this.currentPoint.copy(t.currentPoint),this}toJSON(){let t=super.toJSON();return t.currentPoint=this.currentPoint.toArray(),t}fromJSON(t){return super.fromJSON(t),this.currentPoint.fromArray(t.currentPoint),this}},Hr=class i extends qe{constructor(t=[new xt(0,-.5),new xt(.5,0),new xt(0,.5)],e=12,n=0,s=Math.PI*2){super(),this.type="LatheGeometry",this.parameters={points:t,segments:e,phiStart:n,phiLength:s},e=Math.floor(e),s=cn(s,0,Math.PI*2);let r=[],a=[],o=[],l=[],c=[],h=1/e,u=new O,d=new xt,p=new O,x=new O,y=new O,g=0,m=0;for(let w=0;w<=t.length-1;w++)switch(w){case 0:g=t[w+1].x-t[w].x,m=t[w+1].y-t[w].y,p.x=m*1,p.y=-g,p.z=m*0,y.copy(p),p.normalize(),l.push(p.x,p.y,p.z);break;case t.length-1:l.push(y.x,y.y,y.z);break;default:g=t[w+1].x-t[w].x,m=t[w+1].y-t[w].y,p.x=m*1,p.y=-g,p.z=m*0,x.copy(p),p.x+=y.x,p.y+=y.y,p.z+=y.z,p.normalize(),l.push(p.x,p.y,p.z),y.copy(x)}for(let w=0;w<=e;w++){let v=n+w*h*s,I=Math.sin(v),H=Math.cos(v);for(let U=0;U<=t.length-1;U++){u.x=t[U].x*I,u.y=t[U].y,u.z=t[U].x*H,a.push(u.x,u.y,u.z),d.x=w/e,d.y=U/(t.length-1),o.push(d.x,d.y);let N=l[3*U+0]*I,Y=l[3*U+1],b=l[3*U+0]*H;c.push(N,Y,b)}}for(let w=0;w<e;w++)for(let v=0;v<t.length-1;v++){let I=v+w*t.length,H=I,U=I+t.length,N=I+t.length+1,Y=I+1;r.push(H,U,Y),r.push(N,Y,U)}this.setIndex(r),this.setAttribute("position",new _e(a,3)),this.setAttribute("uv",new _e(o,2)),this.setAttribute("normal",new _e(c,3))}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.points,t.segments,t.phiStart,t.phiLength)}};var rr=class i extends qe{constructor(t=1,e=32,n=0,s=Math.PI*2){super(),this.type="CircleGeometry",this.parameters={radius:t,segments:e,thetaStart:n,thetaLength:s},e=Math.max(3,e);let r=[],a=[],o=[],l=[],c=new O,h=new xt;a.push(0,0,0),o.push(0,0,1),l.push(.5,.5);for(let u=0,d=3;u<=e;u++,d+=3){let p=n+u/e*s;c.x=t*Math.cos(p),c.y=t*Math.sin(p),a.push(c.x,c.y,c.z),o.push(0,0,1),h.x=(a[d]/t+1)/2,h.y=(a[d+1]/t+1)/2,l.push(h.x,h.y)}for(let u=1;u<=e;u++)r.push(u,u+1,0);this.setIndex(r),this.setAttribute("position",new _e(a,3)),this.setAttribute("normal",new _e(o,3)),this.setAttribute("uv",new _e(l,2))}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.radius,t.segments,t.thetaStart,t.thetaLength)}},rn=class i extends qe{constructor(t=1,e=1,n=1,s=32,r=1,a=!1,o=0,l=Math.PI*2){super(),this.type="CylinderGeometry",this.parameters={radiusTop:t,radiusBottom:e,height:n,radialSegments:s,heightSegments:r,openEnded:a,thetaStart:o,thetaLength:l};let c=this;s=Math.floor(s),r=Math.floor(r);let h=[],u=[],d=[],p=[],x=0,y=[],g=n/2,m=0;w(),a===!1&&(t>0&&v(!0),e>0&&v(!1)),this.setIndex(h),this.setAttribute("position",new _e(u,3)),this.setAttribute("normal",new _e(d,3)),this.setAttribute("uv",new _e(p,2));function w(){let I=new O,H=new O,U=0,N=(e-t)/n;for(let Y=0;Y<=r;Y++){let b=[],P=Y/r,X=P*(e-t)+t;for(let rt=0;rt<=s;rt++){let _t=rt/s,k=_t*l+o,q=Math.sin(k),j=Math.cos(k);H.x=X*q,H.y=-P*n+g,H.z=X*j,u.push(H.x,H.y,H.z),I.set(q,N,j).normalize(),d.push(I.x,I.y,I.z),p.push(_t,1-P),b.push(x++)}y.push(b)}for(let Y=0;Y<s;Y++)for(let b=0;b<r;b++){let P=y[b][Y],X=y[b+1][Y],rt=y[b+1][Y+1],_t=y[b][Y+1];h.push(P,X,_t),h.push(X,rt,_t),U+=6}c.addGroup(m,U,0),m+=U}function v(I){let H=x,U=new xt,N=new O,Y=0,b=I===!0?t:e,P=I===!0?1:-1;for(let rt=1;rt<=s;rt++)u.push(0,g*P,0),d.push(0,P,0),p.push(.5,.5),x++;let X=x;for(let rt=0;rt<=s;rt++){let k=rt/s*l+o,q=Math.cos(k),j=Math.sin(k);N.x=b*j,N.y=g*P,N.z=b*q,u.push(N.x,N.y,N.z),d.push(0,P,0),U.x=q*.5+.5,U.y=j*.5*P+.5,p.push(U.x,U.y),x++}for(let rt=0;rt<s;rt++){let _t=H+rt,k=X+rt;I===!0?h.push(k,k+1,_t):h.push(k+1,k,_t),Y+=3}c.addGroup(m,Y,I===!0?1:2),m+=Y}}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.radiusTop,t.radiusBottom,t.height,t.radialSegments,t.heightSegments,t.openEnded,t.thetaStart,t.thetaLength)}},kr=class i extends rn{constructor(t=1,e=1,n=32,s=1,r=!1,a=0,o=Math.PI*2){super(0,t,e,n,s,r,a,o),this.type="ConeGeometry",this.parameters={radius:t,height:e,radialSegments:n,heightSegments:s,openEnded:r,thetaStart:a,thetaLength:o}}static fromJSON(t){return new i(t.radius,t.height,t.radialSegments,t.heightSegments,t.openEnded,t.thetaStart,t.thetaLength)}},Vr=class i extends qe{constructor(t=[],e=[],n=1,s=0){super(),this.type="PolyhedronGeometry",this.parameters={vertices:t,indices:e,radius:n,detail:s};let r=[],a=[];o(s),c(n),h(),this.setAttribute("position",new _e(r,3)),this.setAttribute("normal",new _e(r.slice(),3)),this.setAttribute("uv",new _e(a,2)),s===0?this.computeVertexNormals():this.normalizeNormals();function o(w){let v=new O,I=new O,H=new O;for(let U=0;U<e.length;U+=3)p(e[U+0],v),p(e[U+1],I),p(e[U+2],H),l(v,I,H,w)}function l(w,v,I,H){let U=H+1,N=[];for(let Y=0;Y<=U;Y++){N[Y]=[];let b=w.clone().lerp(I,Y/U),P=v.clone().lerp(I,Y/U),X=U-Y;for(let rt=0;rt<=X;rt++)rt===0&&Y===U?N[Y][rt]=b:N[Y][rt]=b.clone().lerp(P,rt/X)}for(let Y=0;Y<U;Y++)for(let b=0;b<2*(U-Y)-1;b++){let P=Math.floor(b/2);b%2===0?(d(N[Y][P+1]),d(N[Y+1][P]),d(N[Y][P])):(d(N[Y][P+1]),d(N[Y+1][P+1]),d(N[Y+1][P]))}}function c(w){let v=new O;for(let I=0;I<r.length;I+=3)v.x=r[I+0],v.y=r[I+1],v.z=r[I+2],v.normalize().multiplyScalar(w),r[I+0]=v.x,r[I+1]=v.y,r[I+2]=v.z}function h(){let w=new O;for(let v=0;v<r.length;v+=3){w.x=r[v+0],w.y=r[v+1],w.z=r[v+2];let I=g(w)/2/Math.PI+.5,H=m(w)/Math.PI+.5;a.push(I,1-H)}x(),u()}function u(){for(let w=0;w<a.length;w+=6){let v=a[w+0],I=a[w+2],H=a[w+4],U=Math.max(v,I,H),N=Math.min(v,I,H);U>.9&&N<.1&&(v<.2&&(a[w+0]+=1),I<.2&&(a[w+2]+=1),H<.2&&(a[w+4]+=1))}}function d(w){r.push(w.x,w.y,w.z)}function p(w,v){let I=w*3;v.x=t[I+0],v.y=t[I+1],v.z=t[I+2]}function x(){let w=new O,v=new O,I=new O,H=new O,U=new xt,N=new xt,Y=new xt;for(let b=0,P=0;b<r.length;b+=9,P+=6){w.set(r[b+0],r[b+1],r[b+2]),v.set(r[b+3],r[b+4],r[b+5]),I.set(r[b+6],r[b+7],r[b+8]),U.set(a[P+0],a[P+1]),N.set(a[P+2],a[P+3]),Y.set(a[P+4],a[P+5]),H.copy(w).add(v).add(I).divideScalar(3);let X=g(H);y(U,P+0,w,X),y(N,P+2,v,X),y(Y,P+4,I,X)}}function y(w,v,I,H){H<0&&w.x===1&&(a[v]=w.x-1),I.x===0&&I.z===0&&(a[v]=H/2/Math.PI+.5)}function g(w){return Math.atan2(w.z,-w.x)}function m(w){return Math.atan2(-w.y,Math.sqrt(w.x*w.x+w.z*w.z))}}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.vertices,t.indices,t.radius,t.details)}},Gr=class i extends Vr{constructor(t=1,e=0){let n=(1+Math.sqrt(5))/2,s=1/n,r=[-1,-1,-1,-1,-1,1,-1,1,-1,-1,1,1,1,-1,-1,1,-1,1,1,1,-1,1,1,1,0,-s,-n,0,-s,n,0,s,-n,0,s,n,-s,-n,0,-s,n,0,s,-n,0,s,n,0,-n,0,-s,n,0,-s,-n,0,s,n,0,s],a=[3,11,7,3,7,15,3,15,13,7,19,17,7,17,6,7,6,15,17,4,8,17,8,10,17,10,6,8,0,16,8,16,2,8,2,10,0,12,1,0,1,18,0,18,16,6,10,2,6,2,13,6,13,15,2,16,18,2,18,3,2,3,13,18,1,9,18,9,11,18,11,3,4,14,12,4,12,0,4,0,8,11,9,5,11,5,19,11,19,7,19,5,14,19,14,4,19,4,17,1,12,14,1,14,5,1,5,9];super(r,a,t,e),this.type="DodecahedronGeometry",this.parameters={radius:t,detail:e}}static fromJSON(t){return new i(t.radius,t.detail)}};var fi=class extends sr{constructor(t){super(t),this.uuid=ys(),this.type="Shape",this.holes=[]}getPointsHoles(t){let e=[];for(let n=0,s=this.holes.length;n<s;n++)e[n]=this.holes[n].getPoints(t);return e}extractPoints(t){return{shape:this.getPoints(t),holes:this.getPointsHoles(t)}}copy(t){super.copy(t),this.holes=[];for(let e=0,n=t.holes.length;e<n;e++){let s=t.holes[e];this.holes.push(s.clone())}return this}toJSON(){let t=super.toJSON();t.uuid=this.uuid,t.holes=[];for(let e=0,n=this.holes.length;e<n;e++){let s=this.holes[e];t.holes.push(s.toJSON())}return t}fromJSON(t){super.fromJSON(t),this.uuid=t.uuid,this.holes=[];for(let e=0,n=t.holes.length;e<n;e++){let s=t.holes[e];this.holes.push(new sr().fromJSON(s))}return this}},I_={triangulate:function(i,t,e=2){let n=t&&t.length,s=n?t[0]*e:i.length,r=nf(i,0,s,e,!0),a=[];if(!r||r.next===r.prev)return a;let o,l,c,h,u,d,p;if(n&&(r=F_(i,t,r,e)),i.length>80*e){o=c=i[0],l=h=i[1];for(let x=e;x<s;x+=e)u=i[x],d=i[x+1],u<o&&(o=u),d<l&&(l=d),u>c&&(c=u),d>h&&(h=d);p=Math.max(c-o,h-l),p=p!==0?32767/p:0}return Wr(r,a,e,o,l,p,0),a}};function nf(i,t,e,n,s){let r,a;if(s===q_(i,t,e,n)>0)for(r=t;r<e;r+=n)a=Tu(r,i[r],i[r+1],a);else for(r=e-n;r>=t;r-=n)a=Tu(r,i[r],i[r+1],a);return a&&va(a,a.next)&&(Yr(a),a=a.next),a}function _s(i,t){if(!i)return i;t||(t=i);let e=i,n;do if(n=!1,!e.steiner&&(va(e,e.next)||Ye(e.prev,e,e.next)===0)){if(Yr(e),e=t=e.prev,e===e.next)break;n=!0}else e=e.next;while(n||e!==t);return t}function Wr(i,t,e,n,s,r,a){if(!i)return;!a&&r&&k_(i,n,s,r);let o=i,l,c;for(;i.prev!==i.next;){if(l=i.prev,c=i.next,r?U_(i,n,s,r):L_(i)){t.push(l.i/e|0),t.push(i.i/e|0),t.push(c.i/e|0),Yr(i),i=c.next,o=c.next;continue}if(i=c,i===o){a?a===1?(i=D_(_s(i),t,e),Wr(i,t,e,n,s,r,2)):a===2&&N_(i,t,e,n,s,r):Wr(_s(i),t,e,n,s,r,1);break}}}function L_(i){let t=i.prev,e=i,n=i.next;if(Ye(t,e,n)>=0)return!1;let s=t.x,r=e.x,a=n.x,o=t.y,l=e.y,c=n.y,h=s<r?s<a?s:a:r<a?r:a,u=o<l?o<c?o:c:l<c?l:c,d=s>r?s>a?s:a:r>a?r:a,p=o>l?o>c?o:c:l>c?l:c,x=n.next;for(;x!==t;){if(x.x>=h&&x.x<=d&&x.y>=u&&x.y<=p&&Zs(s,o,r,l,a,c,x.x,x.y)&&Ye(x.prev,x,x.next)>=0)return!1;x=x.next}return!0}function U_(i,t,e,n){let s=i.prev,r=i,a=i.next;if(Ye(s,r,a)>=0)return!1;let o=s.x,l=r.x,c=a.x,h=s.y,u=r.y,d=a.y,p=o<l?o<c?o:c:l<c?l:c,x=h<u?h<d?h:d:u<d?u:d,y=o>l?o>c?o:c:l>c?l:c,g=h>u?h>d?h:d:u>d?u:d,m=$l(p,x,t,e,n),w=$l(y,g,t,e,n),v=i.prevZ,I=i.nextZ;for(;v&&v.z>=m&&I&&I.z<=w;){if(v.x>=p&&v.x<=y&&v.y>=x&&v.y<=g&&v!==s&&v!==a&&Zs(o,h,l,u,c,d,v.x,v.y)&&Ye(v.prev,v,v.next)>=0||(v=v.prevZ,I.x>=p&&I.x<=y&&I.y>=x&&I.y<=g&&I!==s&&I!==a&&Zs(o,h,l,u,c,d,I.x,I.y)&&Ye(I.prev,I,I.next)>=0))return!1;I=I.nextZ}for(;v&&v.z>=m;){if(v.x>=p&&v.x<=y&&v.y>=x&&v.y<=g&&v!==s&&v!==a&&Zs(o,h,l,u,c,d,v.x,v.y)&&Ye(v.prev,v,v.next)>=0)return!1;v=v.prevZ}for(;I&&I.z<=w;){if(I.x>=p&&I.x<=y&&I.y>=x&&I.y<=g&&I!==s&&I!==a&&Zs(o,h,l,u,c,d,I.x,I.y)&&Ye(I.prev,I,I.next)>=0)return!1;I=I.nextZ}return!0}function D_(i,t,e){let n=i;do{let s=n.prev,r=n.next.next;!va(s,r)&&sf(s,n,n.next,r)&&Xr(s,r)&&Xr(r,s)&&(t.push(s.i/e|0),t.push(n.i/e|0),t.push(r.i/e|0),Yr(n),Yr(n.next),n=i=r),n=n.next}while(n!==i);return _s(n)}function N_(i,t,e,n,s,r){let a=i;do{let o=a.next.next;for(;o!==a.prev;){if(a.i!==o.i&&W_(a,o)){let l=rf(a,o);a=_s(a,a.next),l=_s(l,l.next),Wr(a,t,e,n,s,r,0),Wr(l,t,e,n,s,r,0);return}o=o.next}a=a.next}while(a!==i)}function F_(i,t,e,n){let s=[],r,a,o,l,c;for(r=0,a=t.length;r<a;r++)o=t[r]*n,l=r<a-1?t[r+1]*n:i.length,c=nf(i,o,l,n,!1),c===c.next&&(c.steiner=!0),s.push(G_(c));for(s.sort(O_),r=0;r<s.length;r++)e=B_(s[r],e);return e}function O_(i,t){return i.x-t.x}function B_(i,t){let e=z_(i,t);if(!e)return t;let n=rf(e,i);return _s(n,n.next),_s(e,e.next)}function z_(i,t){let e=t,n=-1/0,s,r=i.x,a=i.y;do{if(a<=e.y&&a>=e.next.y&&e.next.y!==e.y){let d=e.x+(a-e.y)*(e.next.x-e.x)/(e.next.y-e.y);if(d<=r&&d>n&&(n=d,s=e.x<e.next.x?e:e.next,d===r))return s}e=e.next}while(e!==t);if(!s)return null;let o=s,l=s.x,c=s.y,h=1/0,u;e=s;do r>=e.x&&e.x>=l&&r!==e.x&&Zs(a<c?r:n,a,l,c,a<c?n:r,a,e.x,e.y)&&(u=Math.abs(a-e.y)/(r-e.x),Xr(e,i)&&(u<h||u===h&&(e.x>s.x||e.x===s.x&&H_(s,e)))&&(s=e,h=u)),e=e.next;while(e!==o);return s}function H_(i,t){return Ye(i.prev,i,t.prev)<0&&Ye(t.next,i,i.next)<0}function k_(i,t,e,n){let s=i;do s.z===0&&(s.z=$l(s.x,s.y,t,e,n)),s.prevZ=s.prev,s.nextZ=s.next,s=s.next;while(s!==i);s.prevZ.nextZ=null,s.prevZ=null,V_(s)}function V_(i){let t,e,n,s,r,a,o,l,c=1;do{for(e=i,i=null,r=null,a=0;e;){for(a++,n=e,o=0,t=0;t<c&&(o++,n=n.nextZ,!!n);t++);for(l=c;o>0||l>0&&n;)o!==0&&(l===0||!n||e.z<=n.z)?(s=e,e=e.nextZ,o--):(s=n,n=n.nextZ,l--),r?r.nextZ=s:i=s,s.prevZ=r,r=s;e=n}r.nextZ=null,c*=2}while(a>1);return i}function $l(i,t,e,n,s){return i=(i-e)*s|0,t=(t-n)*s|0,i=(i|i<<8)&16711935,i=(i|i<<4)&252645135,i=(i|i<<2)&858993459,i=(i|i<<1)&1431655765,t=(t|t<<8)&16711935,t=(t|t<<4)&252645135,t=(t|t<<2)&858993459,t=(t|t<<1)&1431655765,i|t<<1}function G_(i){let t=i,e=i;do(t.x<e.x||t.x===e.x&&t.y<e.y)&&(e=t),t=t.next;while(t!==i);return e}function Zs(i,t,e,n,s,r,a,o){return(s-a)*(t-o)>=(i-a)*(r-o)&&(i-a)*(n-o)>=(e-a)*(t-o)&&(e-a)*(r-o)>=(s-a)*(n-o)}function W_(i,t){return i.next.i!==t.i&&i.prev.i!==t.i&&!X_(i,t)&&(Xr(i,t)&&Xr(t,i)&&Y_(i,t)&&(Ye(i.prev,i,t.prev)||Ye(i,t.prev,t))||va(i,t)&&Ye(i.prev,i,i.next)>0&&Ye(t.prev,t,t.next)>0)}function Ye(i,t,e){return(t.y-i.y)*(e.x-t.x)-(t.x-i.x)*(e.y-t.y)}function va(i,t){return i.x===t.x&&i.y===t.y}function sf(i,t,e,n){let s=No(Ye(i,t,e)),r=No(Ye(i,t,n)),a=No(Ye(e,n,i)),o=No(Ye(e,n,t));return!!(s!==r&&a!==o||s===0&&Do(i,e,t)||r===0&&Do(i,n,t)||a===0&&Do(e,i,n)||o===0&&Do(e,t,n))}function Do(i,t,e){return t.x<=Math.max(i.x,e.x)&&t.x>=Math.min(i.x,e.x)&&t.y<=Math.max(i.y,e.y)&&t.y>=Math.min(i.y,e.y)}function No(i){return i>0?1:i<0?-1:0}function X_(i,t){let e=i;do{if(e.i!==i.i&&e.next.i!==i.i&&e.i!==t.i&&e.next.i!==t.i&&sf(e,e.next,i,t))return!0;e=e.next}while(e!==i);return!1}function Xr(i,t){return Ye(i.prev,i,i.next)<0?Ye(i,t,i.next)>=0&&Ye(i,i.prev,t)>=0:Ye(i,t,i.prev)<0||Ye(i,i.next,t)<0}function Y_(i,t){let e=i,n=!1,s=(i.x+t.x)/2,r=(i.y+t.y)/2;do e.y>r!=e.next.y>r&&e.next.y!==e.y&&s<(e.next.x-e.x)*(r-e.y)/(e.next.y-e.y)+e.x&&(n=!n),e=e.next;while(e!==i);return n}function rf(i,t){let e=new Jl(i.i,i.x,i.y),n=new Jl(t.i,t.x,t.y),s=i.next,r=t.prev;return i.next=t,t.prev=i,e.next=s,s.prev=e,n.next=e,e.prev=n,r.next=n,n.prev=r,n}function Tu(i,t,e,n){let s=new Jl(i,t,e);return n?(s.next=n.next,s.prev=n,n.next.prev=s,n.next=s):(s.prev=s,s.next=s),s}function Yr(i){i.next.prev=i.prev,i.prev.next=i.next,i.prevZ&&(i.prevZ.nextZ=i.nextZ),i.nextZ&&(i.nextZ.prevZ=i.prevZ)}function Jl(i,t,e){this.i=i,this.x=t,this.y=e,this.prev=null,this.next=null,this.z=0,this.prevZ=null,this.nextZ=null,this.steiner=!1}function q_(i,t,e,n){let s=0;for(let r=t,a=e-n;r<e;r+=n)s+=(i[a]-i[r])*(i[r+1]+i[a+1]),a=r;return s}var Rr=class i{static area(t){let e=t.length,n=0;for(let s=e-1,r=0;r<e;s=r++)n+=t[s].x*t[r].y-t[r].x*t[s].y;return n*.5}static isClockWise(t){return i.area(t)<0}static triangulateShape(t,e){let n=[],s=[],r=[];Au(t),Ru(n,t);let a=t.length;e.forEach(Au);for(let l=0;l<e.length;l++)s.push(a),a+=e[l].length,Ru(n,e[l]);let o=I_.triangulate(n,s);for(let l=0;l<o.length;l+=3)r.push(o.slice(l,l+3));return r}};function Au(i){let t=i.length;t>2&&i[t-1].equals(i[0])&&i.pop()}function Ru(i,t){for(let e=0;e<t.length;e++)i.push(t[e].x),i.push(t[e].y)}var Ii=class i extends qe{constructor(t=new fi([new xt(.5,.5),new xt(-.5,.5),new xt(-.5,-.5),new xt(.5,-.5)]),e={}){super(),this.type="ExtrudeGeometry",this.parameters={shapes:t,options:e},t=Array.isArray(t)?t:[t];let n=this,s=[],r=[];for(let o=0,l=t.length;o<l;o++){let c=t[o];a(c)}this.setAttribute("position",new _e(s,3)),this.setAttribute("uv",new _e(r,2)),this.computeVertexNormals();function a(o){let l=[],c=e.curveSegments!==void 0?e.curveSegments:12,h=e.steps!==void 0?e.steps:1,u=e.depth!==void 0?e.depth:1,d=e.bevelEnabled!==void 0?e.bevelEnabled:!0,p=e.bevelThickness!==void 0?e.bevelThickness:.2,x=e.bevelSize!==void 0?e.bevelSize:p-.1,y=e.bevelOffset!==void 0?e.bevelOffset:0,g=e.bevelSegments!==void 0?e.bevelSegments:3,m=e.extrudePath,w=e.UVGenerator!==void 0?e.UVGenerator:Z_,v,I=!1,H,U,N,Y;m&&(v=m.getSpacedPoints(h),I=!0,d=!1,H=m.computeFrenetFrames(h,!1),U=new O,N=new O,Y=new O),d||(g=0,p=0,x=0,y=0);let b=o.extractPoints(c),P=b.shape,X=b.holes;if(!Rr.isClockWise(P)){P=P.reverse();for(let F=0,Et=X.length;F<Et;F++){let st=X[F];Rr.isClockWise(st)&&(X[F]=st.reverse())}}let _t=Rr.triangulateShape(P,X),k=P;for(let F=0,Et=X.length;F<Et;F++){let st=X[F];P=P.concat(st)}function q(F,Et,st){return Et||console.error("THREE.ExtrudeGeometry: vec does not exist"),F.clone().addScaledVector(Et,st)}let j=P.length,et=_t.length;function ut(F,Et,st){let vt,ct,Xt,Pt=F.x-Et.x,T=F.y-Et.y,S=st.x-F.x,W=st.y-F.y,gt=Pt*Pt+T*T,pt=Pt*W-T*S;if(Math.abs(pt)>Number.EPSILON){let mt=Math.sqrt(gt),Vt=Math.sqrt(S*S+W*W),It=Et.x-T/mt,Tt=Et.y+Pt/mt,jt=st.x-W/Vt,he=st.y+S/Vt,ft=((jt-It)*W-(he-Tt)*S)/(Pt*W-T*S);vt=It+Pt*ft-F.x,ct=Tt+T*ft-F.y;let Me=vt*vt+ct*ct;if(Me<=2)return new xt(vt,ct);Xt=Math.sqrt(Me/2)}else{let mt=!1;Pt>Number.EPSILON?S>Number.EPSILON&&(mt=!0):Pt<-Number.EPSILON?S<-Number.EPSILON&&(mt=!0):Math.sign(T)===Math.sign(W)&&(mt=!0),mt?(vt=-T,ct=Pt,Xt=Math.sqrt(gt)):(vt=Pt,ct=T,Xt=Math.sqrt(gt/2))}return new xt(vt/Xt,ct/Xt)}let tt=[];for(let F=0,Et=k.length,st=Et-1,vt=F+1;F<Et;F++,st++,vt++)st===Et&&(st=0),vt===Et&&(vt=0),tt[F]=ut(k[F],k[st],k[vt]);let at=[],lt,Ut=tt.concat();for(let F=0,Et=X.length;F<Et;F++){let st=X[F];lt=[];for(let vt=0,ct=st.length,Xt=ct-1,Pt=vt+1;vt<ct;vt++,Xt++,Pt++)Xt===ct&&(Xt=0),Pt===ct&&(Pt=0),lt[vt]=ut(st[vt],st[Xt],st[Pt]);at.push(lt),Ut=Ut.concat(lt)}for(let F=0;F<g;F++){let Et=F/g,st=p*Math.cos(Et*Math.PI/2),vt=x*Math.sin(Et*Math.PI/2)+y;for(let ct=0,Xt=k.length;ct<Xt;ct++){let Pt=q(k[ct],tt[ct],vt);zt(Pt.x,Pt.y,-st)}for(let ct=0,Xt=X.length;ct<Xt;ct++){let Pt=X[ct];lt=at[ct];for(let T=0,S=Pt.length;T<S;T++){let W=q(Pt[T],lt[T],vt);zt(W.x,W.y,-st)}}}let nt=x+y;for(let F=0;F<j;F++){let Et=d?q(P[F],Ut[F],nt):P[F];I?(N.copy(H.normals[0]).multiplyScalar(Et.x),U.copy(H.binormals[0]).multiplyScalar(Et.y),Y.copy(v[0]).add(N).add(U),zt(Y.x,Y.y,Y.z)):zt(Et.x,Et.y,0)}for(let F=1;F<=h;F++)for(let Et=0;Et<j;Et++){let st=d?q(P[Et],Ut[Et],nt):P[Et];I?(N.copy(H.normals[F]).multiplyScalar(st.x),U.copy(H.binormals[F]).multiplyScalar(st.y),Y.copy(v[F]).add(N).add(U),zt(Y.x,Y.y,Y.z)):zt(st.x,st.y,u/h*F)}for(let F=g-1;F>=0;F--){let Et=F/g,st=p*Math.cos(Et*Math.PI/2),vt=x*Math.sin(Et*Math.PI/2)+y;for(let ct=0,Xt=k.length;ct<Xt;ct++){let Pt=q(k[ct],tt[ct],vt);zt(Pt.x,Pt.y,u+st)}for(let ct=0,Xt=X.length;ct<Xt;ct++){let Pt=X[ct];lt=at[ct];for(let T=0,S=Pt.length;T<S;T++){let W=q(Pt[T],lt[T],vt);I?zt(W.x,W.y+v[h-1].y,v[h-1].x+st):zt(W.x,W.y,u+st)}}}ht(),Dt();function ht(){let F=s.length/3;if(d){let Et=0,st=j*Et;for(let vt=0;vt<et;vt++){let ct=_t[vt];ne(ct[2]+st,ct[1]+st,ct[0]+st)}Et=h+g*2,st=j*Et;for(let vt=0;vt<et;vt++){let ct=_t[vt];ne(ct[0]+st,ct[1]+st,ct[2]+st)}}else{for(let Et=0;Et<et;Et++){let st=_t[Et];ne(st[2],st[1],st[0])}for(let Et=0;Et<et;Et++){let st=_t[Et];ne(st[0]+j*h,st[1]+j*h,st[2]+j*h)}}n.addGroup(F,s.length/3-F,0)}function Dt(){let F=s.length/3,Et=0;Bt(k,Et),Et+=k.length;for(let st=0,vt=X.length;st<vt;st++){let ct=X[st];Bt(ct,Et),Et+=ct.length}n.addGroup(F,s.length/3-F,1)}function Bt(F,Et){let st=F.length;for(;--st>=0;){let vt=st,ct=st-1;ct<0&&(ct=F.length-1);for(let Xt=0,Pt=h+g*2;Xt<Pt;Xt++){let T=j*Xt,S=j*(Xt+1),W=Et+vt+T,gt=Et+ct+T,pt=Et+ct+S,mt=Et+vt+S;Zt(W,gt,pt,mt)}}}function zt(F,Et,st){l.push(F),l.push(Et),l.push(st)}function ne(F,Et,st){Wt(F),Wt(Et),Wt(st);let vt=s.length/3,ct=w.generateTopUV(n,s,vt-3,vt-2,vt-1);ae(ct[0]),ae(ct[1]),ae(ct[2])}function Zt(F,Et,st,vt){Wt(F),Wt(Et),Wt(vt),Wt(Et),Wt(st),Wt(vt);let ct=s.length/3,Xt=w.generateSideWallUV(n,s,ct-6,ct-3,ct-2,ct-1);ae(Xt[0]),ae(Xt[1]),ae(Xt[3]),ae(Xt[1]),ae(Xt[2]),ae(Xt[3])}function Wt(F){s.push(l[F*3+0]),s.push(l[F*3+1]),s.push(l[F*3+2])}function ae(F){r.push(F.x),r.push(F.y)}}}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}toJSON(){let t=super.toJSON(),e=this.parameters.shapes,n=this.parameters.options;return $_(e,n,t)}static fromJSON(t,e){let n=[];for(let r=0,a=t.shapes.length;r<a;r++){let o=e[t.shapes[r]];n.push(o)}let s=t.options.extrudePath;return s!==void 0&&(t.options.extrudePath=new ql[s.type]().fromJSON(s)),new i(n,t.options)}},Z_={generateTopUV:function(i,t,e,n,s){let r=t[e*3],a=t[e*3+1],o=t[n*3],l=t[n*3+1],c=t[s*3],h=t[s*3+1];return[new xt(r,a),new xt(o,l),new xt(c,h)]},generateSideWallUV:function(i,t,e,n,s,r){let a=t[e*3],o=t[e*3+1],l=t[e*3+2],c=t[n*3],h=t[n*3+1],u=t[n*3+2],d=t[s*3],p=t[s*3+1],x=t[s*3+2],y=t[r*3],g=t[r*3+1],m=t[r*3+2];return Math.abs(o-h)<Math.abs(a-c)?[new xt(a,1-l),new xt(c,1-u),new xt(d,1-x),new xt(y,1-m)]:[new xt(o,1-l),new xt(h,1-u),new xt(p,1-x),new xt(g,1-m)]}};function $_(i,t,e){if(e.shapes=[],Array.isArray(i))for(let n=0,s=i.length;n<s;n++){let r=i[n];e.shapes.push(r.uuid)}else e.shapes.push(i.uuid);return e.options=Object.assign({},t),t.extrudePath!==void 0&&(e.options.extrudePath=t.extrudePath.toJSON()),e}var la=class i extends Vr{constructor(t=1,e=0){let n=(1+Math.sqrt(5))/2,s=[-1,n,0,1,n,0,-1,-n,0,1,-n,0,0,-1,n,0,1,n,0,-1,-n,0,1,-n,n,0,-1,n,0,1,-n,0,-1,-n,0,1],r=[0,11,5,0,5,1,0,1,7,0,7,10,0,10,11,1,5,9,5,11,4,11,10,2,10,7,6,7,1,8,3,9,4,3,4,2,3,2,6,3,6,8,3,8,9,4,9,5,2,4,11,6,2,10,8,6,7,9,8,1];super(s,r,t,e),this.type="IcosahedronGeometry",this.parameters={radius:t,detail:e}}static fromJSON(t){return new i(t.radius,t.detail)}},ca=class i extends Vr{constructor(t=1,e=0){let n=[1,0,0,-1,0,0,0,1,0,0,-1,0,0,0,1,0,0,-1],s=[0,2,4,0,4,3,0,3,5,0,5,2,1,2,5,1,5,3,1,3,4,1,4,2];super(n,s,t,e),this.type="OctahedronGeometry",this.parameters={radius:t,detail:e}}static fromJSON(t){return new i(t.radius,t.detail)}};var Li=class i extends qe{constructor(t=1,e=32,n=16,s=0,r=Math.PI*2,a=0,o=Math.PI){super(),this.type="SphereGeometry",this.parameters={radius:t,widthSegments:e,heightSegments:n,phiStart:s,phiLength:r,thetaStart:a,thetaLength:o},e=Math.max(3,Math.floor(e)),n=Math.max(2,Math.floor(n));let l=Math.min(a+o,Math.PI),c=0,h=[],u=new O,d=new O,p=[],x=[],y=[],g=[];for(let m=0;m<=n;m++){let w=[],v=m/n,I=0;m===0&&a===0?I=.5/e:m===n&&l===Math.PI&&(I=-.5/e);for(let H=0;H<=e;H++){let U=H/e;u.x=-t*Math.cos(s+U*r)*Math.sin(a+v*o),u.y=t*Math.cos(a+v*o),u.z=t*Math.sin(s+U*r)*Math.sin(a+v*o),x.push(u.x,u.y,u.z),d.copy(u).normalize(),y.push(d.x,d.y,d.z),g.push(U+I,1-v),w.push(c++)}h.push(w)}for(let m=0;m<n;m++)for(let w=0;w<e;w++){let v=h[m][w+1],I=h[m][w],H=h[m+1][w],U=h[m+1][w+1];(m!==0||a>0)&&p.push(v,I,U),(m!==n-1||l<Math.PI)&&p.push(I,H,U)}this.setIndex(p),this.setAttribute("position",new _e(x,3)),this.setAttribute("normal",new _e(y,3)),this.setAttribute("uv",new _e(g,2))}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.radius,t.widthSegments,t.heightSegments,t.phiStart,t.phiLength,t.thetaStart,t.thetaLength)}};var ha=class i extends qe{constructor(t=1,e=.4,n=12,s=48,r=Math.PI*2){super(),this.type="TorusGeometry",this.parameters={radius:t,tube:e,radialSegments:n,tubularSegments:s,arc:r},n=Math.floor(n),s=Math.floor(s);let a=[],o=[],l=[],c=[],h=new O,u=new O,d=new O;for(let p=0;p<=n;p++)for(let x=0;x<=s;x++){let y=x/s*r,g=p/n*Math.PI*2;u.x=(t+e*Math.cos(g))*Math.cos(y),u.y=(t+e*Math.cos(g))*Math.sin(y),u.z=e*Math.sin(g),o.push(u.x,u.y,u.z),h.x=t*Math.cos(y),h.y=t*Math.sin(y),d.subVectors(u,h).normalize(),l.push(d.x,d.y,d.z),c.push(x/s),c.push(p/n)}for(let p=1;p<=n;p++)for(let x=1;x<=s;x++){let y=(s+1)*p+x-1,g=(s+1)*(p-1)+x-1,m=(s+1)*(p-1)+x,w=(s+1)*p+x;a.push(y,g,w),a.push(g,m,w)}this.setIndex(a),this.setAttribute("position",new _e(o,3)),this.setAttribute("normal",new _e(l,3)),this.setAttribute("uv",new _e(c,2))}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.radius,t.tube,t.radialSegments,t.tubularSegments,t.arc)}};var ei=class extends $i{constructor(t){super(),this.isMeshStandardMaterial=!0,this.defines={STANDARD:""},this.type="MeshStandardMaterial",this.color=new ge(16777215),this.roughness=1,this.metalness=0,this.map=null,this.lightMap=null,this.lightMapIntensity=1,this.aoMap=null,this.aoMapIntensity=1,this.emissive=new ge(0),this.emissiveIntensity=1,this.emissiveMap=null,this.bumpMap=null,this.bumpScale=1,this.normalMap=null,this.normalMapType=Xu,this.normalScale=new xt(1,1),this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.roughnessMap=null,this.metalnessMap=null,this.alphaMap=null,this.envMap=null,this.envMapIntensity=1,this.wireframe=!1,this.wireframeLinewidth=1,this.wireframeLinecap="round",this.wireframeLinejoin="round",this.flatShading=!1,this.fog=!0,this.setValues(t)}copy(t){return super.copy(t),this.defines={STANDARD:""},this.color.copy(t.color),this.roughness=t.roughness,this.metalness=t.metalness,this.map=t.map,this.lightMap=t.lightMap,this.lightMapIntensity=t.lightMapIntensity,this.aoMap=t.aoMap,this.aoMapIntensity=t.aoMapIntensity,this.emissive.copy(t.emissive),this.emissiveMap=t.emissiveMap,this.emissiveIntensity=t.emissiveIntensity,this.bumpMap=t.bumpMap,this.bumpScale=t.bumpScale,this.normalMap=t.normalMap,this.normalMapType=t.normalMapType,this.normalScale.copy(t.normalScale),this.displacementMap=t.displacementMap,this.displacementScale=t.displacementScale,this.displacementBias=t.displacementBias,this.roughnessMap=t.roughnessMap,this.metalnessMap=t.metalnessMap,this.alphaMap=t.alphaMap,this.envMap=t.envMap,this.envMapIntensity=t.envMapIntensity,this.wireframe=t.wireframe,this.wireframeLinewidth=t.wireframeLinewidth,this.wireframeLinecap=t.wireframeLinecap,this.wireframeLinejoin=t.wireframeLinejoin,this.flatShading=t.flatShading,this.fog=t.fog,this}};function Fo(i,t,e){return!i||!e&&i.constructor===t?i:typeof t.BYTES_PER_ELEMENT=="number"?new t(i):Array.prototype.slice.call(i)}function J_(i){return ArrayBuffer.isView(i)&&!(i instanceof DataView)}var or=class{constructor(t,e,n,s){this.parameterPositions=t,this._cachedIndex=0,this.resultBuffer=s!==void 0?s:new e.constructor(n),this.sampleValues=e,this.valueSize=n,this.settings=null,this.DefaultSettings_={}}evaluate(t){let e=this.parameterPositions,n=this._cachedIndex,s=e[n],r=e[n-1];n:{t:{let a;e:{i:if(!(t<s)){for(let o=n+2;;){if(s===void 0){if(t<r)break i;return n=e.length,this._cachedIndex=n,this.copySampleValue_(n-1)}if(n===o)break;if(r=s,s=e[++n],t<s)break t}a=e.length;break e}if(!(t>=r)){let o=e[1];t<o&&(n=2,r=o);for(let l=n-2;;){if(r===void 0)return this._cachedIndex=0,this.copySampleValue_(0);if(n===l)break;if(s=r,r=e[--n-1],t>=r)break t}a=n,n=0;break e}break n}for(;n<a;){let o=n+a>>>1;t<e[o]?a=o:n=o+1}if(s=e[n],r=e[n-1],r===void 0)return this._cachedIndex=0,this.copySampleValue_(0);if(s===void 0)return n=e.length,this._cachedIndex=n,this.copySampleValue_(n-1)}this._cachedIndex=n,this.intervalChanged_(n,r,s)}return this.interpolate_(n,r,t,s)}getSettings_(){return this.settings||this.DefaultSettings_}copySampleValue_(t){let e=this.resultBuffer,n=this.sampleValues,s=this.valueSize,r=t*s;for(let a=0;a!==s;++a)e[a]=n[r+a];return e}interpolate_(){throw new Error("call to abstract method")}intervalChanged_(){}},Kl=class extends or{constructor(t,e,n,s){super(t,e,n,s),this._weightPrev=-0,this._offsetPrev=-0,this._weightNext=-0,this._offsetNext=-0,this.DefaultSettings_={endingStart:Ih,endingEnd:Ih}}intervalChanged_(t,e,n){let s=this.parameterPositions,r=t-2,a=t+1,o=s[r],l=s[a];if(o===void 0)switch(this.getSettings_().endingStart){case Lh:r=t,o=2*e-n;break;case Uh:r=s.length-2,o=e+s[r]-s[r+1];break;default:r=t,o=n}if(l===void 0)switch(this.getSettings_().endingEnd){case Lh:a=t,l=2*n-e;break;case Uh:a=1,l=n+s[1]-s[0];break;default:a=t-1,l=e}let c=(n-e)*.5,h=this.valueSize;this._weightPrev=c/(e-o),this._weightNext=c/(l-n),this._offsetPrev=r*h,this._offsetNext=a*h}interpolate_(t,e,n,s){let r=this.resultBuffer,a=this.sampleValues,o=this.valueSize,l=t*o,c=l-o,h=this._offsetPrev,u=this._offsetNext,d=this._weightPrev,p=this._weightNext,x=(n-e)/(s-e),y=x*x,g=y*x,m=-d*g+2*d*y-d*x,w=(1+d)*g+(-1.5-2*d)*y+(-.5+d)*x+1,v=(-1-p)*g+(1.5+p)*y+.5*x,I=p*g-p*y;for(let H=0;H!==o;++H)r[H]=m*a[h+H]+w*a[c+H]+v*a[l+H]+I*a[u+H];return r}},jl=class extends or{constructor(t,e,n,s){super(t,e,n,s)}interpolate_(t,e,n,s){let r=this.resultBuffer,a=this.sampleValues,o=this.valueSize,l=t*o,c=l-o,h=(n-e)/(s-e),u=1-h;for(let d=0;d!==o;++d)r[d]=a[c+d]*u+a[l+d]*h;return r}},Ql=class extends or{constructor(t,e,n,s){super(t,e,n,s)}interpolate_(t){return this.copySampleValue_(t-1)}},ni=class{constructor(t,e,n,s){if(t===void 0)throw new Error("THREE.KeyframeTrack: track name is undefined");if(e===void 0||e.length===0)throw new Error("THREE.KeyframeTrack: no keyframes in track named "+t);this.name=t,this.times=Fo(e,this.TimeBufferType),this.values=Fo(n,this.ValueBufferType),this.setInterpolation(s||this.DefaultInterpolation)}static toJSON(t){let e=t.constructor,n;if(e.toJSON!==this.toJSON)n=e.toJSON(t);else{n={name:t.name,times:Fo(t.times,Array),values:Fo(t.values,Array)};let s=t.getInterpolation();s!==t.DefaultInterpolation&&(n.interpolation=s)}return n.type=t.ValueTypeName,n}InterpolantFactoryMethodDiscrete(t){return new Ql(this.times,this.values,this.getValueSize(),t)}InterpolantFactoryMethodLinear(t){return new jl(this.times,this.values,this.getValueSize(),t)}InterpolantFactoryMethodSmooth(t){return new Kl(this.times,this.values,this.getValueSize(),t)}setInterpolation(t){let e;switch(t){case Bo:e=this.InterpolantFactoryMethodDiscrete;break;case zo:e=this.InterpolantFactoryMethodLinear;break;case Xa:e=this.InterpolantFactoryMethodSmooth;break}if(e===void 0){let n="unsupported interpolation for "+this.ValueTypeName+" keyframe track named "+this.name;if(this.createInterpolant===void 0)if(t!==this.DefaultInterpolation)this.setInterpolation(this.DefaultInterpolation);else throw new Error(n);return console.warn("THREE.KeyframeTrack:",n),this}return this.createInterpolant=e,this}getInterpolation(){switch(this.createInterpolant){case this.InterpolantFactoryMethodDiscrete:return Bo;case this.InterpolantFactoryMethodLinear:return zo;case this.InterpolantFactoryMethodSmooth:return Xa}}getValueSize(){return this.values.length/this.times.length}shift(t){if(t!==0){let e=this.times;for(let n=0,s=e.length;n!==s;++n)e[n]+=t}return this}scale(t){if(t!==1){let e=this.times;for(let n=0,s=e.length;n!==s;++n)e[n]*=t}return this}trim(t,e){let n=this.times,s=n.length,r=0,a=s-1;for(;r!==s&&n[r]<t;)++r;for(;a!==-1&&n[a]>e;)--a;if(++a,r!==0||a!==s){r>=a&&(a=Math.max(a,1),r=a-1);let o=this.getValueSize();this.times=n.slice(r,a),this.values=this.values.slice(r*o,a*o)}return this}validate(){let t=!0,e=this.getValueSize();e-Math.floor(e)!==0&&(console.error("THREE.KeyframeTrack: Invalid value size in track.",this),t=!1);let n=this.times,s=this.values,r=n.length;r===0&&(console.error("THREE.KeyframeTrack: Track is empty.",this),t=!1);let a=null;for(let o=0;o!==r;o++){let l=n[o];if(typeof l=="number"&&isNaN(l)){console.error("THREE.KeyframeTrack: Time is not a valid number.",this,o,l),t=!1;break}if(a!==null&&a>l){console.error("THREE.KeyframeTrack: Out of order keys.",this,o,l,a),t=!1;break}a=l}if(s!==void 0&&J_(s))for(let o=0,l=s.length;o!==l;++o){let c=s[o];if(isNaN(c)){console.error("THREE.KeyframeTrack: Value is not a valid number.",this,o,c),t=!1;break}}return t}optimize(){let t=this.times.slice(),e=this.values.slice(),n=this.getValueSize(),s=this.getInterpolation()===Xa,r=t.length-1,a=1;for(let o=1;o<r;++o){let l=!1,c=t[o],h=t[o+1];if(c!==h&&(o!==1||c!==t[0]))if(s)l=!0;else{let u=o*n,d=u-n,p=u+n;for(let x=0;x!==n;++x){let y=e[u+x];if(y!==e[d+x]||y!==e[p+x]){l=!0;break}}}if(l){if(o!==a){t[a]=t[o];let u=o*n,d=a*n;for(let p=0;p!==n;++p)e[d+p]=e[u+p]}++a}}if(r>0){t[a]=t[r];for(let o=r*n,l=a*n,c=0;c!==n;++c)e[l+c]=e[o+c];++a}return a!==t.length?(this.times=t.slice(0,a),this.values=e.slice(0,a*n)):(this.times=t,this.values=e),this}clone(){let t=this.times.slice(),e=this.values.slice(),n=this.constructor,s=new n(this.name,t,e);return s.createInterpolant=this.createInterpolant,s}};ni.prototype.TimeBufferType=Float32Array;ni.prototype.ValueBufferType=Float32Array;ni.prototype.DefaultInterpolation=zo;var xs=class extends ni{};xs.prototype.ValueTypeName="bool";xs.prototype.ValueBufferType=Array;xs.prototype.DefaultInterpolation=Bo;xs.prototype.InterpolantFactoryMethodLinear=void 0;xs.prototype.InterpolantFactoryMethodSmooth=void 0;var tc=class extends ni{};tc.prototype.ValueTypeName="color";var ec=class extends ni{};ec.prototype.ValueTypeName="number";var nc=class extends or{constructor(t,e,n,s){super(t,e,n,s)}interpolate_(t,e,n,s){let r=this.resultBuffer,a=this.sampleValues,o=this.valueSize,l=(n-e)/(s-e),c=t*o;for(let h=c+o;c!==h;c+=4)ti.slerpFlat(r,0,a,c-o,a,c,l);return r}},qr=class extends ni{InterpolantFactoryMethodLinear(t){return new nc(this.times,this.values,this.getValueSize(),t)}};qr.prototype.ValueTypeName="quaternion";qr.prototype.DefaultInterpolation=zo;qr.prototype.InterpolantFactoryMethodSmooth=void 0;var vs=class extends ni{};vs.prototype.ValueTypeName="string";vs.prototype.ValueBufferType=Array;vs.prototype.DefaultInterpolation=Bo;vs.prototype.InterpolantFactoryMethodLinear=void 0;vs.prototype.InterpolantFactoryMethodSmooth=void 0;var ic=class extends ni{};ic.prototype.ValueTypeName="vector";var Cu={enabled:!1,files:{},add:function(i,t){this.enabled!==!1&&(this.files[i]=t)},get:function(i){if(this.enabled!==!1)return this.files[i]},remove:function(i){delete this.files[i]},clear:function(){this.files={}}},sc=class{constructor(t,e,n){let s=this,r=!1,a=0,o=0,l,c=[];this.onStart=void 0,this.onLoad=t,this.onProgress=e,this.onError=n,this.itemStart=function(h){o++,r===!1&&s.onStart!==void 0&&s.onStart(h,a,o),r=!0},this.itemEnd=function(h){a++,s.onProgress!==void 0&&s.onProgress(h,a,o),a===o&&(r=!1,s.onLoad!==void 0&&s.onLoad())},this.itemError=function(h){s.onError!==void 0&&s.onError(h)},this.resolveURL=function(h){return l?l(h):h},this.setURLModifier=function(h){return l=h,this},this.addHandler=function(h,u){return c.push(h,u),this},this.removeHandler=function(h){let u=c.indexOf(h);return u!==-1&&c.splice(u,2),this},this.getHandler=function(h){for(let u=0,d=c.length;u<d;u+=2){let p=c[u],x=c[u+1];if(p.global&&(p.lastIndex=0),p.test(h))return x}return null}}},K_=new sc,Zr=class{constructor(t){this.manager=t!==void 0?t:K_,this.crossOrigin="anonymous",this.withCredentials=!1,this.path="",this.resourcePath="",this.requestHeader={}}load(){}loadAsync(t,e){let n=this;return new Promise(function(s,r){n.load(t,s,e,r)})}parse(){}setCrossOrigin(t){return this.crossOrigin=t,this}setWithCredentials(t){return this.withCredentials=t,this}setPath(t){return this.path=t,this}setResourcePath(t){return this.resourcePath=t,this}setRequestHeader(t){return this.requestHeader=t,this}};Zr.DEFAULT_MATERIAL_NAME="__DEFAULT";var rc=class extends Zr{constructor(t){super(t)}load(t,e,n,s){this.path!==void 0&&(t=this.path+t),t=this.manager.resolveURL(t);let r=this,a=Cu.get(t);if(a!==void 0)return r.manager.itemStart(t),setTimeout(function(){e&&e(a),r.manager.itemEnd(t)},0),a;let o=Lr("img");function l(){h(),Cu.add(t,this),e&&e(this),r.manager.itemEnd(t)}function c(u){h(),s&&s(u),r.manager.itemError(t),r.manager.itemEnd(t)}function h(){o.removeEventListener("load",l,!1),o.removeEventListener("error",c,!1)}return o.addEventListener("load",l,!1),o.addEventListener("error",c,!1),t.slice(0,5)!=="data:"&&this.crossOrigin!==void 0&&(o.crossOrigin=this.crossOrigin),r.manager.itemStart(t),o.src=t,o}};var ua=class extends Zr{constructor(t){super(t)}load(t,e,n,s){let r=new Dn,a=new rc(this.manager);return a.setCrossOrigin(this.crossOrigin),a.setPath(this.path),a.load(t,function(o){r.image=o,r.needsUpdate=!0,e!==void 0&&e(r)},n,s),r}},$r=class extends bn{constructor(t,e=1){super(),this.isLight=!0,this.type="Light",this.color=new ge(t),this.intensity=e}dispose(){}copy(t,e){return super.copy(t,e),this.color.copy(t.color),this.intensity=t.intensity,this}toJSON(t){let e=super.toJSON(t);return e.object.color=this.color.getHex(),e.object.intensity=this.intensity,this.groundColor!==void 0&&(e.object.groundColor=this.groundColor.getHex()),this.distance!==void 0&&(e.object.distance=this.distance),this.angle!==void 0&&(e.object.angle=this.angle),this.decay!==void 0&&(e.object.decay=this.decay),this.penumbra!==void 0&&(e.object.penumbra=this.penumbra),this.shadow!==void 0&&(e.object.shadow=this.shadow.toJSON()),e}},fa=class extends $r{constructor(t,e,n){super(t,n),this.isHemisphereLight=!0,this.type="HemisphereLight",this.position.copy(bn.DEFAULT_UP),this.updateMatrix(),this.groundColor=new ge(e)}copy(t,e){return super.copy(t,e),this.groundColor.copy(t.groundColor),this}},_l=new De,Pu=new O,Iu=new O,da=class{constructor(t){this.camera=t,this.bias=0,this.normalBias=0,this.radius=1,this.blurSamples=8,this.mapSize=new xt(512,512),this.map=null,this.mapPass=null,this.matrix=new De,this.autoUpdate=!0,this.needsUpdate=!1,this._frustum=new Nr,this._frameExtents=new xt(1,1),this._viewportCount=1,this._viewports=[new Xe(0,0,1,1)]}getViewportCount(){return this._viewportCount}getFrustum(){return this._frustum}updateMatrices(t){let e=this.camera,n=this.matrix;Pu.setFromMatrixPosition(t.matrixWorld),e.position.copy(Pu),Iu.setFromMatrixPosition(t.target.matrixWorld),e.lookAt(Iu),e.updateMatrixWorld(),_l.multiplyMatrices(e.projectionMatrix,e.matrixWorldInverse),this._frustum.setFromProjectionMatrix(_l),n.set(.5,0,0,.5,0,.5,0,.5,0,0,.5,.5,0,0,0,1),n.multiply(_l)}getViewport(t){return this._viewports[t]}getFrameExtents(){return this._frameExtents}dispose(){this.map&&this.map.dispose(),this.mapPass&&this.mapPass.dispose()}copy(t){return this.camera=t.camera.clone(),this.bias=t.bias,this.radius=t.radius,this.mapSize.copy(t.mapSize),this}clone(){return new this.constructor().copy(this)}toJSON(){let t={};return this.bias!==0&&(t.bias=this.bias),this.normalBias!==0&&(t.normalBias=this.normalBias),this.radius!==1&&(t.radius=this.radius),(this.mapSize.x!==512||this.mapSize.y!==512)&&(t.mapSize=this.mapSize.toArray()),t.camera=this.camera.toJSON(!1).object,delete t.camera.matrix,t}};var Lu=new De,Mr=new O,xl=new O,oc=class extends da{constructor(){super(new Mn(90,1,.5,500)),this.isPointLightShadow=!0,this._frameExtents=new xt(4,2),this._viewportCount=6,this._viewports=[new Xe(2,1,1,1),new Xe(0,1,1,1),new Xe(3,1,1,1),new Xe(1,1,1,1),new Xe(3,0,1,1),new Xe(1,0,1,1)],this._cubeDirections=[new O(1,0,0),new O(-1,0,0),new O(0,0,1),new O(0,0,-1),new O(0,1,0),new O(0,-1,0)],this._cubeUps=[new O(0,1,0),new O(0,1,0),new O(0,1,0),new O(0,1,0),new O(0,0,1),new O(0,0,-1)]}updateMatrices(t,e=0){let n=this.camera,s=this.matrix,r=t.distance||n.far;r!==n.far&&(n.far=r,n.updateProjectionMatrix()),Mr.setFromMatrixPosition(t.matrixWorld),n.position.copy(Mr),xl.copy(n.position),xl.add(this._cubeDirections[e]),n.up.copy(this._cubeUps[e]),n.lookAt(xl),n.updateMatrixWorld(),s.makeTranslation(-Mr.x,-Mr.y,-Mr.z),Lu.multiplyMatrices(n.projectionMatrix,n.matrixWorldInverse),this._frustum.setFromProjectionMatrix(Lu)}},Ji=class extends $r{constructor(t,e,n=0,s=2){super(t,e),this.isPointLight=!0,this.type="PointLight",this.distance=n,this.decay=s,this.shadow=new oc}get power(){return this.intensity*4*Math.PI}set power(t){this.intensity=t/(4*Math.PI)}dispose(){this.shadow.dispose()}copy(t,e){return super.copy(t,e),this.distance=t.distance,this.decay=t.decay,this.shadow=t.shadow.clone(),this}},ac=class extends da{constructor(){super(new jo(-5,5,5,-5,.5,500)),this.isDirectionalLightShadow=!0}},pa=class extends $r{constructor(t,e){super(t,e),this.isDirectionalLight=!0,this.type="DirectionalLight",this.position.copy(bn.DEFAULT_UP),this.updateMatrix(),this.target=new bn,this.shadow=new ac}dispose(){this.shadow.dispose()}copy(t){return super.copy(t),this.target=t.target.clone(),this.shadow=t.shadow.clone(),this}};var Jr=class extends qe{constructor(){super(),this.isInstancedBufferGeometry=!0,this.type="InstancedBufferGeometry",this.instanceCount=1/0}copy(t){return super.copy(t),this.instanceCount=t.instanceCount,this}toJSON(){let t=super.toJSON();return t.instanceCount=this.instanceCount,t.isInstancedBufferGeometry=!0,t}};var vc="\\[\\]\\.:\\/",j_=new RegExp("["+vc+"]","g"),yc="[^"+vc+"]",Q_="[^"+vc.replace("\\.","")+"]",tx=/((?:WC+[\/:])*)/.source.replace("WC",yc),ex=/(WCOD+)?/.source.replace("WCOD",Q_),nx=/(?:\.(WC+)(?:\[(.+)\])?)?/.source.replace("WC",yc),ix=/\.(WC+)(?:\[(.+)\])?/.source.replace("WC",yc),sx=new RegExp("^"+tx+ex+nx+ix+"$"),rx=["material","materials","bones","map"],lc=class{constructor(t,e,n){let s=n||We.parseTrackName(e);this._targetGroup=t,this._bindings=t.subscribe_(e,s)}getValue(t,e){this.bind();let n=this._targetGroup.nCachedObjects_,s=this._bindings[n];s!==void 0&&s.getValue(t,e)}setValue(t,e){let n=this._bindings;for(let s=this._targetGroup.nCachedObjects_,r=n.length;s!==r;++s)n[s].setValue(t,e)}bind(){let t=this._bindings;for(let e=this._targetGroup.nCachedObjects_,n=t.length;e!==n;++e)t[e].bind()}unbind(){let t=this._bindings;for(let e=this._targetGroup.nCachedObjects_,n=t.length;e!==n;++e)t[e].unbind()}},We=class i{constructor(t,e,n){this.path=e,this.parsedPath=n||i.parseTrackName(e),this.node=i.findNode(t,this.parsedPath.nodeName),this.rootNode=t,this.getValue=this._getValue_unbound,this.setValue=this._setValue_unbound}static create(t,e,n){return t&&t.isAnimationObjectGroup?new i.Composite(t,e,n):new i(t,e,n)}static sanitizeNodeName(t){return t.replace(/\s/g,"_").replace(j_,"")}static parseTrackName(t){let e=sx.exec(t);if(e===null)throw new Error("PropertyBinding: Cannot parse trackName: "+t);let n={nodeName:e[2],objectName:e[3],objectIndex:e[4],propertyName:e[5],propertyIndex:e[6]},s=n.nodeName&&n.nodeName.lastIndexOf(".");if(s!==void 0&&s!==-1){let r=n.nodeName.substring(s+1);rx.indexOf(r)!==-1&&(n.nodeName=n.nodeName.substring(0,s),n.objectName=r)}if(n.propertyName===null||n.propertyName.length===0)throw new Error("PropertyBinding: can not parse propertyName from trackName: "+t);return n}static findNode(t,e){if(e===void 0||e===""||e==="."||e===-1||e===t.name||e===t.uuid)return t;if(t.skeleton){let n=t.skeleton.getBoneByName(e);if(n!==void 0)return n}if(t.children){let n=function(r){for(let a=0;a<r.length;a++){let o=r[a];if(o.name===e||o.uuid===e)return o;let l=n(o.children);if(l)return l}return null},s=n(t.children);if(s)return s}return null}_getValue_unavailable(){}_setValue_unavailable(){}_getValue_direct(t,e){t[e]=this.targetObject[this.propertyName]}_getValue_array(t,e){let n=this.resolvedProperty;for(let s=0,r=n.length;s!==r;++s)t[e++]=n[s]}_getValue_arrayElement(t,e){t[e]=this.resolvedProperty[this.propertyIndex]}_getValue_toArray(t,e){this.resolvedProperty.toArray(t,e)}_setValue_direct(t,e){this.targetObject[this.propertyName]=t[e]}_setValue_direct_setNeedsUpdate(t,e){this.targetObject[this.propertyName]=t[e],this.targetObject.needsUpdate=!0}_setValue_direct_setMatrixWorldNeedsUpdate(t,e){this.targetObject[this.propertyName]=t[e],this.targetObject.matrixWorldNeedsUpdate=!0}_setValue_array(t,e){let n=this.resolvedProperty;for(let s=0,r=n.length;s!==r;++s)n[s]=t[e++]}_setValue_array_setNeedsUpdate(t,e){let n=this.resolvedProperty;for(let s=0,r=n.length;s!==r;++s)n[s]=t[e++];this.targetObject.needsUpdate=!0}_setValue_array_setMatrixWorldNeedsUpdate(t,e){let n=this.resolvedProperty;for(let s=0,r=n.length;s!==r;++s)n[s]=t[e++];this.targetObject.matrixWorldNeedsUpdate=!0}_setValue_arrayElement(t,e){this.resolvedProperty[this.propertyIndex]=t[e]}_setValue_arrayElement_setNeedsUpdate(t,e){this.resolvedProperty[this.propertyIndex]=t[e],this.targetObject.needsUpdate=!0}_setValue_arrayElement_setMatrixWorldNeedsUpdate(t,e){this.resolvedProperty[this.propertyIndex]=t[e],this.targetObject.matrixWorldNeedsUpdate=!0}_setValue_fromArray(t,e){this.resolvedProperty.fromArray(t,e)}_setValue_fromArray_setNeedsUpdate(t,e){this.resolvedProperty.fromArray(t,e),this.targetObject.needsUpdate=!0}_setValue_fromArray_setMatrixWorldNeedsUpdate(t,e){this.resolvedProperty.fromArray(t,e),this.targetObject.matrixWorldNeedsUpdate=!0}_getValue_unbound(t,e){this.bind(),this.getValue(t,e)}_setValue_unbound(t,e){this.bind(),this.setValue(t,e)}bind(){let t=this.node,e=this.parsedPath,n=e.objectName,s=e.propertyName,r=e.propertyIndex;if(t||(t=i.findNode(this.rootNode,e.nodeName),this.node=t),this.getValue=this._getValue_unavailable,this.setValue=this._setValue_unavailable,!t){console.warn("THREE.PropertyBinding: No target node found for track: "+this.path+".");return}if(n){let c=e.objectIndex;switch(n){case"materials":if(!t.material){console.error("THREE.PropertyBinding: Can not bind to material as node does not have a material.",this);return}if(!t.material.materials){console.error("THREE.PropertyBinding: Can not bind to material.materials as node.material does not have a materials array.",this);return}t=t.material.materials;break;case"bones":if(!t.skeleton){console.error("THREE.PropertyBinding: Can not bind to bones as node does not have a skeleton.",this);return}t=t.skeleton.bones;for(let h=0;h<t.length;h++)if(t[h].name===c){c=h;break}break;case"map":if("map"in t){t=t.map;break}if(!t.material){console.error("THREE.PropertyBinding: Can not bind to material as node does not have a material.",this);return}if(!t.material.map){console.error("THREE.PropertyBinding: Can not bind to material.map as node.material does not have a map.",this);return}t=t.material.map;break;default:if(t[n]===void 0){console.error("THREE.PropertyBinding: Can not bind to objectName of node undefined.",this);return}t=t[n]}if(c!==void 0){if(t[c]===void 0){console.error("THREE.PropertyBinding: Trying to bind to objectIndex of objectName, but is undefined.",this,t);return}t=t[c]}}let a=t[s];if(a===void 0){let c=e.nodeName;console.error("THREE.PropertyBinding: Trying to update property for track: "+c+"."+s+" but it wasn't found.",t);return}let o=this.Versioning.None;this.targetObject=t,t.needsUpdate!==void 0?o=this.Versioning.NeedsUpdate:t.matrixWorldNeedsUpdate!==void 0&&(o=this.Versioning.MatrixWorldNeedsUpdate);let l=this.BindingType.Direct;if(r!==void 0){if(s==="morphTargetInfluences"){if(!t.geometry){console.error("THREE.PropertyBinding: Can not bind to morphTargetInfluences because node does not have a geometry.",this);return}if(!t.geometry.morphAttributes){console.error("THREE.PropertyBinding: Can not bind to morphTargetInfluences because node does not have a geometry.morphAttributes.",this);return}t.morphTargetDictionary[r]!==void 0&&(r=t.morphTargetDictionary[r])}l=this.BindingType.ArrayElement,this.resolvedProperty=a,this.propertyIndex=r}else a.fromArray!==void 0&&a.toArray!==void 0?(l=this.BindingType.HasFromToArray,this.resolvedProperty=a):Array.isArray(a)?(l=this.BindingType.EntireArray,this.resolvedProperty=a):this.propertyName=s;this.getValue=this.GetterByBindingType[l],this.setValue=this.SetterByBindingTypeAndVersioning[l][o]}unbind(){this.node=null,this.getValue=this._getValue_unbound,this.setValue=this._setValue_unbound}};We.Composite=lc;We.prototype.BindingType={Direct:0,EntireArray:1,ArrayElement:2,HasFromToArray:3};We.prototype.Versioning={None:0,NeedsUpdate:1,MatrixWorldNeedsUpdate:2};We.prototype.GetterByBindingType=[We.prototype._getValue_direct,We.prototype._getValue_array,We.prototype._getValue_arrayElement,We.prototype._getValue_toArray];We.prototype.SetterByBindingTypeAndVersioning=[[We.prototype._setValue_direct,We.prototype._setValue_direct_setNeedsUpdate,We.prototype._setValue_direct_setMatrixWorldNeedsUpdate],[We.prototype._setValue_array,We.prototype._setValue_array_setNeedsUpdate,We.prototype._setValue_array_setMatrixWorldNeedsUpdate],[We.prototype._setValue_arrayElement,We.prototype._setValue_arrayElement_setNeedsUpdate,We.prototype._setValue_arrayElement_setMatrixWorldNeedsUpdate],[We.prototype._setValue_fromArray,We.prototype._setValue_fromArray_setNeedsUpdate,We.prototype._setValue_fromArray_setMatrixWorldNeedsUpdate]];var cx=new Float32Array(1);var ma=class{constructor(t,e,n=0,s=1/0){this.ray=new Ur(t,e),this.near=n,this.far=s,this.camera=null,this.layers=new Dr,this.params={Mesh:{},Line:{threshold:1},LOD:{},Points:{threshold:1},Sprite:{}}}set(t,e){this.ray.set(t,e)}setFromCamera(t,e){e.isPerspectiveCamera?(this.ray.origin.setFromMatrixPosition(e.matrixWorld),this.ray.direction.set(t.x,t.y,.5).unproject(e).sub(this.ray.origin).normalize(),this.camera=e):e.isOrthographicCamera?(this.ray.origin.set(t.x,t.y,(e.near+e.far)/(e.near-e.far)).unproject(e),this.ray.direction.set(0,0,-1).transformDirection(e.matrixWorld),this.camera=e):console.error("THREE.Raycaster: Unsupported camera type: "+e.type)}intersectObject(t,e=!0,n=[]){return cc(t,this,n,e),n.sort(Uu),n}intersectObjects(t,e=!0,n=[]){for(let s=0,r=t.length;s<r;s++)cc(t[s],this,n,e);return n.sort(Uu),n}};function Uu(i,t){return i.distance-t.distance}function cc(i,t,e,n){if(i.layers.test(t.layers)&&i.raycast(t,e),n===!0){let s=i.children;for(let r=0,a=s.length;r<a;r++)cc(s[r],t,e,!0)}}typeof __THREE_DEVTOOLS__!="undefined"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("register",{detail:{revision:"160"}}));typeof window!="undefined"&&(window.__THREE__?console.warn("WARNING: Multiple instances of Three.js being imported."):window.__THREE__="160");function Ms(i,t=!1){let e=i[0].index!==null,n=new Set(Object.keys(i[0].attributes)),s=new Set(Object.keys(i[0].morphAttributes)),r={},a={},o=i[0].morphTargetsRelative,l=new qe,c=0;for(let h=0;h<i.length;++h){let u=i[h],d=0;if(e!==(u.index!==null))return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed with geometry at index "+h+". All geometries must have compatible attributes; make sure index attribute exists among all geometries, or in none of them."),null;for(let p in u.attributes){if(!n.has(p))return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed with geometry at index "+h+'. All geometries must have compatible attributes; make sure "'+p+'" attribute exists among all geometries, or in none of them.'),null;r[p]===void 0&&(r[p]=[]),r[p].push(u.attributes[p]),d++}if(d!==n.size)return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed with geometry at index "+h+". Make sure all geometries have the same number of attributes."),null;if(o!==u.morphTargetsRelative)return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed with geometry at index "+h+". .morphTargetsRelative must be consistent throughout all geometries."),null;for(let p in u.morphAttributes){if(!s.has(p))return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed with geometry at index "+h+".  .morphAttributes must be consistent throughout all geometries."),null;a[p]===void 0&&(a[p]=[]),a[p].push(u.morphAttributes[p])}if(t){let p;if(e)p=u.index.count;else if(u.attributes.position!==void 0)p=u.attributes.position.count;else return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed with geometry at index "+h+". The geometry must have either an index or a position attribute"),null;l.addGroup(c,p,h),c+=p}}if(e){let h=0,u=[];for(let d=0;d<i.length;++d){let p=i[d].index;for(let x=0;x<p.count;++x)u.push(p.getX(x)+h);h+=i[d].attributes.position.count}l.setIndex(u)}for(let h in r){let u=of(r[h]);if(!u)return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed while trying to merge the "+h+" attribute."),null;l.setAttribute(h,u)}for(let h in a){let u=a[h][0].length;if(u===0)break;l.morphAttributes=l.morphAttributes||{},l.morphAttributes[h]=[];for(let d=0;d<u;++d){let p=[];for(let y=0;y<a[h].length;++y)p.push(a[h][y][d]);let x=of(p);if(!x)return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed while trying to merge the "+h+" morphAttribute."),null;l.morphAttributes[h].push(x)}}return l}function of(i){let t,e,n,s=-1,r=0;for(let c=0;c<i.length;++c){let h=i[c];if(h.isInterleavedBufferAttribute)return console.error("THREE.BufferGeometryUtils: .mergeAttributes() failed. InterleavedBufferAttributes are not supported."),null;if(t===void 0&&(t=h.array.constructor),t!==h.array.constructor)return console.error("THREE.BufferGeometryUtils: .mergeAttributes() failed. BufferAttribute.array must be of consistent array types across matching attributes."),null;if(e===void 0&&(e=h.itemSize),e!==h.itemSize)return console.error("THREE.BufferGeometryUtils: .mergeAttributes() failed. BufferAttribute.itemSize must be consistent across matching attributes."),null;if(n===void 0&&(n=h.normalized),n!==h.normalized)return console.error("THREE.BufferGeometryUtils: .mergeAttributes() failed. BufferAttribute.normalized must be consistent across matching attributes."),null;if(s===-1&&(s=h.gpuType),s!==h.gpuType)return console.error("THREE.BufferGeometryUtils: .mergeAttributes() failed. BufferAttribute.gpuType must be consistent across matching attributes."),null;r+=h.array.length}let a=new t(r),o=0;for(let c=0;c<i.length;++c)a.set(i[c].array,o),o+=i[c].array.length;let l=new gn(a,e,n);return s!==void 0&&(l.gpuType=s),l}var lr=class i extends Ce{constructor(){let t=i.SkyShader,e=new _n({name:t.name,uniforms:gc.clone(t.uniforms),vertexShader:t.vertexShader,fragmentShader:t.fragmentShader,side:Sn,depthWrite:!1});super(new Ae(1,1,1),e),this.isSky=!0}};lr.SkyShader={name:"SkyShader",uniforms:{turbidity:{value:2},rayleigh:{value:1},mieCoefficient:{value:.005},mieDirectionalG:{value:.8},sunPosition:{value:new O},up:{value:new O(0,1,0)}},vertexShader:`
		uniform vec3 sunPosition;
		uniform float rayleigh;
		uniform float turbidity;
		uniform float mieCoefficient;
		uniform vec3 up;

		varying vec3 vWorldPosition;
		varying vec3 vSunDirection;
		varying float vSunfade;
		varying vec3 vBetaR;
		varying vec3 vBetaM;
		varying float vSunE;

		// constants for atmospheric scattering
		const float e = 2.71828182845904523536028747135266249775724709369995957;
		const float pi = 3.141592653589793238462643383279502884197169;

		// wavelength of used primaries, according to preetham
		const vec3 lambda = vec3( 680E-9, 550E-9, 450E-9 );
		// this pre-calcuation replaces older TotalRayleigh(vec3 lambda) function:
		// (8.0 * pow(pi, 3.0) * pow(pow(n, 2.0) - 1.0, 2.0) * (6.0 + 3.0 * pn)) / (3.0 * N * pow(lambda, vec3(4.0)) * (6.0 - 7.0 * pn))
		const vec3 totalRayleigh = vec3( 5.804542996261093E-6, 1.3562911419845635E-5, 3.0265902468824876E-5 );

		// mie stuff
		// K coefficient for the primaries
		const float v = 4.0;
		const vec3 K = vec3( 0.686, 0.678, 0.666 );
		// MieConst = pi * pow( ( 2.0 * pi ) / lambda, vec3( v - 2.0 ) ) * K
		const vec3 MieConst = vec3( 1.8399918514433978E14, 2.7798023919660528E14, 4.0790479543861094E14 );

		// earth shadow hack
		// cutoffAngle = pi / 1.95;
		const float cutoffAngle = 1.6110731556870734;
		const float steepness = 1.5;
		const float EE = 1000.0;

		float sunIntensity( float zenithAngleCos ) {
			zenithAngleCos = clamp( zenithAngleCos, -1.0, 1.0 );
			return EE * max( 0.0, 1.0 - pow( e, -( ( cutoffAngle - acos( zenithAngleCos ) ) / steepness ) ) );
		}

		vec3 totalMie( float T ) {
			float c = ( 0.2 * T ) * 10E-18;
			return 0.434 * c * MieConst;
		}

		void main() {

			vec4 worldPosition = modelMatrix * vec4( position, 1.0 );
			vWorldPosition = worldPosition.xyz;

			gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );
			gl_Position.z = gl_Position.w; // set z to camera.far

			vSunDirection = normalize( sunPosition );

			vSunE = sunIntensity( dot( vSunDirection, up ) );

			vSunfade = 1.0 - clamp( 1.0 - exp( ( sunPosition.y / 450000.0 ) ), 0.0, 1.0 );

			float rayleighCoefficient = rayleigh - ( 1.0 * ( 1.0 - vSunfade ) );

			// extinction (absorbtion + out scattering)
			// rayleigh coefficients
			vBetaR = totalRayleigh * rayleighCoefficient;

			// mie coefficients
			vBetaM = totalMie( turbidity ) * mieCoefficient;

		}`,fragmentShader:`
		varying vec3 vWorldPosition;
		varying vec3 vSunDirection;
		varying float vSunfade;
		varying vec3 vBetaR;
		varying vec3 vBetaM;
		varying float vSunE;

		uniform float mieDirectionalG;
		uniform vec3 up;

		// constants for atmospheric scattering
		const float pi = 3.141592653589793238462643383279502884197169;

		const float n = 1.0003; // refractive index of air
		const float N = 2.545E25; // number of molecules per unit volume for air at 288.15K and 1013mb (sea level -45 celsius)

		// optical length at zenith for molecules
		const float rayleighZenithLength = 8.4E3;
		const float mieZenithLength = 1.25E3;
		// 66 arc seconds -> degrees, and the cosine of that
		const float sunAngularDiameterCos = 0.999956676946448443553574619906976478926848692873900859324;

		// 3.0 / ( 16.0 * pi )
		const float THREE_OVER_SIXTEENPI = 0.05968310365946075;
		// 1.0 / ( 4.0 * pi )
		const float ONE_OVER_FOURPI = 0.07957747154594767;

		float rayleighPhase( float cosTheta ) {
			return THREE_OVER_SIXTEENPI * ( 1.0 + pow( cosTheta, 2.0 ) );
		}

		float hgPhase( float cosTheta, float g ) {
			float g2 = pow( g, 2.0 );
			float inverse = 1.0 / pow( 1.0 - 2.0 * g * cosTheta + g2, 1.5 );
			return ONE_OVER_FOURPI * ( ( 1.0 - g2 ) * inverse );
		}

		void main() {

			vec3 direction = normalize( vWorldPosition - cameraPosition );

			// optical length
			// cutoff angle at 90 to avoid singularity in next formula.
			float zenithAngle = acos( max( 0.0, dot( up, direction ) ) );
			float inverse = 1.0 / ( cos( zenithAngle ) + 0.15 * pow( 93.885 - ( ( zenithAngle * 180.0 ) / pi ), -1.253 ) );
			float sR = rayleighZenithLength * inverse;
			float sM = mieZenithLength * inverse;

			// combined extinction factor
			vec3 Fex = exp( -( vBetaR * sR + vBetaM * sM ) );

			// in scattering
			float cosTheta = dot( direction, vSunDirection );

			float rPhase = rayleighPhase( cosTheta * 0.5 + 0.5 );
			vec3 betaRTheta = vBetaR * rPhase;

			float mPhase = hgPhase( cosTheta, mieDirectionalG );
			vec3 betaMTheta = vBetaM * mPhase;

			vec3 Lin = pow( vSunE * ( ( betaRTheta + betaMTheta ) / ( vBetaR + vBetaM ) ) * ( 1.0 - Fex ), vec3( 1.5 ) );
			Lin *= mix( vec3( 1.0 ), pow( vSunE * ( ( betaRTheta + betaMTheta ) / ( vBetaR + vBetaM ) ) * Fex, vec3( 1.0 / 2.0 ) ), clamp( pow( 1.0 - dot( up, vSunDirection ), 5.0 ), 0.0, 1.0 ) );

			// nightsky
			float theta = acos( direction.y ); // elevation --> y-axis, [-pi/2, pi/2]
			float phi = atan( direction.z, direction.x ); // azimuth --> x-axis [-pi/2, pi/2]
			vec2 uv = vec2( phi, theta ) / vec2( 2.0 * pi, pi ) + vec2( 0.5, 0.0 );
			vec3 L0 = vec3( 0.1 ) * Fex;

			// composition + solar disc
			float sundisk = smoothstep( sunAngularDiameterCos, sunAngularDiameterCos + 0.00002, cosTheta );
			L0 += ( vSunE * 19000.0 * Fex ) * sundisk;

			vec3 texColor = ( Lin + L0 ) * 0.04 + vec3( 0.0, 0.0003, 0.00075 );

			vec3 retColor = pow( texColor, vec3( 1.0 / ( 1.2 + ( 1.2 * vSunfade ) ) ) );

			gl_FragColor = vec4( retColor, 1.0 );

			#include <tonemapping_fragment>
			#include <colorspace_fragment>

		}`};var cr={gate:[[55,4],[10,2.5,-4]],hall:[[-13.4,-11.2],[-28,2.3,-12]],hearth:[[-16.4,-14.6],[-19.6,.5,-12]],seat:[[-23.2,-12],[-28,2.1,-12]],chamber:[[-4.6,-18.2],[3.2,.9,-21.6]],kitchen:[[-20.6,14.6],[-27,1.1,13.6]],stables:[[10,12.5],[6,1.6,23]],wall:[[60,-44],[19300,950,10400]],sands:[[-50,44],[-2600,-52,3600]]},Ki=[228,17],ya=48.9,Di=32e3;function ax(i){return function(){i|=0,i=i+1831565813|0;let t=Math.imul(i^i>>>15,1|i);return t=t+Math.imul(t^t>>>7,61|t)^t,((t^t>>>14)>>>0)/4294967296}}var Ss=(i,t,e)=>{let n=Math.max(0,Math.min(1,(e-i)/(t-i)));return n*n*(3-2*n)},Wn=(i,t,e)=>Math.max(t,Math.min(e,i));async function Mx(i,t){let e=!!t.cy,n=f=>e?f[1]:f[0],s=Math.min(screen.width,screen.height)<=600,r=matchMedia("(pointer: coarse)").matches,a=matchMedia("(prefers-reduced-motion: reduce)").matches,o=ax(1237),l=f=>new URL(f,document.baseURI).href,c=document.createElement("canvas");c.className="ll-canvas",c.tabIndex=0,c.setAttribute("role","img"),c.setAttribute("aria-label",n(t.ui.canvas)),i.appendChild(c);let h;try{h=new Fr({canvas:c,antialias:!s,powerPreference:"high-performance",logarithmicDepthBuffer:!0})}catch{i.classList.add("fail"),c.remove();return}let u=Math.min(devicePixelRatio||1,s?1.6:2),d=s?Math.min(u,1.25):u;h.setPixelRatio(d),h.outputColorSpace=Je,h.toneMapping=uc,h.toneMappingExposure=.62,h.shadowMap.enabled=!0,h.shadowMap.type=hc;let p=Math.min(8,h.capabilities.getMaxAnisotropy()),x={grass:s?2600:9e3,fireShadow:!s,shadow:s?1024:2048},y=s?"-m":"",g=new ua,m=(f,_)=>new Promise((M,E)=>g.load(l(f),C=>{_&&(C.colorSpace=Je),C.anisotropy=p,M(C)},void 0,E)),w=f=>new Promise((_,M)=>{let E=new Image;E.onload=()=>_(E),E.onerror=M,E.src=l(f)}),v;try{v=await Promise.all([w("llys-h.png"),m(`llys-n${y}.webp`),m(`llys-c${y}.webp`,!0),m(`stone${y}.webp`,!0),m(`stone-n${y}.webp`)])}catch{i.classList.add("fail"),c.remove();return}let[I,H,U,N,Y]=v,b=I.width,P=document.createElement("canvas");P.width=P.height=b;let X=P.getContext("2d",{willReadFrequently:!0});X.drawImage(I,0,0);let rt=X.getImageData(0,0,b,b).data,_t=new Float32Array(b*b);for(let f=0;f<b*b;f++)_t[f]=(rt[f*4]*256+rt[f*4+1])/20-50;function k(f,_){let M=Wn((f+Di)/(2*Di)*b-.5,0,b-1.001),E=Wn((_+Di)/(2*Di)*b-.5,0,b-1.001),C=Math.floor(M),L=Math.floor(E),z=M-C,D=E-L,G=L*b+C;return _t[G]*(1-z)*(1-D)+_t[G+1]*z*(1-D)+_t[G+b]*(1-z)*D+_t[G+b+1]*z*D}let q=f=>f*f/(2*6371e3*1.15);function j(f,_){let M=Math.hypot(f,_),C=(.6*Math.sin(f*.031+1.3)*Math.cos(_*.027)+.35*Math.sin(f*.07+_*.05)+.15*Math.sin(f*.19-_*.13))*Ss(48,110,Math.max(Math.abs(f)*1.25,Math.abs(_)*1.6)),L=Ss(220,760,M);return C*(1-L)+(k(f,_)-ya)*L-q(M)}let et=new Or,ut=new ge(9676733);et.fog=new ta(ut,21e-6);let tt=new Mn(s?68:60,1,.1,8e4);tt.rotation.order="YXZ";let at=f=>{let _=document.createElement("canvas");return _.width=_.height=f,[_,_.getContext("2d")]};function lt(f,_,M=!0){let E=new ia(f);return E.wrapS=E.wrapT=ps,E.anisotropy=p,M&&(E.colorSpace=Je),_&&E.repeat.set(_[0],_[1]),E}function Ut(f,_=2){let M=f.width,E=f.getContext("2d").getImageData(0,0,M,M).data,[C,L]=at(M),z=L.createImageData(M,M),D=z.data,G=($,K)=>E[((K+M)%M*M+($+M)%M)*4]/255;for(let $=0;$<M;$++)for(let K=0;K<M;K++){let Z=(G(K+1,$)-G(K-1,$))*_,it=(G(K,$+1)-G(K,$-1))*_,wt=Math.hypot(Z,it,1),Ot=($*M+K)*4;D[Ot]=(-Z/wt*.5+.5)*255,D[Ot+1]=(it/wt*.5+.5)*255,D[Ot+2]=(1/wt*.5+.5)*255,D[Ot+3]=255}return L.putImageData(z,0,0),lt(C,null,!1)}let nt=(f,_,M,E,C,L,z,D)=>{for(let G=0;G<M;G++){f.fillStyle=`rgba(${E},${C+o()*(L-C)})`;let $=z+o()*(D-z);f.fillRect(o()*_,o()*_,$,$)}},ht=(f,_,M,E,C,L,z)=>{for(let D=0;D<M;D++){let G=o()*_,$=o()*_,K=L+o()*(z-L);for(let Z of[-_,0,_])for(let it of[-_,0,_]){let wt=f.createRadialGradient(G+Z,$+it,0,G+Z,$+it,K);wt.addColorStop(0,`rgba(${E},${C})`),wt.addColorStop(1,`rgba(${E},0)`),f.fillStyle=wt,f.fillRect(G+Z-K,$+it-K,2*K,2*K)}}},[Dt,Bt]=at(512);Bt.fillStyle="#e8e2d4",Bt.fillRect(0,0,512,512),ht(Bt,512,60,"214,205,186",.35,30,120),ht(Bt,512,40,"246,243,236",.5,20,90),ht(Bt,512,14,"180,178,160",.12,40,140),nt(Bt,512,5e3,"120,110,95",.02,.1,1,3);for(let f=0;f<70;f++){Bt.strokeStyle=`rgba(150,140,120,${.03+o()*.05})`,Bt.lineWidth=1+o()*3;let _=o()*512,M=o()*512;Bt.beginPath(),Bt.moveTo(_,M),Bt.lineTo(_+(o()-.5)*6,M+40+o()*90),Bt.stroke()}let zt=lt(Dt),[ne,Zt]=at(256);Zt.drawImage(Dt,0,0,256,256),Zt.strokeStyle="rgba(150,48,30,.85)",Zt.lineWidth=2.2;for(let f=0;f<4;f++){Zt.beginPath(),Zt.moveTo(0,f*64+1),Zt.lineTo(256,f*64+1),Zt.stroke();for(let _=0;_<3;_++){let M=_*96+f%2*48;Zt.beginPath(),Zt.moveTo(M,f*64),Zt.lineTo(M,f*64+64),Zt.stroke()}}let Wt=lt(ne),[ae,F]=at(512),[Et,st]=at(512);F.fillStyle="#6d5a3e",F.fillRect(0,0,512,512),st.fillStyle="#555",st.fillRect(0,0,512,512);for(let f=0;f<9e3;f++){let _=o()*512,M=o()*512,E=18+o()*34,C=.6+o()*1.6,L=o(),z=L<.45?[118+o()*40,100+o()*30,70+o()*20]:L<.85?[150+o()*50,122+o()*35,72+o()*25]:[110,108,100];for(let D of[-512,0,512])for(let G of[-512,0,512]){F.strokeStyle=`rgba(${z[0]|0},${z[1]|0},${z[2]|0},.75)`,F.lineWidth=C,F.beginPath(),F.moveTo(_+D,M+G),F.lineTo(_+D+(o()-.5)*3,M+G+E),F.stroke();let $=110+L*120;st.strokeStyle=`rgba(${$},${$},${$},.7)`,st.lineWidth=C,st.beginPath(),st.moveTo(_+D,M+G),st.lineTo(_+D+(o()-.5)*3,M+G+E),st.stroke()}}for(let f=0;f<512;f+=64){let _=F.createLinearGradient(0,f,0,f+64);_.addColorStop(0,"rgba(30,22,12,.0)"),_.addColorStop(.85,"rgba(30,22,12,.12)"),_.addColorStop(1,"rgba(30,22,12,.4)"),F.fillStyle=_,F.fillRect(0,f,512,64);let M=st.createLinearGradient(0,f,0,f+64);M.addColorStop(0,"rgba(255,255,255,.15)"),M.addColorStop(1,"rgba(0,0,0,.45)"),st.fillStyle=M,st.fillRect(0,f,512,64)}ht(F,512,16,"70,72,60",.25,30,90);let vt=lt(ae),ct=Ut(Et,3),[Xt,Pt]=at(256);Pt.fillStyle="#2a2119",Pt.fillRect(0,0,256,256);for(let f=0;f<2500;f++){let _=30+o()*45;Pt.strokeStyle=`rgba(${_+10},${_},${_-8},.6)`,Pt.lineWidth=.5+o();let M=o()*256,E=o()*256;Pt.beginPath(),Pt.moveTo(M,E),Pt.lineTo(M+(o()-.5)*2,E+10+o()*16),Pt.stroke()}let T=lt(Xt),[S,W]=at(512),[gt,pt]=at(512);W.fillStyle="#6a5440",W.fillRect(0,0,512,512),pt.fillStyle="#808080",pt.fillRect(0,0,512,512);for(let f=0;f<700;f++){let _=o()*512,M=o()<.2?50:25,E=.08+o()*.25,C=.5+o()*2.5,L=(o()-.5)*16;W.strokeStyle=`rgba(${M+20},${M+8},${M-5},${E})`,pt.strokeStyle=`rgba(40,40,40,${E})`,W.lineWidth=pt.lineWidth=C;for(let z of[W,pt])for(let D of[-512,0,512])z.beginPath(),z.moveTo(0,_+D),z.bezierCurveTo(170,_+D+L,340,_+D-L,512,_+D),z.stroke()}ht(W,512,20,"140,118,92",.18,20,80),ht(W,512,12,"40,30,22",.2,10,50);for(let f=0;f<26;f++){let _=o()*512,M=o()*512;W.fillStyle="rgba(35,25,15,.5)",W.beginPath(),W.ellipse(_,M,5+o()*6,2+o()*3,0,0,7),W.fill()}let mt=lt(S),Vt=Ut(gt,1.5),[It,Tt]=at(256);Tt.fillStyle="#e6dfcf",Tt.fillRect(0,0,256,256),Tt.fillStyle="#93331f";for(let f=-1;f<5;f++){let _=f*64;Tt.beginPath(),Tt.moveTo(0,_),Tt.lineTo(128,_+40),Tt.lineTo(256,_),Tt.lineTo(256,_+32),Tt.lineTo(128,_+72),Tt.lineTo(0,_+32),Tt.closePath(),Tt.fill()}Tt.globalAlpha=.25,Tt.drawImage(S,0,0,256,256),Tt.globalAlpha=1,nt(Tt,256,900,"60,40,30",.03,.12,1,3);let jt=lt(It),[he,ft]=at(512);ft.fillStyle="#4e3f2e",ft.fillRect(0,0,512,512),ht(ft,512,50,"70,58,42",.5,20,70),ht(ft,512,30,"38,30,22",.45,15,60);for(let f=0;f<2600;f++){let _=o()*512,M=o()*512,E=o()*Math.PI,C=14+o()*30,L=o();ft.strokeStyle=L<.6?`rgba(${150+o()*40},${140+o()*30},${70+o()*20},.75)`:`rgba(${90+o()*30},${110+o()*30},50,.7)`,ft.lineWidth=.8+o()*1.4,ft.beginPath(),ft.moveTo(_,M),ft.lineTo(_+Math.cos(E)*C,M+Math.sin(E)*C),ft.stroke()}let Me=lt(he),[xe,Yt]=at(512);Yt.fillStyle="#58693c",Yt.fillRect(0,0,512,512),ht(Yt,512,40,"90,104,58",.45,20,80),ht(Yt,512,30,"66,80,42",.4,20,70),ht(Yt,512,10,"120,120,60",.25,30,90);for(let f=0;f<16e3;f++){let _=o()*512,M=o()*512,E=o();Yt.strokeStyle=E<.5?`rgba(${76+o()*44},${96+o()*40},${42+o()*20},.55)`:E<.9?`rgba(${40+o()*30},${60+o()*30},20,.5)`:`rgba(${150+o()*40},${150+o()*30},90,.5)`,Yt.lineWidth=.7+o(),Yt.beginPath(),Yt.moveTo(_,M),Yt.lineTo(_+(o()-.5)*5,M-4-o()*8),Yt.stroke()}let $t=lt(xe),[Ht,re]=at(256);re.fillStyle="#6b5a44",re.fillRect(0,0,256,256),ht(re,256,40,"92,78,58",.5,10,40),ht(re,256,20,"60,50,38",.5,10,30),nt(re,256,3e3,"150,140,120",.1,.4,1,3),nt(re,256,1500,"40,32,24",.1,.4,1,2);let Ee=lt(Ht),[Ve,Kt]=at(512),St=160,B=f=>(f+St/2)/St*512;Kt.fillStyle="#000",Kt.fillRect(0,0,512,512),Kt.lineCap="round",Kt.lineJoin="round",Kt.strokeStyle="rgba(255,255,255,.9)";let At=(f,_)=>{Kt.lineWidth=_/St*512,Kt.beginPath(),f.forEach(([M,E],C)=>C?Kt.lineTo(B(M),B(E)):Kt.moveTo(B(M),B(E))),Kt.stroke()};At([[75,6],[44,1],[20,2],[0,-2],[-14.5,-5.5]],4.2),At([[0,-2],[-4,-15.5]],2.6),At([[20,2],[10,14],[8,19.5]],3.2),At([[0,-2],[-12,8],[-18.5,13.5]],2.8),At([[20,2],[22,-15.5]],3),At([[20,2],[30,11]],2),At([[8,2.5],[8,2.5]],7);for(let[f,_,M]of[[42,1,7],[-14.5,-5,4],[-14.5,-18.5,3.5],[8,19,6],[-18,14,4],[22,-15,5]]){let E=Kt.createRadialGradient(B(f),B(_),0,B(f),B(_),M/St*512);E.addColorStop(0,"rgba(255,255,255,.85)"),E.addColorStop(1,"rgba(255,255,255,0)"),Kt.fillStyle=E,Kt.fillRect(0,0,512,512)}let Lt=Kt.getImageData(0,0,512,512).data,ie=(f,_)=>{let M=Wn(Math.round(B(f)),0,511),E=Wn(Math.round(B(_)),0,511);return Lt[(E*512+M)*4]/255},Jt=lt(Ve,null,!1);Jt.wrapS=Jt.wrapT=Rn,Jt.flipY=!1;function Re(f,_,M,E){let[C,L]=at(256);L.fillStyle=f,L.fillRect(0,0,256,256);for(let z=0;z<4;z++)for(let D=0;D<4;D++){let G=32+D*64,$=32+z*64;L.fillStyle=_,L.beginPath(),L.moveTo(G,$-26),L.lineTo(G+26,$),L.lineTo(G,$+26),L.lineTo(G-26,$),L.closePath(),L.fill(),L.fillStyle=f,L.beginPath(),L.moveTo(G,$-20),L.lineTo(G+20,$),L.lineTo(G,$+20),L.lineTo(G-20,$),L.closePath(),L.fill(),L.fillStyle=M,E==="cross"?(L.fillRect(G-3,$-12,6,24),L.fillRect(G-12,$-3,24,6)):(L.beginPath(),L.arc(G,$,8,0,7),L.fill(),L.fillStyle=_,L.beginPath(),L.arc(G,$,3.5,0,7),L.fill())}for(let z=0;z<2600;z++)L.fillStyle=`rgba(0,0,0,${o()*.08})`,L.fillRect(o()*256,o()*256,1,3);return lt(C)}let Pe=Re("#7d1d1a","#c9962e","#2f5a3a","cross"),Ke=Re("#2c4a35","#c9962e","#8e2a20","ring"),[un,Se]=at(128);Se.fillStyle="#d8d1c0",Se.fillRect(0,0,128,128);for(let f=0;f<128;f+=2)Se.fillStyle="rgba(160,150,130,.12)",Se.fillRect(f,0,1,128),Se.fillRect(0,f,128,1);ht(Se,128,6,"200,190,170",.25,10,30);let fn=lt(un),[Nn,ji]=at(512);function Ma(f,_,M,E,C,L){f.save(),f.translate(_,M),f.scale(E,E),f.fillStyle=C,f.strokeStyle=C,f.lineCap="round",f.lineJoin="round",f.beginPath(),f.moveTo(-34,-6),f.bezierCurveTo(-30,-16,10,-16,20,-12),f.bezierCurveTo(26,-10,28,-2,24,6),f.bezierCurveTo(10,10,-20,10,-32,6),f.closePath(),f.fill(),f.beginPath(),f.arc(24,-18,11,0,7),f.fill(),f.beginPath();for(let z=0;z<18;z++){let D=z%2?12:17,G=z/18*Math.PI*2;f.lineTo(24+Math.cos(G)*D,-18+Math.sin(G)*D)}f.closePath(),f.fill(),f.lineWidth=6,[[-26,4,-32,26],[-16,6,-14,26],[10,6,8,26],[20,2,34,6]].forEach(([z,D,G,$])=>{f.beginPath(),f.moveTo(z,D),f.lineTo(G,$),f.stroke()}),f.lineWidth=4,f.beginPath(),f.moveTo(-33,-4),f.bezierCurveTo(-52,-10,-46,-40,-30,-36),f.stroke(),f.beginPath(),f.moveTo(-30,-36),f.lineTo(-20,-44),f.lineTo(-24,-30),f.closePath(),f.fill(),f.fillStyle=L,f.beginPath(),f.arc(20,-20,2.4,0,7),f.arc(28,-20,2.4,0,7),f.fill(),f.fillRect(19,-12,10,2),f.restore()}let di="#d4a22a",Qi="#a51f1b";[[0,0,di,Qi],[256,0,Qi,di],[0,256,Qi,di],[256,256,di,Qi]].forEach(([f,_,M,E])=>{ji.fillStyle=M,ji.fillRect(f,_,256,256),Ma(ji,f+128,_+140,2.9,E,M)}),nt(ji,512,4e3,"0,0,0",.02,.08,1,3);let bs=lt(Nn),pi=1800,[Kr,Fe]=at(1024),Fn=f=>(f+pi/2)/pi*1024,jr=[];{let _=pi/14,M=[];for(let C=0;C<15;C++){M.push([]);for(let L=0;L<15;L++)M[C].push([-pi/2+C*_+(C&&C<14?(o()-.5)*_*.5:0),-pi/2+L*_+(L&&L<14?(o()-.5)*_*.5:0)])}Fe.fillStyle="#5b7a36",Fe.fillRect(0,0,1024,1024);let E=[["#587a34",0],["#62843a",0],["#4f6f2e",0],["#a39a52",1],["#b4a65c",1],["#8c9248",1],["#7b8a44",2],["#7a6648",3]];for(let C=0;C<14;C++)for(let L=0;L<14;L++){let z=[M[C][L],M[C+1][L],M[C+1][L+1],M[C][L+1]],D=z.reduce((Z,it)=>Z+it[0],0)/4,G=z.reduce((Z,it)=>Z+it[1],0)/4;if(Math.hypot(D,G)<110)continue;let[$,K]=E[Math.floor(o()*E.length)];if(Fe.save(),Fe.beginPath(),z.forEach(([Z,it],wt)=>wt?Fe.lineTo(Fn(Z),Fn(it)):Fe.moveTo(Fn(Z),Fn(it))),Fe.closePath(),Fe.clip(),Fe.fillStyle=$,Fe.fillRect(0,0,1024,1024),K===1||K===3){let Z=Math.atan2(z[1][1]-z[0][1],z[1][0]-z[0][0])+(o()<.5?0:Math.PI/2);Fe.translate(Fn(D),Fn(G)),Fe.rotate(Z);for(let it=-40;it<40;it++)Fe.fillStyle=`rgba(${o()<.5?"255,240,200":"40,50,20"},${.04+o()*.1})`,Fe.fillRect(-200,it*5.7,400,5.7*(.5+o()*.5))}Fe.restore(),Fe.strokeStyle="rgba(48,58,30,.9)",Fe.lineWidth=2.2,Fe.beginPath(),z.forEach(([Z,it],wt)=>wt?Fe.lineTo(Fn(Z),Fn(it)):Fe.moveTo(Fn(Z),Fn(it))),Fe.closePath(),Fe.stroke(),jr.push(z)}ht(Fe,1024,70,"120,110,70",.08,20,80),ht(Fe,1024,60,"30,50,20",.08,20,70)}let A=lt(Kr,null);A.wrapS=A.wrapT=Rn,A.flipY=!1;let V=f=>new ei(Object.assign({roughness:.9,vertexColors:!0},f)),R={stone:V({map:N,normalMap:Y,normalScale:new xt(1.1,1.1),roughness:.95}),lime:V({map:zt,normalMap:Y,normalScale:new xt(.45,.45),roughness:.93}),ash:V({map:Wt,normalMap:Y,normalScale:new xt(.25,.25)}),thatch:V({map:vt,normalMap:ct,normalScale:new xt(1.4,1.4),roughness:1}),soot:V({map:T,roughness:1}),oak:V({map:mt,normalMap:Vt,roughness:.8}),chev:V({map:jt,normalMap:Vt,normalScale:new xt(.4,.4),roughness:.75}),floor:V({map:Me,roughness:1}),linen:V({map:fn,roughness:.95}),hangR:V({map:Pe,roughness:.95,side:mn}),hangG:V({map:Ke,roughness:.95,side:mn}),arms:V({map:bs,roughness:.9,side:mn}),red:V({color:9052186,roughness:.9}),green:V({color:3034419,roughness:.9}),iron:V({color:2828840,roughness:.55,metalness:.7}),gold:V({color:13146666,roughness:.35,metalness:.85}),clay:V({color:10185285,roughness:.8}),glaze:V({color:7305781,roughness:.35}),horn:V({color:10519631,roughness:.45}),straw:V({map:vt,color:14205066,roughness:1}),wattle:V({map:mt,color:10127986,roughness:1}),daub:V({map:zt,color:13352870,normalMap:Y,normalScale:new xt(.3,.3)}),bread:V({color:11039802,roughness:.9}),turf:V({map:$t,color:12108954,roughness:1})},Q=Object.values(R);R.stone.map.wrapS=R.stone.map.wrapT=ps,Y.wrapS=Y.wrapT=ps;let J=new Map,Ft=[],Gt=(f,_,M=0)=>Ft.find(E=>f>E[0]-M&&f<E[2]+M&&_>E[1]-M&&_<E[3]+M),Qt=(f,_,M)=>{let E=f[2]-f[0]>=f[3]-f[1],C=E?(f[3]-f[1])/2:(f[2]-f[0])/2,L=Math.abs(E?M-(f[1]+f[3])/2:_-(f[0]+f[2])/2);return f[4]+(f[5]-f[4])*(1-L/C)};function oe(f,_,M,E,C,L){let z=1,D=f+E*.3,G=_+C*.3,$=M+L*.3,K=Gt(D,$);if(K&&G<Qt(K,D,$)-.2){z*=1-.62*Ss(1.6,K[5],_);let Z=Math.min(f-K[0],K[2]-f,M-K[1],K[3]-M);z*=.78+.22*Ss(0,1.6,Z),z*=.86+.14*Ss(0,.8,_)}else C<.5&&(z*=.74+.26*Ss(0,1.1,_));return z}function dt(f,_,M,E){M&&f.applyMatrix4(M),f.index&&(f=f.toNonIndexed()),f.attributes.normal||f.computeVertexNormals(),f.attributes.uv||f.setAttribute("uv",new _e(new Float32Array(f.attributes.position.count*2),2));let C=f.attributes.position,L=f.attributes.normal,z=new Float32Array(C.count*3);for(let D=0;D<C.count;D++){let G=E?1:oe(C.getX(D),C.getY(D),C.getZ(D),L.getX(D),L.getY(D),L.getZ(D));z[D*3]=z[D*3+1]=z[D*3+2]=G}f.setAttribute("color",new _e(z,3));for(let D of Object.keys(f.attributes))["position","normal","uv","color"].includes(D)||f.deleteAttribute(D);f.clearGroups(),J.has(_)||J.set(_,[]),J.get(_).push(f)}let yt=(f,_,M,E=0,C=0,L=0,z=1)=>new De().compose(new O(f,_,M),new ti().setFromEuler(new ms(C,E,L,"YXZ")),new O(z,z,z));function Mt(f,_,M,E,C,L,z,D=0,G=2,$=1){let K=new Ae(f,_,M,1,$,1),Z=K.attributes.uv,it=[[M,_],[M,_],[f,M],[f,M],[f,_],[f,_]],wt=Z.count/6;for(let Ot=0;Ot<6;Ot++)for(let ue=0;ue<wt;ue++){let Nt=Ot*wt+ue;Z.setXY(Nt,Z.getX(Nt)*it[Ot][0]/G,Z.getY(Nt)*it[Ot][1]/G)}dt(K,E,yt(C,L,z,D))}function be(f,_,M,E,C,L,z,D=8,G=0,$=0,K=0,Z=1){let it=new rn(f,_,M,D,1),wt=it.attributes.uv;for(let Ot=0;Ot<wt.count;Ot++)wt.setXY(Ot,wt.getX(Ot)*Math.PI*(f+_)/Z,wt.getY(Ot)*M/Z);dt(it,E,yt(C,L,z,$,G,K))}function xn(f){let _=f.index?f.toNonIndexed():f,M=[],E=f.groups.length?f.groups:[{start:0,count:_.attributes.position.count,materialIndex:0}];for(let C of E){let L=new qe;for(let z of["position","normal","uv"]){let D=_.attributes[z];D&&L.setAttribute(z,new _e(D.array.slice(C.start*D.itemSize,(C.start+C.count)*D.itemSize),D.itemSize))}M[C.materialIndex]=M[C.materialIndex]?Ms([M[C.materialIndex],L]):L}return M}let Ne=[],Ze=[],we=(f,_,M,E,C=0)=>{let L=Math.cos(C),z=Math.sin(C),D=[[-M/2,-E/2],[M/2,-E/2],[M/2,E/2],[-M/2,E/2]].map(([G,$])=>[f+G*L+$*z,_-G*z+$*L]);for(let G=0;G<4;G++)Ne.push([...D[G],...D[(G+1)%4],.05])};function pe(f,_,M){let E=new fi;f.forEach(([D,G],$)=>$?E.lineTo(D,G):E.moveTo(D,G)),E.closePath();for(let D of _){let G=new sr,$=D.at-D.w/2,K=D.at+D.w/2,Z=D.y+D.h;G.moveTo($,D.y),G.lineTo(K,D.y),D.arch?(G.lineTo(K,Z-D.w/2),G.absarc(D.at,Z-D.w/2,D.w/2,0,Math.PI,!1)):(G.lineTo(K,Z),G.lineTo($,Z)),G.closePath(),E.holes.push(G)}let C=new Ii(E,{depth:M,bevelEnabled:!1,curveSegments:12});C.translate(0,0,-M/2);let[L,z]=xn(C);for(let D of[L,z])if(D){let G=D.attributes.uv;for(let $=0;$<G.count;$++)G.setXY($,G.getX($)/2.2,G.getY($)/2.2)}return[L,z]}function mi(f,_,M,E,C,L,z,D=[],G=null,$=R.ash){let K=Math.hypot(M-f,E-_),Z=-Math.atan2(E-_,M-f),it=yt(f,0,_,Z),wt=(ot,Rt,kt=0,ee=0,qt=0)=>{ot&&dt(ot,Rt,it.clone().multiply(yt(kt,ee,qt)))},Ot=D.filter(ot=>!ot.y).sort((ot,Rt)=>ot.at-Rt.at),ue=D.filter(ot=>ot.y),Nt=ue.filter(ot=>ot.y+ot.h<=C-.15),te=ue.filter(ot=>ot.y+ot.h>C-.15),me=0,se=[];for(let ot of Ot)se.push([me,ot.at-ot.w/2]),me=ot.at+ot.w/2;se.push([me,K]);for(let[ot,Rt]of se){if(Rt-ot<.02)continue;let[kt,ee]=pe([[0,0],[Rt-ot,0],[Rt-ot,C],[0,C]],Nt.filter(qt=>qt.at>ot&&qt.at<Rt).map(qt=>Object.assign({},qt,{at:qt.at-ot})),L);if(wt(kt,z,ot),wt(ee,$,ot),Ne.push([f+(M-f)*ot/K,_+(E-_)*ot/K,f+(M-f)*Rt/K,_+(E-_)*Rt/K,L/2]),z!==R.stone){let qt=new Ae(Rt-ot,.42,L+.14);qt.translate((ot+Rt)/2,.21,0);let le=qt.attributes.uv,Be=Math.max(Rt-ot,L)/2.2;for(let Ge=0;Ge<le.count;Ge++)le.setXY(Ge,le.getX(Ge)*Be,le.getY(Ge)*.2);dt(qt,R.stone,it.clone())}}for(let ot of Ot){let Rt=ot.at-ot.w/2,kt=ot.at+ot.w/2,ee=ot.w/2;if(ot.arch){let qt=new fi;qt.moveTo(Rt,ot.h-ee),qt.absarc(ot.at,ot.h-ee,ee,Math.PI,0,!0),qt.lineTo(kt,C),qt.lineTo(Rt,C),qt.closePath();let le=new Ii(qt,{depth:L,bevelEnabled:!1,curveSegments:12});le.translate(0,0,-L/2);let[Be,Ge]=xn(le);for(let ze of[Be,Ge]){let He=ze.attributes.uv;for(let Pn=0;Pn<He.count;Pn++)He.setXY(Pn,He.getX(Pn)/2.2,He.getY(Pn)/2.2)}wt(Be,z),wt(Ge,$);let je=new fi;je.moveTo(Rt-.3,ot.h-ee),je.absarc(ot.at,ot.h-ee,ee+.3,Math.PI,0,!0),je.lineTo(kt,ot.h-ee),je.absarc(ot.at,ot.h-ee,ee,0,Math.PI,!1),je.closePath();let en=new Ii(je,{depth:L+.04,bevelEnabled:!1,curveSegments:12});en.translate(0,0,-L/2-.02);let fe=en.attributes.uv;for(let ze=0;ze<fe.count;ze++)fe.setXY(ze,fe.getX(ze)/1.2,fe.getY(ze)/1.2);dt(en,z===R.lime?R.ash:R.stone,it.clone())}else{let qt=new Ae(ot.w+.02,C-ot.h,L);qt.translate(ot.at,ot.h+(C-ot.h)/2,0),dt(qt,z,it.clone());let le=new Ae(ot.w+.5,.2,L+.06);le.translate(ot.at,ot.h+.1,0),dt(le,R.oak,it.clone())}if(ot.leaf!==!1){let qt=ot.w-.04,le=ot.arch?ot.h-ee*.25:ot.h,Be=-1,Ge=Be*-1.3,je=it.clone().multiply(yt(Rt+.03,0,Be*(L/2-.06),Ge)),en=new Ae(qt,le,.07);en.translate(qt/2,le/2,0),dt(en,R.oak,je.clone());for(let fe of[.45,le-.5]){let ze=new Ae(qt*.8,.06,.09);ze.translate(qt*.4,fe,0),dt(ze,R.iron,je.clone())}}}for(let ot of Nt.concat(te)){for(let Rt of[-1,1]){let kt=new Ae(ot.w/2,ot.h-ot.w/2,.05);kt.translate(-Rt*ot.w/4,0,0),dt(kt,R.oak,it.clone().multiply(yt(ot.at+Rt*ot.w/2,ot.y+(ot.h-ot.w/2)/2,-L/2-.04,-Rt*1.35)))}Oe.push({x:f+(M-f)*ot.at/K,z:_+(E-_)*ot.at/K,y:ot.y+ot.h/2,w:ot.w,h:ot.h,nx:-(E-_)/K,nz:(M-f)/K})}for(let ot of Ot)Oe.push({x:f+(M-f)*ot.at/K,z:_+(E-_)*ot.at/K,y:ot.h/2,w:ot.w,h:ot.h,nx:-(E-_)/K,nz:(M-f)/K,door:!0});if(G){let[ot,Rt]=G,[kt,ee]=pe([[0,C],[K,C],[K/2+Rt,ot],[K/2-Rt,ot]],te,L);wt(kt,z),wt(ee,$)}return{L:K,ry:Z}}let Oe=[];function ii(f,_,M,E,C,L,z,D=!1,G=null){let K=E/2+.55,Z=M/2+(D?.55:.35),it=.42,wt=C-.55*(L-C)/(E/2),Ot=L-wt,ue=Math.hypot(K,Ot),Nt=D?Math.max(.4,Z-K*.95):Z,te=z?yt(f,0,_,Math.PI/2):yt(f,0,_),me=(Rt,kt,ee,qt,le,Be)=>{let Ge=new qe,je=[Rt,kt,ee],en=le;new O().subVectors(new O(...kt),new O(...Rt)).cross(new O().subVectors(new O(...ee),new O(...Rt))).dot(Be)<0&&(je=[Rt,ee,kt],en=[le[0],le[2],le[1]]),Ge.setAttribute("position",new _e(je.flat(),3)),Ge.setAttribute("uv",new _e(en.flat(),2)),Ge.computeVertexNormals(),dt(Ge,qt,te.clone())};for(let Rt of[1,-1]){let kt=new hn(2,1,10,6),ee=kt.attributes.position,qt=kt.attributes.uv;for(let fe=0;fe<ee.count;fe++){let ze=ee.getX(fe),He=ee.getY(fe)+.5,Pn=Z+(Nt-Z)*He,Qc=ze*Pn,Mf=Math.sin(He*Math.PI)*.09*(1-Math.abs(ze)*.5)+(o()-.5)*.035;ee.setXYZ(fe,Qc,wt+Ot*He-Mf+it/2,Rt*K*(1-He)),qt.setXY(fe,Qc/1.6,He*ue/1.6)}Rt<0&&kt.index.array.reverse(),kt.computeVertexNormals(),dt(kt,R.thatch,te.clone());let le=new hn(2,1,1,4),Be=le.attributes.position,Ge=le.attributes.uv;for(let fe=0;fe<Be.count;fe++){let ze=Be.getX(fe),He=Be.getY(fe)+.5,Pn=ze*(Z-.1+(Nt-Z)*He);Be.setXYZ(fe,Pn,wt+Ot*He-it/2,Rt*(K-.05)*(1-He)),Ge.setXY(fe,Pn,He*ue)}Rt>0&&le.index.array.reverse(),le.computeVertexNormals(),dt(le,R.soot,te.clone());let je=new Ae(2*Z,it*1.15,.32,6,1,1);je.translate(0,wt,Rt*(K-.12));let en=je.attributes.uv;for(let fe=0;fe<en.count;fe++)en.setXY(fe,en.getX(fe)*Z,en.getY(fe)*.3);dt(je,R.thatch,te.clone());for(let fe=-Z+.5;fe<Z-.3;fe+=.6){let ze=Math.max(0,(Math.abs(fe)-Nt)/(Z-Nt||1));if(D&&ze>.98)continue;let He=new Ae(.11,.14,ue*(1-ze)-.2);He.rotateX(Rt*Math.atan2(Ot,K)),He.translate(fe,wt+Ot*(1-ze)/2-it/2-.09,Rt*K*(1-(1-ze)/2)),dt(He,R.oak,te.clone())}for(let fe of[.33,.66]){let ze=new Ae(2*(Z+(Nt-Z)*fe)-.4,.2,.2);ze.translate(0,wt+Ot*fe-it/2-.26,Rt*K*(1-fe)),dt(ze,R.oak,te.clone())}}if(D)for(let Rt of[-1,1]){let kt=[Rt*Z,wt+it/2,-K],ee=[Rt*Z,wt+it/2,K],qt=[Rt*Nt,L+it/2,0],le=new O(Rt,1,0);me(kt,ee,qt,R.thatch,[[-K/1.6,0],[K/1.6,0],[0,ue/1.6]],le),me([kt[0]-Rt*.1,wt-it/2,kt[2]+.05],[ee[0]-Rt*.1,wt-it/2,ee[2]-.05],[qt[0],L-it/2,0],R.soot,[[0,0],[K,0],[K/2,ue]],new O(-Rt,-1,0));let Be=new Ae(.32,it*1.15,2*K);Be.translate(Rt*(Z-.12),wt,0),dt(Be,R.thatch,te.clone())}let se=new rn(.3,.3,2*Nt+.3,10,1);se.rotateZ(Math.PI/2),se.translate(0,L+it/2-.12,0);let ot=se.attributes.uv;for(let Rt=0;Rt<ot.count;Rt++)ot.setXY(Rt,ot.getX(Rt)*1.3,ot.getY(Rt)*Nt/.8);if(dt(se,R.thatch,te.clone()),!D)for(let Rt of[-1,1]){let kt=new fi;kt.moveTo(-K,wt-it*.6),kt.lineTo(0,L-it*.6+.2),kt.lineTo(K,wt-it*.6),kt.lineTo(K,wt+it*.6),kt.lineTo(0,L+it*.6+.2),kt.lineTo(-K,wt+it*.6),kt.closePath();let ee=new Ii(kt,{depth:.3,bevelEnabled:!1});ee.rotateY(Math.PI/2),ee.translate(Rt*Z-(Rt>0?.3:0),0,0);let qt=ee.attributes.uv;for(let le=0;le<qt.count;le++)qt.setXY(le,qt.getX(le)/1.6,qt.getY(le)/1.6);dt(ee,R.thatch,te.clone())}if(G!=null){let Rt=G,kt=z?[f,_+Rt]:[f+Rt,_];Mt(1.3,1,1.3,R.oak,kt[0],L+.45,kt[1],0,1);for(let qt=-1;qt<=1;qt+=2)Mt(1.34,.08,.04,R.soot,kt[0],L+.3+qt*.2,kt[1]+.66,0,1);let ee=new kr(1.2,.85,4,1);ee.rotateY(Math.PI/4),ee.translate(kt[0],L+1.35,kt[1]),dt(ee,R.thatch)}return{ey:wt,hw:K,hl:Z}}function si(f){let{cx:_,cz:M,w:E,d:C,h:L,ridge:z,t:D=.9,mat:G=R.lime}=f,$=_-E/2,K=_+E/2,Z=M-C/2,it=M+C/2,wt=(ot,Rt)=>(f.open||[]).filter(kt=>kt.side===ot).map(kt=>Object.assign({arch:!0,y:0},kt,{at:Rt/2+(ot==="n"||ot==="e"?-kt.at:kt.at)}));f.noRoom||Ft.push([$,Z,K,it,L,z]);let Ot=G===R.lime?R.ash:G,ue=z-.5,Nt=.25;mi($+D/2,it-D/2,K-D/2,it-D/2,L,D,G,wt("s",E-D),null,Ot),mi(K-D/2,Z+D/2,$+D/2,Z+D/2,L,D,G,wt("n",E-D),null,Ot),mi($+D/2,Z+D/2,$+D/2,it-D/2,L,D,G,wt("w",C-D),f.hips?null:[ue,Nt],Ot),mi(K-D/2,it-D/2,K-D/2,Z+D/2,L,D,G,wt("e",C-D),f.hips?null:[ue,Nt],Ot);let te=new hn(E-D*2+.1,C-D*2+.1);te.rotateX(-Math.PI/2),te.translate(_,.025,M);let me=te.attributes.uv;for(let ot=0;ot<me.count;ot++)me.setXY(ot,me.getX(ot)*(E-2*D)/3,me.getY(ot)*(C-2*D)/3);dt(te,f.floor||R.floor);let se=ii(_,M,E,C,L,z,!1,f.hips,f.louvre);return{x0:$,x1:K,z0:Z,z1:it,t:D,h:L,ridge:z,ix0:$+D,ix1:K-D,iz0:Z+D,iz1:it-D,ey:se.ey}}let gi=[[-44,-31],[41,-33],[43,32],[-42,34]];for(let f=0;f<4;f++){let[_,M]=[gi[f],gi[(f+1)%4]],E=Math.hypot(M[0]-_[0],M[1]-_[1]),C=f===1?[{at:Math.hypot(42.03-41,.45+33),w:3.6,h:2.2,y:0,arch:!1,leaf:!1}]:[];mi(_[0],_[1],M[0],M[1],2.2,1.3,R.stone,C);let L=new Ae(E,.14,1.45);L.translate(E/2,2.27,0);let z=L.attributes.uv;for(let D=0;D<z.count;D++)z.setXY(D,z.getX(D)*E/2.2,z.getY(D)*.66);C.length||dt(L,R.stone,yt(_[0],0,_[1],-Math.atan2(M[1]-_[1],M[0]-_[0]))),Mt(1.8,2.5,1.8,R.stone,_[0],1.25,_[1],-Math.atan2(M[1]-_[1],M[0]-_[0]),2.2)}let Ni=42.03,$e=.45;Mt(1.6,3.8,1.6,R.stone,Ni,1.9,$e-2.7),Mt(1.6,3.8,1.6,R.stone,Ni,1.9,$e+2.7),ii(Ni,$e,7.2,3.6,3.8,5.6,!0);for(let f of[-1,1]){let _=new Ae(.08,2.9,1.75);_.translate(0,1.45,f*.88),dt(_,R.oak,yt(Ni-.6,0,$e+f*1.75,f*-1.2))}let Te=si({cx:-20,cz:-12,w:17,d:11,h:3.6,ridge:9.4,louvre:.5,open:[{side:"s",at:5.5,w:1.7,h:3},{side:"n",at:5.5,w:1.7,h:3},{side:"s",at:-4.5,w:.62,h:1.3,y:1.55},{side:"s",at:.5,w:.62,h:1.3,y:1.55},{side:"n",at:-2,w:.62,h:1.3,y:1.55},{side:"w",at:0,w:.7,h:1.6,y:4.3},{side:"e",at:0,w:.62,h:1.4,y:4}]}),In=si({cx:-1,cz:-20,w:13,d:7.5,h:3.3,ridge:7.8,open:[{side:"s",at:-3.4,w:1.3,h:2.5},{side:"s",at:1.8,w:.6,h:1.2,y:1.4},{side:"s",at:4.6,w:.6,h:1.2,y:1.4},{side:"w",at:0,w:.55,h:1.2,y:1.5}]}),on=si({cx:-24,cz:14,w:10,d:6.5,h:2.9,ridge:6.6,mat:R.stone,louvre:-1.5,open:[{side:"e",at:-.4,w:1.4,h:2.3},{side:"s",at:1.5,w:.55,h:.9,y:1.4}]}),an=si({cx:8,cz:24,w:22,d:6.5,h:2.6,ridge:6.2,mat:R.daub,hips:!0,open:[{side:"n",at:-6,w:2.2,h:2.3,arch:!1,leaf:!1},{side:"n",at:2,w:2.2,h:2.3,arch:!1,leaf:!1},{side:"n",at:7.5,w:.55,h:.8,y:1.3,arch:!1}]}),hr=si({cx:24,cz:-20,w:16,d:8,h:3,ridge:7.6,mat:R.daub,hips:!0,open:[{side:"s",at:0,w:3.2,h:2.9,arch:!1,leaf:!1},{side:"n",at:0,w:3.2,h:2.9,arch:!1,leaf:!1}]});si({cx:33,cz:16,w:5.5,d:4,h:2,ridge:4.2,mat:R.daub,hips:!0,open:[{side:"w",at:0,w:1,h:1.5,arch:!1,leaf:!1}]}),si({cx:-37.5,cz:-25.5,w:3,d:2.6,h:2.1,ridge:3.8,mat:R.daub,hips:!0,open:[{side:"s",at:0,w:.9,h:1.8,arch:!1}]});for(let f of[an,hr]){for(let _=f.x0+.3;_<=f.x1-.2;_+=2.2)for(let M of[f.z0-.02,f.z1+.02])Mt(.22,f.h,.08,R.oak,_,f.h/2,M,0,1);for(let _ of[f.z0-.02,f.z1+.02])Mt(f.x1-f.x0,.22,.08,R.oak,(f.x0+f.x1)/2,f.h-.15,_,0,1)}let ce=-12,On=-19.6,ri=[ce-2.7,ce+2.7],Cn=[-26,-22.4,-18.8,-15.2],_i=5;for(let f of Cn)for(let _ of ri)be(.19,.21,_i,R.chev,f,_i/2,_,8,0,0,0,.62),Ze.push([f,_,.3]);for(let f of ri)Mt(Cn[3]-Cn[0]+1.2,.3,.3,R.oak,(Cn[0]+Cn[3])/2,_i+.15,f,0,2);function Mc(f,_,M,E,C,L=.22,z=.26){let D=Math.hypot(M-f,E-_),G=D/2,$=new fi;$.moveTo(-G,C-G-.2),$.lineTo(-G,C-G),$.absarc(0,C-G,G,Math.PI,0,!0),$.lineTo(G,C-G-.2),$.lineTo(G-z,C-G-.2),$.lineTo(G-z,C-G),$.absarc(0,C-G,G-z,0,Math.PI,!1),$.lineTo(-G+z,C-G-.2),$.closePath();let K=new Ii($,{depth:L,bevelEnabled:!1,curveSegments:18});K.translate(0,0,-L/2);let Z=K.attributes.uv;for(let it=0;it<Z.count;it++)Z.setXY(it,Z.getX(it)/1.4,Z.getY(it)/1.4);dt(K,R.ash,yt((f+M)/2,0,(_+E)/2,-Math.atan2(E-_,M-f)))}for(let f=0;f<3;f++)for(let _ of ri)Mc(Cn[f],_,Cn[f+1],_,_i);for(let f of Cn){Mc(f,ri[0],f,ri[1],_i+1.35,.26,.3),Mt(.28,.3,Te.iz1-Te.iz0,R.oak,f,_i+1.5,ce,0,2);for(let _ of[-1,1]){let M=new Ae(.2,.2,1.9);M.rotateX(_*.55),M.translate(f,_i-.75,ce+_*3.7),dt(M,R.oak)}Mt(.18,Te.ridge-_i-2,.18,R.oak,f,(Te.ridge+_i+1.4)/2-.5,ce,0,1)}let lx=[On,ce];for(let f=0;f<22;f++){let _=f/22*Math.PI*2,M=new Gr(.2+o()*.07,0);M.scale(1.3,.7,1);let E=M.attributes.uv;for(let C=0;C<E.count;C++)E.setXY(C,E.getX(C)*.4,E.getY(C)*.4);dt(M,R.stone,yt(On+Math.cos(_)*1.15*1.25,.09,ce+Math.sin(_)*1.15,_+o(),o()*.3,o()*.3))}Ze.push([On,ce,1.25]);let Xn=Te.ix0,Qr=3.4;Mt(Qr,.32,Te.iz1-Te.iz0,R.oak,Xn+Qr/2,.16,ce,0,1.6),Mt(.08,.32,Te.iz1-Te.iz0,R.oak,Xn+Qr,.16,ce,0,1);let ts=Xn+.9;Mt(.75,.5,.7,R.oak,ts,.57,ce,0,1),Mt(.12,1.9,.82,R.oak,ts-.38,1.27,ce,0,1);for(let f of[-1,1])Mt(.7,.1,.1,R.oak,ts+.02,1.1,ce+f*.38,0,1),be(.06,.06,.9,R.oak,ts+.35,.77,ce+f*.38,6);Mt(.6,.14,.62,R.red,ts+.04,.88,ce),Mt(.06,.9,.6,R.red,ts-.3,1.45,ce);for(let f of[-1,1]){let _=new Li(.09,10,8);dt(_,R.gold,yt(ts-.38,2.27,ce+f*.34))}{let f=new hn(Te.iz1-Te.iz0-.2,2.6);f.rotateY(Math.PI/2);let _=f.attributes.uv;for(let M=0;M<_.count;M++)_.setXY(M,_.getX(M)*3.6,_.getY(M));dt(f,R.hangR,yt(Xn+.04,1.65,ce))}{let f=new hn(1.7,2.1,6,6),_=f.attributes.position;for(let M=0;M<_.count;M++)_.setZ(M,Math.sin(_.getX(M)*3.4)*.04);f.computeVertexNormals(),f.rotateY(Math.PI/2),dt(f,R.arms,yt(Xn+.1,3.95,ce),!0)}be(.03,.03,1.9,R.oak,Xn+.14,5,ce,6,Math.PI/2);for(let f of[Te.iz0+.03,Te.iz1-.03])for(let[_,M]of[[-25.4,R.hangG],[-21.6,R.hangR]]){let E=new hn(2.6,1.9),C=E.attributes.uv;for(let L=0;L<C.count;L++)C.setXY(L,C.getX(L)*2.6,C.getY(L)*1.9);dt(E,M,yt(_,2.35,f,f<ce?0:Math.PI))}let af=(()=>{let f=new fi;return f.moveTo(-.3,.32),f.lineTo(.3,.32),f.quadraticCurveTo(.32,-.1,0,-.42),f.quadraticCurveTo(-.32,-.1,-.3,.32),new Ii(f,{depth:.04,bevelEnabled:!0,bevelSize:.015,bevelThickness:.015,bevelSegments:1})})(),Sc=[R.arms,R.red,R.green,R.arms,R.red,R.green,R.arms,R.red],lf=0;for(let f of Cn)for(let _ of ri){let M=_<ce?1:-1,E=af.clone(),C=E.attributes.uv;for(let L=0;L<C.count;L++)C.setXY(L,C.getX(L)*1.4+.5,C.getY(L)*1.4+.5);dt(E,Sc[lf++%Sc.length],yt(f,3.1,_+M*.23,M>0?0:Math.PI,-.12))}function bc(f,_,M,E,C){let[L,z]=E?[M,.85]:[.85,M];if(Mt(L,.07,z,R.oak,f,.78,_,0,1.4),C){Mt(L+.02,.01,z+.2,R.linen,f,.82,_,0,1.2);for(let D of[-1,1])Mt(E?L+.02:.01,.32,E?.01:z+.02,R.linen,E?f:f+D*.52,.66,E?_+D*.52:_,0,1.2)}for(let D of[-.38,.38])Mt(E?.08:.7,.74,E?.7:.08,R.oak,E?f+D*M:f,.37,E?_:_+D*M,0,1);we(f,_,L,z)}bc(Xn+2.35,ce,6.6,!1,!0);for(let f of[-1,1])Mt(.36,.44,2,R.oak,Xn+1.55,.54,ce+f*2.15,0,1);for(let f of[-1,1]){let _=ce+f*4.1;bc(-19.9,_,6.4,!0,f<0),Mt(6.4,.42,.32,R.oak,-19.9,.21,_-f*.75,0,1.4),we(-19.9,_-f*.75,6.4,.32)}let Ec=new rn(.045,.035,.12,10),Sa=new Li(.12,12,6,0,Math.PI*2,Math.PI/2,Math.PI/2),cf=new Hr([[0,0],[.08,0],[.11,.08],[.1,.2],[.06,.28],[.065,.33],[0,.33]].map(([f,_])=>new xt(f,_)),12),to=new Li(.1,10,6);to.scale(1.3,.55,1),Sa.rotateX(Math.PI);let ba=(f,_,M,E)=>{for(let C=0;C<M;C++){let L=(C+.5)/M-.5,z=E?f+L*5.8:f+(o()-.5)*.3,D=E?_+(o()-.5)*.3:_+L*6.2,G=o();G<.4?dt(Ec.clone(),o()<.5?R.horn:R.clay,yt(z,.88,D)):G<.65?dt(Sa.clone(),R.oak,yt(z,.94,D)):G<.85?dt(to.clone(),R.bread,yt(z,.86,D,o()*3)):dt(cf.clone(),R.glaze,yt(z,.82,D))}};ba(Xn+2.35,ce,10,!1),ba(-19.9,ce-4.1,9,!0),ba(-19.9,ce+4.1,7,!0);for(let f=0;f<5;f++)dt(Ec.clone(),R.gold,yt(Xn+2.2,.88,ce-1.6+f*.8));{let f=yt(-17.3,0,-13.6,-.6),_=new rn(.2,.22,.45,8);_.translate(0,.225,0),dt(_,R.oak,f.clone());let M=(E,C,L,z,D)=>{let G=Math.hypot(C[0]-E[0],C[1]-E[1]),$=new Ae(G,L,z);$.rotateZ(Math.atan2(C[1]-E[1],C[0]-E[0])),$.translate((E[0]+C[0])/2,(E[1]+C[1])/2,0),dt($,D,f.clone())};M([0,.47],[.16,1.4],.13,.12,R.oak),M([.16,1.4],[.36,1.36],.07,.05,R.oak),M([.36,1.36],[.6,1.2],.07,.05,R.oak),M([.6,1.2],[.1,.5],.05,.05,R.oak);for(let E=0;E<10;E++){let C=(E+1)/11,L=.02+C*.14,z=.55+C*.82,D=.16+C*.44,G=1.39-C*.19,$=new rn(.003,.003,1,3),K=Math.hypot(D-L,G-z);$.scale(1,K,1),$.rotateZ(-Math.atan2(D-L,G-z)),$.translate((L+D)/2,(z+G)/2,0),dt($,R.gold,f.clone(),!0)}Mt(.5,.04,.5,R.oak,-13.4,.55,-12.4,.3,.5),Mt(.3,.55,.3,R.oak,-13.4,.27,-12.4,.3,.5),Ze.push([-13.4,-12.4,.4]);for(let E=0;E<7;E++)for(let C=0;C<7;C++)(E+C)%2&&Mt(.06,.006,.06,R.soot,-13.4+(E-3)*.062,.573,-12.4+(C-3)*.062,0,.5);for(let E=0;E<9;E++)be(.014,.014,.05,E?R.oak:R.gold,-13.4+(o()-.5)*.38,.6,-12.4+(o()-.5)*.38,6)}let wc=[[Cn[0],ri[0]+.25],[Cn[0],ri[1]-.25],[Cn[2],ri[0]+.25],[Cn[2],ri[1]-.25]];for(let[f,_]of wc)be(.025,.02,.5,R.iron,f,2.75,_,5),be(.04,.03,.45,R.oak,f,3.05,_,6);{Mt(2.2,.5,1.7,R.oak,3,.3,-21.4,0,1),Mt(2.15,.22,1.65,R.red,3,.62,-21.4,0,1),Mt(.5,.14,1.5,R.linen,3+.8,.78,-21.4,0,1);for(let[C,L]of[[-1.1,-.85],[1.1,-.85],[-1.1,.85],[1.1,.85]])be(.05,.05,2.4,R.oak,3+C,1.2,-21.4+L,6);Mt(2.3,.06,1.8,R.oak,3,2.4,-21.4,0,1);for(let[C,L,z,D]of[[2.3,.02,0,-.88],[.02,1.8,1.12,0]])Mt(C,1.6,L,R.green,3+z,1.6,-21.4+D,0,1);for(let C of[-1,1]){let L=new hn(.6,1.9,4,1),z=L.attributes.position;for(let D=0;D<z.count;D++)z.setZ(D,Math.sin(z.getX(D)*18)*.04);L.computeVertexNormals(),dt(L,R.green,yt(3-1.12+.3,1.42,-21.4+C*.87))}we(3,-21.4,2.3,1.8),Mt(1.1,.6,.6,R.oak,-1.8,.3,In.iz0+.4,0,.8),Mt(1.12,.06,.62,R.iron,-1.8,.58,In.iz0+.4,0,.8),we(-1.8,In.iz0+.4,1.1,.6),Mt(.9,.5,.5,R.oak,-6,.25,In.iz1-.35,0,.8),we(-6,In.iz1-.35,.9,.5),Mt(.55,.45,.5,R.oak,0,.45,-19.5,0,.8),Mt(.08,1.1,.5,R.oak,-.24,.9,-19.5,0,.8),Mt(.5,.1,.5,R.red,.02,.73,-19.5);let M=new hn(3,1.8);dt(M,R.hangG,yt(-1.2,1.9,In.iz0+.03));let E=new rn(.35,.2,.3,10,1,!0);dt(E,R.iron,yt(-2.4,.55,-19.4)),be(.03,.03,.45,R.iron,-2.4,.2,-19.4,4)}let oi=-26.8,ai=14;for(let f=0;f<12;f++){let _=f/12*Math.PI*2,M=new Gr(.17,0);dt(M,R.stone,yt(oi+Math.cos(_)*.7,.08,ai+Math.sin(_)*.7,o()*3))}Ze.push([oi,ai,.9]);{let f=new Li(.38,14,8,0,Math.PI*2,Math.PI*.35,Math.PI*.65);dt(f,R.iron,yt(oi,.95,ai)),be(.012,.012,1.6,R.iron,oi,2.1,ai,3);for(let _ of[0,2.1,4.2]){let M=new rn(.04,.05,3.2,5);M.rotateZ(.32),M.translate(.5,1.5,0),dt(M,R.oak,yt(oi,0,ai,_))}}Mt(2.4,.08,.9,R.oak,-23.4,.82,12.1,0,1.2);for(let f of[-1,1])Mt(.08,.78,.7,R.oak,-23.4+f*1,.39,12.1,0,1);we(-23.4,12.1,2.4,.9),dt(to.clone(),R.bread,yt(-23,.9,12.1)),dt(to.clone(),R.bread,yt(-23.4,.9,12.2,1)),dt(Sa.clone(),R.oak,yt(-24,.97,12));let hf=new Hr([[0,0],[.27,0],[.32,.2],[.34,.4],[.32,.6],[.27,.8],[0,.8]].map(([f,_])=>new xt(f,_)),14);for(let f=0;f<3;f++)dt(hf.clone(),R.oak,yt(-20.4+f*.1,0,15.9-f*.75-0,o())),Ze.push([-20.4+f*.1,15.9-f*.75,.35]);for(let f=0;f<4;f++){let _=new Li(.3,10,8);_.scale(1,1.25,.9),dt(_,R.straw,yt(-27.5+f*.55,.35,15.9,o()*3))}Mt(.9,.5,.7,R.stone,-20.6,.25,19.4,0,1);{let f=new Li(1.3,18,10,0,Math.PI*2,0,Math.PI/2),_=f.attributes.uv;for(let M=0;M<_.count;M++)_.setXY(M,_.getX(M)*4,_.getY(M)*1.2);dt(f,R.daub,yt(-17,0,19.5)),Ze.push([-17,19.5,1.4])}for(let f=an.ix0+2.2;f<an.ix1-1;f+=2.2)Mt(.1,1.3,2.4,R.oak,f,.65,an.iz1-1.2,0,1);Mt(an.ix1-an.ix0-.4,.5,.4,R.oak,(an.ix0+an.ix1)/2,1.5,an.iz1-.3,0,1.2),Mt(an.ix1-an.ix0-.4,.2,.3,R.straw,(an.ix0+an.ix1)/2,1.85,an.iz1-.3,0,1);for(let f=0;f<26;f++){let _=new rn(.16,.2,.9,7);dt(_,R.straw,yt(hr.ix0+.6+f%13*.5,.45+Math.floor(f/13)*0,hr.iz0+.4+Math.floor(f/13)*.45,0,.1*(o()-.5)))}{let f=new rn(.95,1,.8,16,1,!0),_=f.attributes.uv;for(let E=0;E<_.count;E++)_.setXY(E,_.getX(E)*3,_.getY(E)*.4);dt(f,R.stone,yt(8,.4,2.5)),dt(new rr(.95,16).rotateX(-Math.PI/2),R.iron,yt(8,.5,2.5),!0);for(let E of[-1,1])Mt(.14,1.7,.14,R.oak,8+E*1.05,.85,2.5,0,1);be(.08,.08,2.3,R.oak,8,1.55,2.5,8,0,0,Math.PI/2),Ze.push([8,2.5,1.2]);let M=new rn(.16,.13,.3,10);dt(M,R.oak,yt(8.6,.65,3.3))}for(let f=0;f<30;f++){let _=new rn(.09+o()*.05,.1+o()*.05,1.1,7);dt(_,R.oak,yt(-9+f%8*.24,.12+Math.floor(f/8)*.2,5+(o()-.5)*.1,0,Math.PI/2))}we(-8.2,5,2.2,1.2);{let f=new rn(.2,2.1,1.8,14),_=f.attributes.uv;for(let C=0;C<_.count;C++)_.setXY(C,_.getX(C)*5,_.getY(C));dt(f,R.straw,yt(33,3.2,-6));let M=new rn(2.1,2.2,2.3,14),E=M.attributes.uv;for(let C=0;C<E.count;C++)E.setXY(C,E.getX(C)*5,E.getY(C)*1.2);dt(M,R.straw,yt(33,1.15,-6)),Ze.push([33,-6,2.3])}{let f=yt(20,0,6,.5),_=new Ae(2.6,.1,1.4);_.translate(0,.78,0),dt(_,R.oak,f.clone());for(let C of[-1,1]){let L=new Ae(2.6,.4,.06);L.translate(0,1,C*.7),dt(L,R.oak,f.clone());let z=new ha(.55,.06,6,18);z.translate(-.3,.58,C*.82),dt(z,R.oak,f.clone())}let M=new Ae(2.2,.08,.08);M.translate(2.3,.55,.35),dt(M,R.oak,f.clone());let E=M.clone();E.translate(0,0,-.7),dt(E,R.oak,f.clone()),Ze.push([20,6,1.5])}Mt(1,.7,1,R.stone,37.5,.35,4.5,.1,1);function Tc(f,_=1.1){for(let M=0;M<f.length-1;M++){let[E,C]=[f[M],f[M+1]],L=Math.hypot(C[0]-E[0],C[1]-E[1]),z=new Ae(L,_,.08);z.translate(L/2,_/2,0);let D=z.attributes.uv;for(let G=0;G<D.count;G++)D.setXY(G,D.getX(G)*L*2,D.getY(G)*_);dt(z,R.wattle,yt(E[0],0,E[1],-Math.atan2(C[1]-E[1],C[0]-E[0]))),Ne.push([E[0],E[1],C[0],C[1],.06]);for(let G=0;G<=L;G+=.6)be(.035,.035,_+.15,R.oak,E[0]+(C[0]-E[0])*G/L,(_+.15)/2,E[1]+(C[1]-E[1])*G/L,5)}}Tc([[30.2,18],[30.2,22.5],[36,22.5],[36,18.2]]),Tc([[-36,18],[-36,26],[-30,26]],.95);let Ac=[[-120,-60,.3],[-150,-20,1.1],[-128,82,-.4],[-160,60,.7],[110,-95,.2],[-60,-120,1.4]];for(let[f,_,M]of Ac){let E=j(f,_),C=yt(f,E,_,M),L=new Ae(7,2,4.2);L.translate(0,1,0);let z=L.attributes.uv;for(let $=0;$<z.count;$++)z.setXY($,z.getX($)*3,z.getY($));dt(L,R.daub,C.clone(),!0);let D=new kr(4.4,3,4,1);D.rotateY(Math.PI/4),D.scale(1.25,1,.78),D.translate(0,3.4,0);let G=D.attributes.uv;for(let $=0;$<G.count;$++)G.setXY($,G.getX($)*6,G.getY($)*3);dt(D,R.thatch,C.clone(),!0),Ne.push([f-4,_,f+4,_,2.4])}{let f=new Set;for(let _ of jr)for(let M=0;M<4;M++){let E=_[M],C=_[(M+1)%4],L=[E,C].map(it=>it.map(wt=>wt.toFixed(1)).join(",")).sort().join("|");if(f.has(L))continue;f.add(L);let z=(E[0]+C[0])/2,D=(E[1]+C[1])/2;if(Math.hypot(z,D)>480||Math.hypot(z,D)<100)continue;let G=(Math.atan2(z,-D)*180/Math.PI+360)%360;if(o()<.45||G>95&&G<135||G>200&&G<250)continue;let $=Math.hypot(C[0]-E[0],C[1]-E[1]),K=-Math.atan2(C[1]-E[1],C[0]-E[0]),Z=Math.ceil($/8);for(let it=0;it<Z;it++){let wt=it/Z,Ot=(it+1)/Z,ue=E[0]+(C[0]-E[0])*wt,Nt=E[1]+(C[1]-E[1])*wt,te=E[0]+(C[0]-E[0])*Ot,me=E[1]+(C[1]-E[1])*Ot,se=(j(ue,Nt)+j(te,me))/2,ot=$/Z+.05,Rt=new Ae(ot,1,1.3),kt=Rt.attributes.uv;for(let qt=0;qt<kt.count;qt++)kt.setXY(qt,kt.getX(qt)*ot/2.2,kt.getY(qt)*.45);dt(Rt,R.stone,yt((ue+te)/2,se+.32,(Nt+me)/2,K),!0);let ee=new Ae(ot,.3,1.2);dt(ee,R.turf,yt((ue+te)/2,se+.92,(Nt+me)/2,K),!0)}Ne.push([E[0],E[1],C[0],C[1],.65])}}for(let[f,_]of J){let M=Ms(_,!1);if(!M)continue;let E=new Ce(M,f);E.castShadow=E.receiveShadow=!0,E.matrixAutoUpdate=!1,et.add(E)}J.clear();{let f=[],_=s?96:160,M=0,E=.9;for(;M<900;)f.push(M),M+=E,E*=M<60?1:1.045;f.push(900);let C=[],L=[],z=[];for(let Z=0;Z<f.length;Z++)for(let it=0;it<(Z?_:1);it++){let wt=it/_*Math.PI*2,Ot=Math.cos(wt)*f[Z],ue=Math.sin(wt)*f[Z];C.push(Ot,j(Ot,ue),ue),L.push(Ot/3,ue/3)}let D=(Z,it)=>Z===0?0:1+(Z-1)*_+it%_;for(let Z=0;Z<f.length-1;Z++)for(let it=0;it<_;it++)Z===0?z.push(0,D(1,it+1),D(1,it)):z.push(D(Z,it),D(Z,it+1),D(Z+1,it),D(Z,it+1),D(Z+1,it+1),D(Z+1,it));let G=new qe;G.setAttribute("position",new _e(C,3)),G.setAttribute("uv",new _e(L,2)),G.setIndex(z),G.computeVertexNormals();let $=new ei({map:$t,roughness:1});$.onBeforeCompile=Z=>{Z.uniforms.splat={value:Jt},Z.uniforms.earth={value:Ee},Z.uniforms.landC={value:U},Z.uniforms.fields={value:A},Z.vertexShader=Z.vertexShader.replace("#include <common>",`#include <common>
varying vec3 vW;`).replace("#include <worldpos_vertex>",`#include <worldpos_vertex>
vW = (modelMatrix * vec4(transformed, 1.)).xyz;`),Z.fragmentShader=Z.fragmentShader.replace("#include <common>",`#include <common>
varying vec3 vW; uniform sampler2D splat, earth, landC, fields;`).replace("#include <map_fragment>",`
          vec2 suv = vW.xz / ${St.toFixed(1)} + .5;
          float wornA = texture2D(splat, suv).r * step(0., suv.x) * step(suv.x, 1.) * step(0., suv.y) * step(suv.y, 1.);
          vec3 g1 = texture2D(map, vMapUv).rgb, g2 = texture2D(map, vMapUv * .21 + .37).rgb, e = texture2D(earth, vMapUv * .8).rgb;
          vec3 gr = mix(g1, g2, .45) * (0.86 + .28 * texture2D(map, vMapUv * .031).g);
          gr = mix(vec3(dot(gr, vec3(.3, .55, .15))), gr, .8);
          float d = length(vW.xz);
          vec3 far = texture2D(landC, vec2(vW.x, -vW.z) / ${(2*Di).toFixed(1)} + .5).rgb * 1.08;
          vec3 fc = texture2D(fields, vW.xz / ${pi.toFixed(1)} + .5).rgb;
          float lum = dot(mix(g1, g2, .45), vec3(.3, .55, .15)) / .36;
          vec3 fld = fc * mix(1., lum, .55) * 1.1;
          vec3 c = mix(gr, fld, smoothstep(70., 130., d));
          c = mix(c, e, smoothstep(.15, .7, wornA));
          c = mix(c, far, smoothstep(620., 880., d));
          diffuseColor.rgb *= c;`)};let K=new Ce(G,$);K.receiveShadow=!0,et.add(K)}{let f=s?192:384,_=new hn(2*Di,2*Di,f-1,f-1);_.rotateX(-Math.PI/2);let M=_.attributes.position;for(let L=0;L<M.count;L++){let z=M.getX(L),D=M.getZ(L),G=Math.hypot(z,D),$=k(z,D)-ya-q(G);$-=4*(1-Ss(820,1100,G)),M.setY(L,Math.max($,-ya-q(G)-25))}_.computeVertexNormals();let E=new ei({map:U,normalMap:H,normalMapType:dc,roughness:1}),C=new Ce(_,E);et.add(C)}let li=new O().setFromSphericalCoords(1,Ui.degToRad(90-Ki[1]),Math.PI-Ui.degToRad(Ki[0]));li.set(Math.sin(Ui.degToRad(Ki[0]))*Math.cos(Ui.degToRad(Ki[1])),Math.sin(Ui.degToRad(Ki[1])),-Math.cos(Ui.degToRad(Ki[0]))*Math.cos(Ui.degToRad(Ki[1])));let Rc={time:{value:0},sunDir:{value:li},deep:{value:new ge(1520711)},skyC:{value:new ge(7310246)},fogC:{value:ut},fogD:{value:et.fog.density}};{let f=new hn(2*Di*2.5,2*Di*2.5,200,200);f.rotateX(-Math.PI/2);{let E=f.attributes.position;for(let C=0;C<E.count;C++)E.setY(C,-q(Math.hypot(E.getX(C),E.getZ(C))))}let _=new _n({uniforms:Rc,transparent:!0,depthWrite:!0,vertexShader:`#include <common>
#include <logdepthbuf_pars_vertex>
varying vec3 vW;void main(){vec4 w=modelMatrix*vec4(position,1.);vW=w.xyz;gl_Position=projectionMatrix*viewMatrix*w;
#include <logdepthbuf_vertex>
}`,fragmentShader:`#include <logdepthbuf_pars_fragment>
uniform float time,fogD;uniform vec3 sunDir,deep,skyC,fogC;varying vec3 vW;
        float h(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
        float n(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(h(i),h(i+vec2(1,0)),f.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),f.x),f.y);}
        vec2 g(vec2 p){float e=.1;return vec2(n(p+vec2(e,0))-n(p-vec2(e,0)),n(p+vec2(0,e))-n(p-vec2(0,e)))/(2.*e);}
        void main(){
#include <logdepthbuf_fragment>
vec3 V=cameraPosition-vW;float d=length(V);V/=d;
          vec2 p=vW.xz*.035;vec2 s=g(p+vec2(time*.06,time*.04))*.5+g(p*2.7-vec2(time*.09,0.))*.3+g(p*7.3+vec2(0.,time*.15))*.2;
          float k=clamp(1.-d/9000.,0.,1.);vec3 N=normalize(vec3(-s.x*.35*k,1.,-s.y*.35*k));
          float fr=.03+.6*pow(1.-max(dot(N,V),0.),5.);
          vec3 R=reflect(-V,N);float sp=pow(max(dot(R,sunDir),0.),220.)*5.+pow(max(dot(R,sunDir),0.),18.)*.25;
          vec3 c=mix(deep,skyC,fr)+vec3(1.,.86,.62)*sp;
          float f=1.-exp(-pow(fogD*d,2.));c=mix(c,fogC,f);
          gl_FragColor=vec4(c,1.);
          #include <tonemapping_fragment>
          #include <colorspace_fragment>
        }`}),M=new Ce(f,_);M.position.y=-ya+.3,M.renderOrder=-1,et.add(M)}let ur=new lr;ur.scale.setScalar(7e4);let fr=ur.material.uniforms;fr.turbidity.value=2.6,fr.rayleigh.value=1.7,fr.mieCoefficient.value=.0028,fr.mieDirectionalG.value=.8,fr.sunPosition.value.copy(li),ur.renderOrder=-2,ur.material.depthTest=!1,et.add(ur);{let f=new ir(h),_=new Or,M=new lr;M.scale.setScalar(60),M.material.uniforms.sunPosition.value.copy(li),M.material.uniforms.turbidity.value=2.6,M.material.uniforms.rayleigh.value=1.7,M.material.uniforms.mieCoefficient.value=.0028,_.add(M);let E=new Ce(new rr(50,24).rotateX(-Math.PI/2),new gs({color:3951148}));E.position.y=-1,_.add(E),et.environment=f.fromScene(_,.04).texture,f.dispose()}let Cc={time:{value:0},sunDir:{value:li}};{let f=new hn(12e4,12e4);f.rotateX(Math.PI/2);let _=new _n({uniforms:Cc,transparent:!0,depthWrite:!1,side:mn,fog:!1,vertexShader:`#include <common>
#include <logdepthbuf_pars_vertex>
varying vec3 vW;void main(){vec4 w=modelMatrix*vec4(position,1.);vW=w.xyz;gl_Position=projectionMatrix*viewMatrix*w;
#include <logdepthbuf_vertex>
}`,fragmentShader:`#include <logdepthbuf_pars_fragment>
uniform float time;uniform vec3 sunDir;varying vec3 vW;
        float h(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
        float n(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(h(i),h(i+vec2(1,0)),f.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),f.x),f.y);}
        float fbm(vec2 p){float v=0.,a=.5;for(int i=0;i<5;i++){v+=a*n(p);p=p*2.03+17.;a*=.5;}return v;}
        void main(){
#include <logdepthbuf_fragment>
vec2 p=vW.xz/2600.+vec2(time*.004,time*.002);
          float c=fbm(p),c2=fbm(p+sunDir.xz*.06);
          float cov=smoothstep(.54,.78,c);
          float lit=clamp(.55+(c-c2)*5.,0.,1.2);
          vec3 col=mix(vec3(.55,.58,.64),vec3(1.,.95,.86),lit);
          float d=length(vW.xz-cameraPosition.xz);
          float fade=1.-smoothstep(16000.,52000.,d);
          gl_FragColor=vec4(col*1.6,cov*.92*fade);
          #include <tonemapping_fragment>
          #include <colorspace_fragment>
        }`}),M=new Ce(f,_);M.position.y=1500,M.renderOrder=1,et.add(M)}let Pc=f=>{f.fragmentShader=f.fragmentShader.replace("#include <normal_fragment_begin>",de.normal_fragment_begin.replace("normal *= faceDirection;",""))},Ic={time:{value:0}};{let[f,_]=at(128),[M,E]=at(128);_.fillStyle="#76844f",_.fillRect(0,0,128,128),E.fillStyle="#000",E.fillRect(0,0,128,128);for(let Nt=0;Nt<70;Nt++){let te=6+o()*116,me=(o()-.5)*34,se=50+o()*74,ot=130+o()*90;_.strokeStyle=`rgb(${ot*.68|0},${ot*.82|0},${ot*.46|0})`,_.lineWidth=E.lineWidth=1.2+o()*2,E.strokeStyle="#fff";for(let Rt of[_,E])Rt.beginPath(),Rt.moveTo(te,128),Rt.quadraticCurveTo(te+me*.3,128-se*.6,te+me,128-se),Rt.stroke()}for(let Nt=0;Nt<6;Nt++){_.fillStyle=`rgb(${170+o()*50},${150+o()*40},90)`;let te=10+o()*108,me=10+o()*40;E.fillStyle="#fff";for(let se of[_,E])se.beginPath(),se.ellipse(te,me,2.5,7,o()-.5,0,7),se.fill()}let C=lt(f),L=lt(M,null,!1);C.wrapS=C.wrapT=L.wrapS=L.wrapT=Rn;let z=new hn(.6,.42);z.translate(0,.2,0);let D=z.clone().rotateY(Math.PI/2),G=z.clone().rotateY(Math.PI/4),$=Ms([z,D,G]);$.setAttribute("normal",new _e(new Float32Array($.attributes.position.count*3).map((Nt,te)=>te%3===1?1:0),3));let K=new ei({map:C,alphaMap:L,alphaTest:.5,side:mn,roughness:1});K.onBeforeCompile=Nt=>{Nt.uniforms.time=Ic.time,Pc(Nt),Nt.vertexShader=Nt.vertexShader.replace("#include <common>",`#include <common>
uniform float time;`).replace("#include <begin_vertex>",`#include <begin_vertex>
        vec4 ip = instanceMatrix * vec4(0.,0.,0.,1.);
        float sw = sin(time * 1.7 + ip.x * .23 + ip.z * .17) * .5 + sin(time * 3.1 + ip.x * .7) * .25;
        transformed.x += sw * .12 * position.y; transformed.z += sw * .06 * position.y;`)};let Z=new ea($,K,x.grass),it=new De,wt=new ge,Ot=0,ue=0;for(;Ot<x.grass&&ue++<x.grass*6;){let Nt=5+Math.pow(o(),1.6)*70,te=o()*Math.PI*2,me=Math.cos(te)*Nt,se=Math.sin(te)*Nt;if(ie(me,se)>.25||Gt(me,se,1.2)||Ne.some(([Rt,kt,ee,qt,le])=>{let Be=ee-Rt,Ge=qt-kt,je=Be*Be+Ge*Ge||1,en=Wn(((me-Rt)*Be+(se-kt)*Ge)/je,0,1);return Math.hypot(me-Rt-Be*en,se-kt-Ge*en)<le+.5}))continue;let ot=.6+o()*.9;it.compose(new O(me,j(me,se)-.02,se),new ti().setFromEuler(new ms(0,o()*6.3,0)),new O(ot,ot*(.7+o()*.6),ot)),Z.setMatrixAt(Ot,it),Z.setColorAt(Ot,wt.setHSL(.19+o()*.05,.25+o()*.15,.42+o()*.16)),Ot++}Z.count=Ot,Z.receiveShadow=!0,et.add(Z)}{let[f,_]=at(128),[M,E]=at(128);_.fillStyle="#4d6a2c",_.fillRect(0,0,128,128),E.fillStyle="#000",E.fillRect(0,0,128,128);for(let Nt=0;Nt<1500;Nt++){let te=80+o()*100,me=o()*6.28,se=Math.sqrt(o())*60,ot=64+Math.cos(me)*se,Rt=64+Math.sin(me)*se,kt=3+o()*3,ee=1.5+o()*2,qt=o()*3;_.fillStyle=`rgb(${te*.58|0},${te*.9|0},${te*.34|0})`,E.fillStyle="#fff";for(let le of[_,E])le.beginPath(),le.ellipse(ot,Rt,kt,ee,qt,0,7),le.fill()}let C=lt(f),L=lt(M,null,!1),z=new ei({map:C,alphaMap:L,alphaTest:.5,side:mn,roughness:.9});z.onBeforeCompile=Pc;let D=new la(1,2),G=[],$=[],K=[[62,-60],[70,-20],[-75,-55],[-85,20],[-104,72],[40,75],[95,40],[-110,-15],[20,-85],[-30,90],[120,-40],[-140,-70],[150,62],[-60,-95],[85,85],[-96,44],[58,98],[130,70],[-120,100],[10,120]],Z=[Math.cos(Ui.degToRad(Ki[0]))*0+.5,.35];for(let[Nt,te]of K){let me=j(Nt,te),se=2.2+o()*2.2,ot=Nt+Z[0]*se*.45,Rt=te-Z[1]*se*.45,kt=me+se*1,ee=new rn(.12*se/2.4,.3*se/2.4,se*1.05,6);ee.translate(0,se*.52,0),ee.rotateZ(-.28),ee.rotateY(.6),ee.translate(Nt,me,te),$.push(ee);for(let qt=0;qt<12;qt++){let le=D.clone(),Be=se*(.38+o()*.3),Ge=(o()-.35)*se*1,je=(o()-.35)*se*.75,en=(o()-.5)*se*1;le.scale(Be*1.1,Be*.95,Be*1.1),le.translate(ot+Ge,kt+je,Rt+en);let fe=le.attributes.position,ze=new Float32Array(fe.count*3);for(let He=0;He<fe.count;He++){let Pn=new O(fe.getX(He)-ot,(fe.getY(He)-kt)*1.4,fe.getZ(He)-Rt).normalize();ze.set([Pn.x,Pn.y,Pn.z],He*3)}le.setAttribute("normal",new gn(ze,3)),G.push(le)}}let it=Ms(G.map(Nt=>Nt.index?Nt.toNonIndexed():Nt)),wt=it.attributes.uv;for(let Nt=0;Nt<wt.count;Nt++)wt.setXY(Nt,wt.getX(Nt)*3,wt.getY(Nt)*3);let Ot=new Ce(it,z);Ot.castShadow=Ot.receiveShadow=!0,et.add(Ot);let ue=new Ce(Ms($),new ei({map:mt,color:9076848,roughness:.9}));ue.castShadow=!0,et.add(ue);for(let[Nt,te]of K)Ze.push([Nt,te,.5])}let Bn=new pa(16769723,3.3);Bn.position.copy(li).multiplyScalar(120),et.add(Bn,Bn.target),Bn.castShadow=!0,Bn.shadow.mapSize.set(x.shadow,x.shadow),Object.assign(Bn.shadow.camera,{left:-38,right:38,top:38,bottom:-38,near:1,far:300}),Bn.shadow.bias=-5e-4,Bn.shadow.normalBias=.04,Bn.shadow.radius=3;let Lc=new fa(12374783,4998195,.15);et.add(Lc);let Yn=new Ji(16747068,60,0,2);Yn.position.set(On,1,ce),et.add(Yn),x.fireShadow&&(Yn.castShadow=!0,Yn.shadow.mapSize.set(512,512),Yn.shadow.bias=-.004,Yn.shadow.camera.near=.3,Yn.shadow.camera.far=22,Yn.shadow.radius=4);let Uc=new Ji(16754784,9,0,2);Uc.position.set(Xn+2.4,2.4,ce),et.add(Uc);let Ea=new Ji(16751178,6,0,2);Ea.position.set(Cn[2],3.4,ce),et.add(Ea);let wa=new Ji(16747068,22,0,2);wa.position.set(oi,.9,ai),et.add(wa);let Ta=new Ji(16749638,9,0,2);Ta.position.set(-2.4,1.1,-19.4),et.add(Ta);let Dc={time:{value:0}},uf=new _n({uniforms:Dc,transparent:!0,depthWrite:!1,blending:js,vertexShader:`#include <common>
#include <logdepthbuf_pars_vertex>
attribute vec4 off;varying vec2 vU;varying float vS;void main(){vU=uv;vS=off.w;vec3 c=off.xyz;vec4 mv=modelViewMatrix*vec4(c,1.);mv.xy+=position.xy*off.w;gl_Position=projectionMatrix*mv;
#include <logdepthbuf_vertex>
}`,fragmentShader:`#include <logdepthbuf_pars_fragment>
uniform float time;varying vec2 vU;varying float vS;
      float h(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
      float n(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(h(i),h(i+vec2(1,0)),f.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),f.x),f.y);}
      void main(){
#include <logdepthbuf_fragment>
vec2 p=vU;float t=time*2.2+vS*31.;
        float q=n(vec2(p.x*4.+vS*9.,p.y*3.-t*1.6))*.6+n(vec2(p.x*9.,p.y*7.-t*2.6))*.4;
        float w=1.-abs(p.x-.5)*2.;float shape=w*(1.-p.y)*1.6-q*.75-p.y*.35;
        float a=smoothstep(.05,.45,shape);
        vec3 c=mix(vec3(1.,.28,.04),vec3(1.,.82,.45),smoothstep(.25,.9,shape));
        gl_FragColor=vec4(c*a*1.8,a);
        #include <tonemapping_fragment>
        #include <colorspace_fragment>
      }`});function ff(f,_){let M=new Jr,E=new hn(1,1);E.translate(0,.5,0),M.setIndex(E.index),M.setAttribute("position",E.attributes.position),M.setAttribute("uv",E.attributes.uv),M.setAttribute("off",new Pi(new Float32Array(f.flat()),4)),M.instanceCount=f.length;let C=new Ce(M,_);return C.frustumCulled=!1,C.renderOrder=3,et.add(C),C}let dr=[];for(let f=0;f<6;f++)dr.push([On+(o()-.5)*.7,.02,ce+(o()-.5)*.5,.7+o()*.4]);for(let f=0;f<3;f++)dr.push([oi+(o()-.5)*.4,.02,ai+(o()-.5)*.4,.45+o()*.2]);for(let[f,_]of wc)dr.push([f,3.25,_,.3]);dr.push([-2.4,.66,-19.4,.32]),ff(dr,uf);let Nc=new gs({color:16734746});{let f=new Ce(new rr(.8,20).rotateX(-Math.PI/2),Nc);f.scale.set(1.2,1,1),f.position.set(On,.04,ce),et.add(f);let _=f.clone();_.scale.set(.55,1,.55),_.position.set(oi,.04,ai),et.add(_);let M=[];for(let C=0;C<6;C++)M.push(new rn(.07,.09,1.2,6).rotateZ(Math.PI/2-.18).rotateY(C*1.05).translate(On,.14,ce));let E=new Ce(Ms(M),new ei({color:2759184,emissive:4198916,roughness:1}));et.add(E)}let Aa={time:{value:0},light:{value:1}},df=new _n({uniforms:Aa,transparent:!0,depthWrite:!1,vertexShader:`#include <common>
#include <logdepthbuf_pars_vertex>
uniform float time;attribute vec4 off;attribute vec3 rise;varying vec2 vU;varying float vA;
      void main(){vU=uv;float life=fract(time/rise.z+off.w);vec3 c=off.xyz;
        float ht=life*rise.x;c.y+=ht;c.x+=sin(life*6.+off.w*30.)*.5*life+life*rise.y;c.z+=cos(life*5.+off.w*20.)*.4*life;
        float sz=.6+life*2.4;vA=sin(life*3.14159)*.55;
        vec4 mv=modelViewMatrix*vec4(c,1.);mv.xy+=(position.xy)*sz;gl_Position=projectionMatrix*mv;
#include <logdepthbuf_vertex>
}`,fragmentShader:`#include <logdepthbuf_pars_fragment>
uniform float light;varying vec2 vU;varying float vA;
      void main(){
#include <logdepthbuf_fragment>
vec2 p=vU-.5;float d=length(p);float a=smoothstep(.5,.0,d)*vA;
        a*=.75+.25*sin(p.x*13.+p.y*9.);gl_FragColor=vec4(vec3(.72,.7,.68)*light,a*.42);
        #include <tonemapping_fragment>
        #include <colorspace_fragment>
      }`});{let f=new hn(1,1),_=new Jr;_.setIndex(f.index),_.setAttribute("position",f.attributes.position),_.setAttribute("uv",f.attributes.uv);let M=[],E=[];for(let L=0;L<26;L++)M.push(On,1.2,ce,L/26),E.push(7.6,.4,9);for(let L=0;L<18;L++)M.push(On+.5,Te.ridge+1.4,ce,L/18),E.push(14,6,14);for(let L=0;L<14;L++)M.push(oi+1.5,on.ridge+1.3,ai,L/14),E.push(12,5,12);for(let[L,z]of Ac.slice(0,4))for(let D=0;D<6;D++)M.push(L,j(L,z)+4.6,z,D/6),E.push(10,4,10);_.setAttribute("off",new Pi(new Float32Array(M),4)),_.setAttribute("rise",new Pi(new Float32Array(E),3)),_.instanceCount=M.length/4;let C=new Ce(_,df);C.frustumCulled=!1,C.renderOrder=4,et.add(C)}let Ra={time:{value:0},k:{value:1}};{let f=new _n({uniforms:Ra,transparent:!0,depthWrite:!1,blending:js,side:mn,vertexShader:`#include <common>
#include <logdepthbuf_pars_vertex>
varying float vL;varying vec2 vU;varying vec3 vN,vV;void main(){vU=uv;vL=position.z;vN=normalMatrix*normal;vec4 mv=modelViewMatrix*vec4(position,1.);vV=mv.xyz;gl_Position=projectionMatrix*mv;
#include <logdepthbuf_vertex>
}`,fragmentShader:`#include <logdepthbuf_pars_fragment>
uniform float time,k;varying float vL;varying vec2 vU;varying vec3 vN,vV;void main(){
#include <logdepthbuf_fragment>
float a=(1.-smoothstep(0.,1.,vL))*smoothstep(0.,.08,vL);float e=smoothstep(0.,.25,vU.x)*smoothstep(1.,.75,vU.x);a*=smoothstep(.12,.85,abs(dot(normalize(vN),normalize(-vV))))*smoothstep(.6,3.,length(vV));gl_FragColor=vec4(vec3(1.,.86,.62)*a*e*.05*k,1.);
        #include <tonemapping_fragment>
        #include <colorspace_fragment>
      }`}),_=[],M=li.clone().negate(),E=(C,L,z,D,G,$,K)=>{if(li.x*$+li.z*K<=.05)return;let Z=Math.min(9,(L+G*.5)/Math.max(.15,-M.y))*1.15,it=new Ae(D,G,1,1,1,1);it.translate(0,0,.5);let wt=it.attributes.position;for(let Nt=0;Nt<wt.count;Nt++){let te=wt.getZ(Nt);wt.setXYZ(Nt,wt.getX(Nt),wt.getY(Nt),te)}let Ot=new Ce(it,f),ue=new De().lookAt(new O(0,0,0),M.clone().multiplyScalar(-1),new O(0,1,0));Ot.quaternion.setFromRotationMatrix(ue),Ot.scale.set(1,1,Z),Ot.position.set(C,L,z),Ot.renderOrder=2,et.add(Ot),_.push(Ot)};for(let C of Oe)C.x<6&&C.z<-4&&C.y<6&&E(C.x-C.nx*.3,C.y,C.z-C.nz*.3,C.w*.9,C.h*.85,C.nx,C.nz);E(Te.x0+.45,4.9,ce,.7,1.2,-1,0),E(-4.4,1.9,In.z1-.45,.6,.9,0,1),E(-1.6,1.9,In.z1-.45,.6,.9,0,1),E(-4.4,1.9,In.z1-.45,.01,.01,0,1)}let Fc=[];for(let f=0;f<160;f++)Fc.push(On-7+o()*14,.3+o()*4.5,ce-4+o()*8);let Ca=new na(new qe().setAttribute("position",new _e(Fc,3)),new Br({color:16767392,size:.022,transparent:!0,opacity:.55,depthWrite:!1,blending:js}));et.add(Ca);let zn=t.stops.filter(f=>cr[f.id]),Pa=[],pf=new ei({color:15909198,emissive:13144090,emissiveIntensity:1.4,roughness:.3,metalness:.4});zn.forEach((f,_)=>{let[[M,E],[C,L,z]]=cr[f.id],D=C-M,G=z-E,$=Math.hypot(D,G),K=new Ce(new ca(.16),pf),Z=M+D/$*1.8,it=E+G/$*1.8;K.position.set(Z,j(Z,it)+2.05,it),K.userData.i=_,K.userData.y=K.position.y,et.add(K),Pa.push(K)});let bt={x:70,z:6,yaw:Math.PI/2,pitch:0,vx:0,vz:0},dn={yaw:bt.yaw,pitch:0},mf=(f,_)=>f>Te.ix0-.1&&f<Te.ix0+Qr&&_>Te.iz0&&_<Te.iz1,Ia=(f,_)=>1.62+(mf(f,_)?.32:0)+j(f,_);function gf(f,_){for(let C=0;C<2;C++){for(let[L,z,D,G,$]of Ne){let K=D-L,Z=G-z,it=K*K+Z*Z||1e-6,wt=Wn(((f-L)*K+(_-z)*Z)/it,0,1),Ot=L+K*wt,ue=z+Z*wt,Nt=f-Ot,te=_-ue,me=Math.hypot(Nt,te),se=.32+$;me<se&&me>1e-6&&(f=Ot+Nt/me*se,_=ue+te/me*se)}for(let[L,z,D]of Ze){let G=f-L,$=_-z,K=Math.hypot(G,$),Z=.32+D;K<Z&&K>1e-6&&(f=L+G/K*Z,_=z+$/K*Z)}}let E=Math.hypot(f,_);return E>260&&(f*=260/E,_*=260/E),[f,_]}let _f=(f,_,M,E)=>Ne.some(([C,L,z,D,G])=>{let $=(M-f)*(D-L)-(E-_)*(z-C);if(Math.abs($)<1e-9)return!1;let K=((C-f)*(D-L)-(L-_)*(z-C))/$,Z=((C-f)*(E-_)-(L-_)*(M-f))/$;return K>0&&K<1&&Z>=0&&Z<=1&&G>.1}),Ie=null,pn=null,ci=!0;function pr(){if(Ie){ci&&Ie.state==="suspended"&&Ie.resume();return}if(!ci)return;try{Ie=new(window.AudioContext||window.webkitAudioContext)}catch{return}let f=Ie.sampleRate,_=Ie.createBuffer(1,f*4,f),M=_.getChannelData(0),E=0,C=0,L=0;for(let Z=0;Z<M.length;Z++){let it=Math.random()*2-1;E=.99765*E+it*.099,C=.963*C+it*.2965,L=.57*L+it*1.0527,M[Z]=(E+C+L+it*.1848)*.2}let z=Ie.createGain();z.gain.value=.9,z.connect(Ie.destination);let D=(Z,it,wt="bandpass")=>{let Ot=Ie.createBufferSource();Ot.buffer=_,Ot.loop=!0,Ot.playbackRate.value=.5+Math.random()*.1;let ue=Ie.createBiquadFilter();ue.type=wt,ue.frequency.value=Z,ue.Q.value=it;let Nt=Ie.createGain();return Nt.gain.value=0,Ot.connect(ue),ue.connect(Nt),Nt.connect(z),Ot.start(),{g:Nt,f:ue}},G=D(500,.6),$=D(260,.4,"lowpass"),K=D(180,.7,"lowpass");pn={wind:G,sea:$,rumble:K,master:z,crackT:0,harpT:2,note:0}}function xf(f){let _=.02+Math.random()*.05,M=Ie.createBuffer(1,Math.ceil(Ie.sampleRate*_),Ie.sampleRate),E=M.getChannelData(0);for(let D=0;D<E.length;D++)E[D]=(Math.random()*2-1)*Math.pow(1-D/E.length,3);let C=Ie.createBufferSource();C.buffer=M;let L=Ie.createBiquadFilter();L.type="highpass",L.frequency.value=900+Math.random()*2500;let z=Ie.createGain();z.gain.value=f*(.2+Math.random()*.5),C.connect(L),L.connect(z),z.connect(pn.master),C.start()}let Oc=[146.83,164.81,174.61,196,220,246.94,261.63,293.66,329.63,349.23,392],Bc=[7,5,4,5,7,7,8,7,5,4,2,4,5,4,2,0,2,4,5,7,5,4,2,4];function zc(f,_){let M=Ie.sampleRate,E=Math.round(M/f),C=Math.ceil(M*2.6),L=Ie.createBuffer(1,C,M),z=L.getChannelData(0),D=new Float32Array(E);for(let it=0;it<E;it++)D[it]=Math.random()*2-1;let G=0;for(let it=0;it<C;it++){let wt=(G+1)%E,Ot=(D[G]+D[wt])*.4985;z[it]=D[G],D[G]=Ot,G=wt}let $=Ie.createBufferSource();$.buffer=L;let K=Ie.createGain();K.gain.value=_;let Z=Ie.createBiquadFilter();Z.type="lowpass",Z.frequency.value=2600,$.connect(Z),Z.connect(K),K.connect(pn.master),$.start()}function vf(f){if(!Ie||!pn)return;let _=Ie.currentTime,M=is,E=Math.hypot(bt.x-On,bt.z-ce),C=Math.hypot(bt.x-oi,bt.z-ai),L=Math.max(so?Wn(1.4-E/9,0,1):0,Wn(1-C/7,0,1)*(Fa?1:.3));if(pn.wind.g.gain.setTargetAtTime((1-M*.8)*(.32+.18*Math.sin(_*.23)+.1*Math.sin(_*.71)),_,.4),pn.wind.f.frequency.setTargetAtTime(380+160*Math.sin(_*.17),_,.5),pn.sea.g.gain.setTargetAtTime((1-M*.7)*(.25+.15*Math.sin(_*.45)),_,.5),pn.rumble.g.gain.setTargetAtTime(L*.7,_,.3),pn.crackT-=f,pn.crackT<0&&L>.02&&(xf(L),pn.crackT=Math.random()*.22),so&&(pn.harpT-=f,pn.harpT<0)){let z=Bc[pn.note++%Bc.length],D=Wn(1.2-Math.hypot(bt.x+17.3,bt.z+13.6)/12,.15,1)*.5;zc(Oc[z],D),pn.note%4===1&&zc(Oc[Math.max(0,z-4)]/2,D*.55),pn.harpT=(pn.note%8===0?1.1:.52)*(1+(Math.random()-.5)*.08)}}let xi=document.createElement("div");xi.className="ll-ui";let qn=f=>String(f).replace(/[&<>"]/g,_=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"})[_]);xi.innerHTML='<div class="ll-panel" hidden><p class="ll-n"></p><h2 tabindex="-1"></h2><div class="ll-txt"></div><p class="ll-src"></p><div class="ll-btns"><button type="button" class="btn" data-k="prev">\u2190 '+qn(n(t.ui.prev))+'</button><button type="button" class="btn solid" data-k="next">'+qn(n(t.ui.next))+' \u2192</button><button type="button" class="ll-x" data-k="close" aria-label="'+qn(n(t.ui.close))+'">\xD7</button></div></div><div class="ll-bar"><button type="button" class="btn solid" data-k="tour">'+qn(n(t.ui.tour))+' \u2192</button><button type="button" class="btn" data-k="snd" aria-pressed="'+ci+'"></button><button type="button" class="btn" data-k="fs">'+qn(n(t.ui.fs))+'</button><span class="ll-help">'+qn(n(r?t.ui.helpTouch:t.ui.help))+'</span></div><canvas class="ll-plan" width="200" height="160" aria-hidden="true"></canvas><div class="ll-stick" aria-hidden="true"><i></i></div><div class="ll-fade"></div>',i.appendChild(xi);let hi=xi.querySelector(".ll-panel"),es=xi.querySelector(".ll-stick"),Hc=es.querySelector("i"),kc=xi.querySelector(".ll-fade"),Vc=xi.querySelector('[data-k="snd"]'),Gc=()=>{Vc.textContent=(ci?"\u266A ":"")+n(ci?t.ui.soundOff:t.ui.soundOn),Vc.setAttribute("aria-pressed",ci)};Gc();let Zn=-1,La=-1,Le=null;function Wc(f){Zn=f;let _=zn[f];hi.hidden=!1,hi.scrollTop=0,hi.querySelector(".ll-n").textContent=n(t.ui.stop).replace("{n}",f+1).replace("{of}",zn.length),hi.querySelector("h2").textContent=n(_.t),hi.querySelector(".ll-txt").innerHTML=n(_.p).map(E=>"<p>"+qn(E)+"</p>").join("");let M=hi.querySelector(".ll-src");M.innerHTML=_.src&&_.src.length?qn(n(t.ui.sources))+": "+_.src.map(E=>E.url?`<a href="${qn(E.url)}" target="_blank" rel="noopener">${qn(n(E.t))}</a>`:qn(n(E.t))).join(" \xB7 "):"",hi.querySelector('[data-k="prev"]').disabled=f===0,hi.querySelector('[data-k="next"]').textContent=(f===zn.length-1?n(t.ui.again):n(t.ui.next))+" \u2192"}let eo=!1;function ns(f,_){f=(f+zn.length)%zn.length;let[[M,E],[C,L,z]]=cr[zn[f].id],D=Math.atan2(-(C-M),-(z-E)),G=Math.atan2(L-Ia(M,E),Math.hypot(C-M,z-E)),$=D-bt.yaw;for(;$>Math.PI;)$-=2*Math.PI;for(;$<-Math.PI;)$+=2*Math.PI;let K=_||a||_f(bt.x,bt.z,M,E)||Math.hypot(M-bt.x,E-bt.z)>90;Le={t:0,dur:K?.9:Math.min(3.4,1+Math.hypot(M-bt.x,E-bt.z)/12),jump:K,from:{...bt},to:{x:M,z:E,yaw:bt.yaw+$,pitch:G}},_&&(Object.assign(bt,Le.to),dn.yaw=bt.yaw,dn.pitch=bt.pitch,Le=null,eo=!0),Wc(f),La=-1}xi.addEventListener("click",f=>{let _=f.target.closest("button");if(!_)return;let M=_.dataset.k;M==="tour"||M==="next"?ns(Zn+1):M==="prev"?ns(Zn-1):M==="close"?(hi.hidden=!0,La=Zn,c.focus({preventScroll:!0})):M==="snd"?(ci=!ci,Gc(),ci?Ie?Ie.resume():pr():Ie&&Ie.suspend()):M==="fs"&&(document.fullscreenElement?document.exitFullscreen():i.requestFullscreen&&i.requestFullscreen().catch(()=>{}))});let Ua=xi.querySelector(".ll-plan"),ye=Ua.getContext("2d"),Xc=1.85,Es=(f,_)=>[100+f*Xc,80+_*Xc*1];function yf(){ye.clearRect(0,0,200,160),ye.fillStyle="rgba(8,10,16,.62)",ye.fillRect(0,0,200,160),ye.strokeStyle="rgba(230,220,200,.75)",ye.lineWidth=2.2,ye.beginPath(),gi.forEach(([M,E],C)=>{let[L,z]=Es(M,E);C?ye.lineTo(L,z):ye.moveTo(L,z)}),ye.closePath(),ye.stroke(),ye.fillStyle="rgba(230,220,200,.45)";for(let M of Ft){if(M[2]-M[0]>40)continue;let[E,C]=Es(M[0],M[1]),[L,z]=Es(M[2],M[3]);ye.fillRect(E,C,L-E,z-C)}zn.forEach((M,E)=>{let[[C,L]]=cr[M.id];if(Math.abs(C)>50||Math.abs(L)>40)return;let[z,D]=Es(C,L);ye.fillStyle=E===Zn?"#fff":"#f2c14e",ye.beginPath(),ye.arc(z,D,3.2,0,7),ye.fill()});let[f,_]=Es(Wn(bt.x,-52,52),Wn(bt.z,-42,42));ye.save(),ye.translate(f,_),ye.rotate(-bt.yaw),ye.fillStyle="#e8483f",ye.beginPath(),ye.moveTo(0,-7),ye.lineTo(5,5),ye.lineTo(0,2),ye.lineTo(-5,5),ye.closePath(),ye.fill(),ye.restore(),ye.fillStyle="rgba(230,220,200,.85)",ye.font="600 10px system-ui, sans-serif",ye.fillText(e?"G":"N",188,14),ye.beginPath(),ye.moveTo(191,18),ye.lineTo(191,30),ye.strokeStyle="rgba(230,220,200,.85)",ye.lineWidth=1.2,ye.stroke()}Ua.addEventListener("click",f=>{let _=Ua.getBoundingClientRect(),M=(f.clientX-_.left)/_.width*200,E=(f.clientY-_.top)/_.height*160,C=-1,L=14;zn.forEach((z,D)=>{let[[G,$]]=cr[z.id],[K,Z]=Es(G,$),it=Math.hypot(K-M,Z-E);it<L&&(L=it,C=D)}),C>=0&&ns(C)});let En={};c.addEventListener("keydown",f=>{let _=f.key.toLowerCase();["w","a","s","d","arrowup","arrowdown","arrowleft","arrowright","q","e","shift"].includes(_)&&(En[_]=1,f.preventDefault(),Le=null),_==="n"&&ns(Zn+1),pr()}),c.addEventListener("keyup",f=>{En[f.key.toLowerCase()]=0}),c.addEventListener("blur",()=>{for(let f in En)En[f]=0});let $n=null,Yc=new ma,qc=new xt;c.addEventListener("pointerdown",f=>{$n={id:f.pointerId,x:f.clientX,y:f.clientY,moved:0},c.setPointerCapture(f.pointerId),c.focus({preventScroll:!0}),pr()}),c.addEventListener("pointermove",f=>{if(!$n||$n.id!==f.pointerId)return;let _=f.clientX-$n.x,M=f.clientY-$n.y;$n.x=f.clientX,$n.y=f.clientY,$n.moved+=Math.abs(_)+Math.abs(M);let E=f.pointerType==="touch"?.0062:.0045;Le&&(dn.yaw=bt.yaw,dn.pitch=bt.pitch,Le=null),dn.yaw+=_*E,dn.pitch=Wn(dn.pitch+M*E,-1.25,1.25)}),c.addEventListener("pointerup",f=>{if($n&&$n.moved<6){let _=c.getBoundingClientRect();qc.set((f.clientX-_.left)/_.width*2-1,-(f.clientY-_.top)/_.height*2+1),Yc.setFromCamera(qc,tt);let M=Yc.intersectObjects(Pa)[0];M&&ns(M.object.userData.i)}$n=null});let ws={x:0,y:0},no=null,Zc=f=>{let _=es.getBoundingClientRect(),M=_.left+_.width/2,E=_.top+_.height/2,C=(f.clientX-M)/(_.width/2),L=(f.clientY-E)/(_.height/2),z=Math.hypot(C,L);z>1&&(C/=z,L/=z),ws.x=C,ws.y=L,Hc.style.transform=`translate(${C*34}px,${L*34}px)`};es.addEventListener("pointerdown",f=>{no=f.pointerId,es.setPointerCapture(no),Zc(f),Le&&(dn.yaw=bt.yaw,dn.pitch=bt.pitch,Le=null),f.preventDefault(),pr()}),es.addEventListener("pointermove",f=>{f.pointerId===no&&Zc(f)});let $c=()=>{no=null,ws.x=ws.y=0,Hc.style.transform=""};es.addEventListener("pointerup",$c),es.addEventListener("pointercancel",$c);function io(){let f=i.clientWidth,_=i.clientHeight;h.setSize(f,_,!1),tt.aspect=f/_,tt.updateProjectionMatrix()}io(),new ResizeObserver(io).observe(i);let Da=!0;new IntersectionObserver(f=>{Da=f[0].isIntersecting,Da&&(Na=performance.now())}).observe(i);let Na=performance.now(),tn=0,is=0,so=!1,Fa=!1,ro=0,oo=0,Jc=0,Oa=new O,Ba=new O;function Kc(f){if(requestAnimationFrame(Kc),!Da||document.hidden)return;let _=Math.min(.5,(f-Na)/1e3),M=Math.min(.05,_);Na=f,tn+=M,_>.034?(ro+=_,oo=0):_<.019&&(oo+=_,ro=0),ro>1.2&&d>.6&&(d=Math.max(.6,d-.15),h.setPixelRatio(d),io(),ro=0),oo>4&&d<u&&(d=Math.min(u,d+.1),h.setPixelRatio(d),io(),oo=0);let E=0;if(Le){Le.t+=_/Le.dur;let K=Le.t>=1?1:(1-Math.cos(Math.PI*Le.t))/2;Le.jump?(kc.style.opacity=String(Math.sin(Math.min(1,Le.t)*Math.PI)),Le.t>=.5&&!Le.done&&(Object.assign(bt,Le.to),Le.done=!0,tt.position.y=Ia(bt.x,bt.z))):["x","z","yaw","pitch"].forEach(Z=>{bt[Z]=Le.from[Z]+(Le.to[Z]-Le.from[Z])*K}),Le.t>=1&&(Object.assign(bt,Le.to),Le=null,kc.style.opacity="0"),dn.yaw=bt.yaw,dn.pitch=bt.pitch,bt.vx=bt.vz=0}else{let K=1-Math.exp(-M*16);bt.yaw+=(dn.yaw-bt.yaw)*K,bt.pitch+=(dn.pitch-bt.pitch)*K,(En.arrowleft||En.q)&&(dn.yaw+=1.8*M),(En.arrowright||En.e)&&(dn.yaw-=1.8*M);let Z=En.shift?2.1:1,it=(En.w||En.arrowup?1:0)-(En.s||En.arrowdown?1:0)-ws.y,wt=(En.d?1:0)-(En.a?1:0)+ws.x,Ot=Math.max(1,Math.hypot(it,wt));it/=Ot,wt/=Ot;let ue=(-Math.sin(bt.yaw)*it+Math.cos(bt.yaw)*wt)*3.3*Z,Nt=(-Math.cos(bt.yaw)*it-Math.sin(bt.yaw)*wt)*3.3*Z,te=1-Math.exp(-M*9);bt.vx+=(ue-bt.vx)*te,bt.vz+=(Nt-bt.vz)*te;let me=Math.hypot(bt.vx,bt.vz);me>.02&&([bt.x,bt.z]=gf(bt.x+bt.vx*M,bt.z+bt.vz*M),E=Math.min(1,me/3.3)),zn.forEach((se,ot)=>{let[[Rt,kt]]=cr[se.id];ot!==Zn&&ot!==La&&Math.hypot(bt.x-Rt,bt.z-kt)<1.8&&Wc(ot)})}Jc+=M*9*E;let C=bt.hy!=null?bt.hy:Ia(bt.x,bt.z)+(a?0:Math.sin(Jc)*.025*E);tt.position.set(bt.x,tt.position.y?tt.position.y+(C-tt.position.y)*Math.min(1,M*10):C,bt.z),tt.rotation.set(bt.pitch,bt.yaw,0);let L=bt.fov||(s?68:60)-(Zn>=0&&(zn[Zn].id==="wall"||zn[Zn].id==="sands")&&!Le?s?38:42:0);eo&&(tt.fov=L,tt.updateProjectionMatrix(),eo=!1),Math.abs(tt.fov-L)>.05&&(tt.fov+=(L-tt.fov)*Math.min(1,M*2.5),tt.updateProjectionMatrix());let z=Gt(bt.x,bt.z,-.3);so=Fa=!1,z&&(so=bt.x>Te.x0&&bt.x<Te.x1&&bt.z>Te.z0&&bt.z<Te.z1,Fa=bt.x>on.x0&&bt.x<on.x1&&bt.z>on.z0&&bt.z<on.z1),is+=((z?1:0)-is)*Math.min(1,M*2.2),h.toneMappingExposure=.62+is*.38;let D=1-is*.82;for(let K of Q)K.envMapIntensity=D;Lc.intensity=.15*D,Aa.light.value=.35+(1-is)*.65,Ra.k.value=.25+is*.45,Oa.set(bt.x,0,bt.z);let G=76/x.shadow;Ba.set(Math.round(Oa.x/G)*G,0,Math.round(Oa.z/G)*G),Bn.target.position.copy(Ba),Bn.position.copy(Ba).addScaledVector(li,120),Bn.target.updateMatrixWorld();let $=1+Math.sin(tn*11)*.07+Math.sin(tn*23.7)*.05+(Math.random()-.5)*.09;Yn.intensity=60*$,wa.intensity=22*$,Ea.intensity=6*(1+Math.sin(tn*13)*.08),Ta.intensity=9*(1+Math.sin(tn*9.3)*.07),Yn.position.x=On+Math.sin(tn*7)*.05,Yn.position.z=ce+Math.cos(tn*9)*.05,Nc.color.setRGB(1,.3+Math.sin(tn*3)*.04,.08),Dc.time.value=tn,Aa.time.value=tn,Rc.time.value=tn,Cc.time.value=tn,Ic.time.value=tn,Ra.time.value=tn,Ca.rotation.y=Math.sin(tn*.05)*.02,Ca.position.y=Math.sin(tn*.3)*.05,Pa.forEach((K,Z)=>{K.rotation.y=tn*1.4+Z,K.position.y=K.userData.y+Math.sin(tn*2+Z)*.06,K.visible=Z!==Zn||!!Le}),vf(M),(tn*10|0)%2===0&&yf(),h.render(et,tt)}i.classList.add("ready"),tt.position.y=0,c.focus({preventScroll:!0}),ci&&pr();let jc={dem:k,ground:j,goStop:(f,_)=>ns(f,_),renderer:h,me:bt,view:(f,_,M,E,C,L,z)=>{hi.hidden=!0,bt.fov=z||0,eo=!0,Le=null,bt.x=f,bt.z=M,bt.hy=_,tt.position.y=_,bt.yaw=dn.yaw=Math.atan2(-(E-f),-(L-M)),bt.pitch=dn.pitch=Math.atan2(C-_,Math.hypot(E-f,L-M))}};return requestAnimationFrame(Kc),setTimeout(()=>ns(0),300),window.LLYS3D=jc,jc}export{Mx as start};
/*! Bundled license information:

three/build/three.module.js:
  (**
   * @license
   * Copyright 2010-2023 Three.js Authors
   * SPDX-License-Identifier: MIT
   *)
*/
