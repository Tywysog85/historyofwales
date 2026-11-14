var ed=0,Ch=1,nd=2;var hf=1,Pl=2,Ii=3,es=0,Tn=1,ln=2;var Ki=0,ar=1,hr=2,Ph=3,Ih=4,id=5,xs=100,sd=101,rd=102,Lh=103,Uh=104,od=200,ad=201,cd=202,ld=203,zc=204,Hc=205,hd=206,ud=207,fd=208,dd=209,pd=210,md=211,gd=212,_d=213,xd=214,vd=0,yd=1,Md=2,ea=3,Sd=4,bd=5,Ed=6,wd=7,uf=0,Td=1,Ad=2,ji=0,Rd=1,Cd=2,Pd=3,Il=4,Id=5,Ld=6;var ff=300,ur=301,fr=302,kc=303,Gc=304,Ua=306,bs=1e3,Ln=1001,Vc=1002,In=1003,Dh=1004;var rc=1005;var $n=1006,Ud=1007;var kr=1008;var Qi=1009,Dd=1010,Nd=1011,Ll=1012,df=1013,$i=1014,Ji=1015,Gr=1016,pf=1017,mf=1018,ys=1020,Fd=1021,hi=1023,Od=1024,Bd=1025,Ms=1026,dr=1027,zd=1028,gf=1029,Hd=1030,_f=1031,xf=1033,oc=33776,ac=33777,cc=33778,lc=33779,Nh=35840,Fh=35841,Oh=35842,Bh=35843,vf=36196,zh=37492,Hh=37496,kh=37808,Gh=37809,Vh=37810,Wh=37811,Xh=37812,Yh=37813,qh=37814,Zh=37815,$h=37816,Jh=37817,Kh=37818,jh=37819,Qh=37820,tu=37821,hc=36492,eu=36494,nu=36495,kd=36283,iu=36284,su=36285,ru=36286;var na=2300,ia=2301,uc=2302,ou=2400,au=2401,cu=2402;var yf=3e3,Ss=3001,Gd=3200,Vd=3201,Mf=0,Ul=1,Jn="",sn="srgb",Di="srgb-linear",Dl="display-p3",Da="display-p3-linear",sa="linear",Xe="srgb",ra="rec709",oa="p3";var Bs=7680;var lu=519,Wd=512,Xd=513,Yd=514,Sf=515,qd=516,Zd=517,$d=518,Jd=519,hu=35044;var uu="300 es",Wc=1035,Ui=2e3,aa=2001,ns=class{addEventListener(t,e){this._listeners===void 0&&(this._listeners={});let n=this._listeners;n[t]===void 0&&(n[t]=[]),n[t].indexOf(e)===-1&&n[t].push(e)}hasEventListener(t,e){if(this._listeners===void 0)return!1;let n=this._listeners;return n[t]!==void 0&&n[t].indexOf(e)!==-1}removeEventListener(t,e){if(this._listeners===void 0)return;let s=this._listeners[t];if(s!==void 0){let r=s.indexOf(e);r!==-1&&s.splice(r,1)}}dispatchEvent(t){if(this._listeners===void 0)return;let n=this._listeners[t.type];if(n!==void 0){t.target=this;let s=n.slice(0);for(let r=0,a=s.length;r<a;r++)s[r].call(this,t);t.target=null}}},bn=["00","01","02","03","04","05","06","07","08","09","0a","0b","0c","0d","0e","0f","10","11","12","13","14","15","16","17","18","19","1a","1b","1c","1d","1e","1f","20","21","22","23","24","25","26","27","28","29","2a","2b","2c","2d","2e","2f","30","31","32","33","34","35","36","37","38","39","3a","3b","3c","3d","3e","3f","40","41","42","43","44","45","46","47","48","49","4a","4b","4c","4d","4e","4f","50","51","52","53","54","55","56","57","58","59","5a","5b","5c","5d","5e","5f","60","61","62","63","64","65","66","67","68","69","6a","6b","6c","6d","6e","6f","70","71","72","73","74","75","76","77","78","79","7a","7b","7c","7d","7e","7f","80","81","82","83","84","85","86","87","88","89","8a","8b","8c","8d","8e","8f","90","91","92","93","94","95","96","97","98","99","9a","9b","9c","9d","9e","9f","a0","a1","a2","a3","a4","a5","a6","a7","a8","a9","aa","ab","ac","ad","ae","af","b0","b1","b2","b3","b4","b5","b6","b7","b8","b9","ba","bb","bc","bd","be","bf","c0","c1","c2","c3","c4","c5","c6","c7","c8","c9","ca","cb","cc","cd","ce","cf","d0","d1","d2","d3","d4","d5","d6","d7","d8","d9","da","db","dc","dd","de","df","e0","e1","e2","e3","e4","e5","e6","e7","e8","e9","ea","eb","ec","ed","ee","ef","f0","f1","f2","f3","f4","f5","f6","f7","f8","f9","fa","fb","fc","fd","fe","ff"],fu=1234567,Nr=Math.PI/180,Vr=180/Math.PI;function Is(){let i=Math.random()*4294967295|0,t=Math.random()*4294967295|0,e=Math.random()*4294967295|0,n=Math.random()*4294967295|0;return(bn[i&255]+bn[i>>8&255]+bn[i>>16&255]+bn[i>>24&255]+"-"+bn[t&255]+bn[t>>8&255]+"-"+bn[t>>16&15|64]+bn[t>>24&255]+"-"+bn[e&63|128]+bn[e>>8&255]+"-"+bn[e>>16&255]+bn[e>>24&255]+bn[n&255]+bn[n>>8&255]+bn[n>>16&255]+bn[n>>24&255]).toLowerCase()}function gn(i,t,e){return Math.max(t,Math.min(e,i))}function Nl(i,t){return(i%t+t)%t}function Kd(i,t,e,n,s){return n+(i-t)*(s-n)/(e-t)}function jd(i,t,e){return i!==t?(e-i)/(t-i):0}function Fr(i,t,e){return(1-e)*i+e*t}function Qd(i,t,e,n){return Fr(i,t,1-Math.exp(-e*n))}function tp(i,t=1){return t-Math.abs(Nl(i,t*2)-t)}function ep(i,t,e){return i<=t?0:i>=e?1:(i=(i-t)/(e-t),i*i*(3-2*i))}function np(i,t,e){return i<=t?0:i>=e?1:(i=(i-t)/(e-t),i*i*i*(i*(i*6-15)+10))}function ip(i,t){return i+Math.floor(Math.random()*(t-i+1))}function sp(i,t){return i+Math.random()*(t-i)}function rp(i){return i*(.5-Math.random())}function op(i){i!==void 0&&(fu=i);let t=fu+=1831565813;return t=Math.imul(t^t>>>15,t|1),t^=t+Math.imul(t^t>>>7,t|61),((t^t>>>14)>>>0)/4294967296}function ap(i){return i*Nr}function cp(i){return i*Vr}function Xc(i){return(i&i-1)===0&&i!==0}function lp(i){return Math.pow(2,Math.ceil(Math.log(i)/Math.LN2))}function ca(i){return Math.pow(2,Math.floor(Math.log(i)/Math.LN2))}function hp(i,t,e,n,s){let r=Math.cos,a=Math.sin,o=r(e/2),c=a(e/2),l=r((t+n)/2),h=a((t+n)/2),f=r((t-n)/2),d=a((t-n)/2),p=r((n-t)/2),x=a((n-t)/2);switch(s){case"XYX":i.set(o*h,c*f,c*d,o*l);break;case"YZY":i.set(c*d,o*h,c*f,o*l);break;case"ZXZ":i.set(c*f,c*d,o*h,o*l);break;case"XZX":i.set(o*h,c*x,c*p,o*l);break;case"YXY":i.set(c*p,o*h,c*x,o*l);break;case"ZYZ":i.set(c*x,c*p,o*h,o*l);break;default:console.warn("THREE.MathUtils: .setQuaternionFromProperEuler() encountered an unknown order: "+s)}}function er(i,t){switch(t.constructor){case Float32Array:return i;case Uint32Array:return i/4294967295;case Uint16Array:return i/65535;case Uint8Array:return i/255;case Int32Array:return Math.max(i/2147483647,-1);case Int16Array:return Math.max(i/32767,-1);case Int8Array:return Math.max(i/127,-1);default:throw new Error("Invalid component type.")}}function Cn(i,t){switch(t.constructor){case Float32Array:return i;case Uint32Array:return Math.round(i*4294967295);case Uint16Array:return Math.round(i*65535);case Uint8Array:return Math.round(i*255);case Int32Array:return Math.round(i*2147483647);case Int16Array:return Math.round(i*32767);case Int8Array:return Math.round(i*127);default:throw new Error("Invalid component type.")}}var zi={DEG2RAD:Nr,RAD2DEG:Vr,generateUUID:Is,clamp:gn,euclideanModulo:Nl,mapLinear:Kd,inverseLerp:jd,lerp:Fr,damp:Qd,pingpong:tp,smoothstep:ep,smootherstep:np,randInt:ip,randFloat:sp,randFloatSpread:rp,seededRandom:op,degToRad:ap,radToDeg:cp,isPowerOfTwo:Xc,ceilPowerOfTwo:lp,floorPowerOfTwo:ca,setQuaternionFromProperEuler:hp,normalize:Cn,denormalize:er},St=class i{constructor(t=0,e=0){i.prototype.isVector2=!0,this.x=t,this.y=e}get width(){return this.x}set width(t){this.x=t}get height(){return this.y}set height(t){this.y=t}set(t,e){return this.x=t,this.y=e,this}setScalar(t){return this.x=t,this.y=t,this}setX(t){return this.x=t,this}setY(t){return this.y=t,this}setComponent(t,e){switch(t){case 0:this.x=e;break;case 1:this.y=e;break;default:throw new Error("index is out of range: "+t)}return this}getComponent(t){switch(t){case 0:return this.x;case 1:return this.y;default:throw new Error("index is out of range: "+t)}}clone(){return new this.constructor(this.x,this.y)}copy(t){return this.x=t.x,this.y=t.y,this}add(t){return this.x+=t.x,this.y+=t.y,this}addScalar(t){return this.x+=t,this.y+=t,this}addVectors(t,e){return this.x=t.x+e.x,this.y=t.y+e.y,this}addScaledVector(t,e){return this.x+=t.x*e,this.y+=t.y*e,this}sub(t){return this.x-=t.x,this.y-=t.y,this}subScalar(t){return this.x-=t,this.y-=t,this}subVectors(t,e){return this.x=t.x-e.x,this.y=t.y-e.y,this}multiply(t){return this.x*=t.x,this.y*=t.y,this}multiplyScalar(t){return this.x*=t,this.y*=t,this}divide(t){return this.x/=t.x,this.y/=t.y,this}divideScalar(t){return this.multiplyScalar(1/t)}applyMatrix3(t){let e=this.x,n=this.y,s=t.elements;return this.x=s[0]*e+s[3]*n+s[6],this.y=s[1]*e+s[4]*n+s[7],this}min(t){return this.x=Math.min(this.x,t.x),this.y=Math.min(this.y,t.y),this}max(t){return this.x=Math.max(this.x,t.x),this.y=Math.max(this.y,t.y),this}clamp(t,e){return this.x=Math.max(t.x,Math.min(e.x,this.x)),this.y=Math.max(t.y,Math.min(e.y,this.y)),this}clampScalar(t,e){return this.x=Math.max(t,Math.min(e,this.x)),this.y=Math.max(t,Math.min(e,this.y)),this}clampLength(t,e){let n=this.length();return this.divideScalar(n||1).multiplyScalar(Math.max(t,Math.min(e,n)))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this}negate(){return this.x=-this.x,this.y=-this.y,this}dot(t){return this.x*t.x+this.y*t.y}cross(t){return this.x*t.y-this.y*t.x}lengthSq(){return this.x*this.x+this.y*this.y}length(){return Math.sqrt(this.x*this.x+this.y*this.y)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)}normalize(){return this.divideScalar(this.length()||1)}angle(){return Math.atan2(-this.y,-this.x)+Math.PI}angleTo(t){let e=Math.sqrt(this.lengthSq()*t.lengthSq());if(e===0)return Math.PI/2;let n=this.dot(t)/e;return Math.acos(gn(n,-1,1))}distanceTo(t){return Math.sqrt(this.distanceToSquared(t))}distanceToSquared(t){let e=this.x-t.x,n=this.y-t.y;return e*e+n*n}manhattanDistanceTo(t){return Math.abs(this.x-t.x)+Math.abs(this.y-t.y)}setLength(t){return this.normalize().multiplyScalar(t)}lerp(t,e){return this.x+=(t.x-this.x)*e,this.y+=(t.y-this.y)*e,this}lerpVectors(t,e,n){return this.x=t.x+(e.x-t.x)*n,this.y=t.y+(e.y-t.y)*n,this}equals(t){return t.x===this.x&&t.y===this.y}fromArray(t,e=0){return this.x=t[e],this.y=t[e+1],this}toArray(t=[],e=0){return t[e]=this.x,t[e+1]=this.y,t}fromBufferAttribute(t,e){return this.x=t.getX(e),this.y=t.getY(e),this}rotateAround(t,e){let n=Math.cos(e),s=Math.sin(e),r=this.x-t.x,a=this.y-t.y;return this.x=r*n-a*s+t.x,this.y=r*s+a*n+t.y,this}random(){return this.x=Math.random(),this.y=Math.random(),this}*[Symbol.iterator](){yield this.x,yield this.y}},we=class i{constructor(t,e,n,s,r,a,o,c,l){i.prototype.isMatrix3=!0,this.elements=[1,0,0,0,1,0,0,0,1],t!==void 0&&this.set(t,e,n,s,r,a,o,c,l)}set(t,e,n,s,r,a,o,c,l){let h=this.elements;return h[0]=t,h[1]=s,h[2]=o,h[3]=e,h[4]=r,h[5]=c,h[6]=n,h[7]=a,h[8]=l,this}identity(){return this.set(1,0,0,0,1,0,0,0,1),this}copy(t){let e=this.elements,n=t.elements;return e[0]=n[0],e[1]=n[1],e[2]=n[2],e[3]=n[3],e[4]=n[4],e[5]=n[5],e[6]=n[6],e[7]=n[7],e[8]=n[8],this}extractBasis(t,e,n){return t.setFromMatrix3Column(this,0),e.setFromMatrix3Column(this,1),n.setFromMatrix3Column(this,2),this}setFromMatrix4(t){let e=t.elements;return this.set(e[0],e[4],e[8],e[1],e[5],e[9],e[2],e[6],e[10]),this}multiply(t){return this.multiplyMatrices(this,t)}premultiply(t){return this.multiplyMatrices(t,this)}multiplyMatrices(t,e){let n=t.elements,s=e.elements,r=this.elements,a=n[0],o=n[3],c=n[6],l=n[1],h=n[4],f=n[7],d=n[2],p=n[5],x=n[8],S=s[0],_=s[3],m=s[6],T=s[1],M=s[4],U=s[7],W=s[2],F=s[5],B=s[8];return r[0]=a*S+o*T+c*W,r[3]=a*_+o*M+c*F,r[6]=a*m+o*U+c*B,r[1]=l*S+h*T+f*W,r[4]=l*_+h*M+f*F,r[7]=l*m+h*U+f*B,r[2]=d*S+p*T+x*W,r[5]=d*_+p*M+x*F,r[8]=d*m+p*U+x*B,this}multiplyScalar(t){let e=this.elements;return e[0]*=t,e[3]*=t,e[6]*=t,e[1]*=t,e[4]*=t,e[7]*=t,e[2]*=t,e[5]*=t,e[8]*=t,this}determinant(){let t=this.elements,e=t[0],n=t[1],s=t[2],r=t[3],a=t[4],o=t[5],c=t[6],l=t[7],h=t[8];return e*a*h-e*o*l-n*r*h+n*o*c+s*r*l-s*a*c}invert(){let t=this.elements,e=t[0],n=t[1],s=t[2],r=t[3],a=t[4],o=t[5],c=t[6],l=t[7],h=t[8],f=h*a-o*l,d=o*c-h*r,p=l*r-a*c,x=e*f+n*d+s*p;if(x===0)return this.set(0,0,0,0,0,0,0,0,0);let S=1/x;return t[0]=f*S,t[1]=(s*l-h*n)*S,t[2]=(o*n-s*a)*S,t[3]=d*S,t[4]=(h*e-s*c)*S,t[5]=(s*r-o*e)*S,t[6]=p*S,t[7]=(n*c-l*e)*S,t[8]=(a*e-n*r)*S,this}transpose(){let t,e=this.elements;return t=e[1],e[1]=e[3],e[3]=t,t=e[2],e[2]=e[6],e[6]=t,t=e[5],e[5]=e[7],e[7]=t,this}getNormalMatrix(t){return this.setFromMatrix4(t).invert().transpose()}transposeIntoArray(t){let e=this.elements;return t[0]=e[0],t[1]=e[3],t[2]=e[6],t[3]=e[1],t[4]=e[4],t[5]=e[7],t[6]=e[2],t[7]=e[5],t[8]=e[8],this}setUvTransform(t,e,n,s,r,a,o){let c=Math.cos(r),l=Math.sin(r);return this.set(n*c,n*l,-n*(c*a+l*o)+a+t,-s*l,s*c,-s*(-l*a+c*o)+o+e,0,0,1),this}scale(t,e){return this.premultiply(fc.makeScale(t,e)),this}rotate(t){return this.premultiply(fc.makeRotation(-t)),this}translate(t,e){return this.premultiply(fc.makeTranslation(t,e)),this}makeTranslation(t,e){return t.isVector2?this.set(1,0,t.x,0,1,t.y,0,0,1):this.set(1,0,t,0,1,e,0,0,1),this}makeRotation(t){let e=Math.cos(t),n=Math.sin(t);return this.set(e,-n,0,n,e,0,0,0,1),this}makeScale(t,e){return this.set(t,0,0,0,e,0,0,0,1),this}equals(t){let e=this.elements,n=t.elements;for(let s=0;s<9;s++)if(e[s]!==n[s])return!1;return!0}fromArray(t,e=0){for(let n=0;n<9;n++)this.elements[n]=t[n+e];return this}toArray(t=[],e=0){let n=this.elements;return t[e]=n[0],t[e+1]=n[1],t[e+2]=n[2],t[e+3]=n[3],t[e+4]=n[4],t[e+5]=n[5],t[e+6]=n[6],t[e+7]=n[7],t[e+8]=n[8],t}clone(){return new this.constructor().fromArray(this.elements)}},fc=new we;function bf(i){for(let t=i.length-1;t>=0;--t)if(i[t]>=65535)return!0;return!1}function Wr(i){return document.createElementNS("http://www.w3.org/1999/xhtml",i)}function up(){let i=Wr("canvas");return i.style.display="block",i}var du={};function Or(i){i in du||(du[i]=!0,console.warn(i))}var pu=new we().set(.8224621,.177538,0,.0331941,.9668058,0,.0170827,.0723974,.9105199),mu=new we().set(1.2249401,-.2249404,0,-.0420569,1.0420571,0,-.0196376,-.0786361,1.0982735),To={[Di]:{transfer:sa,primaries:ra,toReference:i=>i,fromReference:i=>i},[sn]:{transfer:Xe,primaries:ra,toReference:i=>i.convertSRGBToLinear(),fromReference:i=>i.convertLinearToSRGB()},[Da]:{transfer:sa,primaries:oa,toReference:i=>i.applyMatrix3(mu),fromReference:i=>i.applyMatrix3(pu)},[Dl]:{transfer:Xe,primaries:oa,toReference:i=>i.convertSRGBToLinear().applyMatrix3(mu),fromReference:i=>i.applyMatrix3(pu).convertLinearToSRGB()}},fp=new Set([Di,Da]),Be={enabled:!0,_workingColorSpace:Di,get workingColorSpace(){return this._workingColorSpace},set workingColorSpace(i){if(!fp.has(i))throw new Error(`Unsupported working color space, "${i}".`);this._workingColorSpace=i},convert:function(i,t,e){if(this.enabled===!1||t===e||!t||!e)return i;let n=To[t].toReference,s=To[e].fromReference;return s(n(i))},fromWorkingColorSpace:function(i,t){return this.convert(i,this._workingColorSpace,t)},toWorkingColorSpace:function(i,t){return this.convert(i,t,this._workingColorSpace)},getPrimaries:function(i){return To[i].primaries},getTransfer:function(i){return i===Jn?sa:To[i].transfer}};function cr(i){return i<.04045?i*.0773993808:Math.pow(i*.9478672986+.0521327014,2.4)}function dc(i){return i<.0031308?i*12.92:1.055*Math.pow(i,.41666)-.055}var zs,la=class{static getDataURL(t){if(/^data:/i.test(t.src)||typeof HTMLCanvasElement=="undefined")return t.src;let e;if(t instanceof HTMLCanvasElement)e=t;else{zs===void 0&&(zs=Wr("canvas")),zs.width=t.width,zs.height=t.height;let n=zs.getContext("2d");t instanceof ImageData?n.putImageData(t,0,0):n.drawImage(t,0,0,t.width,t.height),e=zs}return e.width>2048||e.height>2048?(console.warn("THREE.ImageUtils.getDataURL: Image converted to jpg for performance reasons",t),e.toDataURL("image/jpeg",.6)):e.toDataURL("image/png")}static sRGBToLinear(t){if(typeof HTMLImageElement!="undefined"&&t instanceof HTMLImageElement||typeof HTMLCanvasElement!="undefined"&&t instanceof HTMLCanvasElement||typeof ImageBitmap!="undefined"&&t instanceof ImageBitmap){let e=Wr("canvas");e.width=t.width,e.height=t.height;let n=e.getContext("2d");n.drawImage(t,0,0,t.width,t.height);let s=n.getImageData(0,0,t.width,t.height),r=s.data;for(let a=0;a<r.length;a++)r[a]=cr(r[a]/255)*255;return n.putImageData(s,0,0),e}else if(t.data){let e=t.data.slice(0);for(let n=0;n<e.length;n++)e instanceof Uint8Array||e instanceof Uint8ClampedArray?e[n]=Math.floor(cr(e[n]/255)*255):e[n]=cr(e[n]);return{data:e,width:t.width,height:t.height}}else return console.warn("THREE.ImageUtils.sRGBToLinear(): Unsupported image type. No color space conversion applied."),t}},dp=0,ha=class{constructor(t=null){this.isSource=!0,Object.defineProperty(this,"id",{value:dp++}),this.uuid=Is(),this.data=t,this.version=0}set needsUpdate(t){t===!0&&this.version++}toJSON(t){let e=t===void 0||typeof t=="string";if(!e&&t.images[this.uuid]!==void 0)return t.images[this.uuid];let n={uuid:this.uuid,url:""},s=this.data;if(s!==null){let r;if(Array.isArray(s)){r=[];for(let a=0,o=s.length;a<o;a++)s[a].isDataTexture?r.push(pc(s[a].image)):r.push(pc(s[a]))}else r=pc(s);n.url=r}return e||(t.images[this.uuid]=n),n}};function pc(i){return typeof HTMLImageElement!="undefined"&&i instanceof HTMLImageElement||typeof HTMLCanvasElement!="undefined"&&i instanceof HTMLCanvasElement||typeof ImageBitmap!="undefined"&&i instanceof ImageBitmap?la.getDataURL(i):i.data?{data:Array.from(i.data),width:i.width,height:i.height,type:i.data.constructor.name}:(console.warn("THREE.Texture: Unable to serialize Texture."),{})}var pp=0,Hn=class i extends ns{constructor(t=i.DEFAULT_IMAGE,e=i.DEFAULT_MAPPING,n=Ln,s=Ln,r=$n,a=kr,o=hi,c=Qi,l=i.DEFAULT_ANISOTROPY,h=Jn){super(),this.isTexture=!0,Object.defineProperty(this,"id",{value:pp++}),this.uuid=Is(),this.name="",this.source=new ha(t),this.mipmaps=[],this.mapping=e,this.channel=0,this.wrapS=n,this.wrapT=s,this.magFilter=r,this.minFilter=a,this.anisotropy=l,this.format=o,this.internalFormat=null,this.type=c,this.offset=new St(0,0),this.repeat=new St(1,1),this.center=new St(0,0),this.rotation=0,this.matrixAutoUpdate=!0,this.matrix=new we,this.generateMipmaps=!0,this.premultiplyAlpha=!1,this.flipY=!0,this.unpackAlignment=4,typeof h=="string"?this.colorSpace=h:(Or("THREE.Texture: Property .encoding has been replaced by .colorSpace."),this.colorSpace=h===Ss?sn:Jn),this.userData={},this.version=0,this.onUpdate=null,this.isRenderTargetTexture=!1,this.needsPMREMUpdate=!1}get image(){return this.source.data}set image(t=null){this.source.data=t}updateMatrix(){this.matrix.setUvTransform(this.offset.x,this.offset.y,this.repeat.x,this.repeat.y,this.rotation,this.center.x,this.center.y)}clone(){return new this.constructor().copy(this)}copy(t){return this.name=t.name,this.source=t.source,this.mipmaps=t.mipmaps.slice(0),this.mapping=t.mapping,this.channel=t.channel,this.wrapS=t.wrapS,this.wrapT=t.wrapT,this.magFilter=t.magFilter,this.minFilter=t.minFilter,this.anisotropy=t.anisotropy,this.format=t.format,this.internalFormat=t.internalFormat,this.type=t.type,this.offset.copy(t.offset),this.repeat.copy(t.repeat),this.center.copy(t.center),this.rotation=t.rotation,this.matrixAutoUpdate=t.matrixAutoUpdate,this.matrix.copy(t.matrix),this.generateMipmaps=t.generateMipmaps,this.premultiplyAlpha=t.premultiplyAlpha,this.flipY=t.flipY,this.unpackAlignment=t.unpackAlignment,this.colorSpace=t.colorSpace,this.userData=JSON.parse(JSON.stringify(t.userData)),this.needsUpdate=!0,this}toJSON(t){let e=t===void 0||typeof t=="string";if(!e&&t.textures[this.uuid]!==void 0)return t.textures[this.uuid];let n={metadata:{version:4.6,type:"Texture",generator:"Texture.toJSON"},uuid:this.uuid,name:this.name,image:this.source.toJSON(t).uuid,mapping:this.mapping,channel:this.channel,repeat:[this.repeat.x,this.repeat.y],offset:[this.offset.x,this.offset.y],center:[this.center.x,this.center.y],rotation:this.rotation,wrap:[this.wrapS,this.wrapT],format:this.format,internalFormat:this.internalFormat,type:this.type,colorSpace:this.colorSpace,minFilter:this.minFilter,magFilter:this.magFilter,anisotropy:this.anisotropy,flipY:this.flipY,generateMipmaps:this.generateMipmaps,premultiplyAlpha:this.premultiplyAlpha,unpackAlignment:this.unpackAlignment};return Object.keys(this.userData).length>0&&(n.userData=this.userData),e||(t.textures[this.uuid]=n),n}dispose(){this.dispatchEvent({type:"dispose"})}transformUv(t){if(this.mapping!==ff)return t;if(t.applyMatrix3(this.matrix),t.x<0||t.x>1)switch(this.wrapS){case bs:t.x=t.x-Math.floor(t.x);break;case Ln:t.x=t.x<0?0:1;break;case Vc:Math.abs(Math.floor(t.x)%2)===1?t.x=Math.ceil(t.x)-t.x:t.x=t.x-Math.floor(t.x);break}if(t.y<0||t.y>1)switch(this.wrapT){case bs:t.y=t.y-Math.floor(t.y);break;case Ln:t.y=t.y<0?0:1;break;case Vc:Math.abs(Math.floor(t.y)%2)===1?t.y=Math.ceil(t.y)-t.y:t.y=t.y-Math.floor(t.y);break}return this.flipY&&(t.y=1-t.y),t}set needsUpdate(t){t===!0&&(this.version++,this.source.needsUpdate=!0)}get encoding(){return Or("THREE.Texture: Property .encoding has been replaced by .colorSpace."),this.colorSpace===sn?Ss:yf}set encoding(t){Or("THREE.Texture: Property .encoding has been replaced by .colorSpace."),this.colorSpace=t===Ss?sn:Jn}};Hn.DEFAULT_IMAGE=null;Hn.DEFAULT_MAPPING=ff;Hn.DEFAULT_ANISOTROPY=1;var Je=class i{constructor(t=0,e=0,n=0,s=1){i.prototype.isVector4=!0,this.x=t,this.y=e,this.z=n,this.w=s}get width(){return this.z}set width(t){this.z=t}get height(){return this.w}set height(t){this.w=t}set(t,e,n,s){return this.x=t,this.y=e,this.z=n,this.w=s,this}setScalar(t){return this.x=t,this.y=t,this.z=t,this.w=t,this}setX(t){return this.x=t,this}setY(t){return this.y=t,this}setZ(t){return this.z=t,this}setW(t){return this.w=t,this}setComponent(t,e){switch(t){case 0:this.x=e;break;case 1:this.y=e;break;case 2:this.z=e;break;case 3:this.w=e;break;default:throw new Error("index is out of range: "+t)}return this}getComponent(t){switch(t){case 0:return this.x;case 1:return this.y;case 2:return this.z;case 3:return this.w;default:throw new Error("index is out of range: "+t)}}clone(){return new this.constructor(this.x,this.y,this.z,this.w)}copy(t){return this.x=t.x,this.y=t.y,this.z=t.z,this.w=t.w!==void 0?t.w:1,this}add(t){return this.x+=t.x,this.y+=t.y,this.z+=t.z,this.w+=t.w,this}addScalar(t){return this.x+=t,this.y+=t,this.z+=t,this.w+=t,this}addVectors(t,e){return this.x=t.x+e.x,this.y=t.y+e.y,this.z=t.z+e.z,this.w=t.w+e.w,this}addScaledVector(t,e){return this.x+=t.x*e,this.y+=t.y*e,this.z+=t.z*e,this.w+=t.w*e,this}sub(t){return this.x-=t.x,this.y-=t.y,this.z-=t.z,this.w-=t.w,this}subScalar(t){return this.x-=t,this.y-=t,this.z-=t,this.w-=t,this}subVectors(t,e){return this.x=t.x-e.x,this.y=t.y-e.y,this.z=t.z-e.z,this.w=t.w-e.w,this}multiply(t){return this.x*=t.x,this.y*=t.y,this.z*=t.z,this.w*=t.w,this}multiplyScalar(t){return this.x*=t,this.y*=t,this.z*=t,this.w*=t,this}applyMatrix4(t){let e=this.x,n=this.y,s=this.z,r=this.w,a=t.elements;return this.x=a[0]*e+a[4]*n+a[8]*s+a[12]*r,this.y=a[1]*e+a[5]*n+a[9]*s+a[13]*r,this.z=a[2]*e+a[6]*n+a[10]*s+a[14]*r,this.w=a[3]*e+a[7]*n+a[11]*s+a[15]*r,this}divideScalar(t){return this.multiplyScalar(1/t)}setAxisAngleFromQuaternion(t){this.w=2*Math.acos(t.w);let e=Math.sqrt(1-t.w*t.w);return e<1e-4?(this.x=1,this.y=0,this.z=0):(this.x=t.x/e,this.y=t.y/e,this.z=t.z/e),this}setAxisAngleFromRotationMatrix(t){let e,n,s,r,c=t.elements,l=c[0],h=c[4],f=c[8],d=c[1],p=c[5],x=c[9],S=c[2],_=c[6],m=c[10];if(Math.abs(h-d)<.01&&Math.abs(f-S)<.01&&Math.abs(x-_)<.01){if(Math.abs(h+d)<.1&&Math.abs(f+S)<.1&&Math.abs(x+_)<.1&&Math.abs(l+p+m-3)<.1)return this.set(1,0,0,0),this;e=Math.PI;let M=(l+1)/2,U=(p+1)/2,W=(m+1)/2,F=(h+d)/4,B=(f+S)/4,J=(x+_)/4;return M>U&&M>W?M<.01?(n=0,s=.707106781,r=.707106781):(n=Math.sqrt(M),s=F/n,r=B/n):U>W?U<.01?(n=.707106781,s=0,r=.707106781):(s=Math.sqrt(U),n=F/s,r=J/s):W<.01?(n=.707106781,s=.707106781,r=0):(r=Math.sqrt(W),n=B/r,s=J/r),this.set(n,s,r,e),this}let T=Math.sqrt((_-x)*(_-x)+(f-S)*(f-S)+(d-h)*(d-h));return Math.abs(T)<.001&&(T=1),this.x=(_-x)/T,this.y=(f-S)/T,this.z=(d-h)/T,this.w=Math.acos((l+p+m-1)/2),this}min(t){return this.x=Math.min(this.x,t.x),this.y=Math.min(this.y,t.y),this.z=Math.min(this.z,t.z),this.w=Math.min(this.w,t.w),this}max(t){return this.x=Math.max(this.x,t.x),this.y=Math.max(this.y,t.y),this.z=Math.max(this.z,t.z),this.w=Math.max(this.w,t.w),this}clamp(t,e){return this.x=Math.max(t.x,Math.min(e.x,this.x)),this.y=Math.max(t.y,Math.min(e.y,this.y)),this.z=Math.max(t.z,Math.min(e.z,this.z)),this.w=Math.max(t.w,Math.min(e.w,this.w)),this}clampScalar(t,e){return this.x=Math.max(t,Math.min(e,this.x)),this.y=Math.max(t,Math.min(e,this.y)),this.z=Math.max(t,Math.min(e,this.z)),this.w=Math.max(t,Math.min(e,this.w)),this}clampLength(t,e){let n=this.length();return this.divideScalar(n||1).multiplyScalar(Math.max(t,Math.min(e,n)))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this.z=Math.floor(this.z),this.w=Math.floor(this.w),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this.z=Math.ceil(this.z),this.w=Math.ceil(this.w),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this.z=Math.round(this.z),this.w=Math.round(this.w),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this.z=Math.trunc(this.z),this.w=Math.trunc(this.w),this}negate(){return this.x=-this.x,this.y=-this.y,this.z=-this.z,this.w=-this.w,this}dot(t){return this.x*t.x+this.y*t.y+this.z*t.z+this.w*t.w}lengthSq(){return this.x*this.x+this.y*this.y+this.z*this.z+this.w*this.w}length(){return Math.sqrt(this.x*this.x+this.y*this.y+this.z*this.z+this.w*this.w)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)+Math.abs(this.z)+Math.abs(this.w)}normalize(){return this.divideScalar(this.length()||1)}setLength(t){return this.normalize().multiplyScalar(t)}lerp(t,e){return this.x+=(t.x-this.x)*e,this.y+=(t.y-this.y)*e,this.z+=(t.z-this.z)*e,this.w+=(t.w-this.w)*e,this}lerpVectors(t,e,n){return this.x=t.x+(e.x-t.x)*n,this.y=t.y+(e.y-t.y)*n,this.z=t.z+(e.z-t.z)*n,this.w=t.w+(e.w-t.w)*n,this}equals(t){return t.x===this.x&&t.y===this.y&&t.z===this.z&&t.w===this.w}fromArray(t,e=0){return this.x=t[e],this.y=t[e+1],this.z=t[e+2],this.w=t[e+3],this}toArray(t=[],e=0){return t[e]=this.x,t[e+1]=this.y,t[e+2]=this.z,t[e+3]=this.w,t}fromBufferAttribute(t,e){return this.x=t.getX(e),this.y=t.getY(e),this.z=t.getZ(e),this.w=t.getW(e),this}random(){return this.x=Math.random(),this.y=Math.random(),this.z=Math.random(),this.w=Math.random(),this}*[Symbol.iterator](){yield this.x,yield this.y,yield this.z,yield this.w}},Yc=class extends ns{constructor(t=1,e=1,n={}){super(),this.isRenderTarget=!0,this.width=t,this.height=e,this.depth=1,this.scissor=new Je(0,0,t,e),this.scissorTest=!1,this.viewport=new Je(0,0,t,e);let s={width:t,height:e,depth:1};n.encoding!==void 0&&(Or("THREE.WebGLRenderTarget: option.encoding has been replaced by option.colorSpace."),n.colorSpace=n.encoding===Ss?sn:Jn),n=Object.assign({generateMipmaps:!1,internalFormat:null,minFilter:$n,depthBuffer:!0,stencilBuffer:!1,depthTexture:null,samples:0},n),this.texture=new Hn(s,n.mapping,n.wrapS,n.wrapT,n.magFilter,n.minFilter,n.format,n.type,n.anisotropy,n.colorSpace),this.texture.isRenderTargetTexture=!0,this.texture.flipY=!1,this.texture.generateMipmaps=n.generateMipmaps,this.texture.internalFormat=n.internalFormat,this.depthBuffer=n.depthBuffer,this.stencilBuffer=n.stencilBuffer,this.depthTexture=n.depthTexture,this.samples=n.samples}setSize(t,e,n=1){(this.width!==t||this.height!==e||this.depth!==n)&&(this.width=t,this.height=e,this.depth=n,this.texture.image.width=t,this.texture.image.height=e,this.texture.image.depth=n,this.dispose()),this.viewport.set(0,0,t,e),this.scissor.set(0,0,t,e)}clone(){return new this.constructor().copy(this)}copy(t){this.width=t.width,this.height=t.height,this.depth=t.depth,this.scissor.copy(t.scissor),this.scissorTest=t.scissorTest,this.viewport.copy(t.viewport),this.texture=t.texture.clone(),this.texture.isRenderTargetTexture=!0;let e=Object.assign({},t.texture.image);return this.texture.source=new ha(e),this.depthBuffer=t.depthBuffer,this.stencilBuffer=t.stencilBuffer,t.depthTexture!==null&&(this.depthTexture=t.depthTexture.clone()),this.samples=t.samples,this}dispose(){this.dispatchEvent({type:"dispose"})}},Ni=class extends Yc{constructor(t=1,e=1,n={}){super(t,e,n),this.isWebGLRenderTarget=!0}},ua=class extends Hn{constructor(t=null,e=1,n=1,s=1){super(null),this.isDataArrayTexture=!0,this.image={data:t,width:e,height:n,depth:s},this.magFilter=In,this.minFilter=In,this.wrapR=Ln,this.generateMipmaps=!1,this.flipY=!1,this.unpackAlignment=1}};var qc=class extends Hn{constructor(t=null,e=1,n=1,s=1){super(null),this.isData3DTexture=!0,this.image={data:t,width:e,height:n,depth:s},this.magFilter=In,this.minFilter=In,this.wrapR=Ln,this.generateMipmaps=!1,this.flipY=!1,this.unpackAlignment=1}};var kn=class{constructor(t=0,e=0,n=0,s=1){this.isQuaternion=!0,this._x=t,this._y=e,this._z=n,this._w=s}static slerpFlat(t,e,n,s,r,a,o){let c=n[s+0],l=n[s+1],h=n[s+2],f=n[s+3],d=r[a+0],p=r[a+1],x=r[a+2],S=r[a+3];if(o===0){t[e+0]=c,t[e+1]=l,t[e+2]=h,t[e+3]=f;return}if(o===1){t[e+0]=d,t[e+1]=p,t[e+2]=x,t[e+3]=S;return}if(f!==S||c!==d||l!==p||h!==x){let _=1-o,m=c*d+l*p+h*x+f*S,T=m>=0?1:-1,M=1-m*m;if(M>Number.EPSILON){let W=Math.sqrt(M),F=Math.atan2(W,m*T);_=Math.sin(_*F)/W,o=Math.sin(o*F)/W}let U=o*T;if(c=c*_+d*U,l=l*_+p*U,h=h*_+x*U,f=f*_+S*U,_===1-o){let W=1/Math.sqrt(c*c+l*l+h*h+f*f);c*=W,l*=W,h*=W,f*=W}}t[e]=c,t[e+1]=l,t[e+2]=h,t[e+3]=f}static multiplyQuaternionsFlat(t,e,n,s,r,a){let o=n[s],c=n[s+1],l=n[s+2],h=n[s+3],f=r[a],d=r[a+1],p=r[a+2],x=r[a+3];return t[e]=o*x+h*f+c*p-l*d,t[e+1]=c*x+h*d+l*f-o*p,t[e+2]=l*x+h*p+o*d-c*f,t[e+3]=h*x-o*f-c*d-l*p,t}get x(){return this._x}set x(t){this._x=t,this._onChangeCallback()}get y(){return this._y}set y(t){this._y=t,this._onChangeCallback()}get z(){return this._z}set z(t){this._z=t,this._onChangeCallback()}get w(){return this._w}set w(t){this._w=t,this._onChangeCallback()}set(t,e,n,s){return this._x=t,this._y=e,this._z=n,this._w=s,this._onChangeCallback(),this}clone(){return new this.constructor(this._x,this._y,this._z,this._w)}copy(t){return this._x=t.x,this._y=t.y,this._z=t.z,this._w=t.w,this._onChangeCallback(),this}setFromEuler(t,e=!0){let n=t._x,s=t._y,r=t._z,a=t._order,o=Math.cos,c=Math.sin,l=o(n/2),h=o(s/2),f=o(r/2),d=c(n/2),p=c(s/2),x=c(r/2);switch(a){case"XYZ":this._x=d*h*f+l*p*x,this._y=l*p*f-d*h*x,this._z=l*h*x+d*p*f,this._w=l*h*f-d*p*x;break;case"YXZ":this._x=d*h*f+l*p*x,this._y=l*p*f-d*h*x,this._z=l*h*x-d*p*f,this._w=l*h*f+d*p*x;break;case"ZXY":this._x=d*h*f-l*p*x,this._y=l*p*f+d*h*x,this._z=l*h*x+d*p*f,this._w=l*h*f-d*p*x;break;case"ZYX":this._x=d*h*f-l*p*x,this._y=l*p*f+d*h*x,this._z=l*h*x-d*p*f,this._w=l*h*f+d*p*x;break;case"YZX":this._x=d*h*f+l*p*x,this._y=l*p*f+d*h*x,this._z=l*h*x-d*p*f,this._w=l*h*f-d*p*x;break;case"XZY":this._x=d*h*f-l*p*x,this._y=l*p*f-d*h*x,this._z=l*h*x+d*p*f,this._w=l*h*f+d*p*x;break;default:console.warn("THREE.Quaternion: .setFromEuler() encountered an unknown order: "+a)}return e===!0&&this._onChangeCallback(),this}setFromAxisAngle(t,e){let n=e/2,s=Math.sin(n);return this._x=t.x*s,this._y=t.y*s,this._z=t.z*s,this._w=Math.cos(n),this._onChangeCallback(),this}setFromRotationMatrix(t){let e=t.elements,n=e[0],s=e[4],r=e[8],a=e[1],o=e[5],c=e[9],l=e[2],h=e[6],f=e[10],d=n+o+f;if(d>0){let p=.5/Math.sqrt(d+1);this._w=.25/p,this._x=(h-c)*p,this._y=(r-l)*p,this._z=(a-s)*p}else if(n>o&&n>f){let p=2*Math.sqrt(1+n-o-f);this._w=(h-c)/p,this._x=.25*p,this._y=(s+a)/p,this._z=(r+l)/p}else if(o>f){let p=2*Math.sqrt(1+o-n-f);this._w=(r-l)/p,this._x=(s+a)/p,this._y=.25*p,this._z=(c+h)/p}else{let p=2*Math.sqrt(1+f-n-o);this._w=(a-s)/p,this._x=(r+l)/p,this._y=(c+h)/p,this._z=.25*p}return this._onChangeCallback(),this}setFromUnitVectors(t,e){let n=t.dot(e)+1;return n<Number.EPSILON?(n=0,Math.abs(t.x)>Math.abs(t.z)?(this._x=-t.y,this._y=t.x,this._z=0,this._w=n):(this._x=0,this._y=-t.z,this._z=t.y,this._w=n)):(this._x=t.y*e.z-t.z*e.y,this._y=t.z*e.x-t.x*e.z,this._z=t.x*e.y-t.y*e.x,this._w=n),this.normalize()}angleTo(t){return 2*Math.acos(Math.abs(gn(this.dot(t),-1,1)))}rotateTowards(t,e){let n=this.angleTo(t);if(n===0)return this;let s=Math.min(1,e/n);return this.slerp(t,s),this}identity(){return this.set(0,0,0,1)}invert(){return this.conjugate()}conjugate(){return this._x*=-1,this._y*=-1,this._z*=-1,this._onChangeCallback(),this}dot(t){return this._x*t._x+this._y*t._y+this._z*t._z+this._w*t._w}lengthSq(){return this._x*this._x+this._y*this._y+this._z*this._z+this._w*this._w}length(){return Math.sqrt(this._x*this._x+this._y*this._y+this._z*this._z+this._w*this._w)}normalize(){let t=this.length();return t===0?(this._x=0,this._y=0,this._z=0,this._w=1):(t=1/t,this._x=this._x*t,this._y=this._y*t,this._z=this._z*t,this._w=this._w*t),this._onChangeCallback(),this}multiply(t){return this.multiplyQuaternions(this,t)}premultiply(t){return this.multiplyQuaternions(t,this)}multiplyQuaternions(t,e){let n=t._x,s=t._y,r=t._z,a=t._w,o=e._x,c=e._y,l=e._z,h=e._w;return this._x=n*h+a*o+s*l-r*c,this._y=s*h+a*c+r*o-n*l,this._z=r*h+a*l+n*c-s*o,this._w=a*h-n*o-s*c-r*l,this._onChangeCallback(),this}slerp(t,e){if(e===0)return this;if(e===1)return this.copy(t);let n=this._x,s=this._y,r=this._z,a=this._w,o=a*t._w+n*t._x+s*t._y+r*t._z;if(o<0?(this._w=-t._w,this._x=-t._x,this._y=-t._y,this._z=-t._z,o=-o):this.copy(t),o>=1)return this._w=a,this._x=n,this._y=s,this._z=r,this;let c=1-o*o;if(c<=Number.EPSILON){let p=1-e;return this._w=p*a+e*this._w,this._x=p*n+e*this._x,this._y=p*s+e*this._y,this._z=p*r+e*this._z,this.normalize(),this}let l=Math.sqrt(c),h=Math.atan2(l,o),f=Math.sin((1-e)*h)/l,d=Math.sin(e*h)/l;return this._w=a*f+this._w*d,this._x=n*f+this._x*d,this._y=s*f+this._y*d,this._z=r*f+this._z*d,this._onChangeCallback(),this}slerpQuaternions(t,e,n){return this.copy(t).slerp(e,n)}random(){let t=Math.random(),e=Math.sqrt(1-t),n=Math.sqrt(t),s=2*Math.PI*Math.random(),r=2*Math.PI*Math.random();return this.set(e*Math.cos(s),n*Math.sin(r),n*Math.cos(r),e*Math.sin(s))}equals(t){return t._x===this._x&&t._y===this._y&&t._z===this._z&&t._w===this._w}fromArray(t,e=0){return this._x=t[e],this._y=t[e+1],this._z=t[e+2],this._w=t[e+3],this._onChangeCallback(),this}toArray(t=[],e=0){return t[e]=this._x,t[e+1]=this._y,t[e+2]=this._z,t[e+3]=this._w,t}fromBufferAttribute(t,e){return this._x=t.getX(e),this._y=t.getY(e),this._z=t.getZ(e),this._w=t.getW(e),this._onChangeCallback(),this}toJSON(){return this.toArray()}_onChange(t){return this._onChangeCallback=t,this}_onChangeCallback(){}*[Symbol.iterator](){yield this._x,yield this._y,yield this._z,yield this._w}},O=class i{constructor(t=0,e=0,n=0){i.prototype.isVector3=!0,this.x=t,this.y=e,this.z=n}set(t,e,n){return n===void 0&&(n=this.z),this.x=t,this.y=e,this.z=n,this}setScalar(t){return this.x=t,this.y=t,this.z=t,this}setX(t){return this.x=t,this}setY(t){return this.y=t,this}setZ(t){return this.z=t,this}setComponent(t,e){switch(t){case 0:this.x=e;break;case 1:this.y=e;break;case 2:this.z=e;break;default:throw new Error("index is out of range: "+t)}return this}getComponent(t){switch(t){case 0:return this.x;case 1:return this.y;case 2:return this.z;default:throw new Error("index is out of range: "+t)}}clone(){return new this.constructor(this.x,this.y,this.z)}copy(t){return this.x=t.x,this.y=t.y,this.z=t.z,this}add(t){return this.x+=t.x,this.y+=t.y,this.z+=t.z,this}addScalar(t){return this.x+=t,this.y+=t,this.z+=t,this}addVectors(t,e){return this.x=t.x+e.x,this.y=t.y+e.y,this.z=t.z+e.z,this}addScaledVector(t,e){return this.x+=t.x*e,this.y+=t.y*e,this.z+=t.z*e,this}sub(t){return this.x-=t.x,this.y-=t.y,this.z-=t.z,this}subScalar(t){return this.x-=t,this.y-=t,this.z-=t,this}subVectors(t,e){return this.x=t.x-e.x,this.y=t.y-e.y,this.z=t.z-e.z,this}multiply(t){return this.x*=t.x,this.y*=t.y,this.z*=t.z,this}multiplyScalar(t){return this.x*=t,this.y*=t,this.z*=t,this}multiplyVectors(t,e){return this.x=t.x*e.x,this.y=t.y*e.y,this.z=t.z*e.z,this}applyEuler(t){return this.applyQuaternion(gu.setFromEuler(t))}applyAxisAngle(t,e){return this.applyQuaternion(gu.setFromAxisAngle(t,e))}applyMatrix3(t){let e=this.x,n=this.y,s=this.z,r=t.elements;return this.x=r[0]*e+r[3]*n+r[6]*s,this.y=r[1]*e+r[4]*n+r[7]*s,this.z=r[2]*e+r[5]*n+r[8]*s,this}applyNormalMatrix(t){return this.applyMatrix3(t).normalize()}applyMatrix4(t){let e=this.x,n=this.y,s=this.z,r=t.elements,a=1/(r[3]*e+r[7]*n+r[11]*s+r[15]);return this.x=(r[0]*e+r[4]*n+r[8]*s+r[12])*a,this.y=(r[1]*e+r[5]*n+r[9]*s+r[13])*a,this.z=(r[2]*e+r[6]*n+r[10]*s+r[14])*a,this}applyQuaternion(t){let e=this.x,n=this.y,s=this.z,r=t.x,a=t.y,o=t.z,c=t.w,l=2*(a*s-o*n),h=2*(o*e-r*s),f=2*(r*n-a*e);return this.x=e+c*l+a*f-o*h,this.y=n+c*h+o*l-r*f,this.z=s+c*f+r*h-a*l,this}project(t){return this.applyMatrix4(t.matrixWorldInverse).applyMatrix4(t.projectionMatrix)}unproject(t){return this.applyMatrix4(t.projectionMatrixInverse).applyMatrix4(t.matrixWorld)}transformDirection(t){let e=this.x,n=this.y,s=this.z,r=t.elements;return this.x=r[0]*e+r[4]*n+r[8]*s,this.y=r[1]*e+r[5]*n+r[9]*s,this.z=r[2]*e+r[6]*n+r[10]*s,this.normalize()}divide(t){return this.x/=t.x,this.y/=t.y,this.z/=t.z,this}divideScalar(t){return this.multiplyScalar(1/t)}min(t){return this.x=Math.min(this.x,t.x),this.y=Math.min(this.y,t.y),this.z=Math.min(this.z,t.z),this}max(t){return this.x=Math.max(this.x,t.x),this.y=Math.max(this.y,t.y),this.z=Math.max(this.z,t.z),this}clamp(t,e){return this.x=Math.max(t.x,Math.min(e.x,this.x)),this.y=Math.max(t.y,Math.min(e.y,this.y)),this.z=Math.max(t.z,Math.min(e.z,this.z)),this}clampScalar(t,e){return this.x=Math.max(t,Math.min(e,this.x)),this.y=Math.max(t,Math.min(e,this.y)),this.z=Math.max(t,Math.min(e,this.z)),this}clampLength(t,e){let n=this.length();return this.divideScalar(n||1).multiplyScalar(Math.max(t,Math.min(e,n)))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this.z=Math.floor(this.z),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this.z=Math.ceil(this.z),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this.z=Math.round(this.z),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this.z=Math.trunc(this.z),this}negate(){return this.x=-this.x,this.y=-this.y,this.z=-this.z,this}dot(t){return this.x*t.x+this.y*t.y+this.z*t.z}lengthSq(){return this.x*this.x+this.y*this.y+this.z*this.z}length(){return Math.sqrt(this.x*this.x+this.y*this.y+this.z*this.z)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)+Math.abs(this.z)}normalize(){return this.divideScalar(this.length()||1)}setLength(t){return this.normalize().multiplyScalar(t)}lerp(t,e){return this.x+=(t.x-this.x)*e,this.y+=(t.y-this.y)*e,this.z+=(t.z-this.z)*e,this}lerpVectors(t,e,n){return this.x=t.x+(e.x-t.x)*n,this.y=t.y+(e.y-t.y)*n,this.z=t.z+(e.z-t.z)*n,this}cross(t){return this.crossVectors(this,t)}crossVectors(t,e){let n=t.x,s=t.y,r=t.z,a=e.x,o=e.y,c=e.z;return this.x=s*c-r*o,this.y=r*a-n*c,this.z=n*o-s*a,this}projectOnVector(t){let e=t.lengthSq();if(e===0)return this.set(0,0,0);let n=t.dot(this)/e;return this.copy(t).multiplyScalar(n)}projectOnPlane(t){return mc.copy(this).projectOnVector(t),this.sub(mc)}reflect(t){return this.sub(mc.copy(t).multiplyScalar(2*this.dot(t)))}angleTo(t){let e=Math.sqrt(this.lengthSq()*t.lengthSq());if(e===0)return Math.PI/2;let n=this.dot(t)/e;return Math.acos(gn(n,-1,1))}distanceTo(t){return Math.sqrt(this.distanceToSquared(t))}distanceToSquared(t){let e=this.x-t.x,n=this.y-t.y,s=this.z-t.z;return e*e+n*n+s*s}manhattanDistanceTo(t){return Math.abs(this.x-t.x)+Math.abs(this.y-t.y)+Math.abs(this.z-t.z)}setFromSpherical(t){return this.setFromSphericalCoords(t.radius,t.phi,t.theta)}setFromSphericalCoords(t,e,n){let s=Math.sin(e)*t;return this.x=s*Math.sin(n),this.y=Math.cos(e)*t,this.z=s*Math.cos(n),this}setFromCylindrical(t){return this.setFromCylindricalCoords(t.radius,t.theta,t.y)}setFromCylindricalCoords(t,e,n){return this.x=t*Math.sin(e),this.y=n,this.z=t*Math.cos(e),this}setFromMatrixPosition(t){let e=t.elements;return this.x=e[12],this.y=e[13],this.z=e[14],this}setFromMatrixScale(t){let e=this.setFromMatrixColumn(t,0).length(),n=this.setFromMatrixColumn(t,1).length(),s=this.setFromMatrixColumn(t,2).length();return this.x=e,this.y=n,this.z=s,this}setFromMatrixColumn(t,e){return this.fromArray(t.elements,e*4)}setFromMatrix3Column(t,e){return this.fromArray(t.elements,e*3)}setFromEuler(t){return this.x=t._x,this.y=t._y,this.z=t._z,this}setFromColor(t){return this.x=t.r,this.y=t.g,this.z=t.b,this}equals(t){return t.x===this.x&&t.y===this.y&&t.z===this.z}fromArray(t,e=0){return this.x=t[e],this.y=t[e+1],this.z=t[e+2],this}toArray(t=[],e=0){return t[e]=this.x,t[e+1]=this.y,t[e+2]=this.z,t}fromBufferAttribute(t,e){return this.x=t.getX(e),this.y=t.getY(e),this.z=t.getZ(e),this}random(){return this.x=Math.random(),this.y=Math.random(),this.z=Math.random(),this}randomDirection(){let t=(Math.random()-.5)*2,e=Math.random()*Math.PI*2,n=Math.sqrt(1-t**2);return this.x=n*Math.cos(e),this.y=n*Math.sin(e),this.z=t,this}*[Symbol.iterator](){yield this.x,yield this.y,yield this.z}},mc=new O,gu=new kn,Fi=class{constructor(t=new O(1/0,1/0,1/0),e=new O(-1/0,-1/0,-1/0)){this.isBox3=!0,this.min=t,this.max=e}set(t,e){return this.min.copy(t),this.max.copy(e),this}setFromArray(t){this.makeEmpty();for(let e=0,n=t.length;e<n;e+=3)this.expandByPoint(ai.fromArray(t,e));return this}setFromBufferAttribute(t){this.makeEmpty();for(let e=0,n=t.count;e<n;e++)this.expandByPoint(ai.fromBufferAttribute(t,e));return this}setFromPoints(t){this.makeEmpty();for(let e=0,n=t.length;e<n;e++)this.expandByPoint(t[e]);return this}setFromCenterAndSize(t,e){let n=ai.copy(e).multiplyScalar(.5);return this.min.copy(t).sub(n),this.max.copy(t).add(n),this}setFromObject(t,e=!1){return this.makeEmpty(),this.expandByObject(t,e)}clone(){return new this.constructor().copy(this)}copy(t){return this.min.copy(t.min),this.max.copy(t.max),this}makeEmpty(){return this.min.x=this.min.y=this.min.z=1/0,this.max.x=this.max.y=this.max.z=-1/0,this}isEmpty(){return this.max.x<this.min.x||this.max.y<this.min.y||this.max.z<this.min.z}getCenter(t){return this.isEmpty()?t.set(0,0,0):t.addVectors(this.min,this.max).multiplyScalar(.5)}getSize(t){return this.isEmpty()?t.set(0,0,0):t.subVectors(this.max,this.min)}expandByPoint(t){return this.min.min(t),this.max.max(t),this}expandByVector(t){return this.min.sub(t),this.max.add(t),this}expandByScalar(t){return this.min.addScalar(-t),this.max.addScalar(t),this}expandByObject(t,e=!1){t.updateWorldMatrix(!1,!1);let n=t.geometry;if(n!==void 0){let r=n.getAttribute("position");if(e===!0&&r!==void 0&&t.isInstancedMesh!==!0)for(let a=0,o=r.count;a<o;a++)t.isMesh===!0?t.getVertexPosition(a,ai):ai.fromBufferAttribute(r,a),ai.applyMatrix4(t.matrixWorld),this.expandByPoint(ai);else t.boundingBox!==void 0?(t.boundingBox===null&&t.computeBoundingBox(),Ao.copy(t.boundingBox)):(n.boundingBox===null&&n.computeBoundingBox(),Ao.copy(n.boundingBox)),Ao.applyMatrix4(t.matrixWorld),this.union(Ao)}let s=t.children;for(let r=0,a=s.length;r<a;r++)this.expandByObject(s[r],e);return this}containsPoint(t){return!(t.x<this.min.x||t.x>this.max.x||t.y<this.min.y||t.y>this.max.y||t.z<this.min.z||t.z>this.max.z)}containsBox(t){return this.min.x<=t.min.x&&t.max.x<=this.max.x&&this.min.y<=t.min.y&&t.max.y<=this.max.y&&this.min.z<=t.min.z&&t.max.z<=this.max.z}getParameter(t,e){return e.set((t.x-this.min.x)/(this.max.x-this.min.x),(t.y-this.min.y)/(this.max.y-this.min.y),(t.z-this.min.z)/(this.max.z-this.min.z))}intersectsBox(t){return!(t.max.x<this.min.x||t.min.x>this.max.x||t.max.y<this.min.y||t.min.y>this.max.y||t.max.z<this.min.z||t.min.z>this.max.z)}intersectsSphere(t){return this.clampPoint(t.center,ai),ai.distanceToSquared(t.center)<=t.radius*t.radius}intersectsPlane(t){let e,n;return t.normal.x>0?(e=t.normal.x*this.min.x,n=t.normal.x*this.max.x):(e=t.normal.x*this.max.x,n=t.normal.x*this.min.x),t.normal.y>0?(e+=t.normal.y*this.min.y,n+=t.normal.y*this.max.y):(e+=t.normal.y*this.max.y,n+=t.normal.y*this.min.y),t.normal.z>0?(e+=t.normal.z*this.min.z,n+=t.normal.z*this.max.z):(e+=t.normal.z*this.max.z,n+=t.normal.z*this.min.z),e<=-t.constant&&n>=-t.constant}intersectsTriangle(t){if(this.isEmpty())return!1;this.getCenter(Rr),Ro.subVectors(this.max,Rr),Hs.subVectors(t.a,Rr),ks.subVectors(t.b,Rr),Gs.subVectors(t.c,Rr),Wi.subVectors(ks,Hs),Xi.subVectors(Gs,ks),ds.subVectors(Hs,Gs);let e=[0,-Wi.z,Wi.y,0,-Xi.z,Xi.y,0,-ds.z,ds.y,Wi.z,0,-Wi.x,Xi.z,0,-Xi.x,ds.z,0,-ds.x,-Wi.y,Wi.x,0,-Xi.y,Xi.x,0,-ds.y,ds.x,0];return!gc(e,Hs,ks,Gs,Ro)||(e=[1,0,0,0,1,0,0,0,1],!gc(e,Hs,ks,Gs,Ro))?!1:(Co.crossVectors(Wi,Xi),e=[Co.x,Co.y,Co.z],gc(e,Hs,ks,Gs,Ro))}clampPoint(t,e){return e.copy(t).clamp(this.min,this.max)}distanceToPoint(t){return this.clampPoint(t,ai).distanceTo(t)}getBoundingSphere(t){return this.isEmpty()?t.makeEmpty():(this.getCenter(t.center),t.radius=this.getSize(ai).length()*.5),t}intersect(t){return this.min.max(t.min),this.max.min(t.max),this.isEmpty()&&this.makeEmpty(),this}union(t){return this.min.min(t.min),this.max.max(t.max),this}applyMatrix4(t){return this.isEmpty()?this:(Ti[0].set(this.min.x,this.min.y,this.min.z).applyMatrix4(t),Ti[1].set(this.min.x,this.min.y,this.max.z).applyMatrix4(t),Ti[2].set(this.min.x,this.max.y,this.min.z).applyMatrix4(t),Ti[3].set(this.min.x,this.max.y,this.max.z).applyMatrix4(t),Ti[4].set(this.max.x,this.min.y,this.min.z).applyMatrix4(t),Ti[5].set(this.max.x,this.min.y,this.max.z).applyMatrix4(t),Ti[6].set(this.max.x,this.max.y,this.min.z).applyMatrix4(t),Ti[7].set(this.max.x,this.max.y,this.max.z).applyMatrix4(t),this.setFromPoints(Ti),this)}translate(t){return this.min.add(t),this.max.add(t),this}equals(t){return t.min.equals(this.min)&&t.max.equals(this.max)}},Ti=[new O,new O,new O,new O,new O,new O,new O,new O],ai=new O,Ao=new Fi,Hs=new O,ks=new O,Gs=new O,Wi=new O,Xi=new O,ds=new O,Rr=new O,Ro=new O,Co=new O,ps=new O;function gc(i,t,e,n,s){for(let r=0,a=i.length-3;r<=a;r+=3){ps.fromArray(i,r);let o=s.x*Math.abs(ps.x)+s.y*Math.abs(ps.y)+s.z*Math.abs(ps.z),c=t.dot(ps),l=e.dot(ps),h=n.dot(ps);if(Math.max(-Math.max(c,l,h),Math.min(c,l,h))>o)return!1}return!0}var mp=new Fi,Cr=new O,_c=new O,is=class{constructor(t=new O,e=-1){this.isSphere=!0,this.center=t,this.radius=e}set(t,e){return this.center.copy(t),this.radius=e,this}setFromPoints(t,e){let n=this.center;e!==void 0?n.copy(e):mp.setFromPoints(t).getCenter(n);let s=0;for(let r=0,a=t.length;r<a;r++)s=Math.max(s,n.distanceToSquared(t[r]));return this.radius=Math.sqrt(s),this}copy(t){return this.center.copy(t.center),this.radius=t.radius,this}isEmpty(){return this.radius<0}makeEmpty(){return this.center.set(0,0,0),this.radius=-1,this}containsPoint(t){return t.distanceToSquared(this.center)<=this.radius*this.radius}distanceToPoint(t){return t.distanceTo(this.center)-this.radius}intersectsSphere(t){let e=this.radius+t.radius;return t.center.distanceToSquared(this.center)<=e*e}intersectsBox(t){return t.intersectsSphere(this)}intersectsPlane(t){return Math.abs(t.distanceToPoint(this.center))<=this.radius}clampPoint(t,e){let n=this.center.distanceToSquared(t);return e.copy(t),n>this.radius*this.radius&&(e.sub(this.center).normalize(),e.multiplyScalar(this.radius).add(this.center)),e}getBoundingBox(t){return this.isEmpty()?(t.makeEmpty(),t):(t.set(this.center,this.center),t.expandByScalar(this.radius),t)}applyMatrix4(t){return this.center.applyMatrix4(t),this.radius=this.radius*t.getMaxScaleOnAxis(),this}translate(t){return this.center.add(t),this}expandByPoint(t){if(this.isEmpty())return this.center.copy(t),this.radius=0,this;Cr.subVectors(t,this.center);let e=Cr.lengthSq();if(e>this.radius*this.radius){let n=Math.sqrt(e),s=(n-this.radius)*.5;this.center.addScaledVector(Cr,s/n),this.radius+=s}return this}union(t){return t.isEmpty()?this:this.isEmpty()?(this.copy(t),this):(this.center.equals(t.center)===!0?this.radius=Math.max(this.radius,t.radius):(_c.subVectors(t.center,this.center).setLength(t.radius),this.expandByPoint(Cr.copy(t.center).add(_c)),this.expandByPoint(Cr.copy(t.center).sub(_c))),this)}equals(t){return t.center.equals(this.center)&&t.radius===this.radius}clone(){return new this.constructor().copy(this)}},Ai=new O,xc=new O,Po=new O,Yi=new O,vc=new O,Io=new O,yc=new O,Xr=class{constructor(t=new O,e=new O(0,0,-1)){this.origin=t,this.direction=e}set(t,e){return this.origin.copy(t),this.direction.copy(e),this}copy(t){return this.origin.copy(t.origin),this.direction.copy(t.direction),this}at(t,e){return e.copy(this.origin).addScaledVector(this.direction,t)}lookAt(t){return this.direction.copy(t).sub(this.origin).normalize(),this}recast(t){return this.origin.copy(this.at(t,Ai)),this}closestPointToPoint(t,e){e.subVectors(t,this.origin);let n=e.dot(this.direction);return n<0?e.copy(this.origin):e.copy(this.origin).addScaledVector(this.direction,n)}distanceToPoint(t){return Math.sqrt(this.distanceSqToPoint(t))}distanceSqToPoint(t){let e=Ai.subVectors(t,this.origin).dot(this.direction);return e<0?this.origin.distanceToSquared(t):(Ai.copy(this.origin).addScaledVector(this.direction,e),Ai.distanceToSquared(t))}distanceSqToSegment(t,e,n,s){xc.copy(t).add(e).multiplyScalar(.5),Po.copy(e).sub(t).normalize(),Yi.copy(this.origin).sub(xc);let r=t.distanceTo(e)*.5,a=-this.direction.dot(Po),o=Yi.dot(this.direction),c=-Yi.dot(Po),l=Yi.lengthSq(),h=Math.abs(1-a*a),f,d,p,x;if(h>0)if(f=a*c-o,d=a*o-c,x=r*h,f>=0)if(d>=-x)if(d<=x){let S=1/h;f*=S,d*=S,p=f*(f+a*d+2*o)+d*(a*f+d+2*c)+l}else d=r,f=Math.max(0,-(a*d+o)),p=-f*f+d*(d+2*c)+l;else d=-r,f=Math.max(0,-(a*d+o)),p=-f*f+d*(d+2*c)+l;else d<=-x?(f=Math.max(0,-(-a*r+o)),d=f>0?-r:Math.min(Math.max(-r,-c),r),p=-f*f+d*(d+2*c)+l):d<=x?(f=0,d=Math.min(Math.max(-r,-c),r),p=d*(d+2*c)+l):(f=Math.max(0,-(a*r+o)),d=f>0?r:Math.min(Math.max(-r,-c),r),p=-f*f+d*(d+2*c)+l);else d=a>0?-r:r,f=Math.max(0,-(a*d+o)),p=-f*f+d*(d+2*c)+l;return n&&n.copy(this.origin).addScaledVector(this.direction,f),s&&s.copy(xc).addScaledVector(Po,d),p}intersectSphere(t,e){Ai.subVectors(t.center,this.origin);let n=Ai.dot(this.direction),s=Ai.dot(Ai)-n*n,r=t.radius*t.radius;if(s>r)return null;let a=Math.sqrt(r-s),o=n-a,c=n+a;return c<0?null:o<0?this.at(c,e):this.at(o,e)}intersectsSphere(t){return this.distanceSqToPoint(t.center)<=t.radius*t.radius}distanceToPlane(t){let e=t.normal.dot(this.direction);if(e===0)return t.distanceToPoint(this.origin)===0?0:null;let n=-(this.origin.dot(t.normal)+t.constant)/e;return n>=0?n:null}intersectPlane(t,e){let n=this.distanceToPlane(t);return n===null?null:this.at(n,e)}intersectsPlane(t){let e=t.distanceToPoint(this.origin);return e===0||t.normal.dot(this.direction)*e<0}intersectBox(t,e){let n,s,r,a,o,c,l=1/this.direction.x,h=1/this.direction.y,f=1/this.direction.z,d=this.origin;return l>=0?(n=(t.min.x-d.x)*l,s=(t.max.x-d.x)*l):(n=(t.max.x-d.x)*l,s=(t.min.x-d.x)*l),h>=0?(r=(t.min.y-d.y)*h,a=(t.max.y-d.y)*h):(r=(t.max.y-d.y)*h,a=(t.min.y-d.y)*h),n>a||r>s||((r>n||isNaN(n))&&(n=r),(a<s||isNaN(s))&&(s=a),f>=0?(o=(t.min.z-d.z)*f,c=(t.max.z-d.z)*f):(o=(t.max.z-d.z)*f,c=(t.min.z-d.z)*f),n>c||o>s)||((o>n||n!==n)&&(n=o),(c<s||s!==s)&&(s=c),s<0)?null:this.at(n>=0?n:s,e)}intersectsBox(t){return this.intersectBox(t,Ai)!==null}intersectTriangle(t,e,n,s,r){vc.subVectors(e,t),Io.subVectors(n,t),yc.crossVectors(vc,Io);let a=this.direction.dot(yc),o;if(a>0){if(s)return null;o=1}else if(a<0)o=-1,a=-a;else return null;Yi.subVectors(this.origin,t);let c=o*this.direction.dot(Io.crossVectors(Yi,Io));if(c<0)return null;let l=o*this.direction.dot(vc.cross(Yi));if(l<0||c+l>a)return null;let h=-o*Yi.dot(yc);return h<0?null:this.at(h/a,r)}applyMatrix4(t){return this.origin.applyMatrix4(t),this.direction.transformDirection(t),this}equals(t){return t.origin.equals(this.origin)&&t.direction.equals(this.direction)}clone(){return new this.constructor().copy(this)}},Ue=class i{constructor(t,e,n,s,r,a,o,c,l,h,f,d,p,x,S,_){i.prototype.isMatrix4=!0,this.elements=[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],t!==void 0&&this.set(t,e,n,s,r,a,o,c,l,h,f,d,p,x,S,_)}set(t,e,n,s,r,a,o,c,l,h,f,d,p,x,S,_){let m=this.elements;return m[0]=t,m[4]=e,m[8]=n,m[12]=s,m[1]=r,m[5]=a,m[9]=o,m[13]=c,m[2]=l,m[6]=h,m[10]=f,m[14]=d,m[3]=p,m[7]=x,m[11]=S,m[15]=_,this}identity(){return this.set(1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1),this}clone(){return new i().fromArray(this.elements)}copy(t){let e=this.elements,n=t.elements;return e[0]=n[0],e[1]=n[1],e[2]=n[2],e[3]=n[3],e[4]=n[4],e[5]=n[5],e[6]=n[6],e[7]=n[7],e[8]=n[8],e[9]=n[9],e[10]=n[10],e[11]=n[11],e[12]=n[12],e[13]=n[13],e[14]=n[14],e[15]=n[15],this}copyPosition(t){let e=this.elements,n=t.elements;return e[12]=n[12],e[13]=n[13],e[14]=n[14],this}setFromMatrix3(t){let e=t.elements;return this.set(e[0],e[3],e[6],0,e[1],e[4],e[7],0,e[2],e[5],e[8],0,0,0,0,1),this}extractBasis(t,e,n){return t.setFromMatrixColumn(this,0),e.setFromMatrixColumn(this,1),n.setFromMatrixColumn(this,2),this}makeBasis(t,e,n){return this.set(t.x,e.x,n.x,0,t.y,e.y,n.y,0,t.z,e.z,n.z,0,0,0,0,1),this}extractRotation(t){let e=this.elements,n=t.elements,s=1/Vs.setFromMatrixColumn(t,0).length(),r=1/Vs.setFromMatrixColumn(t,1).length(),a=1/Vs.setFromMatrixColumn(t,2).length();return e[0]=n[0]*s,e[1]=n[1]*s,e[2]=n[2]*s,e[3]=0,e[4]=n[4]*r,e[5]=n[5]*r,e[6]=n[6]*r,e[7]=0,e[8]=n[8]*a,e[9]=n[9]*a,e[10]=n[10]*a,e[11]=0,e[12]=0,e[13]=0,e[14]=0,e[15]=1,this}makeRotationFromEuler(t){let e=this.elements,n=t.x,s=t.y,r=t.z,a=Math.cos(n),o=Math.sin(n),c=Math.cos(s),l=Math.sin(s),h=Math.cos(r),f=Math.sin(r);if(t.order==="XYZ"){let d=a*h,p=a*f,x=o*h,S=o*f;e[0]=c*h,e[4]=-c*f,e[8]=l,e[1]=p+x*l,e[5]=d-S*l,e[9]=-o*c,e[2]=S-d*l,e[6]=x+p*l,e[10]=a*c}else if(t.order==="YXZ"){let d=c*h,p=c*f,x=l*h,S=l*f;e[0]=d+S*o,e[4]=x*o-p,e[8]=a*l,e[1]=a*f,e[5]=a*h,e[9]=-o,e[2]=p*o-x,e[6]=S+d*o,e[10]=a*c}else if(t.order==="ZXY"){let d=c*h,p=c*f,x=l*h,S=l*f;e[0]=d-S*o,e[4]=-a*f,e[8]=x+p*o,e[1]=p+x*o,e[5]=a*h,e[9]=S-d*o,e[2]=-a*l,e[6]=o,e[10]=a*c}else if(t.order==="ZYX"){let d=a*h,p=a*f,x=o*h,S=o*f;e[0]=c*h,e[4]=x*l-p,e[8]=d*l+S,e[1]=c*f,e[5]=S*l+d,e[9]=p*l-x,e[2]=-l,e[6]=o*c,e[10]=a*c}else if(t.order==="YZX"){let d=a*c,p=a*l,x=o*c,S=o*l;e[0]=c*h,e[4]=S-d*f,e[8]=x*f+p,e[1]=f,e[5]=a*h,e[9]=-o*h,e[2]=-l*h,e[6]=p*f+x,e[10]=d-S*f}else if(t.order==="XZY"){let d=a*c,p=a*l,x=o*c,S=o*l;e[0]=c*h,e[4]=-f,e[8]=l*h,e[1]=d*f+S,e[5]=a*h,e[9]=p*f-x,e[2]=x*f-p,e[6]=o*h,e[10]=S*f+d}return e[3]=0,e[7]=0,e[11]=0,e[12]=0,e[13]=0,e[14]=0,e[15]=1,this}makeRotationFromQuaternion(t){return this.compose(gp,t,_p)}lookAt(t,e,n){let s=this.elements;return Bn.subVectors(t,e),Bn.lengthSq()===0&&(Bn.z=1),Bn.normalize(),qi.crossVectors(n,Bn),qi.lengthSq()===0&&(Math.abs(n.z)===1?Bn.x+=1e-4:Bn.z+=1e-4,Bn.normalize(),qi.crossVectors(n,Bn)),qi.normalize(),Lo.crossVectors(Bn,qi),s[0]=qi.x,s[4]=Lo.x,s[8]=Bn.x,s[1]=qi.y,s[5]=Lo.y,s[9]=Bn.y,s[2]=qi.z,s[6]=Lo.z,s[10]=Bn.z,this}multiply(t){return this.multiplyMatrices(this,t)}premultiply(t){return this.multiplyMatrices(t,this)}multiplyMatrices(t,e){let n=t.elements,s=e.elements,r=this.elements,a=n[0],o=n[4],c=n[8],l=n[12],h=n[1],f=n[5],d=n[9],p=n[13],x=n[2],S=n[6],_=n[10],m=n[14],T=n[3],M=n[7],U=n[11],W=n[15],F=s[0],B=s[4],J=s[8],w=s[12],L=s[1],$=s[5],ot=s[9],Mt=s[13],X=s[2],K=s[6],tt=s[10],it=s[14],ft=s[3],nt=s[7],ct=s[11],lt=s[15];return r[0]=a*F+o*L+c*X+l*ft,r[4]=a*B+o*$+c*K+l*nt,r[8]=a*J+o*ot+c*tt+l*ct,r[12]=a*w+o*Mt+c*it+l*lt,r[1]=h*F+f*L+d*X+p*ft,r[5]=h*B+f*$+d*K+p*nt,r[9]=h*J+f*ot+d*tt+p*ct,r[13]=h*w+f*Mt+d*it+p*lt,r[2]=x*F+S*L+_*X+m*ft,r[6]=x*B+S*$+_*K+m*nt,r[10]=x*J+S*ot+_*tt+m*ct,r[14]=x*w+S*Mt+_*it+m*lt,r[3]=T*F+M*L+U*X+W*ft,r[7]=T*B+M*$+U*K+W*nt,r[11]=T*J+M*ot+U*tt+W*ct,r[15]=T*w+M*Mt+U*it+W*lt,this}multiplyScalar(t){let e=this.elements;return e[0]*=t,e[4]*=t,e[8]*=t,e[12]*=t,e[1]*=t,e[5]*=t,e[9]*=t,e[13]*=t,e[2]*=t,e[6]*=t,e[10]*=t,e[14]*=t,e[3]*=t,e[7]*=t,e[11]*=t,e[15]*=t,this}determinant(){let t=this.elements,e=t[0],n=t[4],s=t[8],r=t[12],a=t[1],o=t[5],c=t[9],l=t[13],h=t[2],f=t[6],d=t[10],p=t[14],x=t[3],S=t[7],_=t[11],m=t[15];return x*(+r*c*f-s*l*f-r*o*d+n*l*d+s*o*p-n*c*p)+S*(+e*c*p-e*l*d+r*a*d-s*a*p+s*l*h-r*c*h)+_*(+e*l*f-e*o*p-r*a*f+n*a*p+r*o*h-n*l*h)+m*(-s*o*h-e*c*f+e*o*d+s*a*f-n*a*d+n*c*h)}transpose(){let t=this.elements,e;return e=t[1],t[1]=t[4],t[4]=e,e=t[2],t[2]=t[8],t[8]=e,e=t[6],t[6]=t[9],t[9]=e,e=t[3],t[3]=t[12],t[12]=e,e=t[7],t[7]=t[13],t[13]=e,e=t[11],t[11]=t[14],t[14]=e,this}setPosition(t,e,n){let s=this.elements;return t.isVector3?(s[12]=t.x,s[13]=t.y,s[14]=t.z):(s[12]=t,s[13]=e,s[14]=n),this}invert(){let t=this.elements,e=t[0],n=t[1],s=t[2],r=t[3],a=t[4],o=t[5],c=t[6],l=t[7],h=t[8],f=t[9],d=t[10],p=t[11],x=t[12],S=t[13],_=t[14],m=t[15],T=f*_*l-S*d*l+S*c*p-o*_*p-f*c*m+o*d*m,M=x*d*l-h*_*l-x*c*p+a*_*p+h*c*m-a*d*m,U=h*S*l-x*f*l+x*o*p-a*S*p-h*o*m+a*f*m,W=x*f*c-h*S*c-x*o*d+a*S*d+h*o*_-a*f*_,F=e*T+n*M+s*U+r*W;if(F===0)return this.set(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);let B=1/F;return t[0]=T*B,t[1]=(S*d*r-f*_*r-S*s*p+n*_*p+f*s*m-n*d*m)*B,t[2]=(o*_*r-S*c*r+S*s*l-n*_*l-o*s*m+n*c*m)*B,t[3]=(f*c*r-o*d*r-f*s*l+n*d*l+o*s*p-n*c*p)*B,t[4]=M*B,t[5]=(h*_*r-x*d*r+x*s*p-e*_*p-h*s*m+e*d*m)*B,t[6]=(x*c*r-a*_*r-x*s*l+e*_*l+a*s*m-e*c*m)*B,t[7]=(a*d*r-h*c*r+h*s*l-e*d*l-a*s*p+e*c*p)*B,t[8]=U*B,t[9]=(x*f*r-h*S*r-x*n*p+e*S*p+h*n*m-e*f*m)*B,t[10]=(a*S*r-x*o*r+x*n*l-e*S*l-a*n*m+e*o*m)*B,t[11]=(h*o*r-a*f*r-h*n*l+e*f*l+a*n*p-e*o*p)*B,t[12]=W*B,t[13]=(h*S*s-x*f*s+x*n*d-e*S*d-h*n*_+e*f*_)*B,t[14]=(x*o*s-a*S*s-x*n*c+e*S*c+a*n*_-e*o*_)*B,t[15]=(a*f*s-h*o*s+h*n*c-e*f*c-a*n*d+e*o*d)*B,this}scale(t){let e=this.elements,n=t.x,s=t.y,r=t.z;return e[0]*=n,e[4]*=s,e[8]*=r,e[1]*=n,e[5]*=s,e[9]*=r,e[2]*=n,e[6]*=s,e[10]*=r,e[3]*=n,e[7]*=s,e[11]*=r,this}getMaxScaleOnAxis(){let t=this.elements,e=t[0]*t[0]+t[1]*t[1]+t[2]*t[2],n=t[4]*t[4]+t[5]*t[5]+t[6]*t[6],s=t[8]*t[8]+t[9]*t[9]+t[10]*t[10];return Math.sqrt(Math.max(e,n,s))}makeTranslation(t,e,n){return t.isVector3?this.set(1,0,0,t.x,0,1,0,t.y,0,0,1,t.z,0,0,0,1):this.set(1,0,0,t,0,1,0,e,0,0,1,n,0,0,0,1),this}makeRotationX(t){let e=Math.cos(t),n=Math.sin(t);return this.set(1,0,0,0,0,e,-n,0,0,n,e,0,0,0,0,1),this}makeRotationY(t){let e=Math.cos(t),n=Math.sin(t);return this.set(e,0,n,0,0,1,0,0,-n,0,e,0,0,0,0,1),this}makeRotationZ(t){let e=Math.cos(t),n=Math.sin(t);return this.set(e,-n,0,0,n,e,0,0,0,0,1,0,0,0,0,1),this}makeRotationAxis(t,e){let n=Math.cos(e),s=Math.sin(e),r=1-n,a=t.x,o=t.y,c=t.z,l=r*a,h=r*o;return this.set(l*a+n,l*o-s*c,l*c+s*o,0,l*o+s*c,h*o+n,h*c-s*a,0,l*c-s*o,h*c+s*a,r*c*c+n,0,0,0,0,1),this}makeScale(t,e,n){return this.set(t,0,0,0,0,e,0,0,0,0,n,0,0,0,0,1),this}makeShear(t,e,n,s,r,a){return this.set(1,n,r,0,t,1,a,0,e,s,1,0,0,0,0,1),this}compose(t,e,n){let s=this.elements,r=e._x,a=e._y,o=e._z,c=e._w,l=r+r,h=a+a,f=o+o,d=r*l,p=r*h,x=r*f,S=a*h,_=a*f,m=o*f,T=c*l,M=c*h,U=c*f,W=n.x,F=n.y,B=n.z;return s[0]=(1-(S+m))*W,s[1]=(p+U)*W,s[2]=(x-M)*W,s[3]=0,s[4]=(p-U)*F,s[5]=(1-(d+m))*F,s[6]=(_+T)*F,s[7]=0,s[8]=(x+M)*B,s[9]=(_-T)*B,s[10]=(1-(d+S))*B,s[11]=0,s[12]=t.x,s[13]=t.y,s[14]=t.z,s[15]=1,this}decompose(t,e,n){let s=this.elements,r=Vs.set(s[0],s[1],s[2]).length(),a=Vs.set(s[4],s[5],s[6]).length(),o=Vs.set(s[8],s[9],s[10]).length();this.determinant()<0&&(r=-r),t.x=s[12],t.y=s[13],t.z=s[14],ci.copy(this);let l=1/r,h=1/a,f=1/o;return ci.elements[0]*=l,ci.elements[1]*=l,ci.elements[2]*=l,ci.elements[4]*=h,ci.elements[5]*=h,ci.elements[6]*=h,ci.elements[8]*=f,ci.elements[9]*=f,ci.elements[10]*=f,e.setFromRotationMatrix(ci),n.x=r,n.y=a,n.z=o,this}makePerspective(t,e,n,s,r,a,o=Ui){let c=this.elements,l=2*r/(e-t),h=2*r/(n-s),f=(e+t)/(e-t),d=(n+s)/(n-s),p,x;if(o===Ui)p=-(a+r)/(a-r),x=-2*a*r/(a-r);else if(o===aa)p=-a/(a-r),x=-a*r/(a-r);else throw new Error("THREE.Matrix4.makePerspective(): Invalid coordinate system: "+o);return c[0]=l,c[4]=0,c[8]=f,c[12]=0,c[1]=0,c[5]=h,c[9]=d,c[13]=0,c[2]=0,c[6]=0,c[10]=p,c[14]=x,c[3]=0,c[7]=0,c[11]=-1,c[15]=0,this}makeOrthographic(t,e,n,s,r,a,o=Ui){let c=this.elements,l=1/(e-t),h=1/(n-s),f=1/(a-r),d=(e+t)*l,p=(n+s)*h,x,S;if(o===Ui)x=(a+r)*f,S=-2*f;else if(o===aa)x=r*f,S=-1*f;else throw new Error("THREE.Matrix4.makeOrthographic(): Invalid coordinate system: "+o);return c[0]=2*l,c[4]=0,c[8]=0,c[12]=-d,c[1]=0,c[5]=2*h,c[9]=0,c[13]=-p,c[2]=0,c[6]=0,c[10]=S,c[14]=-x,c[3]=0,c[7]=0,c[11]=0,c[15]=1,this}equals(t){let e=this.elements,n=t.elements;for(let s=0;s<16;s++)if(e[s]!==n[s])return!1;return!0}fromArray(t,e=0){for(let n=0;n<16;n++)this.elements[n]=t[n+e];return this}toArray(t=[],e=0){let n=this.elements;return t[e]=n[0],t[e+1]=n[1],t[e+2]=n[2],t[e+3]=n[3],t[e+4]=n[4],t[e+5]=n[5],t[e+6]=n[6],t[e+7]=n[7],t[e+8]=n[8],t[e+9]=n[9],t[e+10]=n[10],t[e+11]=n[11],t[e+12]=n[12],t[e+13]=n[13],t[e+14]=n[14],t[e+15]=n[15],t}},Vs=new O,ci=new Ue,gp=new O(0,0,0),_p=new O(1,1,1),qi=new O,Lo=new O,Bn=new O,_u=new Ue,xu=new kn,ss=class i{constructor(t=0,e=0,n=0,s=i.DEFAULT_ORDER){this.isEuler=!0,this._x=t,this._y=e,this._z=n,this._order=s}get x(){return this._x}set x(t){this._x=t,this._onChangeCallback()}get y(){return this._y}set y(t){this._y=t,this._onChangeCallback()}get z(){return this._z}set z(t){this._z=t,this._onChangeCallback()}get order(){return this._order}set order(t){this._order=t,this._onChangeCallback()}set(t,e,n,s=this._order){return this._x=t,this._y=e,this._z=n,this._order=s,this._onChangeCallback(),this}clone(){return new this.constructor(this._x,this._y,this._z,this._order)}copy(t){return this._x=t._x,this._y=t._y,this._z=t._z,this._order=t._order,this._onChangeCallback(),this}setFromRotationMatrix(t,e=this._order,n=!0){let s=t.elements,r=s[0],a=s[4],o=s[8],c=s[1],l=s[5],h=s[9],f=s[2],d=s[6],p=s[10];switch(e){case"XYZ":this._y=Math.asin(gn(o,-1,1)),Math.abs(o)<.9999999?(this._x=Math.atan2(-h,p),this._z=Math.atan2(-a,r)):(this._x=Math.atan2(d,l),this._z=0);break;case"YXZ":this._x=Math.asin(-gn(h,-1,1)),Math.abs(h)<.9999999?(this._y=Math.atan2(o,p),this._z=Math.atan2(c,l)):(this._y=Math.atan2(-f,r),this._z=0);break;case"ZXY":this._x=Math.asin(gn(d,-1,1)),Math.abs(d)<.9999999?(this._y=Math.atan2(-f,p),this._z=Math.atan2(-a,l)):(this._y=0,this._z=Math.atan2(c,r));break;case"ZYX":this._y=Math.asin(-gn(f,-1,1)),Math.abs(f)<.9999999?(this._x=Math.atan2(d,p),this._z=Math.atan2(c,r)):(this._x=0,this._z=Math.atan2(-a,l));break;case"YZX":this._z=Math.asin(gn(c,-1,1)),Math.abs(c)<.9999999?(this._x=Math.atan2(-h,l),this._y=Math.atan2(-f,r)):(this._x=0,this._y=Math.atan2(o,p));break;case"XZY":this._z=Math.asin(-gn(a,-1,1)),Math.abs(a)<.9999999?(this._x=Math.atan2(d,l),this._y=Math.atan2(o,r)):(this._x=Math.atan2(-h,p),this._y=0);break;default:console.warn("THREE.Euler: .setFromRotationMatrix() encountered an unknown order: "+e)}return this._order=e,n===!0&&this._onChangeCallback(),this}setFromQuaternion(t,e,n){return _u.makeRotationFromQuaternion(t),this.setFromRotationMatrix(_u,e,n)}setFromVector3(t,e=this._order){return this.set(t.x,t.y,t.z,e)}reorder(t){return xu.setFromEuler(this),this.setFromQuaternion(xu,t)}equals(t){return t._x===this._x&&t._y===this._y&&t._z===this._z&&t._order===this._order}fromArray(t){return this._x=t[0],this._y=t[1],this._z=t[2],t[3]!==void 0&&(this._order=t[3]),this._onChangeCallback(),this}toArray(t=[],e=0){return t[e]=this._x,t[e+1]=this._y,t[e+2]=this._z,t[e+3]=this._order,t}_onChange(t){return this._onChangeCallback=t,this}_onChangeCallback(){}*[Symbol.iterator](){yield this._x,yield this._y,yield this._z,yield this._order}};ss.DEFAULT_ORDER="XYZ";var Yr=class{constructor(){this.mask=1}set(t){this.mask=(1<<t|0)>>>0}enable(t){this.mask|=1<<t|0}enableAll(){this.mask=-1}toggle(t){this.mask^=1<<t|0}disable(t){this.mask&=~(1<<t|0)}disableAll(){this.mask=0}test(t){return(this.mask&t.mask)!==0}isEnabled(t){return(this.mask&(1<<t|0))!==0}},xp=0,vu=new O,Ws=new kn,Ri=new Ue,Uo=new O,Pr=new O,vp=new O,yp=new kn,yu=new O(1,0,0),Mu=new O(0,1,0),Su=new O(0,0,1),Mp={type:"added"},Sp={type:"removed"},An=class i extends ns{constructor(){super(),this.isObject3D=!0,Object.defineProperty(this,"id",{value:xp++}),this.uuid=Is(),this.name="",this.type="Object3D",this.parent=null,this.children=[],this.up=i.DEFAULT_UP.clone();let t=new O,e=new ss,n=new kn,s=new O(1,1,1);function r(){n.setFromEuler(e,!1)}function a(){e.setFromQuaternion(n,void 0,!1)}e._onChange(r),n._onChange(a),Object.defineProperties(this,{position:{configurable:!0,enumerable:!0,value:t},rotation:{configurable:!0,enumerable:!0,value:e},quaternion:{configurable:!0,enumerable:!0,value:n},scale:{configurable:!0,enumerable:!0,value:s},modelViewMatrix:{value:new Ue},normalMatrix:{value:new we}}),this.matrix=new Ue,this.matrixWorld=new Ue,this.matrixAutoUpdate=i.DEFAULT_MATRIX_AUTO_UPDATE,this.matrixWorldAutoUpdate=i.DEFAULT_MATRIX_WORLD_AUTO_UPDATE,this.matrixWorldNeedsUpdate=!1,this.layers=new Yr,this.visible=!0,this.castShadow=!1,this.receiveShadow=!1,this.frustumCulled=!0,this.renderOrder=0,this.animations=[],this.userData={}}onBeforeShadow(){}onAfterShadow(){}onBeforeRender(){}onAfterRender(){}applyMatrix4(t){this.matrixAutoUpdate&&this.updateMatrix(),this.matrix.premultiply(t),this.matrix.decompose(this.position,this.quaternion,this.scale)}applyQuaternion(t){return this.quaternion.premultiply(t),this}setRotationFromAxisAngle(t,e){this.quaternion.setFromAxisAngle(t,e)}setRotationFromEuler(t){this.quaternion.setFromEuler(t,!0)}setRotationFromMatrix(t){this.quaternion.setFromRotationMatrix(t)}setRotationFromQuaternion(t){this.quaternion.copy(t)}rotateOnAxis(t,e){return Ws.setFromAxisAngle(t,e),this.quaternion.multiply(Ws),this}rotateOnWorldAxis(t,e){return Ws.setFromAxisAngle(t,e),this.quaternion.premultiply(Ws),this}rotateX(t){return this.rotateOnAxis(yu,t)}rotateY(t){return this.rotateOnAxis(Mu,t)}rotateZ(t){return this.rotateOnAxis(Su,t)}translateOnAxis(t,e){return vu.copy(t).applyQuaternion(this.quaternion),this.position.add(vu.multiplyScalar(e)),this}translateX(t){return this.translateOnAxis(yu,t)}translateY(t){return this.translateOnAxis(Mu,t)}translateZ(t){return this.translateOnAxis(Su,t)}localToWorld(t){return this.updateWorldMatrix(!0,!1),t.applyMatrix4(this.matrixWorld)}worldToLocal(t){return this.updateWorldMatrix(!0,!1),t.applyMatrix4(Ri.copy(this.matrixWorld).invert())}lookAt(t,e,n){t.isVector3?Uo.copy(t):Uo.set(t,e,n);let s=this.parent;this.updateWorldMatrix(!0,!1),Pr.setFromMatrixPosition(this.matrixWorld),this.isCamera||this.isLight?Ri.lookAt(Pr,Uo,this.up):Ri.lookAt(Uo,Pr,this.up),this.quaternion.setFromRotationMatrix(Ri),s&&(Ri.extractRotation(s.matrixWorld),Ws.setFromRotationMatrix(Ri),this.quaternion.premultiply(Ws.invert()))}add(t){if(arguments.length>1){for(let e=0;e<arguments.length;e++)this.add(arguments[e]);return this}return t===this?(console.error("THREE.Object3D.add: object can't be added as a child of itself.",t),this):(t&&t.isObject3D?(t.parent!==null&&t.parent.remove(t),t.parent=this,this.children.push(t),t.dispatchEvent(Mp)):console.error("THREE.Object3D.add: object not an instance of THREE.Object3D.",t),this)}remove(t){if(arguments.length>1){for(let n=0;n<arguments.length;n++)this.remove(arguments[n]);return this}let e=this.children.indexOf(t);return e!==-1&&(t.parent=null,this.children.splice(e,1),t.dispatchEvent(Sp)),this}removeFromParent(){let t=this.parent;return t!==null&&t.remove(this),this}clear(){return this.remove(...this.children)}attach(t){return this.updateWorldMatrix(!0,!1),Ri.copy(this.matrixWorld).invert(),t.parent!==null&&(t.parent.updateWorldMatrix(!0,!1),Ri.multiply(t.parent.matrixWorld)),t.applyMatrix4(Ri),this.add(t),t.updateWorldMatrix(!1,!0),this}getObjectById(t){return this.getObjectByProperty("id",t)}getObjectByName(t){return this.getObjectByProperty("name",t)}getObjectByProperty(t,e){if(this[t]===e)return this;for(let n=0,s=this.children.length;n<s;n++){let a=this.children[n].getObjectByProperty(t,e);if(a!==void 0)return a}}getObjectsByProperty(t,e,n=[]){this[t]===e&&n.push(this);let s=this.children;for(let r=0,a=s.length;r<a;r++)s[r].getObjectsByProperty(t,e,n);return n}getWorldPosition(t){return this.updateWorldMatrix(!0,!1),t.setFromMatrixPosition(this.matrixWorld)}getWorldQuaternion(t){return this.updateWorldMatrix(!0,!1),this.matrixWorld.decompose(Pr,t,vp),t}getWorldScale(t){return this.updateWorldMatrix(!0,!1),this.matrixWorld.decompose(Pr,yp,t),t}getWorldDirection(t){this.updateWorldMatrix(!0,!1);let e=this.matrixWorld.elements;return t.set(e[8],e[9],e[10]).normalize()}raycast(){}traverse(t){t(this);let e=this.children;for(let n=0,s=e.length;n<s;n++)e[n].traverse(t)}traverseVisible(t){if(this.visible===!1)return;t(this);let e=this.children;for(let n=0,s=e.length;n<s;n++)e[n].traverseVisible(t)}traverseAncestors(t){let e=this.parent;e!==null&&(t(e),e.traverseAncestors(t))}updateMatrix(){this.matrix.compose(this.position,this.quaternion,this.scale),this.matrixWorldNeedsUpdate=!0}updateMatrixWorld(t){this.matrixAutoUpdate&&this.updateMatrix(),(this.matrixWorldNeedsUpdate||t)&&(this.parent===null?this.matrixWorld.copy(this.matrix):this.matrixWorld.multiplyMatrices(this.parent.matrixWorld,this.matrix),this.matrixWorldNeedsUpdate=!1,t=!0);let e=this.children;for(let n=0,s=e.length;n<s;n++){let r=e[n];(r.matrixWorldAutoUpdate===!0||t===!0)&&r.updateMatrixWorld(t)}}updateWorldMatrix(t,e){let n=this.parent;if(t===!0&&n!==null&&n.matrixWorldAutoUpdate===!0&&n.updateWorldMatrix(!0,!1),this.matrixAutoUpdate&&this.updateMatrix(),this.parent===null?this.matrixWorld.copy(this.matrix):this.matrixWorld.multiplyMatrices(this.parent.matrixWorld,this.matrix),e===!0){let s=this.children;for(let r=0,a=s.length;r<a;r++){let o=s[r];o.matrixWorldAutoUpdate===!0&&o.updateWorldMatrix(!1,!0)}}}toJSON(t){let e=t===void 0||typeof t=="string",n={};e&&(t={geometries:{},materials:{},textures:{},images:{},shapes:{},skeletons:{},animations:{},nodes:{}},n.metadata={version:4.6,type:"Object",generator:"Object3D.toJSON"});let s={};s.uuid=this.uuid,s.type=this.type,this.name!==""&&(s.name=this.name),this.castShadow===!0&&(s.castShadow=!0),this.receiveShadow===!0&&(s.receiveShadow=!0),this.visible===!1&&(s.visible=!1),this.frustumCulled===!1&&(s.frustumCulled=!1),this.renderOrder!==0&&(s.renderOrder=this.renderOrder),Object.keys(this.userData).length>0&&(s.userData=this.userData),s.layers=this.layers.mask,s.matrix=this.matrix.toArray(),s.up=this.up.toArray(),this.matrixAutoUpdate===!1&&(s.matrixAutoUpdate=!1),this.isInstancedMesh&&(s.type="InstancedMesh",s.count=this.count,s.instanceMatrix=this.instanceMatrix.toJSON(),this.instanceColor!==null&&(s.instanceColor=this.instanceColor.toJSON())),this.isBatchedMesh&&(s.type="BatchedMesh",s.perObjectFrustumCulled=this.perObjectFrustumCulled,s.sortObjects=this.sortObjects,s.drawRanges=this._drawRanges,s.reservedRanges=this._reservedRanges,s.visibility=this._visibility,s.active=this._active,s.bounds=this._bounds.map(o=>({boxInitialized:o.boxInitialized,boxMin:o.box.min.toArray(),boxMax:o.box.max.toArray(),sphereInitialized:o.sphereInitialized,sphereRadius:o.sphere.radius,sphereCenter:o.sphere.center.toArray()})),s.maxGeometryCount=this._maxGeometryCount,s.maxVertexCount=this._maxVertexCount,s.maxIndexCount=this._maxIndexCount,s.geometryInitialized=this._geometryInitialized,s.geometryCount=this._geometryCount,s.matricesTexture=this._matricesTexture.toJSON(t),this.boundingSphere!==null&&(s.boundingSphere={center:s.boundingSphere.center.toArray(),radius:s.boundingSphere.radius}),this.boundingBox!==null&&(s.boundingBox={min:s.boundingBox.min.toArray(),max:s.boundingBox.max.toArray()}));function r(o,c){return o[c.uuid]===void 0&&(o[c.uuid]=c.toJSON(t)),c.uuid}if(this.isScene)this.background&&(this.background.isColor?s.background=this.background.toJSON():this.background.isTexture&&(s.background=this.background.toJSON(t).uuid)),this.environment&&this.environment.isTexture&&this.environment.isRenderTargetTexture!==!0&&(s.environment=this.environment.toJSON(t).uuid);else if(this.isMesh||this.isLine||this.isPoints){s.geometry=r(t.geometries,this.geometry);let o=this.geometry.parameters;if(o!==void 0&&o.shapes!==void 0){let c=o.shapes;if(Array.isArray(c))for(let l=0,h=c.length;l<h;l++){let f=c[l];r(t.shapes,f)}else r(t.shapes,c)}}if(this.isSkinnedMesh&&(s.bindMode=this.bindMode,s.bindMatrix=this.bindMatrix.toArray(),this.skeleton!==void 0&&(r(t.skeletons,this.skeleton),s.skeleton=this.skeleton.uuid)),this.material!==void 0)if(Array.isArray(this.material)){let o=[];for(let c=0,l=this.material.length;c<l;c++)o.push(r(t.materials,this.material[c]));s.material=o}else s.material=r(t.materials,this.material);if(this.children.length>0){s.children=[];for(let o=0;o<this.children.length;o++)s.children.push(this.children[o].toJSON(t).object)}if(this.animations.length>0){s.animations=[];for(let o=0;o<this.animations.length;o++){let c=this.animations[o];s.animations.push(r(t.animations,c))}}if(e){let o=a(t.geometries),c=a(t.materials),l=a(t.textures),h=a(t.images),f=a(t.shapes),d=a(t.skeletons),p=a(t.animations),x=a(t.nodes);o.length>0&&(n.geometries=o),c.length>0&&(n.materials=c),l.length>0&&(n.textures=l),h.length>0&&(n.images=h),f.length>0&&(n.shapes=f),d.length>0&&(n.skeletons=d),p.length>0&&(n.animations=p),x.length>0&&(n.nodes=x)}return n.object=s,n;function a(o){let c=[];for(let l in o){let h=o[l];delete h.metadata,c.push(h)}return c}}clone(t){return new this.constructor().copy(this,t)}copy(t,e=!0){if(this.name=t.name,this.up.copy(t.up),this.position.copy(t.position),this.rotation.order=t.rotation.order,this.quaternion.copy(t.quaternion),this.scale.copy(t.scale),this.matrix.copy(t.matrix),this.matrixWorld.copy(t.matrixWorld),this.matrixAutoUpdate=t.matrixAutoUpdate,this.matrixWorldAutoUpdate=t.matrixWorldAutoUpdate,this.matrixWorldNeedsUpdate=t.matrixWorldNeedsUpdate,this.layers.mask=t.layers.mask,this.visible=t.visible,this.castShadow=t.castShadow,this.receiveShadow=t.receiveShadow,this.frustumCulled=t.frustumCulled,this.renderOrder=t.renderOrder,this.animations=t.animations.slice(),this.userData=JSON.parse(JSON.stringify(t.userData)),e===!0)for(let n=0;n<t.children.length;n++){let s=t.children[n];this.add(s.clone())}return this}};An.DEFAULT_UP=new O(0,1,0);An.DEFAULT_MATRIX_AUTO_UPDATE=!0;An.DEFAULT_MATRIX_WORLD_AUTO_UPDATE=!0;var li=new O,Ci=new O,Mc=new O,Pi=new O,Xs=new O,Ys=new O,bu=new O,Sc=new O,bc=new O,Ec=new O,Do=!1,nr=class i{constructor(t=new O,e=new O,n=new O){this.a=t,this.b=e,this.c=n}static getNormal(t,e,n,s){s.subVectors(n,e),li.subVectors(t,e),s.cross(li);let r=s.lengthSq();return r>0?s.multiplyScalar(1/Math.sqrt(r)):s.set(0,0,0)}static getBarycoord(t,e,n,s,r){li.subVectors(s,e),Ci.subVectors(n,e),Mc.subVectors(t,e);let a=li.dot(li),o=li.dot(Ci),c=li.dot(Mc),l=Ci.dot(Ci),h=Ci.dot(Mc),f=a*l-o*o;if(f===0)return r.set(0,0,0),null;let d=1/f,p=(l*c-o*h)*d,x=(a*h-o*c)*d;return r.set(1-p-x,x,p)}static containsPoint(t,e,n,s){return this.getBarycoord(t,e,n,s,Pi)===null?!1:Pi.x>=0&&Pi.y>=0&&Pi.x+Pi.y<=1}static getUV(t,e,n,s,r,a,o,c){return Do===!1&&(console.warn("THREE.Triangle.getUV() has been renamed to THREE.Triangle.getInterpolation()."),Do=!0),this.getInterpolation(t,e,n,s,r,a,o,c)}static getInterpolation(t,e,n,s,r,a,o,c){return this.getBarycoord(t,e,n,s,Pi)===null?(c.x=0,c.y=0,"z"in c&&(c.z=0),"w"in c&&(c.w=0),null):(c.setScalar(0),c.addScaledVector(r,Pi.x),c.addScaledVector(a,Pi.y),c.addScaledVector(o,Pi.z),c)}static isFrontFacing(t,e,n,s){return li.subVectors(n,e),Ci.subVectors(t,e),li.cross(Ci).dot(s)<0}set(t,e,n){return this.a.copy(t),this.b.copy(e),this.c.copy(n),this}setFromPointsAndIndices(t,e,n,s){return this.a.copy(t[e]),this.b.copy(t[n]),this.c.copy(t[s]),this}setFromAttributeAndIndices(t,e,n,s){return this.a.fromBufferAttribute(t,e),this.b.fromBufferAttribute(t,n),this.c.fromBufferAttribute(t,s),this}clone(){return new this.constructor().copy(this)}copy(t){return this.a.copy(t.a),this.b.copy(t.b),this.c.copy(t.c),this}getArea(){return li.subVectors(this.c,this.b),Ci.subVectors(this.a,this.b),li.cross(Ci).length()*.5}getMidpoint(t){return t.addVectors(this.a,this.b).add(this.c).multiplyScalar(1/3)}getNormal(t){return i.getNormal(this.a,this.b,this.c,t)}getPlane(t){return t.setFromCoplanarPoints(this.a,this.b,this.c)}getBarycoord(t,e){return i.getBarycoord(t,this.a,this.b,this.c,e)}getUV(t,e,n,s,r){return Do===!1&&(console.warn("THREE.Triangle.getUV() has been renamed to THREE.Triangle.getInterpolation()."),Do=!0),i.getInterpolation(t,this.a,this.b,this.c,e,n,s,r)}getInterpolation(t,e,n,s,r){return i.getInterpolation(t,this.a,this.b,this.c,e,n,s,r)}containsPoint(t){return i.containsPoint(t,this.a,this.b,this.c)}isFrontFacing(t){return i.isFrontFacing(this.a,this.b,this.c,t)}intersectsBox(t){return t.intersectsTriangle(this)}closestPointToPoint(t,e){let n=this.a,s=this.b,r=this.c,a,o;Xs.subVectors(s,n),Ys.subVectors(r,n),Sc.subVectors(t,n);let c=Xs.dot(Sc),l=Ys.dot(Sc);if(c<=0&&l<=0)return e.copy(n);bc.subVectors(t,s);let h=Xs.dot(bc),f=Ys.dot(bc);if(h>=0&&f<=h)return e.copy(s);let d=c*f-h*l;if(d<=0&&c>=0&&h<=0)return a=c/(c-h),e.copy(n).addScaledVector(Xs,a);Ec.subVectors(t,r);let p=Xs.dot(Ec),x=Ys.dot(Ec);if(x>=0&&p<=x)return e.copy(r);let S=p*l-c*x;if(S<=0&&l>=0&&x<=0)return o=l/(l-x),e.copy(n).addScaledVector(Ys,o);let _=h*x-p*f;if(_<=0&&f-h>=0&&p-x>=0)return bu.subVectors(r,s),o=(f-h)/(f-h+(p-x)),e.copy(s).addScaledVector(bu,o);let m=1/(_+S+d);return a=S*m,o=d*m,e.copy(n).addScaledVector(Xs,a).addScaledVector(Ys,o)}equals(t){return t.a.equals(this.a)&&t.b.equals(this.b)&&t.c.equals(this.c)}},Ef={aliceblue:15792383,antiquewhite:16444375,aqua:65535,aquamarine:8388564,azure:15794175,beige:16119260,bisque:16770244,black:0,blanchedalmond:16772045,blue:255,blueviolet:9055202,brown:10824234,burlywood:14596231,cadetblue:6266528,chartreuse:8388352,chocolate:13789470,coral:16744272,cornflowerblue:6591981,cornsilk:16775388,crimson:14423100,cyan:65535,darkblue:139,darkcyan:35723,darkgoldenrod:12092939,darkgray:11119017,darkgreen:25600,darkgrey:11119017,darkkhaki:12433259,darkmagenta:9109643,darkolivegreen:5597999,darkorange:16747520,darkorchid:10040012,darkred:9109504,darksalmon:15308410,darkseagreen:9419919,darkslateblue:4734347,darkslategray:3100495,darkslategrey:3100495,darkturquoise:52945,darkviolet:9699539,deeppink:16716947,deepskyblue:49151,dimgray:6908265,dimgrey:6908265,dodgerblue:2003199,firebrick:11674146,floralwhite:16775920,forestgreen:2263842,fuchsia:16711935,gainsboro:14474460,ghostwhite:16316671,gold:16766720,goldenrod:14329120,gray:8421504,green:32768,greenyellow:11403055,grey:8421504,honeydew:15794160,hotpink:16738740,indianred:13458524,indigo:4915330,ivory:16777200,khaki:15787660,lavender:15132410,lavenderblush:16773365,lawngreen:8190976,lemonchiffon:16775885,lightblue:11393254,lightcoral:15761536,lightcyan:14745599,lightgoldenrodyellow:16448210,lightgray:13882323,lightgreen:9498256,lightgrey:13882323,lightpink:16758465,lightsalmon:16752762,lightseagreen:2142890,lightskyblue:8900346,lightslategray:7833753,lightslategrey:7833753,lightsteelblue:11584734,lightyellow:16777184,lime:65280,limegreen:3329330,linen:16445670,magenta:16711935,maroon:8388608,mediumaquamarine:6737322,mediumblue:205,mediumorchid:12211667,mediumpurple:9662683,mediumseagreen:3978097,mediumslateblue:8087790,mediumspringgreen:64154,mediumturquoise:4772300,mediumvioletred:13047173,midnightblue:1644912,mintcream:16121850,mistyrose:16770273,moccasin:16770229,navajowhite:16768685,navy:128,oldlace:16643558,olive:8421376,olivedrab:7048739,orange:16753920,orangered:16729344,orchid:14315734,palegoldenrod:15657130,palegreen:10025880,paleturquoise:11529966,palevioletred:14381203,papayawhip:16773077,peachpuff:16767673,peru:13468991,pink:16761035,plum:14524637,powderblue:11591910,purple:8388736,rebeccapurple:6697881,red:16711680,rosybrown:12357519,royalblue:4286945,saddlebrown:9127187,salmon:16416882,sandybrown:16032864,seagreen:3050327,seashell:16774638,sienna:10506797,silver:12632256,skyblue:8900331,slateblue:6970061,slategray:7372944,slategrey:7372944,snow:16775930,springgreen:65407,steelblue:4620980,tan:13808780,teal:32896,thistle:14204888,tomato:16737095,turquoise:4251856,violet:15631086,wheat:16113331,white:16777215,whitesmoke:16119285,yellow:16776960,yellowgreen:10145074},Zi={h:0,s:0,l:0},No={h:0,s:0,l:0};function wc(i,t,e){return e<0&&(e+=1),e>1&&(e-=1),e<1/6?i+(t-i)*6*e:e<1/2?t:e<2/3?i+(t-i)*6*(2/3-e):i}var fe=class{constructor(t,e,n){return this.isColor=!0,this.r=1,this.g=1,this.b=1,this.set(t,e,n)}set(t,e,n){if(e===void 0&&n===void 0){let s=t;s&&s.isColor?this.copy(s):typeof s=="number"?this.setHex(s):typeof s=="string"&&this.setStyle(s)}else this.setRGB(t,e,n);return this}setScalar(t){return this.r=t,this.g=t,this.b=t,this}setHex(t,e=sn){return t=Math.floor(t),this.r=(t>>16&255)/255,this.g=(t>>8&255)/255,this.b=(t&255)/255,Be.toWorkingColorSpace(this,e),this}setRGB(t,e,n,s=Be.workingColorSpace){return this.r=t,this.g=e,this.b=n,Be.toWorkingColorSpace(this,s),this}setHSL(t,e,n,s=Be.workingColorSpace){if(t=Nl(t,1),e=gn(e,0,1),n=gn(n,0,1),e===0)this.r=this.g=this.b=n;else{let r=n<=.5?n*(1+e):n+e-n*e,a=2*n-r;this.r=wc(a,r,t+1/3),this.g=wc(a,r,t),this.b=wc(a,r,t-1/3)}return Be.toWorkingColorSpace(this,s),this}setStyle(t,e=sn){function n(r){r!==void 0&&parseFloat(r)<1&&console.warn("THREE.Color: Alpha component of "+t+" will be ignored.")}let s;if(s=/^(\w+)\(([^\)]*)\)/.exec(t)){let r,a=s[1],o=s[2];switch(a){case"rgb":case"rgba":if(r=/^\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*(\d*\.?\d+)\s*)?$/.exec(o))return n(r[4]),this.setRGB(Math.min(255,parseInt(r[1],10))/255,Math.min(255,parseInt(r[2],10))/255,Math.min(255,parseInt(r[3],10))/255,e);if(r=/^\s*(\d+)\%\s*,\s*(\d+)\%\s*,\s*(\d+)\%\s*(?:,\s*(\d*\.?\d+)\s*)?$/.exec(o))return n(r[4]),this.setRGB(Math.min(100,parseInt(r[1],10))/100,Math.min(100,parseInt(r[2],10))/100,Math.min(100,parseInt(r[3],10))/100,e);break;case"hsl":case"hsla":if(r=/^\s*(\d*\.?\d+)\s*,\s*(\d*\.?\d+)\%\s*,\s*(\d*\.?\d+)\%\s*(?:,\s*(\d*\.?\d+)\s*)?$/.exec(o))return n(r[4]),this.setHSL(parseFloat(r[1])/360,parseFloat(r[2])/100,parseFloat(r[3])/100,e);break;default:console.warn("THREE.Color: Unknown color model "+t)}}else if(s=/^\#([A-Fa-f\d]+)$/.exec(t)){let r=s[1],a=r.length;if(a===3)return this.setRGB(parseInt(r.charAt(0),16)/15,parseInt(r.charAt(1),16)/15,parseInt(r.charAt(2),16)/15,e);if(a===6)return this.setHex(parseInt(r,16),e);console.warn("THREE.Color: Invalid hex color "+t)}else if(t&&t.length>0)return this.setColorName(t,e);return this}setColorName(t,e=sn){let n=Ef[t.toLowerCase()];return n!==void 0?this.setHex(n,e):console.warn("THREE.Color: Unknown color "+t),this}clone(){return new this.constructor(this.r,this.g,this.b)}copy(t){return this.r=t.r,this.g=t.g,this.b=t.b,this}copySRGBToLinear(t){return this.r=cr(t.r),this.g=cr(t.g),this.b=cr(t.b),this}copyLinearToSRGB(t){return this.r=dc(t.r),this.g=dc(t.g),this.b=dc(t.b),this}convertSRGBToLinear(){return this.copySRGBToLinear(this),this}convertLinearToSRGB(){return this.copyLinearToSRGB(this),this}getHex(t=sn){return Be.fromWorkingColorSpace(En.copy(this),t),Math.round(gn(En.r*255,0,255))*65536+Math.round(gn(En.g*255,0,255))*256+Math.round(gn(En.b*255,0,255))}getHexString(t=sn){return("000000"+this.getHex(t).toString(16)).slice(-6)}getHSL(t,e=Be.workingColorSpace){Be.fromWorkingColorSpace(En.copy(this),e);let n=En.r,s=En.g,r=En.b,a=Math.max(n,s,r),o=Math.min(n,s,r),c,l,h=(o+a)/2;if(o===a)c=0,l=0;else{let f=a-o;switch(l=h<=.5?f/(a+o):f/(2-a-o),a){case n:c=(s-r)/f+(s<r?6:0);break;case s:c=(r-n)/f+2;break;case r:c=(n-s)/f+4;break}c/=6}return t.h=c,t.s=l,t.l=h,t}getRGB(t,e=Be.workingColorSpace){return Be.fromWorkingColorSpace(En.copy(this),e),t.r=En.r,t.g=En.g,t.b=En.b,t}getStyle(t=sn){Be.fromWorkingColorSpace(En.copy(this),t);let e=En.r,n=En.g,s=En.b;return t!==sn?`color(${t} ${e.toFixed(3)} ${n.toFixed(3)} ${s.toFixed(3)})`:`rgb(${Math.round(e*255)},${Math.round(n*255)},${Math.round(s*255)})`}offsetHSL(t,e,n){return this.getHSL(Zi),this.setHSL(Zi.h+t,Zi.s+e,Zi.l+n)}add(t){return this.r+=t.r,this.g+=t.g,this.b+=t.b,this}addColors(t,e){return this.r=t.r+e.r,this.g=t.g+e.g,this.b=t.b+e.b,this}addScalar(t){return this.r+=t,this.g+=t,this.b+=t,this}sub(t){return this.r=Math.max(0,this.r-t.r),this.g=Math.max(0,this.g-t.g),this.b=Math.max(0,this.b-t.b),this}multiply(t){return this.r*=t.r,this.g*=t.g,this.b*=t.b,this}multiplyScalar(t){return this.r*=t,this.g*=t,this.b*=t,this}lerp(t,e){return this.r+=(t.r-this.r)*e,this.g+=(t.g-this.g)*e,this.b+=(t.b-this.b)*e,this}lerpColors(t,e,n){return this.r=t.r+(e.r-t.r)*n,this.g=t.g+(e.g-t.g)*n,this.b=t.b+(e.b-t.b)*n,this}lerpHSL(t,e){this.getHSL(Zi),t.getHSL(No);let n=Fr(Zi.h,No.h,e),s=Fr(Zi.s,No.s,e),r=Fr(Zi.l,No.l,e);return this.setHSL(n,s,r),this}setFromVector3(t){return this.r=t.x,this.g=t.y,this.b=t.z,this}applyMatrix3(t){let e=this.r,n=this.g,s=this.b,r=t.elements;return this.r=r[0]*e+r[3]*n+r[6]*s,this.g=r[1]*e+r[4]*n+r[7]*s,this.b=r[2]*e+r[5]*n+r[8]*s,this}equals(t){return t.r===this.r&&t.g===this.g&&t.b===this.b}fromArray(t,e=0){return this.r=t[e],this.g=t[e+1],this.b=t[e+2],this}toArray(t=[],e=0){return t[e]=this.r,t[e+1]=this.g,t[e+2]=this.b,t}fromBufferAttribute(t,e){return this.r=t.getX(e),this.g=t.getY(e),this.b=t.getZ(e),this}toJSON(){return this.getHex()}*[Symbol.iterator](){yield this.r,yield this.g,yield this.b}},En=new fe;fe.NAMES=Ef;var bp=0,yi=class extends ns{constructor(){super(),this.isMaterial=!0,Object.defineProperty(this,"id",{value:bp++}),this.uuid=Is(),this.name="",this.type="Material",this.blending=ar,this.side=es,this.vertexColors=!1,this.opacity=1,this.transparent=!1,this.alphaHash=!1,this.blendSrc=zc,this.blendDst=Hc,this.blendEquation=xs,this.blendSrcAlpha=null,this.blendDstAlpha=null,this.blendEquationAlpha=null,this.blendColor=new fe(0,0,0),this.blendAlpha=0,this.depthFunc=ea,this.depthTest=!0,this.depthWrite=!0,this.stencilWriteMask=255,this.stencilFunc=lu,this.stencilRef=0,this.stencilFuncMask=255,this.stencilFail=Bs,this.stencilZFail=Bs,this.stencilZPass=Bs,this.stencilWrite=!1,this.clippingPlanes=null,this.clipIntersection=!1,this.clipShadows=!1,this.shadowSide=null,this.colorWrite=!0,this.precision=null,this.polygonOffset=!1,this.polygonOffsetFactor=0,this.polygonOffsetUnits=0,this.dithering=!1,this.alphaToCoverage=!1,this.premultipliedAlpha=!1,this.forceSinglePass=!1,this.visible=!0,this.toneMapped=!0,this.userData={},this.version=0,this._alphaTest=0}get alphaTest(){return this._alphaTest}set alphaTest(t){this._alphaTest>0!=t>0&&this.version++,this._alphaTest=t}onBuild(){}onBeforeRender(){}onBeforeCompile(){}customProgramCacheKey(){return this.onBeforeCompile.toString()}setValues(t){if(t!==void 0)for(let e in t){let n=t[e];if(n===void 0){console.warn(`THREE.Material: parameter '${e}' has value of undefined.`);continue}let s=this[e];if(s===void 0){console.warn(`THREE.Material: '${e}' is not a property of THREE.${this.type}.`);continue}s&&s.isColor?s.set(n):s&&s.isVector3&&n&&n.isVector3?s.copy(n):this[e]=n}}toJSON(t){let e=t===void 0||typeof t=="string";e&&(t={textures:{},images:{}});let n={metadata:{version:4.6,type:"Material",generator:"Material.toJSON"}};n.uuid=this.uuid,n.type=this.type,this.name!==""&&(n.name=this.name),this.color&&this.color.isColor&&(n.color=this.color.getHex()),this.roughness!==void 0&&(n.roughness=this.roughness),this.metalness!==void 0&&(n.metalness=this.metalness),this.sheen!==void 0&&(n.sheen=this.sheen),this.sheenColor&&this.sheenColor.isColor&&(n.sheenColor=this.sheenColor.getHex()),this.sheenRoughness!==void 0&&(n.sheenRoughness=this.sheenRoughness),this.emissive&&this.emissive.isColor&&(n.emissive=this.emissive.getHex()),this.emissiveIntensity&&this.emissiveIntensity!==1&&(n.emissiveIntensity=this.emissiveIntensity),this.specular&&this.specular.isColor&&(n.specular=this.specular.getHex()),this.specularIntensity!==void 0&&(n.specularIntensity=this.specularIntensity),this.specularColor&&this.specularColor.isColor&&(n.specularColor=this.specularColor.getHex()),this.shininess!==void 0&&(n.shininess=this.shininess),this.clearcoat!==void 0&&(n.clearcoat=this.clearcoat),this.clearcoatRoughness!==void 0&&(n.clearcoatRoughness=this.clearcoatRoughness),this.clearcoatMap&&this.clearcoatMap.isTexture&&(n.clearcoatMap=this.clearcoatMap.toJSON(t).uuid),this.clearcoatRoughnessMap&&this.clearcoatRoughnessMap.isTexture&&(n.clearcoatRoughnessMap=this.clearcoatRoughnessMap.toJSON(t).uuid),this.clearcoatNormalMap&&this.clearcoatNormalMap.isTexture&&(n.clearcoatNormalMap=this.clearcoatNormalMap.toJSON(t).uuid,n.clearcoatNormalScale=this.clearcoatNormalScale.toArray()),this.iridescence!==void 0&&(n.iridescence=this.iridescence),this.iridescenceIOR!==void 0&&(n.iridescenceIOR=this.iridescenceIOR),this.iridescenceThicknessRange!==void 0&&(n.iridescenceThicknessRange=this.iridescenceThicknessRange),this.iridescenceMap&&this.iridescenceMap.isTexture&&(n.iridescenceMap=this.iridescenceMap.toJSON(t).uuid),this.iridescenceThicknessMap&&this.iridescenceThicknessMap.isTexture&&(n.iridescenceThicknessMap=this.iridescenceThicknessMap.toJSON(t).uuid),this.anisotropy!==void 0&&(n.anisotropy=this.anisotropy),this.anisotropyRotation!==void 0&&(n.anisotropyRotation=this.anisotropyRotation),this.anisotropyMap&&this.anisotropyMap.isTexture&&(n.anisotropyMap=this.anisotropyMap.toJSON(t).uuid),this.map&&this.map.isTexture&&(n.map=this.map.toJSON(t).uuid),this.matcap&&this.matcap.isTexture&&(n.matcap=this.matcap.toJSON(t).uuid),this.alphaMap&&this.alphaMap.isTexture&&(n.alphaMap=this.alphaMap.toJSON(t).uuid),this.lightMap&&this.lightMap.isTexture&&(n.lightMap=this.lightMap.toJSON(t).uuid,n.lightMapIntensity=this.lightMapIntensity),this.aoMap&&this.aoMap.isTexture&&(n.aoMap=this.aoMap.toJSON(t).uuid,n.aoMapIntensity=this.aoMapIntensity),this.bumpMap&&this.bumpMap.isTexture&&(n.bumpMap=this.bumpMap.toJSON(t).uuid,n.bumpScale=this.bumpScale),this.normalMap&&this.normalMap.isTexture&&(n.normalMap=this.normalMap.toJSON(t).uuid,n.normalMapType=this.normalMapType,n.normalScale=this.normalScale.toArray()),this.displacementMap&&this.displacementMap.isTexture&&(n.displacementMap=this.displacementMap.toJSON(t).uuid,n.displacementScale=this.displacementScale,n.displacementBias=this.displacementBias),this.roughnessMap&&this.roughnessMap.isTexture&&(n.roughnessMap=this.roughnessMap.toJSON(t).uuid),this.metalnessMap&&this.metalnessMap.isTexture&&(n.metalnessMap=this.metalnessMap.toJSON(t).uuid),this.emissiveMap&&this.emissiveMap.isTexture&&(n.emissiveMap=this.emissiveMap.toJSON(t).uuid),this.specularMap&&this.specularMap.isTexture&&(n.specularMap=this.specularMap.toJSON(t).uuid),this.specularIntensityMap&&this.specularIntensityMap.isTexture&&(n.specularIntensityMap=this.specularIntensityMap.toJSON(t).uuid),this.specularColorMap&&this.specularColorMap.isTexture&&(n.specularColorMap=this.specularColorMap.toJSON(t).uuid),this.envMap&&this.envMap.isTexture&&(n.envMap=this.envMap.toJSON(t).uuid,this.combine!==void 0&&(n.combine=this.combine)),this.envMapIntensity!==void 0&&(n.envMapIntensity=this.envMapIntensity),this.reflectivity!==void 0&&(n.reflectivity=this.reflectivity),this.refractionRatio!==void 0&&(n.refractionRatio=this.refractionRatio),this.gradientMap&&this.gradientMap.isTexture&&(n.gradientMap=this.gradientMap.toJSON(t).uuid),this.transmission!==void 0&&(n.transmission=this.transmission),this.transmissionMap&&this.transmissionMap.isTexture&&(n.transmissionMap=this.transmissionMap.toJSON(t).uuid),this.thickness!==void 0&&(n.thickness=this.thickness),this.thicknessMap&&this.thicknessMap.isTexture&&(n.thicknessMap=this.thicknessMap.toJSON(t).uuid),this.attenuationDistance!==void 0&&this.attenuationDistance!==1/0&&(n.attenuationDistance=this.attenuationDistance),this.attenuationColor!==void 0&&(n.attenuationColor=this.attenuationColor.getHex()),this.size!==void 0&&(n.size=this.size),this.shadowSide!==null&&(n.shadowSide=this.shadowSide),this.sizeAttenuation!==void 0&&(n.sizeAttenuation=this.sizeAttenuation),this.blending!==ar&&(n.blending=this.blending),this.side!==es&&(n.side=this.side),this.vertexColors===!0&&(n.vertexColors=!0),this.opacity<1&&(n.opacity=this.opacity),this.transparent===!0&&(n.transparent=!0),this.blendSrc!==zc&&(n.blendSrc=this.blendSrc),this.blendDst!==Hc&&(n.blendDst=this.blendDst),this.blendEquation!==xs&&(n.blendEquation=this.blendEquation),this.blendSrcAlpha!==null&&(n.blendSrcAlpha=this.blendSrcAlpha),this.blendDstAlpha!==null&&(n.blendDstAlpha=this.blendDstAlpha),this.blendEquationAlpha!==null&&(n.blendEquationAlpha=this.blendEquationAlpha),this.blendColor&&this.blendColor.isColor&&(n.blendColor=this.blendColor.getHex()),this.blendAlpha!==0&&(n.blendAlpha=this.blendAlpha),this.depthFunc!==ea&&(n.depthFunc=this.depthFunc),this.depthTest===!1&&(n.depthTest=this.depthTest),this.depthWrite===!1&&(n.depthWrite=this.depthWrite),this.colorWrite===!1&&(n.colorWrite=this.colorWrite),this.stencilWriteMask!==255&&(n.stencilWriteMask=this.stencilWriteMask),this.stencilFunc!==lu&&(n.stencilFunc=this.stencilFunc),this.stencilRef!==0&&(n.stencilRef=this.stencilRef),this.stencilFuncMask!==255&&(n.stencilFuncMask=this.stencilFuncMask),this.stencilFail!==Bs&&(n.stencilFail=this.stencilFail),this.stencilZFail!==Bs&&(n.stencilZFail=this.stencilZFail),this.stencilZPass!==Bs&&(n.stencilZPass=this.stencilZPass),this.stencilWrite===!0&&(n.stencilWrite=this.stencilWrite),this.rotation!==void 0&&this.rotation!==0&&(n.rotation=this.rotation),this.polygonOffset===!0&&(n.polygonOffset=!0),this.polygonOffsetFactor!==0&&(n.polygonOffsetFactor=this.polygonOffsetFactor),this.polygonOffsetUnits!==0&&(n.polygonOffsetUnits=this.polygonOffsetUnits),this.linewidth!==void 0&&this.linewidth!==1&&(n.linewidth=this.linewidth),this.dashSize!==void 0&&(n.dashSize=this.dashSize),this.gapSize!==void 0&&(n.gapSize=this.gapSize),this.scale!==void 0&&(n.scale=this.scale),this.dithering===!0&&(n.dithering=!0),this.alphaTest>0&&(n.alphaTest=this.alphaTest),this.alphaHash===!0&&(n.alphaHash=!0),this.alphaToCoverage===!0&&(n.alphaToCoverage=!0),this.premultipliedAlpha===!0&&(n.premultipliedAlpha=!0),this.forceSinglePass===!0&&(n.forceSinglePass=!0),this.wireframe===!0&&(n.wireframe=!0),this.wireframeLinewidth>1&&(n.wireframeLinewidth=this.wireframeLinewidth),this.wireframeLinecap!=="round"&&(n.wireframeLinecap=this.wireframeLinecap),this.wireframeLinejoin!=="round"&&(n.wireframeLinejoin=this.wireframeLinejoin),this.flatShading===!0&&(n.flatShading=!0),this.visible===!1&&(n.visible=!1),this.toneMapped===!1&&(n.toneMapped=!1),this.fog===!1&&(n.fog=!1),Object.keys(this.userData).length>0&&(n.userData=this.userData);function s(r){let a=[];for(let o in r){let c=r[o];delete c.metadata,a.push(c)}return a}if(e){let r=s(t.textures),a=s(t.images);r.length>0&&(n.textures=r),a.length>0&&(n.images=a)}return n}clone(){return new this.constructor().copy(this)}copy(t){this.name=t.name,this.blending=t.blending,this.side=t.side,this.vertexColors=t.vertexColors,this.opacity=t.opacity,this.transparent=t.transparent,this.blendSrc=t.blendSrc,this.blendDst=t.blendDst,this.blendEquation=t.blendEquation,this.blendSrcAlpha=t.blendSrcAlpha,this.blendDstAlpha=t.blendDstAlpha,this.blendEquationAlpha=t.blendEquationAlpha,this.blendColor.copy(t.blendColor),this.blendAlpha=t.blendAlpha,this.depthFunc=t.depthFunc,this.depthTest=t.depthTest,this.depthWrite=t.depthWrite,this.stencilWriteMask=t.stencilWriteMask,this.stencilFunc=t.stencilFunc,this.stencilRef=t.stencilRef,this.stencilFuncMask=t.stencilFuncMask,this.stencilFail=t.stencilFail,this.stencilZFail=t.stencilZFail,this.stencilZPass=t.stencilZPass,this.stencilWrite=t.stencilWrite;let e=t.clippingPlanes,n=null;if(e!==null){let s=e.length;n=new Array(s);for(let r=0;r!==s;++r)n[r]=e[r].clone()}return this.clippingPlanes=n,this.clipIntersection=t.clipIntersection,this.clipShadows=t.clipShadows,this.shadowSide=t.shadowSide,this.colorWrite=t.colorWrite,this.precision=t.precision,this.polygonOffset=t.polygonOffset,this.polygonOffsetFactor=t.polygonOffsetFactor,this.polygonOffsetUnits=t.polygonOffsetUnits,this.dithering=t.dithering,this.alphaTest=t.alphaTest,this.alphaHash=t.alphaHash,this.alphaToCoverage=t.alphaToCoverage,this.premultipliedAlpha=t.premultipliedAlpha,this.forceSinglePass=t.forceSinglePass,this.visible=t.visible,this.toneMapped=t.toneMapped,this.userData=JSON.parse(JSON.stringify(t.userData)),this}dispose(){this.dispatchEvent({type:"dispose"})}set needsUpdate(t){t===!0&&this.version++}},Es=class extends yi{constructor(t){super(),this.isMeshBasicMaterial=!0,this.type="MeshBasicMaterial",this.color=new fe(16777215),this.map=null,this.lightMap=null,this.lightMapIntensity=1,this.aoMap=null,this.aoMapIntensity=1,this.specularMap=null,this.alphaMap=null,this.envMap=null,this.combine=uf,this.reflectivity=1,this.refractionRatio=.98,this.wireframe=!1,this.wireframeLinewidth=1,this.wireframeLinecap="round",this.wireframeLinejoin="round",this.fog=!0,this.setValues(t)}copy(t){return super.copy(t),this.color.copy(t.color),this.map=t.map,this.lightMap=t.lightMap,this.lightMapIntensity=t.lightMapIntensity,this.aoMap=t.aoMap,this.aoMapIntensity=t.aoMapIntensity,this.specularMap=t.specularMap,this.alphaMap=t.alphaMap,this.envMap=t.envMap,this.combine=t.combine,this.reflectivity=t.reflectivity,this.refractionRatio=t.refractionRatio,this.wireframe=t.wireframe,this.wireframeLinewidth=t.wireframeLinewidth,this.wireframeLinecap=t.wireframeLinecap,this.wireframeLinejoin=t.wireframeLinejoin,this.fog=t.fog,this}};var an=new O,Fo=new St,Mn=class{constructor(t,e,n=!1){if(Array.isArray(t))throw new TypeError("THREE.BufferAttribute: array should be a Typed Array.");this.isBufferAttribute=!0,this.name="",this.array=t,this.itemSize=e,this.count=t!==void 0?t.length/e:0,this.normalized=n,this.usage=hu,this._updateRange={offset:0,count:-1},this.updateRanges=[],this.gpuType=Ji,this.version=0}onUploadCallback(){}set needsUpdate(t){t===!0&&this.version++}get updateRange(){return console.warn("THREE.BufferAttribute: updateRange() is deprecated and will be removed in r169. Use addUpdateRange() instead."),this._updateRange}setUsage(t){return this.usage=t,this}addUpdateRange(t,e){this.updateRanges.push({start:t,count:e})}clearUpdateRanges(){this.updateRanges.length=0}copy(t){return this.name=t.name,this.array=new t.array.constructor(t.array),this.itemSize=t.itemSize,this.count=t.count,this.normalized=t.normalized,this.usage=t.usage,this.gpuType=t.gpuType,this}copyAt(t,e,n){t*=this.itemSize,n*=e.itemSize;for(let s=0,r=this.itemSize;s<r;s++)this.array[t+s]=e.array[n+s];return this}copyArray(t){return this.array.set(t),this}applyMatrix3(t){if(this.itemSize===2)for(let e=0,n=this.count;e<n;e++)Fo.fromBufferAttribute(this,e),Fo.applyMatrix3(t),this.setXY(e,Fo.x,Fo.y);else if(this.itemSize===3)for(let e=0,n=this.count;e<n;e++)an.fromBufferAttribute(this,e),an.applyMatrix3(t),this.setXYZ(e,an.x,an.y,an.z);return this}applyMatrix4(t){for(let e=0,n=this.count;e<n;e++)an.fromBufferAttribute(this,e),an.applyMatrix4(t),this.setXYZ(e,an.x,an.y,an.z);return this}applyNormalMatrix(t){for(let e=0,n=this.count;e<n;e++)an.fromBufferAttribute(this,e),an.applyNormalMatrix(t),this.setXYZ(e,an.x,an.y,an.z);return this}transformDirection(t){for(let e=0,n=this.count;e<n;e++)an.fromBufferAttribute(this,e),an.transformDirection(t),this.setXYZ(e,an.x,an.y,an.z);return this}set(t,e=0){return this.array.set(t,e),this}getComponent(t,e){let n=this.array[t*this.itemSize+e];return this.normalized&&(n=er(n,this.array)),n}setComponent(t,e,n){return this.normalized&&(n=Cn(n,this.array)),this.array[t*this.itemSize+e]=n,this}getX(t){let e=this.array[t*this.itemSize];return this.normalized&&(e=er(e,this.array)),e}setX(t,e){return this.normalized&&(e=Cn(e,this.array)),this.array[t*this.itemSize]=e,this}getY(t){let e=this.array[t*this.itemSize+1];return this.normalized&&(e=er(e,this.array)),e}setY(t,e){return this.normalized&&(e=Cn(e,this.array)),this.array[t*this.itemSize+1]=e,this}getZ(t){let e=this.array[t*this.itemSize+2];return this.normalized&&(e=er(e,this.array)),e}setZ(t,e){return this.normalized&&(e=Cn(e,this.array)),this.array[t*this.itemSize+2]=e,this}getW(t){let e=this.array[t*this.itemSize+3];return this.normalized&&(e=er(e,this.array)),e}setW(t,e){return this.normalized&&(e=Cn(e,this.array)),this.array[t*this.itemSize+3]=e,this}setXY(t,e,n){return t*=this.itemSize,this.normalized&&(e=Cn(e,this.array),n=Cn(n,this.array)),this.array[t+0]=e,this.array[t+1]=n,this}setXYZ(t,e,n,s){return t*=this.itemSize,this.normalized&&(e=Cn(e,this.array),n=Cn(n,this.array),s=Cn(s,this.array)),this.array[t+0]=e,this.array[t+1]=n,this.array[t+2]=s,this}setXYZW(t,e,n,s,r){return t*=this.itemSize,this.normalized&&(e=Cn(e,this.array),n=Cn(n,this.array),s=Cn(s,this.array),r=Cn(r,this.array)),this.array[t+0]=e,this.array[t+1]=n,this.array[t+2]=s,this.array[t+3]=r,this}onUpload(t){return this.onUploadCallback=t,this}clone(){return new this.constructor(this.array,this.itemSize).copy(this)}toJSON(){let t={itemSize:this.itemSize,type:this.array.constructor.name,array:Array.from(this.array),normalized:this.normalized};return this.name!==""&&(t.name=this.name),this.usage!==hu&&(t.usage=this.usage),t}};var fa=class extends Mn{constructor(t,e,n){super(new Uint16Array(t),e,n)}};var da=class extends Mn{constructor(t,e,n){super(new Uint32Array(t),e,n)}};var de=class extends Mn{constructor(t,e,n){super(new Float32Array(t),e,n)}};var Ep=0,Zn=new Ue,Tc=new An,qs=new O,zn=new Fi,Ir=new Fi,mn=new O,Ke=class i extends ns{constructor(){super(),this.isBufferGeometry=!0,Object.defineProperty(this,"id",{value:Ep++}),this.uuid=Is(),this.name="",this.type="BufferGeometry",this.index=null,this.attributes={},this.morphAttributes={},this.morphTargetsRelative=!1,this.groups=[],this.boundingBox=null,this.boundingSphere=null,this.drawRange={start:0,count:1/0},this.userData={}}getIndex(){return this.index}setIndex(t){return Array.isArray(t)?this.index=new(bf(t)?da:fa)(t,1):this.index=t,this}getAttribute(t){return this.attributes[t]}setAttribute(t,e){return this.attributes[t]=e,this}deleteAttribute(t){return delete this.attributes[t],this}hasAttribute(t){return this.attributes[t]!==void 0}addGroup(t,e,n=0){this.groups.push({start:t,count:e,materialIndex:n})}clearGroups(){this.groups=[]}setDrawRange(t,e){this.drawRange.start=t,this.drawRange.count=e}applyMatrix4(t){let e=this.attributes.position;e!==void 0&&(e.applyMatrix4(t),e.needsUpdate=!0);let n=this.attributes.normal;if(n!==void 0){let r=new we().getNormalMatrix(t);n.applyNormalMatrix(r),n.needsUpdate=!0}let s=this.attributes.tangent;return s!==void 0&&(s.transformDirection(t),s.needsUpdate=!0),this.boundingBox!==null&&this.computeBoundingBox(),this.boundingSphere!==null&&this.computeBoundingSphere(),this}applyQuaternion(t){return Zn.makeRotationFromQuaternion(t),this.applyMatrix4(Zn),this}rotateX(t){return Zn.makeRotationX(t),this.applyMatrix4(Zn),this}rotateY(t){return Zn.makeRotationY(t),this.applyMatrix4(Zn),this}rotateZ(t){return Zn.makeRotationZ(t),this.applyMatrix4(Zn),this}translate(t,e,n){return Zn.makeTranslation(t,e,n),this.applyMatrix4(Zn),this}scale(t,e,n){return Zn.makeScale(t,e,n),this.applyMatrix4(Zn),this}lookAt(t){return Tc.lookAt(t),Tc.updateMatrix(),this.applyMatrix4(Tc.matrix),this}center(){return this.computeBoundingBox(),this.boundingBox.getCenter(qs).negate(),this.translate(qs.x,qs.y,qs.z),this}setFromPoints(t){let e=[];for(let n=0,s=t.length;n<s;n++){let r=t[n];e.push(r.x,r.y,r.z||0)}return this.setAttribute("position",new de(e,3)),this}computeBoundingBox(){this.boundingBox===null&&(this.boundingBox=new Fi);let t=this.attributes.position,e=this.morphAttributes.position;if(t&&t.isGLBufferAttribute){console.error('THREE.BufferGeometry.computeBoundingBox(): GLBufferAttribute requires a manual bounding box. Alternatively set "mesh.frustumCulled" to "false".',this),this.boundingBox.set(new O(-1/0,-1/0,-1/0),new O(1/0,1/0,1/0));return}if(t!==void 0){if(this.boundingBox.setFromBufferAttribute(t),e)for(let n=0,s=e.length;n<s;n++){let r=e[n];zn.setFromBufferAttribute(r),this.morphTargetsRelative?(mn.addVectors(this.boundingBox.min,zn.min),this.boundingBox.expandByPoint(mn),mn.addVectors(this.boundingBox.max,zn.max),this.boundingBox.expandByPoint(mn)):(this.boundingBox.expandByPoint(zn.min),this.boundingBox.expandByPoint(zn.max))}}else this.boundingBox.makeEmpty();(isNaN(this.boundingBox.min.x)||isNaN(this.boundingBox.min.y)||isNaN(this.boundingBox.min.z))&&console.error('THREE.BufferGeometry.computeBoundingBox(): Computed min/max have NaN values. The "position" attribute is likely to have NaN values.',this)}computeBoundingSphere(){this.boundingSphere===null&&(this.boundingSphere=new is);let t=this.attributes.position,e=this.morphAttributes.position;if(t&&t.isGLBufferAttribute){console.error('THREE.BufferGeometry.computeBoundingSphere(): GLBufferAttribute requires a manual bounding sphere. Alternatively set "mesh.frustumCulled" to "false".',this),this.boundingSphere.set(new O,1/0);return}if(t){let n=this.boundingSphere.center;if(zn.setFromBufferAttribute(t),e)for(let r=0,a=e.length;r<a;r++){let o=e[r];Ir.setFromBufferAttribute(o),this.morphTargetsRelative?(mn.addVectors(zn.min,Ir.min),zn.expandByPoint(mn),mn.addVectors(zn.max,Ir.max),zn.expandByPoint(mn)):(zn.expandByPoint(Ir.min),zn.expandByPoint(Ir.max))}zn.getCenter(n);let s=0;for(let r=0,a=t.count;r<a;r++)mn.fromBufferAttribute(t,r),s=Math.max(s,n.distanceToSquared(mn));if(e)for(let r=0,a=e.length;r<a;r++){let o=e[r],c=this.morphTargetsRelative;for(let l=0,h=o.count;l<h;l++)mn.fromBufferAttribute(o,l),c&&(qs.fromBufferAttribute(t,l),mn.add(qs)),s=Math.max(s,n.distanceToSquared(mn))}this.boundingSphere.radius=Math.sqrt(s),isNaN(this.boundingSphere.radius)&&console.error('THREE.BufferGeometry.computeBoundingSphere(): Computed radius is NaN. The "position" attribute is likely to have NaN values.',this)}}computeTangents(){let t=this.index,e=this.attributes;if(t===null||e.position===void 0||e.normal===void 0||e.uv===void 0){console.error("THREE.BufferGeometry: .computeTangents() failed. Missing required attributes (index, position, normal or uv)");return}let n=t.array,s=e.position.array,r=e.normal.array,a=e.uv.array,o=s.length/3;this.hasAttribute("tangent")===!1&&this.setAttribute("tangent",new Mn(new Float32Array(4*o),4));let c=this.getAttribute("tangent").array,l=[],h=[];for(let L=0;L<o;L++)l[L]=new O,h[L]=new O;let f=new O,d=new O,p=new O,x=new St,S=new St,_=new St,m=new O,T=new O;function M(L,$,ot){f.fromArray(s,L*3),d.fromArray(s,$*3),p.fromArray(s,ot*3),x.fromArray(a,L*2),S.fromArray(a,$*2),_.fromArray(a,ot*2),d.sub(f),p.sub(f),S.sub(x),_.sub(x);let Mt=1/(S.x*_.y-_.x*S.y);isFinite(Mt)&&(m.copy(d).multiplyScalar(_.y).addScaledVector(p,-S.y).multiplyScalar(Mt),T.copy(p).multiplyScalar(S.x).addScaledVector(d,-_.x).multiplyScalar(Mt),l[L].add(m),l[$].add(m),l[ot].add(m),h[L].add(T),h[$].add(T),h[ot].add(T))}let U=this.groups;U.length===0&&(U=[{start:0,count:n.length}]);for(let L=0,$=U.length;L<$;++L){let ot=U[L],Mt=ot.start,X=ot.count;for(let K=Mt,tt=Mt+X;K<tt;K+=3)M(n[K+0],n[K+1],n[K+2])}let W=new O,F=new O,B=new O,J=new O;function w(L){B.fromArray(r,L*3),J.copy(B);let $=l[L];W.copy($),W.sub(B.multiplyScalar(B.dot($))).normalize(),F.crossVectors(J,$);let Mt=F.dot(h[L])<0?-1:1;c[L*4]=W.x,c[L*4+1]=W.y,c[L*4+2]=W.z,c[L*4+3]=Mt}for(let L=0,$=U.length;L<$;++L){let ot=U[L],Mt=ot.start,X=ot.count;for(let K=Mt,tt=Mt+X;K<tt;K+=3)w(n[K+0]),w(n[K+1]),w(n[K+2])}}computeVertexNormals(){let t=this.index,e=this.getAttribute("position");if(e!==void 0){let n=this.getAttribute("normal");if(n===void 0)n=new Mn(new Float32Array(e.count*3),3),this.setAttribute("normal",n);else for(let d=0,p=n.count;d<p;d++)n.setXYZ(d,0,0,0);let s=new O,r=new O,a=new O,o=new O,c=new O,l=new O,h=new O,f=new O;if(t)for(let d=0,p=t.count;d<p;d+=3){let x=t.getX(d+0),S=t.getX(d+1),_=t.getX(d+2);s.fromBufferAttribute(e,x),r.fromBufferAttribute(e,S),a.fromBufferAttribute(e,_),h.subVectors(a,r),f.subVectors(s,r),h.cross(f),o.fromBufferAttribute(n,x),c.fromBufferAttribute(n,S),l.fromBufferAttribute(n,_),o.add(h),c.add(h),l.add(h),n.setXYZ(x,o.x,o.y,o.z),n.setXYZ(S,c.x,c.y,c.z),n.setXYZ(_,l.x,l.y,l.z)}else for(let d=0,p=e.count;d<p;d+=3)s.fromBufferAttribute(e,d+0),r.fromBufferAttribute(e,d+1),a.fromBufferAttribute(e,d+2),h.subVectors(a,r),f.subVectors(s,r),h.cross(f),n.setXYZ(d+0,h.x,h.y,h.z),n.setXYZ(d+1,h.x,h.y,h.z),n.setXYZ(d+2,h.x,h.y,h.z);this.normalizeNormals(),n.needsUpdate=!0}}normalizeNormals(){let t=this.attributes.normal;for(let e=0,n=t.count;e<n;e++)mn.fromBufferAttribute(t,e),mn.normalize(),t.setXYZ(e,mn.x,mn.y,mn.z)}toNonIndexed(){function t(o,c){let l=o.array,h=o.itemSize,f=o.normalized,d=new l.constructor(c.length*h),p=0,x=0;for(let S=0,_=c.length;S<_;S++){o.isInterleavedBufferAttribute?p=c[S]*o.data.stride+o.offset:p=c[S]*h;for(let m=0;m<h;m++)d[x++]=l[p++]}return new Mn(d,h,f)}if(this.index===null)return console.warn("THREE.BufferGeometry.toNonIndexed(): BufferGeometry is already non-indexed."),this;let e=new i,n=this.index.array,s=this.attributes;for(let o in s){let c=s[o],l=t(c,n);e.setAttribute(o,l)}let r=this.morphAttributes;for(let o in r){let c=[],l=r[o];for(let h=0,f=l.length;h<f;h++){let d=l[h],p=t(d,n);c.push(p)}e.morphAttributes[o]=c}e.morphTargetsRelative=this.morphTargetsRelative;let a=this.groups;for(let o=0,c=a.length;o<c;o++){let l=a[o];e.addGroup(l.start,l.count,l.materialIndex)}return e}toJSON(){let t={metadata:{version:4.6,type:"BufferGeometry",generator:"BufferGeometry.toJSON"}};if(t.uuid=this.uuid,t.type=this.type,this.name!==""&&(t.name=this.name),Object.keys(this.userData).length>0&&(t.userData=this.userData),this.parameters!==void 0){let c=this.parameters;for(let l in c)c[l]!==void 0&&(t[l]=c[l]);return t}t.data={attributes:{}};let e=this.index;e!==null&&(t.data.index={type:e.array.constructor.name,array:Array.prototype.slice.call(e.array)});let n=this.attributes;for(let c in n){let l=n[c];t.data.attributes[c]=l.toJSON(t.data)}let s={},r=!1;for(let c in this.morphAttributes){let l=this.morphAttributes[c],h=[];for(let f=0,d=l.length;f<d;f++){let p=l[f];h.push(p.toJSON(t.data))}h.length>0&&(s[c]=h,r=!0)}r&&(t.data.morphAttributes=s,t.data.morphTargetsRelative=this.morphTargetsRelative);let a=this.groups;a.length>0&&(t.data.groups=JSON.parse(JSON.stringify(a)));let o=this.boundingSphere;return o!==null&&(t.data.boundingSphere={center:o.center.toArray(),radius:o.radius}),t}clone(){return new this.constructor().copy(this)}copy(t){this.index=null,this.attributes={},this.morphAttributes={},this.groups=[],this.boundingBox=null,this.boundingSphere=null;let e={};this.name=t.name;let n=t.index;n!==null&&this.setIndex(n.clone(e));let s=t.attributes;for(let l in s){let h=s[l];this.setAttribute(l,h.clone(e))}let r=t.morphAttributes;for(let l in r){let h=[],f=r[l];for(let d=0,p=f.length;d<p;d++)h.push(f[d].clone(e));this.morphAttributes[l]=h}this.morphTargetsRelative=t.morphTargetsRelative;let a=t.groups;for(let l=0,h=a.length;l<h;l++){let f=a[l];this.addGroup(f.start,f.count,f.materialIndex)}let o=t.boundingBox;o!==null&&(this.boundingBox=o.clone());let c=t.boundingSphere;return c!==null&&(this.boundingSphere=c.clone()),this.drawRange.start=t.drawRange.start,this.drawRange.count=t.drawRange.count,this.userData=t.userData,this}dispose(){this.dispatchEvent({type:"dispose"})}},Eu=new Ue,ms=new Xr,Oo=new is,wu=new O,Zs=new O,$s=new O,Js=new O,Ac=new O,Bo=new O,zo=new St,Ho=new St,ko=new St,Tu=new O,Au=new O,Ru=new O,Go=new O,Vo=new O,Ne=class extends An{constructor(t=new Ke,e=new Es){super(),this.isMesh=!0,this.type="Mesh",this.geometry=t,this.material=e,this.updateMorphTargets()}copy(t,e){return super.copy(t,e),t.morphTargetInfluences!==void 0&&(this.morphTargetInfluences=t.morphTargetInfluences.slice()),t.morphTargetDictionary!==void 0&&(this.morphTargetDictionary=Object.assign({},t.morphTargetDictionary)),this.material=Array.isArray(t.material)?t.material.slice():t.material,this.geometry=t.geometry,this}updateMorphTargets(){let e=this.geometry.morphAttributes,n=Object.keys(e);if(n.length>0){let s=e[n[0]];if(s!==void 0){this.morphTargetInfluences=[],this.morphTargetDictionary={};for(let r=0,a=s.length;r<a;r++){let o=s[r].name||String(r);this.morphTargetInfluences.push(0),this.morphTargetDictionary[o]=r}}}}getVertexPosition(t,e){let n=this.geometry,s=n.attributes.position,r=n.morphAttributes.position,a=n.morphTargetsRelative;e.fromBufferAttribute(s,t);let o=this.morphTargetInfluences;if(r&&o){Bo.set(0,0,0);for(let c=0,l=r.length;c<l;c++){let h=o[c],f=r[c];h!==0&&(Ac.fromBufferAttribute(f,t),a?Bo.addScaledVector(Ac,h):Bo.addScaledVector(Ac.sub(e),h))}e.add(Bo)}return e}raycast(t,e){let n=this.geometry,s=this.material,r=this.matrixWorld;s!==void 0&&(n.boundingSphere===null&&n.computeBoundingSphere(),Oo.copy(n.boundingSphere),Oo.applyMatrix4(r),ms.copy(t.ray).recast(t.near),!(Oo.containsPoint(ms.origin)===!1&&(ms.intersectSphere(Oo,wu)===null||ms.origin.distanceToSquared(wu)>(t.far-t.near)**2))&&(Eu.copy(r).invert(),ms.copy(t.ray).applyMatrix4(Eu),!(n.boundingBox!==null&&ms.intersectsBox(n.boundingBox)===!1)&&this._computeIntersections(t,e,ms)))}_computeIntersections(t,e,n){let s,r=this.geometry,a=this.material,o=r.index,c=r.attributes.position,l=r.attributes.uv,h=r.attributes.uv1,f=r.attributes.normal,d=r.groups,p=r.drawRange;if(o!==null)if(Array.isArray(a))for(let x=0,S=d.length;x<S;x++){let _=d[x],m=a[_.materialIndex],T=Math.max(_.start,p.start),M=Math.min(o.count,Math.min(_.start+_.count,p.start+p.count));for(let U=T,W=M;U<W;U+=3){let F=o.getX(U),B=o.getX(U+1),J=o.getX(U+2);s=Wo(this,m,t,n,l,h,f,F,B,J),s&&(s.faceIndex=Math.floor(U/3),s.face.materialIndex=_.materialIndex,e.push(s))}}else{let x=Math.max(0,p.start),S=Math.min(o.count,p.start+p.count);for(let _=x,m=S;_<m;_+=3){let T=o.getX(_),M=o.getX(_+1),U=o.getX(_+2);s=Wo(this,a,t,n,l,h,f,T,M,U),s&&(s.faceIndex=Math.floor(_/3),e.push(s))}}else if(c!==void 0)if(Array.isArray(a))for(let x=0,S=d.length;x<S;x++){let _=d[x],m=a[_.materialIndex],T=Math.max(_.start,p.start),M=Math.min(c.count,Math.min(_.start+_.count,p.start+p.count));for(let U=T,W=M;U<W;U+=3){let F=U,B=U+1,J=U+2;s=Wo(this,m,t,n,l,h,f,F,B,J),s&&(s.faceIndex=Math.floor(U/3),s.face.materialIndex=_.materialIndex,e.push(s))}}else{let x=Math.max(0,p.start),S=Math.min(c.count,p.start+p.count);for(let _=x,m=S;_<m;_+=3){let T=_,M=_+1,U=_+2;s=Wo(this,a,t,n,l,h,f,T,M,U),s&&(s.faceIndex=Math.floor(_/3),e.push(s))}}}};function wp(i,t,e,n,s,r,a,o){let c;if(t.side===Tn?c=n.intersectTriangle(a,r,s,!0,o):c=n.intersectTriangle(s,r,a,t.side===es,o),c===null)return null;Vo.copy(o),Vo.applyMatrix4(i.matrixWorld);let l=e.ray.origin.distanceTo(Vo);return l<e.near||l>e.far?null:{distance:l,point:Vo.clone(),object:i}}function Wo(i,t,e,n,s,r,a,o,c,l){i.getVertexPosition(o,Zs),i.getVertexPosition(c,$s),i.getVertexPosition(l,Js);let h=wp(i,t,e,n,Zs,$s,Js,Go);if(h){s&&(zo.fromBufferAttribute(s,o),Ho.fromBufferAttribute(s,c),ko.fromBufferAttribute(s,l),h.uv=nr.getInterpolation(Go,Zs,$s,Js,zo,Ho,ko,new St)),r&&(zo.fromBufferAttribute(r,o),Ho.fromBufferAttribute(r,c),ko.fromBufferAttribute(r,l),h.uv1=nr.getInterpolation(Go,Zs,$s,Js,zo,Ho,ko,new St),h.uv2=h.uv1),a&&(Tu.fromBufferAttribute(a,o),Au.fromBufferAttribute(a,c),Ru.fromBufferAttribute(a,l),h.normal=nr.getInterpolation(Go,Zs,$s,Js,Tu,Au,Ru,new O),h.normal.dot(n.direction)>0&&h.normal.multiplyScalar(-1));let f={a:o,b:c,c:l,normal:new O,materialIndex:0};nr.getNormal(Zs,$s,Js,f.normal),h.face=f}return h}var Pe=class i extends Ke{constructor(t=1,e=1,n=1,s=1,r=1,a=1){super(),this.type="BoxGeometry",this.parameters={width:t,height:e,depth:n,widthSegments:s,heightSegments:r,depthSegments:a};let o=this;s=Math.floor(s),r=Math.floor(r),a=Math.floor(a);let c=[],l=[],h=[],f=[],d=0,p=0;x("z","y","x",-1,-1,n,e,t,a,r,0),x("z","y","x",1,-1,n,e,-t,a,r,1),x("x","z","y",1,1,t,n,e,s,a,2),x("x","z","y",1,-1,t,n,-e,s,a,3),x("x","y","z",1,-1,t,e,n,s,r,4),x("x","y","z",-1,-1,t,e,-n,s,r,5),this.setIndex(c),this.setAttribute("position",new de(l,3)),this.setAttribute("normal",new de(h,3)),this.setAttribute("uv",new de(f,2));function x(S,_,m,T,M,U,W,F,B,J,w){let L=U/B,$=W/J,ot=U/2,Mt=W/2,X=F/2,K=B+1,tt=J+1,it=0,ft=0,nt=new O;for(let ct=0;ct<tt;ct++){let lt=ct*$-Mt;for(let Dt=0;Dt<K;Dt++){let st=Dt*L-ot;nt[S]=st*T,nt[_]=lt*M,nt[m]=X,l.push(nt.x,nt.y,nt.z),nt[S]=0,nt[_]=0,nt[m]=F>0?1:-1,h.push(nt.x,nt.y,nt.z),f.push(Dt/B),f.push(1-ct/J),it+=1}}for(let ct=0;ct<J;ct++)for(let lt=0;lt<B;lt++){let Dt=d+lt+K*ct,st=d+lt+K*(ct+1),ut=d+(lt+1)+K*(ct+1),Nt=d+(lt+1)+K*ct;c.push(Dt,st,Nt),c.push(st,ut,Nt),ft+=6}o.addGroup(p,ft,w),p+=ft,d+=it}}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.width,t.height,t.depth,t.widthSegments,t.heightSegments,t.depthSegments)}};function pr(i){let t={};for(let e in i){t[e]={};for(let n in i[e]){let s=i[e][n];s&&(s.isColor||s.isMatrix3||s.isMatrix4||s.isVector2||s.isVector3||s.isVector4||s.isTexture||s.isQuaternion)?s.isRenderTargetTexture?(console.warn("UniformsUtils: Textures of render targets cannot be cloned via cloneUniforms() or mergeUniforms()."),t[e][n]=null):t[e][n]=s.clone():Array.isArray(s)?t[e][n]=s.slice():t[e][n]=s}}return t}function Pn(i){let t={};for(let e=0;e<i.length;e++){let n=pr(i[e]);for(let s in n)t[s]=n[s]}return t}function Tp(i){let t=[];for(let e=0;e<i.length;e++)t.push(i[e].clone());return t}function wf(i){return i.getRenderTarget()===null?i.outputColorSpace:Be.workingColorSpace}var Fl={clone:pr,merge:Pn},Ap=`void main() {
	gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );
}`,Rp=`void main() {
	gl_FragColor = vec4( 1.0, 0.0, 0.0, 1.0 );
}`,Sn=class extends yi{constructor(t){super(),this.isShaderMaterial=!0,this.type="ShaderMaterial",this.defines={},this.uniforms={},this.uniformsGroups=[],this.vertexShader=Ap,this.fragmentShader=Rp,this.linewidth=1,this.wireframe=!1,this.wireframeLinewidth=1,this.fog=!1,this.lights=!1,this.clipping=!1,this.forceSinglePass=!0,this.extensions={derivatives:!1,fragDepth:!1,drawBuffers:!1,shaderTextureLOD:!1,clipCullDistance:!1},this.defaultAttributeValues={color:[1,1,1],uv:[0,0],uv1:[0,0]},this.index0AttributeName=void 0,this.uniformsNeedUpdate=!1,this.glslVersion=null,t!==void 0&&this.setValues(t)}copy(t){return super.copy(t),this.fragmentShader=t.fragmentShader,this.vertexShader=t.vertexShader,this.uniforms=pr(t.uniforms),this.uniformsGroups=Tp(t.uniformsGroups),this.defines=Object.assign({},t.defines),this.wireframe=t.wireframe,this.wireframeLinewidth=t.wireframeLinewidth,this.fog=t.fog,this.lights=t.lights,this.clipping=t.clipping,this.extensions=Object.assign({},t.extensions),this.glslVersion=t.glslVersion,this}toJSON(t){let e=super.toJSON(t);e.glslVersion=this.glslVersion,e.uniforms={};for(let s in this.uniforms){let a=this.uniforms[s].value;a&&a.isTexture?e.uniforms[s]={type:"t",value:a.toJSON(t).uuid}:a&&a.isColor?e.uniforms[s]={type:"c",value:a.getHex()}:a&&a.isVector2?e.uniforms[s]={type:"v2",value:a.toArray()}:a&&a.isVector3?e.uniforms[s]={type:"v3",value:a.toArray()}:a&&a.isVector4?e.uniforms[s]={type:"v4",value:a.toArray()}:a&&a.isMatrix3?e.uniforms[s]={type:"m3",value:a.toArray()}:a&&a.isMatrix4?e.uniforms[s]={type:"m4",value:a.toArray()}:e.uniforms[s]={value:a}}Object.keys(this.defines).length>0&&(e.defines=this.defines),e.vertexShader=this.vertexShader,e.fragmentShader=this.fragmentShader,e.lights=this.lights,e.clipping=this.clipping;let n={};for(let s in this.extensions)this.extensions[s]===!0&&(n[s]=!0);return Object.keys(n).length>0&&(e.extensions=n),e}},pa=class extends An{constructor(){super(),this.isCamera=!0,this.type="Camera",this.matrixWorldInverse=new Ue,this.projectionMatrix=new Ue,this.projectionMatrixInverse=new Ue,this.coordinateSystem=Ui}copy(t,e){return super.copy(t,e),this.matrixWorldInverse.copy(t.matrixWorldInverse),this.projectionMatrix.copy(t.projectionMatrix),this.projectionMatrixInverse.copy(t.projectionMatrixInverse),this.coordinateSystem=t.coordinateSystem,this}getWorldDirection(t){return super.getWorldDirection(t).negate()}updateMatrixWorld(t){super.updateMatrixWorld(t),this.matrixWorldInverse.copy(this.matrixWorld).invert()}updateWorldMatrix(t,e){super.updateWorldMatrix(t,e),this.matrixWorldInverse.copy(this.matrixWorld).invert()}clone(){return new this.constructor().copy(this)}},wn=class extends pa{constructor(t=50,e=1,n=.1,s=2e3){super(),this.isPerspectiveCamera=!0,this.type="PerspectiveCamera",this.fov=t,this.zoom=1,this.near=n,this.far=s,this.focus=10,this.aspect=e,this.view=null,this.filmGauge=35,this.filmOffset=0,this.updateProjectionMatrix()}copy(t,e){return super.copy(t,e),this.fov=t.fov,this.zoom=t.zoom,this.near=t.near,this.far=t.far,this.focus=t.focus,this.aspect=t.aspect,this.view=t.view===null?null:Object.assign({},t.view),this.filmGauge=t.filmGauge,this.filmOffset=t.filmOffset,this}setFocalLength(t){let e=.5*this.getFilmHeight()/t;this.fov=Vr*2*Math.atan(e),this.updateProjectionMatrix()}getFocalLength(){let t=Math.tan(Nr*.5*this.fov);return .5*this.getFilmHeight()/t}getEffectiveFOV(){return Vr*2*Math.atan(Math.tan(Nr*.5*this.fov)/this.zoom)}getFilmWidth(){return this.filmGauge*Math.min(this.aspect,1)}getFilmHeight(){return this.filmGauge/Math.max(this.aspect,1)}setViewOffset(t,e,n,s,r,a){this.aspect=t/e,this.view===null&&(this.view={enabled:!0,fullWidth:1,fullHeight:1,offsetX:0,offsetY:0,width:1,height:1}),this.view.enabled=!0,this.view.fullWidth=t,this.view.fullHeight=e,this.view.offsetX=n,this.view.offsetY=s,this.view.width=r,this.view.height=a,this.updateProjectionMatrix()}clearViewOffset(){this.view!==null&&(this.view.enabled=!1),this.updateProjectionMatrix()}updateProjectionMatrix(){let t=this.near,e=t*Math.tan(Nr*.5*this.fov)/this.zoom,n=2*e,s=this.aspect*n,r=-.5*s,a=this.view;if(this.view!==null&&this.view.enabled){let c=a.fullWidth,l=a.fullHeight;r+=a.offsetX*s/c,e-=a.offsetY*n/l,s*=a.width/c,n*=a.height/l}let o=this.filmOffset;o!==0&&(r+=t*o/this.getFilmWidth()),this.projectionMatrix.makePerspective(r,r+s,e,e-n,t,this.far,this.coordinateSystem),this.projectionMatrixInverse.copy(this.projectionMatrix).invert()}toJSON(t){let e=super.toJSON(t);return e.object.fov=this.fov,e.object.zoom=this.zoom,e.object.near=this.near,e.object.far=this.far,e.object.focus=this.focus,e.object.aspect=this.aspect,this.view!==null&&(e.object.view=Object.assign({},this.view)),e.object.filmGauge=this.filmGauge,e.object.filmOffset=this.filmOffset,e}},Ks=-90,js=1,Zc=class extends An{constructor(t,e,n){super(),this.type="CubeCamera",this.renderTarget=n,this.coordinateSystem=null,this.activeMipmapLevel=0;let s=new wn(Ks,js,t,e);s.layers=this.layers,this.add(s);let r=new wn(Ks,js,t,e);r.layers=this.layers,this.add(r);let a=new wn(Ks,js,t,e);a.layers=this.layers,this.add(a);let o=new wn(Ks,js,t,e);o.layers=this.layers,this.add(o);let c=new wn(Ks,js,t,e);c.layers=this.layers,this.add(c);let l=new wn(Ks,js,t,e);l.layers=this.layers,this.add(l)}updateCoordinateSystem(){let t=this.coordinateSystem,e=this.children.concat(),[n,s,r,a,o,c]=e;for(let l of e)this.remove(l);if(t===Ui)n.up.set(0,1,0),n.lookAt(1,0,0),s.up.set(0,1,0),s.lookAt(-1,0,0),r.up.set(0,0,-1),r.lookAt(0,1,0),a.up.set(0,0,1),a.lookAt(0,-1,0),o.up.set(0,1,0),o.lookAt(0,0,1),c.up.set(0,1,0),c.lookAt(0,0,-1);else if(t===aa)n.up.set(0,-1,0),n.lookAt(-1,0,0),s.up.set(0,-1,0),s.lookAt(1,0,0),r.up.set(0,0,1),r.lookAt(0,1,0),a.up.set(0,0,-1),a.lookAt(0,-1,0),o.up.set(0,-1,0),o.lookAt(0,0,1),c.up.set(0,-1,0),c.lookAt(0,0,-1);else throw new Error("THREE.CubeCamera.updateCoordinateSystem(): Invalid coordinate system: "+t);for(let l of e)this.add(l),l.updateMatrixWorld()}update(t,e){this.parent===null&&this.updateMatrixWorld();let{renderTarget:n,activeMipmapLevel:s}=this;this.coordinateSystem!==t.coordinateSystem&&(this.coordinateSystem=t.coordinateSystem,this.updateCoordinateSystem());let[r,a,o,c,l,h]=this.children,f=t.getRenderTarget(),d=t.getActiveCubeFace(),p=t.getActiveMipmapLevel(),x=t.xr.enabled;t.xr.enabled=!1;let S=n.texture.generateMipmaps;n.texture.generateMipmaps=!1,t.setRenderTarget(n,0,s),t.render(e,r),t.setRenderTarget(n,1,s),t.render(e,a),t.setRenderTarget(n,2,s),t.render(e,o),t.setRenderTarget(n,3,s),t.render(e,c),t.setRenderTarget(n,4,s),t.render(e,l),n.texture.generateMipmaps=S,t.setRenderTarget(n,5,s),t.render(e,h),t.setRenderTarget(f,d,p),t.xr.enabled=x,n.texture.needsPMREMUpdate=!0}},ma=class extends Hn{constructor(t,e,n,s,r,a,o,c,l,h){t=t!==void 0?t:[],e=e!==void 0?e:ur,super(t,e,n,s,r,a,o,c,l,h),this.isCubeTexture=!0,this.flipY=!1}get images(){return this.image}set images(t){this.image=t}},$c=class extends Ni{constructor(t=1,e={}){super(t,t,e),this.isWebGLCubeRenderTarget=!0;let n={width:t,height:t,depth:1},s=[n,n,n,n,n,n];e.encoding!==void 0&&(Or("THREE.WebGLCubeRenderTarget: option.encoding has been replaced by option.colorSpace."),e.colorSpace=e.encoding===Ss?sn:Jn),this.texture=new ma(s,e.mapping,e.wrapS,e.wrapT,e.magFilter,e.minFilter,e.format,e.type,e.anisotropy,e.colorSpace),this.texture.isRenderTargetTexture=!0,this.texture.generateMipmaps=e.generateMipmaps!==void 0?e.generateMipmaps:!1,this.texture.minFilter=e.minFilter!==void 0?e.minFilter:$n}fromEquirectangularTexture(t,e){this.texture.type=e.type,this.texture.colorSpace=e.colorSpace,this.texture.generateMipmaps=e.generateMipmaps,this.texture.minFilter=e.minFilter,this.texture.magFilter=e.magFilter;let n={uniforms:{tEquirect:{value:null}},vertexShader:`

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
			`},s=new Pe(5,5,5),r=new Sn({name:"CubemapFromEquirect",uniforms:pr(n.uniforms),vertexShader:n.vertexShader,fragmentShader:n.fragmentShader,side:Tn,blending:Ki});r.uniforms.tEquirect.value=e;let a=new Ne(s,r),o=e.minFilter;return e.minFilter===kr&&(e.minFilter=$n),new Zc(1,10,this).update(t,a),e.minFilter=o,a.geometry.dispose(),a.material.dispose(),this}clear(t,e,n,s){let r=t.getRenderTarget();for(let a=0;a<6;a++)t.setRenderTarget(this,a),t.clear(e,n,s);t.setRenderTarget(r)}},Rc=new O,Cp=new O,Pp=new we,Li=class{constructor(t=new O(1,0,0),e=0){this.isPlane=!0,this.normal=t,this.constant=e}set(t,e){return this.normal.copy(t),this.constant=e,this}setComponents(t,e,n,s){return this.normal.set(t,e,n),this.constant=s,this}setFromNormalAndCoplanarPoint(t,e){return this.normal.copy(t),this.constant=-e.dot(this.normal),this}setFromCoplanarPoints(t,e,n){let s=Rc.subVectors(n,e).cross(Cp.subVectors(t,e)).normalize();return this.setFromNormalAndCoplanarPoint(s,t),this}copy(t){return this.normal.copy(t.normal),this.constant=t.constant,this}normalize(){let t=1/this.normal.length();return this.normal.multiplyScalar(t),this.constant*=t,this}negate(){return this.constant*=-1,this.normal.negate(),this}distanceToPoint(t){return this.normal.dot(t)+this.constant}distanceToSphere(t){return this.distanceToPoint(t.center)-t.radius}projectPoint(t,e){return e.copy(t).addScaledVector(this.normal,-this.distanceToPoint(t))}intersectLine(t,e){let n=t.delta(Rc),s=this.normal.dot(n);if(s===0)return this.distanceToPoint(t.start)===0?e.copy(t.start):null;let r=-(t.start.dot(this.normal)+this.constant)/s;return r<0||r>1?null:e.copy(t.start).addScaledVector(n,r)}intersectsLine(t){let e=this.distanceToPoint(t.start),n=this.distanceToPoint(t.end);return e<0&&n>0||n<0&&e>0}intersectsBox(t){return t.intersectsPlane(this)}intersectsSphere(t){return t.intersectsPlane(this)}coplanarPoint(t){return t.copy(this.normal).multiplyScalar(-this.constant)}applyMatrix4(t,e){let n=e||Pp.getNormalMatrix(t),s=this.coplanarPoint(Rc).applyMatrix4(t),r=this.normal.applyMatrix3(n).normalize();return this.constant=-s.dot(r),this}translate(t){return this.constant-=t.dot(this.normal),this}equals(t){return t.normal.equals(this.normal)&&t.constant===this.constant}clone(){return new this.constructor().copy(this)}},gs=new is,Xo=new O,qr=class{constructor(t=new Li,e=new Li,n=new Li,s=new Li,r=new Li,a=new Li){this.planes=[t,e,n,s,r,a]}set(t,e,n,s,r,a){let o=this.planes;return o[0].copy(t),o[1].copy(e),o[2].copy(n),o[3].copy(s),o[4].copy(r),o[5].copy(a),this}copy(t){let e=this.planes;for(let n=0;n<6;n++)e[n].copy(t.planes[n]);return this}setFromProjectionMatrix(t,e=Ui){let n=this.planes,s=t.elements,r=s[0],a=s[1],o=s[2],c=s[3],l=s[4],h=s[5],f=s[6],d=s[7],p=s[8],x=s[9],S=s[10],_=s[11],m=s[12],T=s[13],M=s[14],U=s[15];if(n[0].setComponents(c-r,d-l,_-p,U-m).normalize(),n[1].setComponents(c+r,d+l,_+p,U+m).normalize(),n[2].setComponents(c+a,d+h,_+x,U+T).normalize(),n[3].setComponents(c-a,d-h,_-x,U-T).normalize(),n[4].setComponents(c-o,d-f,_-S,U-M).normalize(),e===Ui)n[5].setComponents(c+o,d+f,_+S,U+M).normalize();else if(e===aa)n[5].setComponents(o,f,S,M).normalize();else throw new Error("THREE.Frustum.setFromProjectionMatrix(): Invalid coordinate system: "+e);return this}intersectsObject(t){if(t.boundingSphere!==void 0)t.boundingSphere===null&&t.computeBoundingSphere(),gs.copy(t.boundingSphere).applyMatrix4(t.matrixWorld);else{let e=t.geometry;e.boundingSphere===null&&e.computeBoundingSphere(),gs.copy(e.boundingSphere).applyMatrix4(t.matrixWorld)}return this.intersectsSphere(gs)}intersectsSprite(t){return gs.center.set(0,0,0),gs.radius=.7071067811865476,gs.applyMatrix4(t.matrixWorld),this.intersectsSphere(gs)}intersectsSphere(t){let e=this.planes,n=t.center,s=-t.radius;for(let r=0;r<6;r++)if(e[r].distanceToPoint(n)<s)return!1;return!0}intersectsBox(t){let e=this.planes;for(let n=0;n<6;n++){let s=e[n];if(Xo.x=s.normal.x>0?t.max.x:t.min.x,Xo.y=s.normal.y>0?t.max.y:t.min.y,Xo.z=s.normal.z>0?t.max.z:t.min.z,s.distanceToPoint(Xo)<0)return!1}return!0}containsPoint(t){let e=this.planes;for(let n=0;n<6;n++)if(e[n].distanceToPoint(t)<0)return!1;return!0}clone(){return new this.constructor().copy(this)}};function Tf(){let i=null,t=!1,e=null,n=null;function s(r,a){e(r,a),n=i.requestAnimationFrame(s)}return{start:function(){t!==!0&&e!==null&&(n=i.requestAnimationFrame(s),t=!0)},stop:function(){i.cancelAnimationFrame(n),t=!1},setAnimationLoop:function(r){e=r},setContext:function(r){i=r}}}function Ip(i,t){let e=t.isWebGL2,n=new WeakMap;function s(l,h){let f=l.array,d=l.usage,p=f.byteLength,x=i.createBuffer();i.bindBuffer(h,x),i.bufferData(h,f,d),l.onUploadCallback();let S;if(f instanceof Float32Array)S=i.FLOAT;else if(f instanceof Uint16Array)if(l.isFloat16BufferAttribute)if(e)S=i.HALF_FLOAT;else throw new Error("THREE.WebGLAttributes: Usage of Float16BufferAttribute requires WebGL2.");else S=i.UNSIGNED_SHORT;else if(f instanceof Int16Array)S=i.SHORT;else if(f instanceof Uint32Array)S=i.UNSIGNED_INT;else if(f instanceof Int32Array)S=i.INT;else if(f instanceof Int8Array)S=i.BYTE;else if(f instanceof Uint8Array)S=i.UNSIGNED_BYTE;else if(f instanceof Uint8ClampedArray)S=i.UNSIGNED_BYTE;else throw new Error("THREE.WebGLAttributes: Unsupported buffer data format: "+f);return{buffer:x,type:S,bytesPerElement:f.BYTES_PER_ELEMENT,version:l.version,size:p}}function r(l,h,f){let d=h.array,p=h._updateRange,x=h.updateRanges;if(i.bindBuffer(f,l),p.count===-1&&x.length===0&&i.bufferSubData(f,0,d),x.length!==0){for(let S=0,_=x.length;S<_;S++){let m=x[S];e?i.bufferSubData(f,m.start*d.BYTES_PER_ELEMENT,d,m.start,m.count):i.bufferSubData(f,m.start*d.BYTES_PER_ELEMENT,d.subarray(m.start,m.start+m.count))}h.clearUpdateRanges()}p.count!==-1&&(e?i.bufferSubData(f,p.offset*d.BYTES_PER_ELEMENT,d,p.offset,p.count):i.bufferSubData(f,p.offset*d.BYTES_PER_ELEMENT,d.subarray(p.offset,p.offset+p.count)),p.count=-1),h.onUploadCallback()}function a(l){return l.isInterleavedBufferAttribute&&(l=l.data),n.get(l)}function o(l){l.isInterleavedBufferAttribute&&(l=l.data);let h=n.get(l);h&&(i.deleteBuffer(h.buffer),n.delete(l))}function c(l,h){if(l.isGLBufferAttribute){let d=n.get(l);(!d||d.version<l.version)&&n.set(l,{buffer:l.buffer,type:l.type,bytesPerElement:l.elementSize,version:l.version});return}l.isInterleavedBufferAttribute&&(l=l.data);let f=n.get(l);if(f===void 0)n.set(l,s(l,h));else if(f.version<l.version){if(f.size!==l.array.byteLength)throw new Error("THREE.WebGLAttributes: The size of the buffer attribute's array buffer does not match the original size. Resizing buffer attributes is not supported.");r(f.buffer,l,h),f.version=l.version}}return{get:a,remove:o,update:c}}var _n=class i extends Ke{constructor(t=1,e=1,n=1,s=1){super(),this.type="PlaneGeometry",this.parameters={width:t,height:e,widthSegments:n,heightSegments:s};let r=t/2,a=e/2,o=Math.floor(n),c=Math.floor(s),l=o+1,h=c+1,f=t/o,d=e/c,p=[],x=[],S=[],_=[];for(let m=0;m<h;m++){let T=m*d-a;for(let M=0;M<l;M++){let U=M*f-r;x.push(U,-T,0),S.push(0,0,1),_.push(M/o),_.push(1-m/c)}}for(let m=0;m<c;m++)for(let T=0;T<o;T++){let M=T+l*m,U=T+l*(m+1),W=T+1+l*(m+1),F=T+1+l*m;p.push(M,U,F),p.push(U,W,F)}this.setIndex(p),this.setAttribute("position",new de(x,3)),this.setAttribute("normal",new de(S,3)),this.setAttribute("uv",new de(_,2))}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.width,t.height,t.widthSegments,t.heightSegments)}},Lp=`#ifdef USE_ALPHAHASH
	if ( diffuseColor.a < getAlphaHashThreshold( vPosition ) ) discard;
#endif`,Up=`#ifdef USE_ALPHAHASH
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
#endif`,Dp=`#ifdef USE_ALPHAMAP
	diffuseColor.a *= texture2D( alphaMap, vAlphaMapUv ).g;
#endif`,Np=`#ifdef USE_ALPHAMAP
	uniform sampler2D alphaMap;
#endif`,Fp=`#ifdef USE_ALPHATEST
	if ( diffuseColor.a < alphaTest ) discard;
#endif`,Op=`#ifdef USE_ALPHATEST
	uniform float alphaTest;
#endif`,Bp=`#ifdef USE_AOMAP
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
#endif`,zp=`#ifdef USE_AOMAP
	uniform sampler2D aoMap;
	uniform float aoMapIntensity;
#endif`,Hp=`#ifdef USE_BATCHING
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
#endif`,kp=`#ifdef USE_BATCHING
	mat4 batchingMatrix = getBatchingMatrix( batchId );
#endif`,Gp=`vec3 transformed = vec3( position );
#ifdef USE_ALPHAHASH
	vPosition = vec3( position );
#endif`,Vp=`vec3 objectNormal = vec3( normal );
#ifdef USE_TANGENT
	vec3 objectTangent = vec3( tangent.xyz );
#endif`,Wp=`float G_BlinnPhong_Implicit( ) {
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
} // validated`,Xp=`#ifdef USE_IRIDESCENCE
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
#endif`,Yp=`#ifdef USE_BUMPMAP
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
#endif`,qp=`#if NUM_CLIPPING_PLANES > 0
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
#endif`,Zp=`#if NUM_CLIPPING_PLANES > 0
	varying vec3 vClipPosition;
	uniform vec4 clippingPlanes[ NUM_CLIPPING_PLANES ];
#endif`,$p=`#if NUM_CLIPPING_PLANES > 0
	varying vec3 vClipPosition;
#endif`,Jp=`#if NUM_CLIPPING_PLANES > 0
	vClipPosition = - mvPosition.xyz;
#endif`,Kp=`#if defined( USE_COLOR_ALPHA )
	diffuseColor *= vColor;
#elif defined( USE_COLOR )
	diffuseColor.rgb *= vColor;
#endif`,jp=`#if defined( USE_COLOR_ALPHA )
	varying vec4 vColor;
#elif defined( USE_COLOR )
	varying vec3 vColor;
#endif`,Qp=`#if defined( USE_COLOR_ALPHA )
	varying vec4 vColor;
#elif defined( USE_COLOR ) || defined( USE_INSTANCING_COLOR )
	varying vec3 vColor;
#endif`,tm=`#if defined( USE_COLOR_ALPHA )
	vColor = vec4( 1.0 );
#elif defined( USE_COLOR ) || defined( USE_INSTANCING_COLOR )
	vColor = vec3( 1.0 );
#endif
#ifdef USE_COLOR
	vColor *= color;
#endif
#ifdef USE_INSTANCING_COLOR
	vColor.xyz *= instanceColor.xyz;
#endif`,em=`#define PI 3.141592653589793
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
} // validated`,nm=`#ifdef ENVMAP_TYPE_CUBE_UV
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
#endif`,im=`vec3 transformedNormal = objectNormal;
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
#endif`,sm=`#ifdef USE_DISPLACEMENTMAP
	uniform sampler2D displacementMap;
	uniform float displacementScale;
	uniform float displacementBias;
#endif`,rm=`#ifdef USE_DISPLACEMENTMAP
	transformed += normalize( objectNormal ) * ( texture2D( displacementMap, vDisplacementMapUv ).x * displacementScale + displacementBias );
#endif`,om=`#ifdef USE_EMISSIVEMAP
	vec4 emissiveColor = texture2D( emissiveMap, vEmissiveMapUv );
	totalEmissiveRadiance *= emissiveColor.rgb;
#endif`,am=`#ifdef USE_EMISSIVEMAP
	uniform sampler2D emissiveMap;
#endif`,cm="gl_FragColor = linearToOutputTexel( gl_FragColor );",lm=`
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
}`,hm=`#ifdef USE_ENVMAP
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
#endif`,um=`#ifdef USE_ENVMAP
	uniform float envMapIntensity;
	uniform float flipEnvMap;
	#ifdef ENVMAP_TYPE_CUBE
		uniform samplerCube envMap;
	#else
		uniform sampler2D envMap;
	#endif
	
#endif`,fm=`#ifdef USE_ENVMAP
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
#endif`,dm=`#ifdef USE_ENVMAP
	#if defined( USE_BUMPMAP ) || defined( USE_NORMALMAP ) || defined( PHONG ) || defined( LAMBERT )
		#define ENV_WORLDPOS
	#endif
	#ifdef ENV_WORLDPOS
		
		varying vec3 vWorldPosition;
	#else
		varying vec3 vReflect;
		uniform float refractionRatio;
	#endif
#endif`,pm=`#ifdef USE_ENVMAP
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
#endif`,mm=`#ifdef USE_FOG
	vFogDepth = - mvPosition.z;
#endif`,gm=`#ifdef USE_FOG
	varying float vFogDepth;
#endif`,_m=`#ifdef USE_FOG
	#ifdef FOG_EXP2
		float fogFactor = 1.0 - exp( - fogDensity * fogDensity * vFogDepth * vFogDepth );
	#else
		float fogFactor = smoothstep( fogNear, fogFar, vFogDepth );
	#endif
	gl_FragColor.rgb = mix( gl_FragColor.rgb, fogColor, fogFactor );
#endif`,xm=`#ifdef USE_FOG
	uniform vec3 fogColor;
	varying float vFogDepth;
	#ifdef FOG_EXP2
		uniform float fogDensity;
	#else
		uniform float fogNear;
		uniform float fogFar;
	#endif
#endif`,vm=`#ifdef USE_GRADIENTMAP
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
}`,ym=`#ifdef USE_LIGHTMAP
	vec4 lightMapTexel = texture2D( lightMap, vLightMapUv );
	vec3 lightMapIrradiance = lightMapTexel.rgb * lightMapIntensity;
	reflectedLight.indirectDiffuse += lightMapIrradiance;
#endif`,Mm=`#ifdef USE_LIGHTMAP
	uniform sampler2D lightMap;
	uniform float lightMapIntensity;
#endif`,Sm=`LambertMaterial material;
material.diffuseColor = diffuseColor.rgb;
material.specularStrength = specularStrength;`,bm=`varying vec3 vViewPosition;
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
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Lambert`,Em=`uniform bool receiveShadow;
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
#endif`,wm=`#ifdef USE_ENVMAP
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
#endif`,Tm=`ToonMaterial material;
material.diffuseColor = diffuseColor.rgb;`,Am=`varying vec3 vViewPosition;
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
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Toon`,Rm=`BlinnPhongMaterial material;
material.diffuseColor = diffuseColor.rgb;
material.specularColor = specular;
material.specularShininess = shininess;
material.specularStrength = specularStrength;`,Cm=`varying vec3 vViewPosition;
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
#define RE_IndirectDiffuse		RE_IndirectDiffuse_BlinnPhong`,Pm=`PhysicalMaterial material;
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
#endif`,Im=`struct PhysicalMaterial {
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
}`,Lm=`
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
#endif`,Um=`#if defined( RE_IndirectDiffuse )
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
#endif`,Dm=`#if defined( RE_IndirectDiffuse )
	RE_IndirectDiffuse( irradiance, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
#endif
#if defined( RE_IndirectSpecular )
	RE_IndirectSpecular( radiance, iblIrradiance, clearcoatRadiance, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
#endif`,Nm=`#if defined( USE_LOGDEPTHBUF ) && defined( USE_LOGDEPTHBUF_EXT )
	gl_FragDepthEXT = vIsPerspective == 0.0 ? gl_FragCoord.z : log2( vFragDepth ) * logDepthBufFC * 0.5;
#endif`,Fm=`#if defined( USE_LOGDEPTHBUF ) && defined( USE_LOGDEPTHBUF_EXT )
	uniform float logDepthBufFC;
	varying float vFragDepth;
	varying float vIsPerspective;
#endif`,Om=`#ifdef USE_LOGDEPTHBUF
	#ifdef USE_LOGDEPTHBUF_EXT
		varying float vFragDepth;
		varying float vIsPerspective;
	#else
		uniform float logDepthBufFC;
	#endif
#endif`,Bm=`#ifdef USE_LOGDEPTHBUF
	#ifdef USE_LOGDEPTHBUF_EXT
		vFragDepth = 1.0 + gl_Position.w;
		vIsPerspective = float( isPerspectiveMatrix( projectionMatrix ) );
	#else
		if ( isPerspectiveMatrix( projectionMatrix ) ) {
			gl_Position.z = log2( max( EPSILON, gl_Position.w + 1.0 ) ) * logDepthBufFC - 1.0;
			gl_Position.z *= gl_Position.w;
		}
	#endif
#endif`,zm=`#ifdef USE_MAP
	vec4 sampledDiffuseColor = texture2D( map, vMapUv );
	#ifdef DECODE_VIDEO_TEXTURE
		sampledDiffuseColor = vec4( mix( pow( sampledDiffuseColor.rgb * 0.9478672986 + vec3( 0.0521327014 ), vec3( 2.4 ) ), sampledDiffuseColor.rgb * 0.0773993808, vec3( lessThanEqual( sampledDiffuseColor.rgb, vec3( 0.04045 ) ) ) ), sampledDiffuseColor.w );
	
	#endif
	diffuseColor *= sampledDiffuseColor;
#endif`,Hm=`#ifdef USE_MAP
	uniform sampler2D map;
#endif`,km=`#if defined( USE_MAP ) || defined( USE_ALPHAMAP )
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
#endif`,Gm=`#if defined( USE_POINTS_UV )
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
#endif`,Vm=`float metalnessFactor = metalness;
#ifdef USE_METALNESSMAP
	vec4 texelMetalness = texture2D( metalnessMap, vMetalnessMapUv );
	metalnessFactor *= texelMetalness.b;
#endif`,Wm=`#ifdef USE_METALNESSMAP
	uniform sampler2D metalnessMap;
#endif`,Xm=`#if defined( USE_MORPHCOLORS ) && defined( MORPHTARGETS_TEXTURE )
	vColor *= morphTargetBaseInfluence;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		#if defined( USE_COLOR_ALPHA )
			if ( morphTargetInfluences[ i ] != 0.0 ) vColor += getMorph( gl_VertexID, i, 2 ) * morphTargetInfluences[ i ];
		#elif defined( USE_COLOR )
			if ( morphTargetInfluences[ i ] != 0.0 ) vColor += getMorph( gl_VertexID, i, 2 ).rgb * morphTargetInfluences[ i ];
		#endif
	}
#endif`,Ym=`#ifdef USE_MORPHNORMALS
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
#endif`,qm=`#ifdef USE_MORPHTARGETS
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
#endif`,Zm=`#ifdef USE_MORPHTARGETS
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
#endif`,$m=`float faceDirection = gl_FrontFacing ? 1.0 : - 1.0;
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
vec3 nonPerturbedNormal = normal;`,Jm=`#ifdef USE_NORMALMAP_OBJECTSPACE
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
#endif`,Km=`#ifndef FLAT_SHADED
	varying vec3 vNormal;
	#ifdef USE_TANGENT
		varying vec3 vTangent;
		varying vec3 vBitangent;
	#endif
#endif`,jm=`#ifndef FLAT_SHADED
	varying vec3 vNormal;
	#ifdef USE_TANGENT
		varying vec3 vTangent;
		varying vec3 vBitangent;
	#endif
#endif`,Qm=`#ifndef FLAT_SHADED
	vNormal = normalize( transformedNormal );
	#ifdef USE_TANGENT
		vTangent = normalize( transformedTangent );
		vBitangent = normalize( cross( vNormal, vTangent ) * tangent.w );
	#endif
#endif`,t0=`#ifdef USE_NORMALMAP
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
#endif`,e0=`#ifdef USE_CLEARCOAT
	vec3 clearcoatNormal = nonPerturbedNormal;
#endif`,n0=`#ifdef USE_CLEARCOAT_NORMALMAP
	vec3 clearcoatMapN = texture2D( clearcoatNormalMap, vClearcoatNormalMapUv ).xyz * 2.0 - 1.0;
	clearcoatMapN.xy *= clearcoatNormalScale;
	clearcoatNormal = normalize( tbn2 * clearcoatMapN );
#endif`,i0=`#ifdef USE_CLEARCOATMAP
	uniform sampler2D clearcoatMap;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	uniform sampler2D clearcoatNormalMap;
	uniform vec2 clearcoatNormalScale;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	uniform sampler2D clearcoatRoughnessMap;
#endif`,s0=`#ifdef USE_IRIDESCENCEMAP
	uniform sampler2D iridescenceMap;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	uniform sampler2D iridescenceThicknessMap;
#endif`,r0=`#ifdef OPAQUE
diffuseColor.a = 1.0;
#endif
#ifdef USE_TRANSMISSION
diffuseColor.a *= material.transmissionAlpha;
#endif
gl_FragColor = vec4( outgoingLight, diffuseColor.a );`,o0=`vec3 packNormalToRGB( const in vec3 normal ) {
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
}`,a0=`#ifdef PREMULTIPLIED_ALPHA
	gl_FragColor.rgb *= gl_FragColor.a;
#endif`,c0=`vec4 mvPosition = vec4( transformed, 1.0 );
#ifdef USE_BATCHING
	mvPosition = batchingMatrix * mvPosition;
#endif
#ifdef USE_INSTANCING
	mvPosition = instanceMatrix * mvPosition;
#endif
mvPosition = modelViewMatrix * mvPosition;
gl_Position = projectionMatrix * mvPosition;`,l0=`#ifdef DITHERING
	gl_FragColor.rgb = dithering( gl_FragColor.rgb );
#endif`,h0=`#ifdef DITHERING
	vec3 dithering( vec3 color ) {
		float grid_position = rand( gl_FragCoord.xy );
		vec3 dither_shift_RGB = vec3( 0.25 / 255.0, -0.25 / 255.0, 0.25 / 255.0 );
		dither_shift_RGB = mix( 2.0 * dither_shift_RGB, -2.0 * dither_shift_RGB, grid_position );
		return color + dither_shift_RGB;
	}
#endif`,u0=`float roughnessFactor = roughness;
#ifdef USE_ROUGHNESSMAP
	vec4 texelRoughness = texture2D( roughnessMap, vRoughnessMapUv );
	roughnessFactor *= texelRoughness.g;
#endif`,f0=`#ifdef USE_ROUGHNESSMAP
	uniform sampler2D roughnessMap;
#endif`,d0=`#if NUM_SPOT_LIGHT_COORDS > 0
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
#endif`,p0=`#if NUM_SPOT_LIGHT_COORDS > 0
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
#endif`,m0=`#if ( defined( USE_SHADOWMAP ) && ( NUM_DIR_LIGHT_SHADOWS > 0 || NUM_POINT_LIGHT_SHADOWS > 0 ) ) || ( NUM_SPOT_LIGHT_COORDS > 0 )
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
#endif`,g0=`float getShadowMask() {
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
}`,_0=`#ifdef USE_SKINNING
	mat4 boneMatX = getBoneMatrix( skinIndex.x );
	mat4 boneMatY = getBoneMatrix( skinIndex.y );
	mat4 boneMatZ = getBoneMatrix( skinIndex.z );
	mat4 boneMatW = getBoneMatrix( skinIndex.w );
#endif`,x0=`#ifdef USE_SKINNING
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
#endif`,v0=`#ifdef USE_SKINNING
	vec4 skinVertex = bindMatrix * vec4( transformed, 1.0 );
	vec4 skinned = vec4( 0.0 );
	skinned += boneMatX * skinVertex * skinWeight.x;
	skinned += boneMatY * skinVertex * skinWeight.y;
	skinned += boneMatZ * skinVertex * skinWeight.z;
	skinned += boneMatW * skinVertex * skinWeight.w;
	transformed = ( bindMatrixInverse * skinned ).xyz;
#endif`,y0=`#ifdef USE_SKINNING
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
#endif`,M0=`float specularStrength;
#ifdef USE_SPECULARMAP
	vec4 texelSpecular = texture2D( specularMap, vSpecularMapUv );
	specularStrength = texelSpecular.r;
#else
	specularStrength = 1.0;
#endif`,S0=`#ifdef USE_SPECULARMAP
	uniform sampler2D specularMap;
#endif`,b0=`#if defined( TONE_MAPPING )
	gl_FragColor.rgb = toneMapping( gl_FragColor.rgb );
#endif`,E0=`#ifndef saturate
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
vec3 CustomToneMapping( vec3 color ) { return color; }`,w0=`#ifdef USE_TRANSMISSION
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
#endif`,T0=`#ifdef USE_TRANSMISSION
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
#endif`,A0=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
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
#endif`,R0=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
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
#endif`,C0=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
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
#endif`,P0=`#if defined( USE_ENVMAP ) || defined( DISTANCE ) || defined ( USE_SHADOWMAP ) || defined ( USE_TRANSMISSION ) || NUM_SPOT_LIGHT_COORDS > 0
	vec4 worldPosition = vec4( transformed, 1.0 );
	#ifdef USE_BATCHING
		worldPosition = batchingMatrix * worldPosition;
	#endif
	#ifdef USE_INSTANCING
		worldPosition = instanceMatrix * worldPosition;
	#endif
	worldPosition = modelMatrix * worldPosition;
#endif`,I0=`varying vec2 vUv;
uniform mat3 uvTransform;
void main() {
	vUv = ( uvTransform * vec3( uv, 1 ) ).xy;
	gl_Position = vec4( position.xy, 1.0, 1.0 );
}`,L0=`uniform sampler2D t2D;
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
}`,U0=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
	gl_Position.z = gl_Position.w;
}`,D0=`#ifdef ENVMAP_TYPE_CUBE
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
}`,N0=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
	gl_Position.z = gl_Position.w;
}`,F0=`uniform samplerCube tCube;
uniform float tFlip;
uniform float opacity;
varying vec3 vWorldDirection;
void main() {
	vec4 texColor = textureCube( tCube, vec3( tFlip * vWorldDirection.x, vWorldDirection.yz ) );
	gl_FragColor = texColor;
	gl_FragColor.a *= opacity;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,O0=`#include <common>
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
}`,B0=`#if DEPTH_PACKING == 3200
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
}`,z0=`#define DISTANCE
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
}`,H0=`#define DISTANCE
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
}`,k0=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
}`,G0=`uniform sampler2D tEquirect;
varying vec3 vWorldDirection;
#include <common>
void main() {
	vec3 direction = normalize( vWorldDirection );
	vec2 sampleUV = equirectUv( direction );
	gl_FragColor = texture2D( tEquirect, sampleUV );
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,V0=`uniform float scale;
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
}`,W0=`uniform vec3 diffuse;
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
}`,X0=`#include <common>
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
}`,Y0=`uniform vec3 diffuse;
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
}`,q0=`#define LAMBERT
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
}`,Z0=`#define LAMBERT
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
}`,$0=`#define MATCAP
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
}`,J0=`#define MATCAP
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
}`,K0=`#define NORMAL
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
}`,j0=`#define NORMAL
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
}`,Q0=`#define PHONG
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
}`,tg=`#define PHONG
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
}`,eg=`#define STANDARD
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
}`,ng=`#define STANDARD
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
}`,ig=`#define TOON
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
}`,sg=`#define TOON
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
}`,rg=`uniform float size;
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
}`,og=`uniform vec3 diffuse;
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
}`,ag=`#include <common>
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
}`,cg=`uniform vec3 color;
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
}`,lg=`uniform float rotation;
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
}`,hg=`uniform vec3 diffuse;
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
}`,_e={alphahash_fragment:Lp,alphahash_pars_fragment:Up,alphamap_fragment:Dp,alphamap_pars_fragment:Np,alphatest_fragment:Fp,alphatest_pars_fragment:Op,aomap_fragment:Bp,aomap_pars_fragment:zp,batching_pars_vertex:Hp,batching_vertex:kp,begin_vertex:Gp,beginnormal_vertex:Vp,bsdfs:Wp,iridescence_fragment:Xp,bumpmap_pars_fragment:Yp,clipping_planes_fragment:qp,clipping_planes_pars_fragment:Zp,clipping_planes_pars_vertex:$p,clipping_planes_vertex:Jp,color_fragment:Kp,color_pars_fragment:jp,color_pars_vertex:Qp,color_vertex:tm,common:em,cube_uv_reflection_fragment:nm,defaultnormal_vertex:im,displacementmap_pars_vertex:sm,displacementmap_vertex:rm,emissivemap_fragment:om,emissivemap_pars_fragment:am,colorspace_fragment:cm,colorspace_pars_fragment:lm,envmap_fragment:hm,envmap_common_pars_fragment:um,envmap_pars_fragment:fm,envmap_pars_vertex:dm,envmap_physical_pars_fragment:wm,envmap_vertex:pm,fog_vertex:mm,fog_pars_vertex:gm,fog_fragment:_m,fog_pars_fragment:xm,gradientmap_pars_fragment:vm,lightmap_fragment:ym,lightmap_pars_fragment:Mm,lights_lambert_fragment:Sm,lights_lambert_pars_fragment:bm,lights_pars_begin:Em,lights_toon_fragment:Tm,lights_toon_pars_fragment:Am,lights_phong_fragment:Rm,lights_phong_pars_fragment:Cm,lights_physical_fragment:Pm,lights_physical_pars_fragment:Im,lights_fragment_begin:Lm,lights_fragment_maps:Um,lights_fragment_end:Dm,logdepthbuf_fragment:Nm,logdepthbuf_pars_fragment:Fm,logdepthbuf_pars_vertex:Om,logdepthbuf_vertex:Bm,map_fragment:zm,map_pars_fragment:Hm,map_particle_fragment:km,map_particle_pars_fragment:Gm,metalnessmap_fragment:Vm,metalnessmap_pars_fragment:Wm,morphcolor_vertex:Xm,morphnormal_vertex:Ym,morphtarget_pars_vertex:qm,morphtarget_vertex:Zm,normal_fragment_begin:$m,normal_fragment_maps:Jm,normal_pars_fragment:Km,normal_pars_vertex:jm,normal_vertex:Qm,normalmap_pars_fragment:t0,clearcoat_normal_fragment_begin:e0,clearcoat_normal_fragment_maps:n0,clearcoat_pars_fragment:i0,iridescence_pars_fragment:s0,opaque_fragment:r0,packing:o0,premultiplied_alpha_fragment:a0,project_vertex:c0,dithering_fragment:l0,dithering_pars_fragment:h0,roughnessmap_fragment:u0,roughnessmap_pars_fragment:f0,shadowmap_pars_fragment:d0,shadowmap_pars_vertex:p0,shadowmap_vertex:m0,shadowmask_pars_fragment:g0,skinbase_vertex:_0,skinning_pars_vertex:x0,skinning_vertex:v0,skinnormal_vertex:y0,specularmap_fragment:M0,specularmap_pars_fragment:S0,tonemapping_fragment:b0,tonemapping_pars_fragment:E0,transmission_fragment:w0,transmission_pars_fragment:T0,uv_pars_fragment:A0,uv_pars_vertex:R0,uv_vertex:C0,worldpos_vertex:P0,background_vert:I0,background_frag:L0,backgroundCube_vert:U0,backgroundCube_frag:D0,cube_vert:N0,cube_frag:F0,depth_vert:O0,depth_frag:B0,distanceRGBA_vert:z0,distanceRGBA_frag:H0,equirect_vert:k0,equirect_frag:G0,linedashed_vert:V0,linedashed_frag:W0,meshbasic_vert:X0,meshbasic_frag:Y0,meshlambert_vert:q0,meshlambert_frag:Z0,meshmatcap_vert:$0,meshmatcap_frag:J0,meshnormal_vert:K0,meshnormal_frag:j0,meshphong_vert:Q0,meshphong_frag:tg,meshphysical_vert:eg,meshphysical_frag:ng,meshtoon_vert:ig,meshtoon_frag:sg,points_vert:rg,points_frag:og,shadow_vert:ag,shadow_frag:cg,sprite_vert:lg,sprite_frag:hg},Pt={common:{diffuse:{value:new fe(16777215)},opacity:{value:1},map:{value:null},mapTransform:{value:new we},alphaMap:{value:null},alphaMapTransform:{value:new we},alphaTest:{value:0}},specularmap:{specularMap:{value:null},specularMapTransform:{value:new we}},envmap:{envMap:{value:null},flipEnvMap:{value:-1},reflectivity:{value:1},ior:{value:1.5},refractionRatio:{value:.98}},aomap:{aoMap:{value:null},aoMapIntensity:{value:1},aoMapTransform:{value:new we}},lightmap:{lightMap:{value:null},lightMapIntensity:{value:1},lightMapTransform:{value:new we}},bumpmap:{bumpMap:{value:null},bumpMapTransform:{value:new we},bumpScale:{value:1}},normalmap:{normalMap:{value:null},normalMapTransform:{value:new we},normalScale:{value:new St(1,1)}},displacementmap:{displacementMap:{value:null},displacementMapTransform:{value:new we},displacementScale:{value:1},displacementBias:{value:0}},emissivemap:{emissiveMap:{value:null},emissiveMapTransform:{value:new we}},metalnessmap:{metalnessMap:{value:null},metalnessMapTransform:{value:new we}},roughnessmap:{roughnessMap:{value:null},roughnessMapTransform:{value:new we}},gradientmap:{gradientMap:{value:null}},fog:{fogDensity:{value:25e-5},fogNear:{value:1},fogFar:{value:2e3},fogColor:{value:new fe(16777215)}},lights:{ambientLightColor:{value:[]},lightProbe:{value:[]},directionalLights:{value:[],properties:{direction:{},color:{}}},directionalLightShadows:{value:[],properties:{shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{}}},directionalShadowMap:{value:[]},directionalShadowMatrix:{value:[]},spotLights:{value:[],properties:{color:{},position:{},direction:{},distance:{},coneCos:{},penumbraCos:{},decay:{}}},spotLightShadows:{value:[],properties:{shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{}}},spotLightMap:{value:[]},spotShadowMap:{value:[]},spotLightMatrix:{value:[]},pointLights:{value:[],properties:{color:{},position:{},decay:{},distance:{}}},pointLightShadows:{value:[],properties:{shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{},shadowCameraNear:{},shadowCameraFar:{}}},pointShadowMap:{value:[]},pointShadowMatrix:{value:[]},hemisphereLights:{value:[],properties:{direction:{},skyColor:{},groundColor:{}}},rectAreaLights:{value:[],properties:{color:{},position:{},width:{},height:{}}},ltc_1:{value:null},ltc_2:{value:null}},points:{diffuse:{value:new fe(16777215)},opacity:{value:1},size:{value:1},scale:{value:1},map:{value:null},alphaMap:{value:null},alphaMapTransform:{value:new we},alphaTest:{value:0},uvTransform:{value:new we}},sprite:{diffuse:{value:new fe(16777215)},opacity:{value:1},center:{value:new St(.5,.5)},rotation:{value:0},map:{value:null},mapTransform:{value:new we},alphaMap:{value:null},alphaMapTransform:{value:new we},alphaTest:{value:0}}},vi={basic:{uniforms:Pn([Pt.common,Pt.specularmap,Pt.envmap,Pt.aomap,Pt.lightmap,Pt.fog]),vertexShader:_e.meshbasic_vert,fragmentShader:_e.meshbasic_frag},lambert:{uniforms:Pn([Pt.common,Pt.specularmap,Pt.envmap,Pt.aomap,Pt.lightmap,Pt.emissivemap,Pt.bumpmap,Pt.normalmap,Pt.displacementmap,Pt.fog,Pt.lights,{emissive:{value:new fe(0)}}]),vertexShader:_e.meshlambert_vert,fragmentShader:_e.meshlambert_frag},phong:{uniforms:Pn([Pt.common,Pt.specularmap,Pt.envmap,Pt.aomap,Pt.lightmap,Pt.emissivemap,Pt.bumpmap,Pt.normalmap,Pt.displacementmap,Pt.fog,Pt.lights,{emissive:{value:new fe(0)},specular:{value:new fe(1118481)},shininess:{value:30}}]),vertexShader:_e.meshphong_vert,fragmentShader:_e.meshphong_frag},standard:{uniforms:Pn([Pt.common,Pt.envmap,Pt.aomap,Pt.lightmap,Pt.emissivemap,Pt.bumpmap,Pt.normalmap,Pt.displacementmap,Pt.roughnessmap,Pt.metalnessmap,Pt.fog,Pt.lights,{emissive:{value:new fe(0)},roughness:{value:1},metalness:{value:0},envMapIntensity:{value:1}}]),vertexShader:_e.meshphysical_vert,fragmentShader:_e.meshphysical_frag},toon:{uniforms:Pn([Pt.common,Pt.aomap,Pt.lightmap,Pt.emissivemap,Pt.bumpmap,Pt.normalmap,Pt.displacementmap,Pt.gradientmap,Pt.fog,Pt.lights,{emissive:{value:new fe(0)}}]),vertexShader:_e.meshtoon_vert,fragmentShader:_e.meshtoon_frag},matcap:{uniforms:Pn([Pt.common,Pt.bumpmap,Pt.normalmap,Pt.displacementmap,Pt.fog,{matcap:{value:null}}]),vertexShader:_e.meshmatcap_vert,fragmentShader:_e.meshmatcap_frag},points:{uniforms:Pn([Pt.points,Pt.fog]),vertexShader:_e.points_vert,fragmentShader:_e.points_frag},dashed:{uniforms:Pn([Pt.common,Pt.fog,{scale:{value:1},dashSize:{value:1},totalSize:{value:2}}]),vertexShader:_e.linedashed_vert,fragmentShader:_e.linedashed_frag},depth:{uniforms:Pn([Pt.common,Pt.displacementmap]),vertexShader:_e.depth_vert,fragmentShader:_e.depth_frag},normal:{uniforms:Pn([Pt.common,Pt.bumpmap,Pt.normalmap,Pt.displacementmap,{opacity:{value:1}}]),vertexShader:_e.meshnormal_vert,fragmentShader:_e.meshnormal_frag},sprite:{uniforms:Pn([Pt.sprite,Pt.fog]),vertexShader:_e.sprite_vert,fragmentShader:_e.sprite_frag},background:{uniforms:{uvTransform:{value:new we},t2D:{value:null},backgroundIntensity:{value:1}},vertexShader:_e.background_vert,fragmentShader:_e.background_frag},backgroundCube:{uniforms:{envMap:{value:null},flipEnvMap:{value:-1},backgroundBlurriness:{value:0},backgroundIntensity:{value:1}},vertexShader:_e.backgroundCube_vert,fragmentShader:_e.backgroundCube_frag},cube:{uniforms:{tCube:{value:null},tFlip:{value:-1},opacity:{value:1}},vertexShader:_e.cube_vert,fragmentShader:_e.cube_frag},equirect:{uniforms:{tEquirect:{value:null}},vertexShader:_e.equirect_vert,fragmentShader:_e.equirect_frag},distanceRGBA:{uniforms:Pn([Pt.common,Pt.displacementmap,{referencePosition:{value:new O},nearDistance:{value:1},farDistance:{value:1e3}}]),vertexShader:_e.distanceRGBA_vert,fragmentShader:_e.distanceRGBA_frag},shadow:{uniforms:Pn([Pt.lights,Pt.fog,{color:{value:new fe(0)},opacity:{value:1}}]),vertexShader:_e.shadow_vert,fragmentShader:_e.shadow_frag}};vi.physical={uniforms:Pn([vi.standard.uniforms,{clearcoat:{value:0},clearcoatMap:{value:null},clearcoatMapTransform:{value:new we},clearcoatNormalMap:{value:null},clearcoatNormalMapTransform:{value:new we},clearcoatNormalScale:{value:new St(1,1)},clearcoatRoughness:{value:0},clearcoatRoughnessMap:{value:null},clearcoatRoughnessMapTransform:{value:new we},iridescence:{value:0},iridescenceMap:{value:null},iridescenceMapTransform:{value:new we},iridescenceIOR:{value:1.3},iridescenceThicknessMinimum:{value:100},iridescenceThicknessMaximum:{value:400},iridescenceThicknessMap:{value:null},iridescenceThicknessMapTransform:{value:new we},sheen:{value:0},sheenColor:{value:new fe(0)},sheenColorMap:{value:null},sheenColorMapTransform:{value:new we},sheenRoughness:{value:1},sheenRoughnessMap:{value:null},sheenRoughnessMapTransform:{value:new we},transmission:{value:0},transmissionMap:{value:null},transmissionMapTransform:{value:new we},transmissionSamplerSize:{value:new St},transmissionSamplerMap:{value:null},thickness:{value:0},thicknessMap:{value:null},thicknessMapTransform:{value:new we},attenuationDistance:{value:0},attenuationColor:{value:new fe(0)},specularColor:{value:new fe(1,1,1)},specularColorMap:{value:null},specularColorMapTransform:{value:new we},specularIntensity:{value:1},specularIntensityMap:{value:null},specularIntensityMapTransform:{value:new we},anisotropyVector:{value:new St},anisotropyMap:{value:null},anisotropyMapTransform:{value:new we}}]),vertexShader:_e.meshphysical_vert,fragmentShader:_e.meshphysical_frag};var Yo={r:0,b:0,g:0};function ug(i,t,e,n,s,r,a){let o=new fe(0),c=r===!0?0:1,l,h,f=null,d=0,p=null;function x(_,m){let T=!1,M=m.isScene===!0?m.background:null;M&&M.isTexture&&(M=(m.backgroundBlurriness>0?e:t).get(M)),M===null?S(o,c):M&&M.isColor&&(S(M,1),T=!0);let U=i.xr.getEnvironmentBlendMode();U==="additive"?n.buffers.color.setClear(0,0,0,1,a):U==="alpha-blend"&&n.buffers.color.setClear(0,0,0,0,a),(i.autoClear||T)&&i.clear(i.autoClearColor,i.autoClearDepth,i.autoClearStencil),M&&(M.isCubeTexture||M.mapping===Ua)?(h===void 0&&(h=new Ne(new Pe(1,1,1),new Sn({name:"BackgroundCubeMaterial",uniforms:pr(vi.backgroundCube.uniforms),vertexShader:vi.backgroundCube.vertexShader,fragmentShader:vi.backgroundCube.fragmentShader,side:Tn,depthTest:!1,depthWrite:!1,fog:!1})),h.geometry.deleteAttribute("normal"),h.geometry.deleteAttribute("uv"),h.onBeforeRender=function(W,F,B){this.matrixWorld.copyPosition(B.matrixWorld)},Object.defineProperty(h.material,"envMap",{get:function(){return this.uniforms.envMap.value}}),s.update(h)),h.material.uniforms.envMap.value=M,h.material.uniforms.flipEnvMap.value=M.isCubeTexture&&M.isRenderTargetTexture===!1?-1:1,h.material.uniforms.backgroundBlurriness.value=m.backgroundBlurriness,h.material.uniforms.backgroundIntensity.value=m.backgroundIntensity,h.material.toneMapped=Be.getTransfer(M.colorSpace)!==Xe,(f!==M||d!==M.version||p!==i.toneMapping)&&(h.material.needsUpdate=!0,f=M,d=M.version,p=i.toneMapping),h.layers.enableAll(),_.unshift(h,h.geometry,h.material,0,0,null)):M&&M.isTexture&&(l===void 0&&(l=new Ne(new _n(2,2),new Sn({name:"BackgroundMaterial",uniforms:pr(vi.background.uniforms),vertexShader:vi.background.vertexShader,fragmentShader:vi.background.fragmentShader,side:es,depthTest:!1,depthWrite:!1,fog:!1})),l.geometry.deleteAttribute("normal"),Object.defineProperty(l.material,"map",{get:function(){return this.uniforms.t2D.value}}),s.update(l)),l.material.uniforms.t2D.value=M,l.material.uniforms.backgroundIntensity.value=m.backgroundIntensity,l.material.toneMapped=Be.getTransfer(M.colorSpace)!==Xe,M.matrixAutoUpdate===!0&&M.updateMatrix(),l.material.uniforms.uvTransform.value.copy(M.matrix),(f!==M||d!==M.version||p!==i.toneMapping)&&(l.material.needsUpdate=!0,f=M,d=M.version,p=i.toneMapping),l.layers.enableAll(),_.unshift(l,l.geometry,l.material,0,0,null))}function S(_,m){_.getRGB(Yo,wf(i)),n.buffers.color.setClear(Yo.r,Yo.g,Yo.b,m,a)}return{getClearColor:function(){return o},setClearColor:function(_,m=1){o.set(_),c=m,S(o,c)},getClearAlpha:function(){return c},setClearAlpha:function(_){c=_,S(o,c)},render:x}}function fg(i,t,e,n){let s=i.getParameter(i.MAX_VERTEX_ATTRIBS),r=n.isWebGL2?null:t.get("OES_vertex_array_object"),a=n.isWebGL2||r!==null,o={},c=_(null),l=c,h=!1;function f(X,K,tt,it,ft){let nt=!1;if(a){let ct=S(it,tt,K);l!==ct&&(l=ct,p(l.object)),nt=m(X,it,tt,ft),nt&&T(X,it,tt,ft)}else{let ct=K.wireframe===!0;(l.geometry!==it.id||l.program!==tt.id||l.wireframe!==ct)&&(l.geometry=it.id,l.program=tt.id,l.wireframe=ct,nt=!0)}ft!==null&&e.update(ft,i.ELEMENT_ARRAY_BUFFER),(nt||h)&&(h=!1,J(X,K,tt,it),ft!==null&&i.bindBuffer(i.ELEMENT_ARRAY_BUFFER,e.get(ft).buffer))}function d(){return n.isWebGL2?i.createVertexArray():r.createVertexArrayOES()}function p(X){return n.isWebGL2?i.bindVertexArray(X):r.bindVertexArrayOES(X)}function x(X){return n.isWebGL2?i.deleteVertexArray(X):r.deleteVertexArrayOES(X)}function S(X,K,tt){let it=tt.wireframe===!0,ft=o[X.id];ft===void 0&&(ft={},o[X.id]=ft);let nt=ft[K.id];nt===void 0&&(nt={},ft[K.id]=nt);let ct=nt[it];return ct===void 0&&(ct=_(d()),nt[it]=ct),ct}function _(X){let K=[],tt=[],it=[];for(let ft=0;ft<s;ft++)K[ft]=0,tt[ft]=0,it[ft]=0;return{geometry:null,program:null,wireframe:!1,newAttributes:K,enabledAttributes:tt,attributeDivisors:it,object:X,attributes:{},index:null}}function m(X,K,tt,it){let ft=l.attributes,nt=K.attributes,ct=0,lt=tt.getAttributes();for(let Dt in lt)if(lt[Dt].location>=0){let ut=ft[Dt],Nt=nt[Dt];if(Nt===void 0&&(Dt==="instanceMatrix"&&X.instanceMatrix&&(Nt=X.instanceMatrix),Dt==="instanceColor"&&X.instanceColor&&(Nt=X.instanceColor)),ut===void 0||ut.attribute!==Nt||Nt&&ut.data!==Nt.data)return!0;ct++}return l.attributesNum!==ct||l.index!==it}function T(X,K,tt,it){let ft={},nt=K.attributes,ct=0,lt=tt.getAttributes();for(let Dt in lt)if(lt[Dt].location>=0){let ut=nt[Dt];ut===void 0&&(Dt==="instanceMatrix"&&X.instanceMatrix&&(ut=X.instanceMatrix),Dt==="instanceColor"&&X.instanceColor&&(ut=X.instanceColor));let Nt={};Nt.attribute=ut,ut&&ut.data&&(Nt.data=ut.data),ft[Dt]=Nt,ct++}l.attributes=ft,l.attributesNum=ct,l.index=it}function M(){let X=l.newAttributes;for(let K=0,tt=X.length;K<tt;K++)X[K]=0}function U(X){W(X,0)}function W(X,K){let tt=l.newAttributes,it=l.enabledAttributes,ft=l.attributeDivisors;tt[X]=1,it[X]===0&&(i.enableVertexAttribArray(X),it[X]=1),ft[X]!==K&&((n.isWebGL2?i:t.get("ANGLE_instanced_arrays"))[n.isWebGL2?"vertexAttribDivisor":"vertexAttribDivisorANGLE"](X,K),ft[X]=K)}function F(){let X=l.newAttributes,K=l.enabledAttributes;for(let tt=0,it=K.length;tt<it;tt++)K[tt]!==X[tt]&&(i.disableVertexAttribArray(tt),K[tt]=0)}function B(X,K,tt,it,ft,nt,ct){ct===!0?i.vertexAttribIPointer(X,K,tt,ft,nt):i.vertexAttribPointer(X,K,tt,it,ft,nt)}function J(X,K,tt,it){if(n.isWebGL2===!1&&(X.isInstancedMesh||it.isInstancedBufferGeometry)&&t.get("ANGLE_instanced_arrays")===null)return;M();let ft=it.attributes,nt=tt.getAttributes(),ct=K.defaultAttributeValues;for(let lt in nt){let Dt=nt[lt];if(Dt.location>=0){let st=ft[lt];if(st===void 0&&(lt==="instanceMatrix"&&X.instanceMatrix&&(st=X.instanceMatrix),lt==="instanceColor"&&X.instanceColor&&(st=X.instanceColor)),st!==void 0){let ut=st.normalized,Nt=st.itemSize,Ft=e.get(st);if(Ft===void 0)continue;let Bt=Ft.buffer,se=Ft.type,Jt=Ft.bytesPerElement,Wt=n.isWebGL2===!0&&(se===i.INT||se===i.UNSIGNED_INT||st.gpuType===df);if(st.isInterleavedBufferAttribute){let le=st.data,z=le.stride,Tt=st.offset;if(le.isInstancedInterleavedBuffer){for(let rt=0;rt<Dt.locationSize;rt++)W(Dt.location+rt,le.meshPerAttribute);X.isInstancedMesh!==!0&&it._maxInstanceCount===void 0&&(it._maxInstanceCount=le.meshPerAttribute*le.count)}else for(let rt=0;rt<Dt.locationSize;rt++)U(Dt.location+rt);i.bindBuffer(i.ARRAY_BUFFER,Bt);for(let rt=0;rt<Dt.locationSize;rt++)B(Dt.location+rt,Nt/Dt.locationSize,se,ut,z*Jt,(Tt+Nt/Dt.locationSize*rt)*Jt,Wt)}else{if(st.isInstancedBufferAttribute){for(let le=0;le<Dt.locationSize;le++)W(Dt.location+le,st.meshPerAttribute);X.isInstancedMesh!==!0&&it._maxInstanceCount===void 0&&(it._maxInstanceCount=st.meshPerAttribute*st.count)}else for(let le=0;le<Dt.locationSize;le++)U(Dt.location+le);i.bindBuffer(i.ARRAY_BUFFER,Bt);for(let le=0;le<Dt.locationSize;le++)B(Dt.location+le,Nt/Dt.locationSize,se,ut,Nt*Jt,Nt/Dt.locationSize*le*Jt,Wt)}}else if(ct!==void 0){let ut=ct[lt];if(ut!==void 0)switch(ut.length){case 2:i.vertexAttrib2fv(Dt.location,ut);break;case 3:i.vertexAttrib3fv(Dt.location,ut);break;case 4:i.vertexAttrib4fv(Dt.location,ut);break;default:i.vertexAttrib1fv(Dt.location,ut)}}}}F()}function w(){ot();for(let X in o){let K=o[X];for(let tt in K){let it=K[tt];for(let ft in it)x(it[ft].object),delete it[ft];delete K[tt]}delete o[X]}}function L(X){if(o[X.id]===void 0)return;let K=o[X.id];for(let tt in K){let it=K[tt];for(let ft in it)x(it[ft].object),delete it[ft];delete K[tt]}delete o[X.id]}function $(X){for(let K in o){let tt=o[K];if(tt[X.id]===void 0)continue;let it=tt[X.id];for(let ft in it)x(it[ft].object),delete it[ft];delete tt[X.id]}}function ot(){Mt(),h=!0,l!==c&&(l=c,p(l.object))}function Mt(){c.geometry=null,c.program=null,c.wireframe=!1}return{setup:f,reset:ot,resetDefaultState:Mt,dispose:w,releaseStatesOfGeometry:L,releaseStatesOfProgram:$,initAttributes:M,enableAttribute:U,disableUnusedAttributes:F}}function dg(i,t,e,n){let s=n.isWebGL2,r;function a(h){r=h}function o(h,f){i.drawArrays(r,h,f),e.update(f,r,1)}function c(h,f,d){if(d===0)return;let p,x;if(s)p=i,x="drawArraysInstanced";else if(p=t.get("ANGLE_instanced_arrays"),x="drawArraysInstancedANGLE",p===null){console.error("THREE.WebGLBufferRenderer: using THREE.InstancedBufferGeometry but hardware does not support extension ANGLE_instanced_arrays.");return}p[x](r,h,f,d),e.update(f,r,d)}function l(h,f,d){if(d===0)return;let p=t.get("WEBGL_multi_draw");if(p===null)for(let x=0;x<d;x++)this.render(h[x],f[x]);else{p.multiDrawArraysWEBGL(r,h,0,f,0,d);let x=0;for(let S=0;S<d;S++)x+=f[S];e.update(x,r,1)}}this.setMode=a,this.render=o,this.renderInstances=c,this.renderMultiDraw=l}function pg(i,t,e){let n;function s(){if(n!==void 0)return n;if(t.has("EXT_texture_filter_anisotropic")===!0){let B=t.get("EXT_texture_filter_anisotropic");n=i.getParameter(B.MAX_TEXTURE_MAX_ANISOTROPY_EXT)}else n=0;return n}function r(B){if(B==="highp"){if(i.getShaderPrecisionFormat(i.VERTEX_SHADER,i.HIGH_FLOAT).precision>0&&i.getShaderPrecisionFormat(i.FRAGMENT_SHADER,i.HIGH_FLOAT).precision>0)return"highp";B="mediump"}return B==="mediump"&&i.getShaderPrecisionFormat(i.VERTEX_SHADER,i.MEDIUM_FLOAT).precision>0&&i.getShaderPrecisionFormat(i.FRAGMENT_SHADER,i.MEDIUM_FLOAT).precision>0?"mediump":"lowp"}let a=typeof WebGL2RenderingContext!="undefined"&&i.constructor.name==="WebGL2RenderingContext",o=e.precision!==void 0?e.precision:"highp",c=r(o);c!==o&&(console.warn("THREE.WebGLRenderer:",o,"not supported, using",c,"instead."),o=c);let l=a||t.has("WEBGL_draw_buffers"),h=e.logarithmicDepthBuffer===!0,f=i.getParameter(i.MAX_TEXTURE_IMAGE_UNITS),d=i.getParameter(i.MAX_VERTEX_TEXTURE_IMAGE_UNITS),p=i.getParameter(i.MAX_TEXTURE_SIZE),x=i.getParameter(i.MAX_CUBE_MAP_TEXTURE_SIZE),S=i.getParameter(i.MAX_VERTEX_ATTRIBS),_=i.getParameter(i.MAX_VERTEX_UNIFORM_VECTORS),m=i.getParameter(i.MAX_VARYING_VECTORS),T=i.getParameter(i.MAX_FRAGMENT_UNIFORM_VECTORS),M=d>0,U=a||t.has("OES_texture_float"),W=M&&U,F=a?i.getParameter(i.MAX_SAMPLES):0;return{isWebGL2:a,drawBuffers:l,getMaxAnisotropy:s,getMaxPrecision:r,precision:o,logarithmicDepthBuffer:h,maxTextures:f,maxVertexTextures:d,maxTextureSize:p,maxCubemapSize:x,maxAttributes:S,maxVertexUniforms:_,maxVaryings:m,maxFragmentUniforms:T,vertexTextures:M,floatFragmentTextures:U,floatVertexTextures:W,maxSamples:F}}function mg(i){let t=this,e=null,n=0,s=!1,r=!1,a=new Li,o=new we,c={value:null,needsUpdate:!1};this.uniform=c,this.numPlanes=0,this.numIntersection=0,this.init=function(f,d){let p=f.length!==0||d||n!==0||s;return s=d,n=f.length,p},this.beginShadows=function(){r=!0,h(null)},this.endShadows=function(){r=!1},this.setGlobalState=function(f,d){e=h(f,d,0)},this.setState=function(f,d,p){let x=f.clippingPlanes,S=f.clipIntersection,_=f.clipShadows,m=i.get(f);if(!s||x===null||x.length===0||r&&!_)r?h(null):l();else{let T=r?0:n,M=T*4,U=m.clippingState||null;c.value=U,U=h(x,d,M,p);for(let W=0;W!==M;++W)U[W]=e[W];m.clippingState=U,this.numIntersection=S?this.numPlanes:0,this.numPlanes+=T}};function l(){c.value!==e&&(c.value=e,c.needsUpdate=n>0),t.numPlanes=n,t.numIntersection=0}function h(f,d,p,x){let S=f!==null?f.length:0,_=null;if(S!==0){if(_=c.value,x!==!0||_===null){let m=p+S*4,T=d.matrixWorldInverse;o.getNormalMatrix(T),(_===null||_.length<m)&&(_=new Float32Array(m));for(let M=0,U=p;M!==S;++M,U+=4)a.copy(f[M]).applyMatrix4(T,o),a.normal.toArray(_,U),_[U+3]=a.constant}c.value=_,c.needsUpdate=!0}return t.numPlanes=S,t.numIntersection=0,_}}function gg(i){let t=new WeakMap;function e(a,o){return o===kc?a.mapping=ur:o===Gc&&(a.mapping=fr),a}function n(a){if(a&&a.isTexture){let o=a.mapping;if(o===kc||o===Gc)if(t.has(a)){let c=t.get(a).texture;return e(c,a.mapping)}else{let c=a.image;if(c&&c.height>0){let l=new $c(c.height/2);return l.fromEquirectangularTexture(i,a),t.set(a,l),a.addEventListener("dispose",s),e(l.texture,a.mapping)}else return null}}return a}function s(a){let o=a.target;o.removeEventListener("dispose",s);let c=t.get(o);c!==void 0&&(t.delete(o),c.dispose())}function r(){t=new WeakMap}return{get:n,dispose:r}}var ga=class extends pa{constructor(t=-1,e=1,n=1,s=-1,r=.1,a=2e3){super(),this.isOrthographicCamera=!0,this.type="OrthographicCamera",this.zoom=1,this.view=null,this.left=t,this.right=e,this.top=n,this.bottom=s,this.near=r,this.far=a,this.updateProjectionMatrix()}copy(t,e){return super.copy(t,e),this.left=t.left,this.right=t.right,this.top=t.top,this.bottom=t.bottom,this.near=t.near,this.far=t.far,this.zoom=t.zoom,this.view=t.view===null?null:Object.assign({},t.view),this}setViewOffset(t,e,n,s,r,a){this.view===null&&(this.view={enabled:!0,fullWidth:1,fullHeight:1,offsetX:0,offsetY:0,width:1,height:1}),this.view.enabled=!0,this.view.fullWidth=t,this.view.fullHeight=e,this.view.offsetX=n,this.view.offsetY=s,this.view.width=r,this.view.height=a,this.updateProjectionMatrix()}clearViewOffset(){this.view!==null&&(this.view.enabled=!1),this.updateProjectionMatrix()}updateProjectionMatrix(){let t=(this.right-this.left)/(2*this.zoom),e=(this.top-this.bottom)/(2*this.zoom),n=(this.right+this.left)/2,s=(this.top+this.bottom)/2,r=n-t,a=n+t,o=s+e,c=s-e;if(this.view!==null&&this.view.enabled){let l=(this.right-this.left)/this.view.fullWidth/this.zoom,h=(this.top-this.bottom)/this.view.fullHeight/this.zoom;r+=l*this.view.offsetX,a=r+l*this.view.width,o-=h*this.view.offsetY,c=o-h*this.view.height}this.projectionMatrix.makeOrthographic(r,a,o,c,this.near,this.far,this.coordinateSystem),this.projectionMatrixInverse.copy(this.projectionMatrix).invert()}toJSON(t){let e=super.toJSON(t);return e.object.zoom=this.zoom,e.object.left=this.left,e.object.right=this.right,e.object.top=this.top,e.object.bottom=this.bottom,e.object.near=this.near,e.object.far=this.far,this.view!==null&&(e.object.view=Object.assign({},this.view)),e}},ir=4,Cu=[.125,.215,.35,.446,.526,.582],vs=20,Cc=new ga,Pu=new fe,Pc=null,Ic=0,Lc=0,_s=(1+Math.sqrt(5))/2,Qs=1/_s,Iu=[new O(1,1,1),new O(-1,1,1),new O(1,1,-1),new O(-1,1,-1),new O(0,_s,Qs),new O(0,_s,-Qs),new O(Qs,0,_s),new O(-Qs,0,_s),new O(_s,Qs,0),new O(-_s,Qs,0)],mr=class{constructor(t){this._renderer=t,this._pingPongRenderTarget=null,this._lodMax=0,this._cubeSize=0,this._lodPlanes=[],this._sizeLods=[],this._sigmas=[],this._blurMaterial=null,this._cubemapMaterial=null,this._equirectMaterial=null,this._compileMaterial(this._blurMaterial)}fromScene(t,e=0,n=.1,s=100){Pc=this._renderer.getRenderTarget(),Ic=this._renderer.getActiveCubeFace(),Lc=this._renderer.getActiveMipmapLevel(),this._setSize(256);let r=this._allocateTargets();return r.depthBuffer=!0,this._sceneToCubeUV(t,n,s,r),e>0&&this._blur(r,0,0,e),this._applyPMREM(r),this._cleanup(r),r}fromEquirectangular(t,e=null){return this._fromTexture(t,e)}fromCubemap(t,e=null){return this._fromTexture(t,e)}compileCubemapShader(){this._cubemapMaterial===null&&(this._cubemapMaterial=Du(),this._compileMaterial(this._cubemapMaterial))}compileEquirectangularShader(){this._equirectMaterial===null&&(this._equirectMaterial=Uu(),this._compileMaterial(this._equirectMaterial))}dispose(){this._dispose(),this._cubemapMaterial!==null&&this._cubemapMaterial.dispose(),this._equirectMaterial!==null&&this._equirectMaterial.dispose()}_setSize(t){this._lodMax=Math.floor(Math.log2(t)),this._cubeSize=Math.pow(2,this._lodMax)}_dispose(){this._blurMaterial!==null&&this._blurMaterial.dispose(),this._pingPongRenderTarget!==null&&this._pingPongRenderTarget.dispose();for(let t=0;t<this._lodPlanes.length;t++)this._lodPlanes[t].dispose()}_cleanup(t){this._renderer.setRenderTarget(Pc,Ic,Lc),t.scissorTest=!1,qo(t,0,0,t.width,t.height)}_fromTexture(t,e){t.mapping===ur||t.mapping===fr?this._setSize(t.image.length===0?16:t.image[0].width||t.image[0].image.width):this._setSize(t.image.width/4),Pc=this._renderer.getRenderTarget(),Ic=this._renderer.getActiveCubeFace(),Lc=this._renderer.getActiveMipmapLevel();let n=e||this._allocateTargets();return this._textureToCubeUV(t,n),this._applyPMREM(n),this._cleanup(n),n}_allocateTargets(){let t=3*Math.max(this._cubeSize,112),e=4*this._cubeSize,n={magFilter:$n,minFilter:$n,generateMipmaps:!1,type:Gr,format:hi,colorSpace:Di,depthBuffer:!1},s=Lu(t,e,n);if(this._pingPongRenderTarget===null||this._pingPongRenderTarget.width!==t||this._pingPongRenderTarget.height!==e){this._pingPongRenderTarget!==null&&this._dispose(),this._pingPongRenderTarget=Lu(t,e,n);let{_lodMax:r}=this;({sizeLods:this._sizeLods,lodPlanes:this._lodPlanes,sigmas:this._sigmas}=_g(r)),this._blurMaterial=xg(r,t,e)}return s}_compileMaterial(t){let e=new Ne(this._lodPlanes[0],t);this._renderer.compile(e,Cc)}_sceneToCubeUV(t,e,n,s){let o=new wn(90,1,e,n),c=[1,-1,1,1,1,1],l=[1,1,1,-1,-1,-1],h=this._renderer,f=h.autoClear,d=h.toneMapping;h.getClearColor(Pu),h.toneMapping=ji,h.autoClear=!1;let p=new Es({name:"PMREM.Background",side:Tn,depthWrite:!1,depthTest:!1}),x=new Ne(new Pe,p),S=!1,_=t.background;_?_.isColor&&(p.color.copy(_),t.background=null,S=!0):(p.color.copy(Pu),S=!0);for(let m=0;m<6;m++){let T=m%3;T===0?(o.up.set(0,c[m],0),o.lookAt(l[m],0,0)):T===1?(o.up.set(0,0,c[m]),o.lookAt(0,l[m],0)):(o.up.set(0,c[m],0),o.lookAt(0,0,l[m]));let M=this._cubeSize;qo(s,T*M,m>2?M:0,M,M),h.setRenderTarget(s),S&&h.render(x,o),h.render(t,o)}x.geometry.dispose(),x.material.dispose(),h.toneMapping=d,h.autoClear=f,t.background=_}_textureToCubeUV(t,e){let n=this._renderer,s=t.mapping===ur||t.mapping===fr;s?(this._cubemapMaterial===null&&(this._cubemapMaterial=Du()),this._cubemapMaterial.uniforms.flipEnvMap.value=t.isRenderTargetTexture===!1?-1:1):this._equirectMaterial===null&&(this._equirectMaterial=Uu());let r=s?this._cubemapMaterial:this._equirectMaterial,a=new Ne(this._lodPlanes[0],r),o=r.uniforms;o.envMap.value=t;let c=this._cubeSize;qo(e,0,0,3*c,2*c),n.setRenderTarget(e),n.render(a,Cc)}_applyPMREM(t){let e=this._renderer,n=e.autoClear;e.autoClear=!1;for(let s=1;s<this._lodPlanes.length;s++){let r=Math.sqrt(this._sigmas[s]*this._sigmas[s]-this._sigmas[s-1]*this._sigmas[s-1]),a=Iu[(s-1)%Iu.length];this._blur(t,s-1,s,r,a)}e.autoClear=n}_blur(t,e,n,s,r){let a=this._pingPongRenderTarget;this._halfBlur(t,a,e,n,s,"latitudinal",r),this._halfBlur(a,t,n,n,s,"longitudinal",r)}_halfBlur(t,e,n,s,r,a,o){let c=this._renderer,l=this._blurMaterial;a!=="latitudinal"&&a!=="longitudinal"&&console.error("blur direction must be either latitudinal or longitudinal!");let h=3,f=new Ne(this._lodPlanes[s],l),d=l.uniforms,p=this._sizeLods[n]-1,x=isFinite(r)?Math.PI/(2*p):2*Math.PI/(2*vs-1),S=r/x,_=isFinite(r)?1+Math.floor(h*S):vs;_>vs&&console.warn(`sigmaRadians, ${r}, is too large and will clip, as it requested ${_} samples when the maximum is set to ${vs}`);let m=[],T=0;for(let B=0;B<vs;++B){let J=B/S,w=Math.exp(-J*J/2);m.push(w),B===0?T+=w:B<_&&(T+=2*w)}for(let B=0;B<m.length;B++)m[B]=m[B]/T;d.envMap.value=t.texture,d.samples.value=_,d.weights.value=m,d.latitudinal.value=a==="latitudinal",o&&(d.poleAxis.value=o);let{_lodMax:M}=this;d.dTheta.value=x,d.mipInt.value=M-n;let U=this._sizeLods[s],W=3*U*(s>M-ir?s-M+ir:0),F=4*(this._cubeSize-U);qo(e,W,F,3*U,2*U),c.setRenderTarget(e),c.render(f,Cc)}};function _g(i){let t=[],e=[],n=[],s=i,r=i-ir+1+Cu.length;for(let a=0;a<r;a++){let o=Math.pow(2,s);e.push(o);let c=1/o;a>i-ir?c=Cu[a-i+ir-1]:a===0&&(c=0),n.push(c);let l=1/(o-2),h=-l,f=1+l,d=[h,h,f,h,f,f,h,h,f,f,h,f],p=6,x=6,S=3,_=2,m=1,T=new Float32Array(S*x*p),M=new Float32Array(_*x*p),U=new Float32Array(m*x*p);for(let F=0;F<p;F++){let B=F%3*2/3-1,J=F>2?0:-1,w=[B,J,0,B+2/3,J,0,B+2/3,J+1,0,B,J,0,B+2/3,J+1,0,B,J+1,0];T.set(w,S*x*F),M.set(d,_*x*F);let L=[F,F,F,F,F,F];U.set(L,m*x*F)}let W=new Ke;W.setAttribute("position",new Mn(T,S)),W.setAttribute("uv",new Mn(M,_)),W.setAttribute("faceIndex",new Mn(U,m)),t.push(W),s>ir&&s--}return{lodPlanes:t,sizeLods:e,sigmas:n}}function Lu(i,t,e){let n=new Ni(i,t,e);return n.texture.mapping=Ua,n.texture.name="PMREM.cubeUv",n.scissorTest=!0,n}function qo(i,t,e,n,s){i.viewport.set(t,e,n,s),i.scissor.set(t,e,n,s)}function xg(i,t,e){let n=new Float32Array(vs),s=new O(0,1,0);return new Sn({name:"SphericalGaussianBlur",defines:{n:vs,CUBEUV_TEXEL_WIDTH:1/t,CUBEUV_TEXEL_HEIGHT:1/e,CUBEUV_MAX_MIP:`${i}.0`},uniforms:{envMap:{value:null},samples:{value:1},weights:{value:n},latitudinal:{value:!1},dTheta:{value:0},mipInt:{value:0},poleAxis:{value:s}},vertexShader:Ol(),fragmentShader:`

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
		`,blending:Ki,depthTest:!1,depthWrite:!1})}function Uu(){return new Sn({name:"EquirectangularToCubeUV",uniforms:{envMap:{value:null}},vertexShader:Ol(),fragmentShader:`

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
		`,blending:Ki,depthTest:!1,depthWrite:!1})}function Du(){return new Sn({name:"CubemapToCubeUV",uniforms:{envMap:{value:null},flipEnvMap:{value:-1}},vertexShader:Ol(),fragmentShader:`

			precision mediump float;
			precision mediump int;

			uniform float flipEnvMap;

			varying vec3 vOutputDirection;

			uniform samplerCube envMap;

			void main() {

				gl_FragColor = textureCube( envMap, vec3( flipEnvMap * vOutputDirection.x, vOutputDirection.yz ) );

			}
		`,blending:Ki,depthTest:!1,depthWrite:!1})}function Ol(){return`

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
	`}function vg(i){let t=new WeakMap,e=null;function n(o){if(o&&o.isTexture){let c=o.mapping,l=c===kc||c===Gc,h=c===ur||c===fr;if(l||h)if(o.isRenderTargetTexture&&o.needsPMREMUpdate===!0){o.needsPMREMUpdate=!1;let f=t.get(o);return e===null&&(e=new mr(i)),f=l?e.fromEquirectangular(o,f):e.fromCubemap(o,f),t.set(o,f),f.texture}else{if(t.has(o))return t.get(o).texture;{let f=o.image;if(l&&f&&f.height>0||h&&f&&s(f)){e===null&&(e=new mr(i));let d=l?e.fromEquirectangular(o):e.fromCubemap(o);return t.set(o,d),o.addEventListener("dispose",r),d.texture}else return null}}}return o}function s(o){let c=0,l=6;for(let h=0;h<l;h++)o[h]!==void 0&&c++;return c===l}function r(o){let c=o.target;c.removeEventListener("dispose",r);let l=t.get(c);l!==void 0&&(t.delete(c),l.dispose())}function a(){t=new WeakMap,e!==null&&(e.dispose(),e=null)}return{get:n,dispose:a}}function yg(i){let t={};function e(n){if(t[n]!==void 0)return t[n];let s;switch(n){case"WEBGL_depth_texture":s=i.getExtension("WEBGL_depth_texture")||i.getExtension("MOZ_WEBGL_depth_texture")||i.getExtension("WEBKIT_WEBGL_depth_texture");break;case"EXT_texture_filter_anisotropic":s=i.getExtension("EXT_texture_filter_anisotropic")||i.getExtension("MOZ_EXT_texture_filter_anisotropic")||i.getExtension("WEBKIT_EXT_texture_filter_anisotropic");break;case"WEBGL_compressed_texture_s3tc":s=i.getExtension("WEBGL_compressed_texture_s3tc")||i.getExtension("MOZ_WEBGL_compressed_texture_s3tc")||i.getExtension("WEBKIT_WEBGL_compressed_texture_s3tc");break;case"WEBGL_compressed_texture_pvrtc":s=i.getExtension("WEBGL_compressed_texture_pvrtc")||i.getExtension("WEBKIT_WEBGL_compressed_texture_pvrtc");break;default:s=i.getExtension(n)}return t[n]=s,s}return{has:function(n){return e(n)!==null},init:function(n){n.isWebGL2?(e("EXT_color_buffer_float"),e("WEBGL_clip_cull_distance")):(e("WEBGL_depth_texture"),e("OES_texture_float"),e("OES_texture_half_float"),e("OES_texture_half_float_linear"),e("OES_standard_derivatives"),e("OES_element_index_uint"),e("OES_vertex_array_object"),e("ANGLE_instanced_arrays")),e("OES_texture_float_linear"),e("EXT_color_buffer_half_float"),e("WEBGL_multisampled_render_to_texture")},get:function(n){let s=e(n);return s===null&&console.warn("THREE.WebGLRenderer: "+n+" extension not supported."),s}}}function Mg(i,t,e,n){let s={},r=new WeakMap;function a(f){let d=f.target;d.index!==null&&t.remove(d.index);for(let x in d.attributes)t.remove(d.attributes[x]);for(let x in d.morphAttributes){let S=d.morphAttributes[x];for(let _=0,m=S.length;_<m;_++)t.remove(S[_])}d.removeEventListener("dispose",a),delete s[d.id];let p=r.get(d);p&&(t.remove(p),r.delete(d)),n.releaseStatesOfGeometry(d),d.isInstancedBufferGeometry===!0&&delete d._maxInstanceCount,e.memory.geometries--}function o(f,d){return s[d.id]===!0||(d.addEventListener("dispose",a),s[d.id]=!0,e.memory.geometries++),d}function c(f){let d=f.attributes;for(let x in d)t.update(d[x],i.ARRAY_BUFFER);let p=f.morphAttributes;for(let x in p){let S=p[x];for(let _=0,m=S.length;_<m;_++)t.update(S[_],i.ARRAY_BUFFER)}}function l(f){let d=[],p=f.index,x=f.attributes.position,S=0;if(p!==null){let T=p.array;S=p.version;for(let M=0,U=T.length;M<U;M+=3){let W=T[M+0],F=T[M+1],B=T[M+2];d.push(W,F,F,B,B,W)}}else if(x!==void 0){let T=x.array;S=x.version;for(let M=0,U=T.length/3-1;M<U;M+=3){let W=M+0,F=M+1,B=M+2;d.push(W,F,F,B,B,W)}}else return;let _=new(bf(d)?da:fa)(d,1);_.version=S;let m=r.get(f);m&&t.remove(m),r.set(f,_)}function h(f){let d=r.get(f);if(d){let p=f.index;p!==null&&d.version<p.version&&l(f)}else l(f);return r.get(f)}return{get:o,update:c,getWireframeAttribute:h}}function Sg(i,t,e,n){let s=n.isWebGL2,r;function a(p){r=p}let o,c;function l(p){o=p.type,c=p.bytesPerElement}function h(p,x){i.drawElements(r,x,o,p*c),e.update(x,r,1)}function f(p,x,S){if(S===0)return;let _,m;if(s)_=i,m="drawElementsInstanced";else if(_=t.get("ANGLE_instanced_arrays"),m="drawElementsInstancedANGLE",_===null){console.error("THREE.WebGLIndexedBufferRenderer: using THREE.InstancedBufferGeometry but hardware does not support extension ANGLE_instanced_arrays.");return}_[m](r,x,o,p*c,S),e.update(x,r,S)}function d(p,x,S){if(S===0)return;let _=t.get("WEBGL_multi_draw");if(_===null)for(let m=0;m<S;m++)this.render(p[m]/c,x[m]);else{_.multiDrawElementsWEBGL(r,x,0,o,p,0,S);let m=0;for(let T=0;T<S;T++)m+=x[T];e.update(m,r,1)}}this.setMode=a,this.setIndex=l,this.render=h,this.renderInstances=f,this.renderMultiDraw=d}function bg(i){let t={geometries:0,textures:0},e={frame:0,calls:0,triangles:0,points:0,lines:0};function n(r,a,o){switch(e.calls++,a){case i.TRIANGLES:e.triangles+=o*(r/3);break;case i.LINES:e.lines+=o*(r/2);break;case i.LINE_STRIP:e.lines+=o*(r-1);break;case i.LINE_LOOP:e.lines+=o*r;break;case i.POINTS:e.points+=o*r;break;default:console.error("THREE.WebGLInfo: Unknown draw mode:",a);break}}function s(){e.calls=0,e.triangles=0,e.points=0,e.lines=0}return{memory:t,render:e,programs:null,autoReset:!0,reset:s,update:n}}function Eg(i,t){return i[0]-t[0]}function wg(i,t){return Math.abs(t[1])-Math.abs(i[1])}function Tg(i,t,e){let n={},s=new Float32Array(8),r=new WeakMap,a=new Je,o=[];for(let l=0;l<8;l++)o[l]=[l,0];function c(l,h,f){let d=l.morphTargetInfluences;if(t.isWebGL2===!0){let p=h.morphAttributes.position||h.morphAttributes.normal||h.morphAttributes.color,x=p!==void 0?p.length:0,S=r.get(h);if(S===void 0||S.count!==x){let X=function(){ot.dispose(),r.delete(h),h.removeEventListener("dispose",X)};S!==void 0&&S.texture.dispose();let T=h.morphAttributes.position!==void 0,M=h.morphAttributes.normal!==void 0,U=h.morphAttributes.color!==void 0,W=h.morphAttributes.position||[],F=h.morphAttributes.normal||[],B=h.morphAttributes.color||[],J=0;T===!0&&(J=1),M===!0&&(J=2),U===!0&&(J=3);let w=h.attributes.position.count*J,L=1;w>t.maxTextureSize&&(L=Math.ceil(w/t.maxTextureSize),w=t.maxTextureSize);let $=new Float32Array(w*L*4*x),ot=new ua($,w,L,x);ot.type=Ji,ot.needsUpdate=!0;let Mt=J*4;for(let K=0;K<x;K++){let tt=W[K],it=F[K],ft=B[K],nt=w*L*4*K;for(let ct=0;ct<tt.count;ct++){let lt=ct*Mt;T===!0&&(a.fromBufferAttribute(tt,ct),$[nt+lt+0]=a.x,$[nt+lt+1]=a.y,$[nt+lt+2]=a.z,$[nt+lt+3]=0),M===!0&&(a.fromBufferAttribute(it,ct),$[nt+lt+4]=a.x,$[nt+lt+5]=a.y,$[nt+lt+6]=a.z,$[nt+lt+7]=0),U===!0&&(a.fromBufferAttribute(ft,ct),$[nt+lt+8]=a.x,$[nt+lt+9]=a.y,$[nt+lt+10]=a.z,$[nt+lt+11]=ft.itemSize===4?a.w:1)}}S={count:x,texture:ot,size:new St(w,L)},r.set(h,S),h.addEventListener("dispose",X)}let _=0;for(let T=0;T<d.length;T++)_+=d[T];let m=h.morphTargetsRelative?1:1-_;f.getUniforms().setValue(i,"morphTargetBaseInfluence",m),f.getUniforms().setValue(i,"morphTargetInfluences",d),f.getUniforms().setValue(i,"morphTargetsTexture",S.texture,e),f.getUniforms().setValue(i,"morphTargetsTextureSize",S.size)}else{let p=d===void 0?0:d.length,x=n[h.id];if(x===void 0||x.length!==p){x=[];for(let M=0;M<p;M++)x[M]=[M,0];n[h.id]=x}for(let M=0;M<p;M++){let U=x[M];U[0]=M,U[1]=d[M]}x.sort(wg);for(let M=0;M<8;M++)M<p&&x[M][1]?(o[M][0]=x[M][0],o[M][1]=x[M][1]):(o[M][0]=Number.MAX_SAFE_INTEGER,o[M][1]=0);o.sort(Eg);let S=h.morphAttributes.position,_=h.morphAttributes.normal,m=0;for(let M=0;M<8;M++){let U=o[M],W=U[0],F=U[1];W!==Number.MAX_SAFE_INTEGER&&F?(S&&h.getAttribute("morphTarget"+M)!==S[W]&&h.setAttribute("morphTarget"+M,S[W]),_&&h.getAttribute("morphNormal"+M)!==_[W]&&h.setAttribute("morphNormal"+M,_[W]),s[M]=F,m+=F):(S&&h.hasAttribute("morphTarget"+M)===!0&&h.deleteAttribute("morphTarget"+M),_&&h.hasAttribute("morphNormal"+M)===!0&&h.deleteAttribute("morphNormal"+M),s[M]=0)}let T=h.morphTargetsRelative?1:1-m;f.getUniforms().setValue(i,"morphTargetBaseInfluence",T),f.getUniforms().setValue(i,"morphTargetInfluences",s)}}return{update:c}}function Ag(i,t,e,n){let s=new WeakMap;function r(c){let l=n.render.frame,h=c.geometry,f=t.get(c,h);if(s.get(f)!==l&&(t.update(f),s.set(f,l)),c.isInstancedMesh&&(c.hasEventListener("dispose",o)===!1&&c.addEventListener("dispose",o),s.get(c)!==l&&(e.update(c.instanceMatrix,i.ARRAY_BUFFER),c.instanceColor!==null&&e.update(c.instanceColor,i.ARRAY_BUFFER),s.set(c,l))),c.isSkinnedMesh){let d=c.skeleton;s.get(d)!==l&&(d.update(),s.set(d,l))}return f}function a(){s=new WeakMap}function o(c){let l=c.target;l.removeEventListener("dispose",o),e.remove(l.instanceMatrix),l.instanceColor!==null&&e.remove(l.instanceColor)}return{update:r,dispose:a}}var _a=class extends Hn{constructor(t,e,n,s,r,a,o,c,l,h){if(h=h!==void 0?h:Ms,h!==Ms&&h!==dr)throw new Error("DepthTexture format must be either THREE.DepthFormat or THREE.DepthStencilFormat");n===void 0&&h===Ms&&(n=$i),n===void 0&&h===dr&&(n=ys),super(null,s,r,a,o,c,h,n,l),this.isDepthTexture=!0,this.image={width:t,height:e},this.magFilter=o!==void 0?o:In,this.minFilter=c!==void 0?c:In,this.flipY=!1,this.generateMipmaps=!1,this.compareFunction=null}copy(t){return super.copy(t),this.compareFunction=t.compareFunction,this}toJSON(t){let e=super.toJSON(t);return this.compareFunction!==null&&(e.compareFunction=this.compareFunction),e}},Af=new Hn,Rf=new _a(1,1);Rf.compareFunction=Sf;var Cf=new ua,Pf=new qc,If=new ma,Nu=[],Fu=[],Ou=new Float32Array(16),Bu=new Float32Array(9),zu=new Float32Array(4);function xr(i,t,e){let n=i[0];if(n<=0||n>0)return i;let s=t*e,r=Nu[s];if(r===void 0&&(r=new Float32Array(s),Nu[s]=r),t!==0){n.toArray(r,0);for(let a=1,o=0;a!==t;++a)o+=e,i[a].toArray(r,o)}return r}function hn(i,t){if(i.length!==t.length)return!1;for(let e=0,n=i.length;e<n;e++)if(i[e]!==t[e])return!1;return!0}function un(i,t){for(let e=0,n=t.length;e<n;e++)i[e]=t[e]}function Na(i,t){let e=Fu[t];e===void 0&&(e=new Int32Array(t),Fu[t]=e);for(let n=0;n!==t;++n)e[n]=i.allocateTextureUnit();return e}function Rg(i,t){let e=this.cache;e[0]!==t&&(i.uniform1f(this.addr,t),e[0]=t)}function Cg(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y)&&(i.uniform2f(this.addr,t.x,t.y),e[0]=t.x,e[1]=t.y);else{if(hn(e,t))return;i.uniform2fv(this.addr,t),un(e,t)}}function Pg(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z)&&(i.uniform3f(this.addr,t.x,t.y,t.z),e[0]=t.x,e[1]=t.y,e[2]=t.z);else if(t.r!==void 0)(e[0]!==t.r||e[1]!==t.g||e[2]!==t.b)&&(i.uniform3f(this.addr,t.r,t.g,t.b),e[0]=t.r,e[1]=t.g,e[2]=t.b);else{if(hn(e,t))return;i.uniform3fv(this.addr,t),un(e,t)}}function Ig(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z||e[3]!==t.w)&&(i.uniform4f(this.addr,t.x,t.y,t.z,t.w),e[0]=t.x,e[1]=t.y,e[2]=t.z,e[3]=t.w);else{if(hn(e,t))return;i.uniform4fv(this.addr,t),un(e,t)}}function Lg(i,t){let e=this.cache,n=t.elements;if(n===void 0){if(hn(e,t))return;i.uniformMatrix2fv(this.addr,!1,t),un(e,t)}else{if(hn(e,n))return;zu.set(n),i.uniformMatrix2fv(this.addr,!1,zu),un(e,n)}}function Ug(i,t){let e=this.cache,n=t.elements;if(n===void 0){if(hn(e,t))return;i.uniformMatrix3fv(this.addr,!1,t),un(e,t)}else{if(hn(e,n))return;Bu.set(n),i.uniformMatrix3fv(this.addr,!1,Bu),un(e,n)}}function Dg(i,t){let e=this.cache,n=t.elements;if(n===void 0){if(hn(e,t))return;i.uniformMatrix4fv(this.addr,!1,t),un(e,t)}else{if(hn(e,n))return;Ou.set(n),i.uniformMatrix4fv(this.addr,!1,Ou),un(e,n)}}function Ng(i,t){let e=this.cache;e[0]!==t&&(i.uniform1i(this.addr,t),e[0]=t)}function Fg(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y)&&(i.uniform2i(this.addr,t.x,t.y),e[0]=t.x,e[1]=t.y);else{if(hn(e,t))return;i.uniform2iv(this.addr,t),un(e,t)}}function Og(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z)&&(i.uniform3i(this.addr,t.x,t.y,t.z),e[0]=t.x,e[1]=t.y,e[2]=t.z);else{if(hn(e,t))return;i.uniform3iv(this.addr,t),un(e,t)}}function Bg(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z||e[3]!==t.w)&&(i.uniform4i(this.addr,t.x,t.y,t.z,t.w),e[0]=t.x,e[1]=t.y,e[2]=t.z,e[3]=t.w);else{if(hn(e,t))return;i.uniform4iv(this.addr,t),un(e,t)}}function zg(i,t){let e=this.cache;e[0]!==t&&(i.uniform1ui(this.addr,t),e[0]=t)}function Hg(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y)&&(i.uniform2ui(this.addr,t.x,t.y),e[0]=t.x,e[1]=t.y);else{if(hn(e,t))return;i.uniform2uiv(this.addr,t),un(e,t)}}function kg(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z)&&(i.uniform3ui(this.addr,t.x,t.y,t.z),e[0]=t.x,e[1]=t.y,e[2]=t.z);else{if(hn(e,t))return;i.uniform3uiv(this.addr,t),un(e,t)}}function Gg(i,t){let e=this.cache;if(t.x!==void 0)(e[0]!==t.x||e[1]!==t.y||e[2]!==t.z||e[3]!==t.w)&&(i.uniform4ui(this.addr,t.x,t.y,t.z,t.w),e[0]=t.x,e[1]=t.y,e[2]=t.z,e[3]=t.w);else{if(hn(e,t))return;i.uniform4uiv(this.addr,t),un(e,t)}}function Vg(i,t,e){let n=this.cache,s=e.allocateTextureUnit();n[0]!==s&&(i.uniform1i(this.addr,s),n[0]=s);let r=this.type===i.SAMPLER_2D_SHADOW?Rf:Af;e.setTexture2D(t||r,s)}function Wg(i,t,e){let n=this.cache,s=e.allocateTextureUnit();n[0]!==s&&(i.uniform1i(this.addr,s),n[0]=s),e.setTexture3D(t||Pf,s)}function Xg(i,t,e){let n=this.cache,s=e.allocateTextureUnit();n[0]!==s&&(i.uniform1i(this.addr,s),n[0]=s),e.setTextureCube(t||If,s)}function Yg(i,t,e){let n=this.cache,s=e.allocateTextureUnit();n[0]!==s&&(i.uniform1i(this.addr,s),n[0]=s),e.setTexture2DArray(t||Cf,s)}function qg(i){switch(i){case 5126:return Rg;case 35664:return Cg;case 35665:return Pg;case 35666:return Ig;case 35674:return Lg;case 35675:return Ug;case 35676:return Dg;case 5124:case 35670:return Ng;case 35667:case 35671:return Fg;case 35668:case 35672:return Og;case 35669:case 35673:return Bg;case 5125:return zg;case 36294:return Hg;case 36295:return kg;case 36296:return Gg;case 35678:case 36198:case 36298:case 36306:case 35682:return Vg;case 35679:case 36299:case 36307:return Wg;case 35680:case 36300:case 36308:case 36293:return Xg;case 36289:case 36303:case 36311:case 36292:return Yg}}function Zg(i,t){i.uniform1fv(this.addr,t)}function $g(i,t){let e=xr(t,this.size,2);i.uniform2fv(this.addr,e)}function Jg(i,t){let e=xr(t,this.size,3);i.uniform3fv(this.addr,e)}function Kg(i,t){let e=xr(t,this.size,4);i.uniform4fv(this.addr,e)}function jg(i,t){let e=xr(t,this.size,4);i.uniformMatrix2fv(this.addr,!1,e)}function Qg(i,t){let e=xr(t,this.size,9);i.uniformMatrix3fv(this.addr,!1,e)}function t_(i,t){let e=xr(t,this.size,16);i.uniformMatrix4fv(this.addr,!1,e)}function e_(i,t){i.uniform1iv(this.addr,t)}function n_(i,t){i.uniform2iv(this.addr,t)}function i_(i,t){i.uniform3iv(this.addr,t)}function s_(i,t){i.uniform4iv(this.addr,t)}function r_(i,t){i.uniform1uiv(this.addr,t)}function o_(i,t){i.uniform2uiv(this.addr,t)}function a_(i,t){i.uniform3uiv(this.addr,t)}function c_(i,t){i.uniform4uiv(this.addr,t)}function l_(i,t,e){let n=this.cache,s=t.length,r=Na(e,s);hn(n,r)||(i.uniform1iv(this.addr,r),un(n,r));for(let a=0;a!==s;++a)e.setTexture2D(t[a]||Af,r[a])}function h_(i,t,e){let n=this.cache,s=t.length,r=Na(e,s);hn(n,r)||(i.uniform1iv(this.addr,r),un(n,r));for(let a=0;a!==s;++a)e.setTexture3D(t[a]||Pf,r[a])}function u_(i,t,e){let n=this.cache,s=t.length,r=Na(e,s);hn(n,r)||(i.uniform1iv(this.addr,r),un(n,r));for(let a=0;a!==s;++a)e.setTextureCube(t[a]||If,r[a])}function f_(i,t,e){let n=this.cache,s=t.length,r=Na(e,s);hn(n,r)||(i.uniform1iv(this.addr,r),un(n,r));for(let a=0;a!==s;++a)e.setTexture2DArray(t[a]||Cf,r[a])}function d_(i){switch(i){case 5126:return Zg;case 35664:return $g;case 35665:return Jg;case 35666:return Kg;case 35674:return jg;case 35675:return Qg;case 35676:return t_;case 5124:case 35670:return e_;case 35667:case 35671:return n_;case 35668:case 35672:return i_;case 35669:case 35673:return s_;case 5125:return r_;case 36294:return o_;case 36295:return a_;case 36296:return c_;case 35678:case 36198:case 36298:case 36306:case 35682:return l_;case 35679:case 36299:case 36307:return h_;case 35680:case 36300:case 36308:case 36293:return u_;case 36289:case 36303:case 36311:case 36292:return f_}}var Jc=class{constructor(t,e,n){this.id=t,this.addr=n,this.cache=[],this.type=e.type,this.setValue=qg(e.type)}},Kc=class{constructor(t,e,n){this.id=t,this.addr=n,this.cache=[],this.type=e.type,this.size=e.size,this.setValue=d_(e.type)}},jc=class{constructor(t){this.id=t,this.seq=[],this.map={}}setValue(t,e,n){let s=this.seq;for(let r=0,a=s.length;r!==a;++r){let o=s[r];o.setValue(t,e[o.id],n)}}},Uc=/(\w+)(\])?(\[|\.)?/g;function Hu(i,t){i.seq.push(t),i.map[t.id]=t}function p_(i,t,e){let n=i.name,s=n.length;for(Uc.lastIndex=0;;){let r=Uc.exec(n),a=Uc.lastIndex,o=r[1],c=r[2]==="]",l=r[3];if(c&&(o=o|0),l===void 0||l==="["&&a+2===s){Hu(e,l===void 0?new Jc(o,i,t):new Kc(o,i,t));break}else{let f=e.map[o];f===void 0&&(f=new jc(o),Hu(e,f)),e=f}}}var lr=class{constructor(t,e){this.seq=[],this.map={};let n=t.getProgramParameter(e,t.ACTIVE_UNIFORMS);for(let s=0;s<n;++s){let r=t.getActiveUniform(e,s),a=t.getUniformLocation(e,r.name);p_(r,a,this)}}setValue(t,e,n,s){let r=this.map[e];r!==void 0&&r.setValue(t,n,s)}setOptional(t,e,n){let s=e[n];s!==void 0&&this.setValue(t,n,s)}static upload(t,e,n,s){for(let r=0,a=e.length;r!==a;++r){let o=e[r],c=n[o.id];c.needsUpdate!==!1&&o.setValue(t,c.value,s)}}static seqWithValue(t,e){let n=[];for(let s=0,r=t.length;s!==r;++s){let a=t[s];a.id in e&&n.push(a)}return n}};function ku(i,t,e){let n=i.createShader(t);return i.shaderSource(n,e),i.compileShader(n),n}var m_=37297,g_=0;function __(i,t){let e=i.split(`
`),n=[],s=Math.max(t-6,0),r=Math.min(t+6,e.length);for(let a=s;a<r;a++){let o=a+1;n.push(`${o===t?">":" "} ${o}: ${e[a]}`)}return n.join(`
`)}function x_(i){let t=Be.getPrimaries(Be.workingColorSpace),e=Be.getPrimaries(i),n;switch(t===e?n="":t===oa&&e===ra?n="LinearDisplayP3ToLinearSRGB":t===ra&&e===oa&&(n="LinearSRGBToLinearDisplayP3"),i){case Di:case Da:return[n,"LinearTransferOETF"];case sn:case Dl:return[n,"sRGBTransferOETF"];default:return console.warn("THREE.WebGLProgram: Unsupported color space:",i),[n,"LinearTransferOETF"]}}function Gu(i,t,e){let n=i.getShaderParameter(t,i.COMPILE_STATUS),s=i.getShaderInfoLog(t).trim();if(n&&s==="")return"";let r=/ERROR: 0:(\d+)/.exec(s);if(r){let a=parseInt(r[1]);return e.toUpperCase()+`

`+s+`

`+__(i.getShaderSource(t),a)}else return s}function v_(i,t){let e=x_(t);return`vec4 ${i}( vec4 value ) { return ${e[0]}( ${e[1]}( value ) ); }`}function y_(i,t){let e;switch(t){case Rd:e="Linear";break;case Cd:e="Reinhard";break;case Pd:e="OptimizedCineon";break;case Il:e="ACESFilmic";break;case Ld:e="AgX";break;case Id:e="Custom";break;default:console.warn("THREE.WebGLProgram: Unsupported toneMapping:",t),e="Linear"}return"vec3 "+i+"( vec3 color ) { return "+e+"ToneMapping( color ); }"}function M_(i){return[i.extensionDerivatives||i.envMapCubeUVHeight||i.bumpMap||i.normalMapTangentSpace||i.clearcoatNormalMap||i.flatShading||i.shaderID==="physical"?"#extension GL_OES_standard_derivatives : enable":"",(i.extensionFragDepth||i.logarithmicDepthBuffer)&&i.rendererExtensionFragDepth?"#extension GL_EXT_frag_depth : enable":"",i.extensionDrawBuffers&&i.rendererExtensionDrawBuffers?"#extension GL_EXT_draw_buffers : require":"",(i.extensionShaderTextureLOD||i.envMap||i.transmission)&&i.rendererExtensionShaderTextureLod?"#extension GL_EXT_shader_texture_lod : enable":""].filter(sr).join(`
`)}function S_(i){return[i.extensionClipCullDistance?"#extension GL_ANGLE_clip_cull_distance : require":""].filter(sr).join(`
`)}function b_(i){let t=[];for(let e in i){let n=i[e];n!==!1&&t.push("#define "+e+" "+n)}return t.join(`
`)}function E_(i,t){let e={},n=i.getProgramParameter(t,i.ACTIVE_ATTRIBUTES);for(let s=0;s<n;s++){let r=i.getActiveAttrib(t,s),a=r.name,o=1;r.type===i.FLOAT_MAT2&&(o=2),r.type===i.FLOAT_MAT3&&(o=3),r.type===i.FLOAT_MAT4&&(o=4),e[a]={type:r.type,location:i.getAttribLocation(t,a),locationSize:o}}return e}function sr(i){return i!==""}function Vu(i,t){let e=t.numSpotLightShadows+t.numSpotLightMaps-t.numSpotLightShadowsWithMaps;return i.replace(/NUM_DIR_LIGHTS/g,t.numDirLights).replace(/NUM_SPOT_LIGHTS/g,t.numSpotLights).replace(/NUM_SPOT_LIGHT_MAPS/g,t.numSpotLightMaps).replace(/NUM_SPOT_LIGHT_COORDS/g,e).replace(/NUM_RECT_AREA_LIGHTS/g,t.numRectAreaLights).replace(/NUM_POINT_LIGHTS/g,t.numPointLights).replace(/NUM_HEMI_LIGHTS/g,t.numHemiLights).replace(/NUM_DIR_LIGHT_SHADOWS/g,t.numDirLightShadows).replace(/NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS/g,t.numSpotLightShadowsWithMaps).replace(/NUM_SPOT_LIGHT_SHADOWS/g,t.numSpotLightShadows).replace(/NUM_POINT_LIGHT_SHADOWS/g,t.numPointLightShadows)}function Wu(i,t){return i.replace(/NUM_CLIPPING_PLANES/g,t.numClippingPlanes).replace(/UNION_CLIPPING_PLANES/g,t.numClippingPlanes-t.numClipIntersection)}var w_=/^[ \t]*#include +<([\w\d./]+)>/gm;function Qc(i){return i.replace(w_,A_)}var T_=new Map([["encodings_fragment","colorspace_fragment"],["encodings_pars_fragment","colorspace_pars_fragment"],["output_fragment","opaque_fragment"]]);function A_(i,t){let e=_e[t];if(e===void 0){let n=T_.get(t);if(n!==void 0)e=_e[n],console.warn('THREE.WebGLRenderer: Shader chunk "%s" has been deprecated. Use "%s" instead.',t,n);else throw new Error("Can not resolve #include <"+t+">")}return Qc(e)}var R_=/#pragma unroll_loop_start\s+for\s*\(\s*int\s+i\s*=\s*(\d+)\s*;\s*i\s*<\s*(\d+)\s*;\s*i\s*\+\+\s*\)\s*{([\s\S]+?)}\s+#pragma unroll_loop_end/g;function Xu(i){return i.replace(R_,C_)}function C_(i,t,e,n){let s="";for(let r=parseInt(t);r<parseInt(e);r++)s+=n.replace(/\[\s*i\s*\]/g,"[ "+r+" ]").replace(/UNROLLED_LOOP_INDEX/g,r);return s}function Yu(i){let t="precision "+i.precision+` float;
precision `+i.precision+" int;";return i.precision==="highp"?t+=`
#define HIGH_PRECISION`:i.precision==="mediump"?t+=`
#define MEDIUM_PRECISION`:i.precision==="lowp"&&(t+=`
#define LOW_PRECISION`),t}function P_(i){let t="SHADOWMAP_TYPE_BASIC";return i.shadowMapType===hf?t="SHADOWMAP_TYPE_PCF":i.shadowMapType===Pl?t="SHADOWMAP_TYPE_PCF_SOFT":i.shadowMapType===Ii&&(t="SHADOWMAP_TYPE_VSM"),t}function I_(i){let t="ENVMAP_TYPE_CUBE";if(i.envMap)switch(i.envMapMode){case ur:case fr:t="ENVMAP_TYPE_CUBE";break;case Ua:t="ENVMAP_TYPE_CUBE_UV";break}return t}function L_(i){let t="ENVMAP_MODE_REFLECTION";return i.envMap&&i.envMapMode===fr&&(t="ENVMAP_MODE_REFRACTION"),t}function U_(i){let t="ENVMAP_BLENDING_NONE";if(i.envMap)switch(i.combine){case uf:t="ENVMAP_BLENDING_MULTIPLY";break;case Td:t="ENVMAP_BLENDING_MIX";break;case Ad:t="ENVMAP_BLENDING_ADD";break}return t}function D_(i){let t=i.envMapCubeUVHeight;if(t===null)return null;let e=Math.log2(t)-2,n=1/t;return{texelWidth:1/(3*Math.max(Math.pow(2,e),112)),texelHeight:n,maxMip:e}}function N_(i,t,e,n){let s=i.getContext(),r=e.defines,a=e.vertexShader,o=e.fragmentShader,c=P_(e),l=I_(e),h=L_(e),f=U_(e),d=D_(e),p=e.isWebGL2?"":M_(e),x=S_(e),S=b_(r),_=s.createProgram(),m,T,M=e.glslVersion?"#version "+e.glslVersion+`
`:"";e.isRawShaderMaterial?(m=["#define SHADER_TYPE "+e.shaderType,"#define SHADER_NAME "+e.shaderName,S].filter(sr).join(`
`),m.length>0&&(m+=`
`),T=[p,"#define SHADER_TYPE "+e.shaderType,"#define SHADER_NAME "+e.shaderName,S].filter(sr).join(`
`),T.length>0&&(T+=`
`)):(m=[Yu(e),"#define SHADER_TYPE "+e.shaderType,"#define SHADER_NAME "+e.shaderName,S,e.extensionClipCullDistance?"#define USE_CLIP_DISTANCE":"",e.batching?"#define USE_BATCHING":"",e.instancing?"#define USE_INSTANCING":"",e.instancingColor?"#define USE_INSTANCING_COLOR":"",e.useFog&&e.fog?"#define USE_FOG":"",e.useFog&&e.fogExp2?"#define FOG_EXP2":"",e.map?"#define USE_MAP":"",e.envMap?"#define USE_ENVMAP":"",e.envMap?"#define "+h:"",e.lightMap?"#define USE_LIGHTMAP":"",e.aoMap?"#define USE_AOMAP":"",e.bumpMap?"#define USE_BUMPMAP":"",e.normalMap?"#define USE_NORMALMAP":"",e.normalMapObjectSpace?"#define USE_NORMALMAP_OBJECTSPACE":"",e.normalMapTangentSpace?"#define USE_NORMALMAP_TANGENTSPACE":"",e.displacementMap?"#define USE_DISPLACEMENTMAP":"",e.emissiveMap?"#define USE_EMISSIVEMAP":"",e.anisotropy?"#define USE_ANISOTROPY":"",e.anisotropyMap?"#define USE_ANISOTROPYMAP":"",e.clearcoatMap?"#define USE_CLEARCOATMAP":"",e.clearcoatRoughnessMap?"#define USE_CLEARCOAT_ROUGHNESSMAP":"",e.clearcoatNormalMap?"#define USE_CLEARCOAT_NORMALMAP":"",e.iridescenceMap?"#define USE_IRIDESCENCEMAP":"",e.iridescenceThicknessMap?"#define USE_IRIDESCENCE_THICKNESSMAP":"",e.specularMap?"#define USE_SPECULARMAP":"",e.specularColorMap?"#define USE_SPECULAR_COLORMAP":"",e.specularIntensityMap?"#define USE_SPECULAR_INTENSITYMAP":"",e.roughnessMap?"#define USE_ROUGHNESSMAP":"",e.metalnessMap?"#define USE_METALNESSMAP":"",e.alphaMap?"#define USE_ALPHAMAP":"",e.alphaHash?"#define USE_ALPHAHASH":"",e.transmission?"#define USE_TRANSMISSION":"",e.transmissionMap?"#define USE_TRANSMISSIONMAP":"",e.thicknessMap?"#define USE_THICKNESSMAP":"",e.sheenColorMap?"#define USE_SHEEN_COLORMAP":"",e.sheenRoughnessMap?"#define USE_SHEEN_ROUGHNESSMAP":"",e.mapUv?"#define MAP_UV "+e.mapUv:"",e.alphaMapUv?"#define ALPHAMAP_UV "+e.alphaMapUv:"",e.lightMapUv?"#define LIGHTMAP_UV "+e.lightMapUv:"",e.aoMapUv?"#define AOMAP_UV "+e.aoMapUv:"",e.emissiveMapUv?"#define EMISSIVEMAP_UV "+e.emissiveMapUv:"",e.bumpMapUv?"#define BUMPMAP_UV "+e.bumpMapUv:"",e.normalMapUv?"#define NORMALMAP_UV "+e.normalMapUv:"",e.displacementMapUv?"#define DISPLACEMENTMAP_UV "+e.displacementMapUv:"",e.metalnessMapUv?"#define METALNESSMAP_UV "+e.metalnessMapUv:"",e.roughnessMapUv?"#define ROUGHNESSMAP_UV "+e.roughnessMapUv:"",e.anisotropyMapUv?"#define ANISOTROPYMAP_UV "+e.anisotropyMapUv:"",e.clearcoatMapUv?"#define CLEARCOATMAP_UV "+e.clearcoatMapUv:"",e.clearcoatNormalMapUv?"#define CLEARCOAT_NORMALMAP_UV "+e.clearcoatNormalMapUv:"",e.clearcoatRoughnessMapUv?"#define CLEARCOAT_ROUGHNESSMAP_UV "+e.clearcoatRoughnessMapUv:"",e.iridescenceMapUv?"#define IRIDESCENCEMAP_UV "+e.iridescenceMapUv:"",e.iridescenceThicknessMapUv?"#define IRIDESCENCE_THICKNESSMAP_UV "+e.iridescenceThicknessMapUv:"",e.sheenColorMapUv?"#define SHEEN_COLORMAP_UV "+e.sheenColorMapUv:"",e.sheenRoughnessMapUv?"#define SHEEN_ROUGHNESSMAP_UV "+e.sheenRoughnessMapUv:"",e.specularMapUv?"#define SPECULARMAP_UV "+e.specularMapUv:"",e.specularColorMapUv?"#define SPECULAR_COLORMAP_UV "+e.specularColorMapUv:"",e.specularIntensityMapUv?"#define SPECULAR_INTENSITYMAP_UV "+e.specularIntensityMapUv:"",e.transmissionMapUv?"#define TRANSMISSIONMAP_UV "+e.transmissionMapUv:"",e.thicknessMapUv?"#define THICKNESSMAP_UV "+e.thicknessMapUv:"",e.vertexTangents&&e.flatShading===!1?"#define USE_TANGENT":"",e.vertexColors?"#define USE_COLOR":"",e.vertexAlphas?"#define USE_COLOR_ALPHA":"",e.vertexUv1s?"#define USE_UV1":"",e.vertexUv2s?"#define USE_UV2":"",e.vertexUv3s?"#define USE_UV3":"",e.pointsUvs?"#define USE_POINTS_UV":"",e.flatShading?"#define FLAT_SHADED":"",e.skinning?"#define USE_SKINNING":"",e.morphTargets?"#define USE_MORPHTARGETS":"",e.morphNormals&&e.flatShading===!1?"#define USE_MORPHNORMALS":"",e.morphColors&&e.isWebGL2?"#define USE_MORPHCOLORS":"",e.morphTargetsCount>0&&e.isWebGL2?"#define MORPHTARGETS_TEXTURE":"",e.morphTargetsCount>0&&e.isWebGL2?"#define MORPHTARGETS_TEXTURE_STRIDE "+e.morphTextureStride:"",e.morphTargetsCount>0&&e.isWebGL2?"#define MORPHTARGETS_COUNT "+e.morphTargetsCount:"",e.doubleSided?"#define DOUBLE_SIDED":"",e.flipSided?"#define FLIP_SIDED":"",e.shadowMapEnabled?"#define USE_SHADOWMAP":"",e.shadowMapEnabled?"#define "+c:"",e.sizeAttenuation?"#define USE_SIZEATTENUATION":"",e.numLightProbes>0?"#define USE_LIGHT_PROBES":"",e.useLegacyLights?"#define LEGACY_LIGHTS":"",e.logarithmicDepthBuffer?"#define USE_LOGDEPTHBUF":"",e.logarithmicDepthBuffer&&e.rendererExtensionFragDepth?"#define USE_LOGDEPTHBUF_EXT":"","uniform mat4 modelMatrix;","uniform mat4 modelViewMatrix;","uniform mat4 projectionMatrix;","uniform mat4 viewMatrix;","uniform mat3 normalMatrix;","uniform vec3 cameraPosition;","uniform bool isOrthographic;","#ifdef USE_INSTANCING","	attribute mat4 instanceMatrix;","#endif","#ifdef USE_INSTANCING_COLOR","	attribute vec3 instanceColor;","#endif","attribute vec3 position;","attribute vec3 normal;","attribute vec2 uv;","#ifdef USE_UV1","	attribute vec2 uv1;","#endif","#ifdef USE_UV2","	attribute vec2 uv2;","#endif","#ifdef USE_UV3","	attribute vec2 uv3;","#endif","#ifdef USE_TANGENT","	attribute vec4 tangent;","#endif","#if defined( USE_COLOR_ALPHA )","	attribute vec4 color;","#elif defined( USE_COLOR )","	attribute vec3 color;","#endif","#if ( defined( USE_MORPHTARGETS ) && ! defined( MORPHTARGETS_TEXTURE ) )","	attribute vec3 morphTarget0;","	attribute vec3 morphTarget1;","	attribute vec3 morphTarget2;","	attribute vec3 morphTarget3;","	#ifdef USE_MORPHNORMALS","		attribute vec3 morphNormal0;","		attribute vec3 morphNormal1;","		attribute vec3 morphNormal2;","		attribute vec3 morphNormal3;","	#else","		attribute vec3 morphTarget4;","		attribute vec3 morphTarget5;","		attribute vec3 morphTarget6;","		attribute vec3 morphTarget7;","	#endif","#endif","#ifdef USE_SKINNING","	attribute vec4 skinIndex;","	attribute vec4 skinWeight;","#endif",`
`].filter(sr).join(`
`),T=[p,Yu(e),"#define SHADER_TYPE "+e.shaderType,"#define SHADER_NAME "+e.shaderName,S,e.useFog&&e.fog?"#define USE_FOG":"",e.useFog&&e.fogExp2?"#define FOG_EXP2":"",e.map?"#define USE_MAP":"",e.matcap?"#define USE_MATCAP":"",e.envMap?"#define USE_ENVMAP":"",e.envMap?"#define "+l:"",e.envMap?"#define "+h:"",e.envMap?"#define "+f:"",d?"#define CUBEUV_TEXEL_WIDTH "+d.texelWidth:"",d?"#define CUBEUV_TEXEL_HEIGHT "+d.texelHeight:"",d?"#define CUBEUV_MAX_MIP "+d.maxMip+".0":"",e.lightMap?"#define USE_LIGHTMAP":"",e.aoMap?"#define USE_AOMAP":"",e.bumpMap?"#define USE_BUMPMAP":"",e.normalMap?"#define USE_NORMALMAP":"",e.normalMapObjectSpace?"#define USE_NORMALMAP_OBJECTSPACE":"",e.normalMapTangentSpace?"#define USE_NORMALMAP_TANGENTSPACE":"",e.emissiveMap?"#define USE_EMISSIVEMAP":"",e.anisotropy?"#define USE_ANISOTROPY":"",e.anisotropyMap?"#define USE_ANISOTROPYMAP":"",e.clearcoat?"#define USE_CLEARCOAT":"",e.clearcoatMap?"#define USE_CLEARCOATMAP":"",e.clearcoatRoughnessMap?"#define USE_CLEARCOAT_ROUGHNESSMAP":"",e.clearcoatNormalMap?"#define USE_CLEARCOAT_NORMALMAP":"",e.iridescence?"#define USE_IRIDESCENCE":"",e.iridescenceMap?"#define USE_IRIDESCENCEMAP":"",e.iridescenceThicknessMap?"#define USE_IRIDESCENCE_THICKNESSMAP":"",e.specularMap?"#define USE_SPECULARMAP":"",e.specularColorMap?"#define USE_SPECULAR_COLORMAP":"",e.specularIntensityMap?"#define USE_SPECULAR_INTENSITYMAP":"",e.roughnessMap?"#define USE_ROUGHNESSMAP":"",e.metalnessMap?"#define USE_METALNESSMAP":"",e.alphaMap?"#define USE_ALPHAMAP":"",e.alphaTest?"#define USE_ALPHATEST":"",e.alphaHash?"#define USE_ALPHAHASH":"",e.sheen?"#define USE_SHEEN":"",e.sheenColorMap?"#define USE_SHEEN_COLORMAP":"",e.sheenRoughnessMap?"#define USE_SHEEN_ROUGHNESSMAP":"",e.transmission?"#define USE_TRANSMISSION":"",e.transmissionMap?"#define USE_TRANSMISSIONMAP":"",e.thicknessMap?"#define USE_THICKNESSMAP":"",e.vertexTangents&&e.flatShading===!1?"#define USE_TANGENT":"",e.vertexColors||e.instancingColor?"#define USE_COLOR":"",e.vertexAlphas?"#define USE_COLOR_ALPHA":"",e.vertexUv1s?"#define USE_UV1":"",e.vertexUv2s?"#define USE_UV2":"",e.vertexUv3s?"#define USE_UV3":"",e.pointsUvs?"#define USE_POINTS_UV":"",e.gradientMap?"#define USE_GRADIENTMAP":"",e.flatShading?"#define FLAT_SHADED":"",e.doubleSided?"#define DOUBLE_SIDED":"",e.flipSided?"#define FLIP_SIDED":"",e.shadowMapEnabled?"#define USE_SHADOWMAP":"",e.shadowMapEnabled?"#define "+c:"",e.premultipliedAlpha?"#define PREMULTIPLIED_ALPHA":"",e.numLightProbes>0?"#define USE_LIGHT_PROBES":"",e.useLegacyLights?"#define LEGACY_LIGHTS":"",e.decodeVideoTexture?"#define DECODE_VIDEO_TEXTURE":"",e.logarithmicDepthBuffer?"#define USE_LOGDEPTHBUF":"",e.logarithmicDepthBuffer&&e.rendererExtensionFragDepth?"#define USE_LOGDEPTHBUF_EXT":"","uniform mat4 viewMatrix;","uniform vec3 cameraPosition;","uniform bool isOrthographic;",e.toneMapping!==ji?"#define TONE_MAPPING":"",e.toneMapping!==ji?_e.tonemapping_pars_fragment:"",e.toneMapping!==ji?y_("toneMapping",e.toneMapping):"",e.dithering?"#define DITHERING":"",e.opaque?"#define OPAQUE":"",_e.colorspace_pars_fragment,v_("linearToOutputTexel",e.outputColorSpace),e.useDepthPacking?"#define DEPTH_PACKING "+e.depthPacking:"",`
`].filter(sr).join(`
`)),a=Qc(a),a=Vu(a,e),a=Wu(a,e),o=Qc(o),o=Vu(o,e),o=Wu(o,e),a=Xu(a),o=Xu(o),e.isWebGL2&&e.isRawShaderMaterial!==!0&&(M=`#version 300 es
`,m=[x,"precision mediump sampler2DArray;","#define attribute in","#define varying out","#define texture2D texture"].join(`
`)+`
`+m,T=["precision mediump sampler2DArray;","#define varying in",e.glslVersion===uu?"":"layout(location = 0) out highp vec4 pc_fragColor;",e.glslVersion===uu?"":"#define gl_FragColor pc_fragColor","#define gl_FragDepthEXT gl_FragDepth","#define texture2D texture","#define textureCube texture","#define texture2DProj textureProj","#define texture2DLodEXT textureLod","#define texture2DProjLodEXT textureProjLod","#define textureCubeLodEXT textureLod","#define texture2DGradEXT textureGrad","#define texture2DProjGradEXT textureProjGrad","#define textureCubeGradEXT textureGrad"].join(`
`)+`
`+T);let U=M+m+a,W=M+T+o,F=ku(s,s.VERTEX_SHADER,U),B=ku(s,s.FRAGMENT_SHADER,W);s.attachShader(_,F),s.attachShader(_,B),e.index0AttributeName!==void 0?s.bindAttribLocation(_,0,e.index0AttributeName):e.morphTargets===!0&&s.bindAttribLocation(_,0,"position"),s.linkProgram(_);function J(ot){if(i.debug.checkShaderErrors){let Mt=s.getProgramInfoLog(_).trim(),X=s.getShaderInfoLog(F).trim(),K=s.getShaderInfoLog(B).trim(),tt=!0,it=!0;if(s.getProgramParameter(_,s.LINK_STATUS)===!1)if(tt=!1,typeof i.debug.onShaderError=="function")i.debug.onShaderError(s,_,F,B);else{let ft=Gu(s,F,"vertex"),nt=Gu(s,B,"fragment");console.error("THREE.WebGLProgram: Shader Error "+s.getError()+" - VALIDATE_STATUS "+s.getProgramParameter(_,s.VALIDATE_STATUS)+`

Program Info Log: `+Mt+`
`+ft+`
`+nt)}else Mt!==""?console.warn("THREE.WebGLProgram: Program Info Log:",Mt):(X===""||K==="")&&(it=!1);it&&(ot.diagnostics={runnable:tt,programLog:Mt,vertexShader:{log:X,prefix:m},fragmentShader:{log:K,prefix:T}})}s.deleteShader(F),s.deleteShader(B),w=new lr(s,_),L=E_(s,_)}let w;this.getUniforms=function(){return w===void 0&&J(this),w};let L;this.getAttributes=function(){return L===void 0&&J(this),L};let $=e.rendererExtensionParallelShaderCompile===!1;return this.isReady=function(){return $===!1&&($=s.getProgramParameter(_,m_)),$},this.destroy=function(){n.releaseStatesOfProgram(this),s.deleteProgram(_),this.program=void 0},this.type=e.shaderType,this.name=e.shaderName,this.id=g_++,this.cacheKey=t,this.usedTimes=1,this.program=_,this.vertexShader=F,this.fragmentShader=B,this}var F_=0,tl=class{constructor(){this.shaderCache=new Map,this.materialCache=new Map}update(t){let e=t.vertexShader,n=t.fragmentShader,s=this._getShaderStage(e),r=this._getShaderStage(n),a=this._getShaderCacheForMaterial(t);return a.has(s)===!1&&(a.add(s),s.usedTimes++),a.has(r)===!1&&(a.add(r),r.usedTimes++),this}remove(t){let e=this.materialCache.get(t);for(let n of e)n.usedTimes--,n.usedTimes===0&&this.shaderCache.delete(n.code);return this.materialCache.delete(t),this}getVertexShaderID(t){return this._getShaderStage(t.vertexShader).id}getFragmentShaderID(t){return this._getShaderStage(t.fragmentShader).id}dispose(){this.shaderCache.clear(),this.materialCache.clear()}_getShaderCacheForMaterial(t){let e=this.materialCache,n=e.get(t);return n===void 0&&(n=new Set,e.set(t,n)),n}_getShaderStage(t){let e=this.shaderCache,n=e.get(t);return n===void 0&&(n=new el(t),e.set(t,n)),n}},el=class{constructor(t){this.id=F_++,this.code=t,this.usedTimes=0}};function O_(i,t,e,n,s,r,a){let o=new Yr,c=new tl,l=[],h=s.isWebGL2,f=s.logarithmicDepthBuffer,d=s.vertexTextures,p=s.precision,x={MeshDepthMaterial:"depth",MeshDistanceMaterial:"distanceRGBA",MeshNormalMaterial:"normal",MeshBasicMaterial:"basic",MeshLambertMaterial:"lambert",MeshPhongMaterial:"phong",MeshToonMaterial:"toon",MeshStandardMaterial:"physical",MeshPhysicalMaterial:"physical",MeshMatcapMaterial:"matcap",LineBasicMaterial:"basic",LineDashedMaterial:"dashed",PointsMaterial:"points",ShadowMaterial:"shadow",SpriteMaterial:"sprite"};function S(w){return w===0?"uv":`uv${w}`}function _(w,L,$,ot,Mt){let X=ot.fog,K=Mt.geometry,tt=w.isMeshStandardMaterial?ot.environment:null,it=(w.isMeshStandardMaterial?e:t).get(w.envMap||tt),ft=it&&it.mapping===Ua?it.image.height:null,nt=x[w.type];w.precision!==null&&(p=s.getMaxPrecision(w.precision),p!==w.precision&&console.warn("THREE.WebGLProgram.getParameters:",w.precision,"not supported, using",p,"instead."));let ct=K.morphAttributes.position||K.morphAttributes.normal||K.morphAttributes.color,lt=ct!==void 0?ct.length:0,Dt=0;K.morphAttributes.position!==void 0&&(Dt=1),K.morphAttributes.normal!==void 0&&(Dt=2),K.morphAttributes.color!==void 0&&(Dt=3);let st,ut,Nt,Ft;if(nt){let xn=vi[nt];st=xn.vertexShader,ut=xn.fragmentShader}else st=w.vertexShader,ut=w.fragmentShader,c.update(w),Nt=c.getVertexShaderID(w),Ft=c.getFragmentShaderID(w);let Bt=i.getRenderTarget(),se=Mt.isInstancedMesh===!0,Jt=Mt.isBatchedMesh===!0,Wt=!!w.map,le=!!w.matcap,z=!!it,Tt=!!w.aoMap,rt=!!w.lightMap,bt=!!w.bumpMap,ht=!!w.normalMap,qt=!!w.displacementMap,It=!!w.emissiveMap,R=!!w.metalnessMap,b=!!w.roughnessMap,Y=w.anisotropy>0,xt=w.clearcoat>0,mt=w.iridescence>0,gt=w.sheen>0,Gt=w.transmission>0,Lt=Y&&!!w.anisotropyMap,At=xt&&!!w.clearcoatMap,ee=xt&&!!w.clearcoatNormalMap,pe=xt&&!!w.clearcoatRoughnessMap,dt=mt&&!!w.iridescenceMap,Re=mt&&!!w.iridescenceThicknessMap,Se=gt&&!!w.sheenColorMap,Zt=gt&&!!w.sheenRoughnessMap,Kt=!!w.specularMap,Ht=!!w.specularColorMap,ae=!!w.specularIntensityMap,Ie=Gt&&!!w.transmissionMap,Ye=Gt&&!!w.thicknessMap,te=!!w.gradientMap,wt=!!w.alphaMap,k=w.alphaTest>0,Rt=!!w.alphaHash,Ut=!!w.extensions,re=!!K.attributes.uv1,jt=!!K.attributes.uv2,De=!!K.attributes.uv3,Fe=ji;return w.toneMapped&&(Bt===null||Bt.isXRRenderTarget===!0)&&(Fe=i.toneMapping),{isWebGL2:h,shaderID:nt,shaderType:w.type,shaderName:w.name,vertexShader:st,fragmentShader:ut,defines:w.defines,customVertexShaderID:Nt,customFragmentShaderID:Ft,isRawShaderMaterial:w.isRawShaderMaterial===!0,glslVersion:w.glslVersion,precision:p,batching:Jt,instancing:se,instancingColor:se&&Mt.instanceColor!==null,supportsVertexTextures:d,outputColorSpace:Bt===null?i.outputColorSpace:Bt.isXRRenderTarget===!0?Bt.texture.colorSpace:Di,map:Wt,matcap:le,envMap:z,envMapMode:z&&it.mapping,envMapCubeUVHeight:ft,aoMap:Tt,lightMap:rt,bumpMap:bt,normalMap:ht,displacementMap:d&&qt,emissiveMap:It,normalMapObjectSpace:ht&&w.normalMapType===Ul,normalMapTangentSpace:ht&&w.normalMapType===Mf,metalnessMap:R,roughnessMap:b,anisotropy:Y,anisotropyMap:Lt,clearcoat:xt,clearcoatMap:At,clearcoatNormalMap:ee,clearcoatRoughnessMap:pe,iridescence:mt,iridescenceMap:dt,iridescenceThicknessMap:Re,sheen:gt,sheenColorMap:Se,sheenRoughnessMap:Zt,specularMap:Kt,specularColorMap:Ht,specularIntensityMap:ae,transmission:Gt,transmissionMap:Ie,thicknessMap:Ye,gradientMap:te,opaque:w.transparent===!1&&w.blending===ar,alphaMap:wt,alphaTest:k,alphaHash:Rt,combine:w.combine,mapUv:Wt&&S(w.map.channel),aoMapUv:Tt&&S(w.aoMap.channel),lightMapUv:rt&&S(w.lightMap.channel),bumpMapUv:bt&&S(w.bumpMap.channel),normalMapUv:ht&&S(w.normalMap.channel),displacementMapUv:qt&&S(w.displacementMap.channel),emissiveMapUv:It&&S(w.emissiveMap.channel),metalnessMapUv:R&&S(w.metalnessMap.channel),roughnessMapUv:b&&S(w.roughnessMap.channel),anisotropyMapUv:Lt&&S(w.anisotropyMap.channel),clearcoatMapUv:At&&S(w.clearcoatMap.channel),clearcoatNormalMapUv:ee&&S(w.clearcoatNormalMap.channel),clearcoatRoughnessMapUv:pe&&S(w.clearcoatRoughnessMap.channel),iridescenceMapUv:dt&&S(w.iridescenceMap.channel),iridescenceThicknessMapUv:Re&&S(w.iridescenceThicknessMap.channel),sheenColorMapUv:Se&&S(w.sheenColorMap.channel),sheenRoughnessMapUv:Zt&&S(w.sheenRoughnessMap.channel),specularMapUv:Kt&&S(w.specularMap.channel),specularColorMapUv:Ht&&S(w.specularColorMap.channel),specularIntensityMapUv:ae&&S(w.specularIntensityMap.channel),transmissionMapUv:Ie&&S(w.transmissionMap.channel),thicknessMapUv:Ye&&S(w.thicknessMap.channel),alphaMapUv:wt&&S(w.alphaMap.channel),vertexTangents:!!K.attributes.tangent&&(ht||Y),vertexColors:w.vertexColors,vertexAlphas:w.vertexColors===!0&&!!K.attributes.color&&K.attributes.color.itemSize===4,vertexUv1s:re,vertexUv2s:jt,vertexUv3s:De,pointsUvs:Mt.isPoints===!0&&!!K.attributes.uv&&(Wt||wt),fog:!!X,useFog:w.fog===!0,fogExp2:X&&X.isFogExp2,flatShading:w.flatShading===!0,sizeAttenuation:w.sizeAttenuation===!0,logarithmicDepthBuffer:f,skinning:Mt.isSkinnedMesh===!0,morphTargets:K.morphAttributes.position!==void 0,morphNormals:K.morphAttributes.normal!==void 0,morphColors:K.morphAttributes.color!==void 0,morphTargetsCount:lt,morphTextureStride:Dt,numDirLights:L.directional.length,numPointLights:L.point.length,numSpotLights:L.spot.length,numSpotLightMaps:L.spotLightMap.length,numRectAreaLights:L.rectArea.length,numHemiLights:L.hemi.length,numDirLightShadows:L.directionalShadowMap.length,numPointLightShadows:L.pointShadowMap.length,numSpotLightShadows:L.spotShadowMap.length,numSpotLightShadowsWithMaps:L.numSpotLightShadowsWithMaps,numLightProbes:L.numLightProbes,numClippingPlanes:a.numPlanes,numClipIntersection:a.numIntersection,dithering:w.dithering,shadowMapEnabled:i.shadowMap.enabled&&$.length>0,shadowMapType:i.shadowMap.type,toneMapping:Fe,useLegacyLights:i._useLegacyLights,decodeVideoTexture:Wt&&w.map.isVideoTexture===!0&&Be.getTransfer(w.map.colorSpace)===Xe,premultipliedAlpha:w.premultipliedAlpha,doubleSided:w.side===ln,flipSided:w.side===Tn,useDepthPacking:w.depthPacking>=0,depthPacking:w.depthPacking||0,index0AttributeName:w.index0AttributeName,extensionDerivatives:Ut&&w.extensions.derivatives===!0,extensionFragDepth:Ut&&w.extensions.fragDepth===!0,extensionDrawBuffers:Ut&&w.extensions.drawBuffers===!0,extensionShaderTextureLOD:Ut&&w.extensions.shaderTextureLOD===!0,extensionClipCullDistance:Ut&&w.extensions.clipCullDistance&&n.has("WEBGL_clip_cull_distance"),rendererExtensionFragDepth:h||n.has("EXT_frag_depth"),rendererExtensionDrawBuffers:h||n.has("WEBGL_draw_buffers"),rendererExtensionShaderTextureLod:h||n.has("EXT_shader_texture_lod"),rendererExtensionParallelShaderCompile:n.has("KHR_parallel_shader_compile"),customProgramCacheKey:w.customProgramCacheKey()}}function m(w){let L=[];if(w.shaderID?L.push(w.shaderID):(L.push(w.customVertexShaderID),L.push(w.customFragmentShaderID)),w.defines!==void 0)for(let $ in w.defines)L.push($),L.push(w.defines[$]);return w.isRawShaderMaterial===!1&&(T(L,w),M(L,w),L.push(i.outputColorSpace)),L.push(w.customProgramCacheKey),L.join()}function T(w,L){w.push(L.precision),w.push(L.outputColorSpace),w.push(L.envMapMode),w.push(L.envMapCubeUVHeight),w.push(L.mapUv),w.push(L.alphaMapUv),w.push(L.lightMapUv),w.push(L.aoMapUv),w.push(L.bumpMapUv),w.push(L.normalMapUv),w.push(L.displacementMapUv),w.push(L.emissiveMapUv),w.push(L.metalnessMapUv),w.push(L.roughnessMapUv),w.push(L.anisotropyMapUv),w.push(L.clearcoatMapUv),w.push(L.clearcoatNormalMapUv),w.push(L.clearcoatRoughnessMapUv),w.push(L.iridescenceMapUv),w.push(L.iridescenceThicknessMapUv),w.push(L.sheenColorMapUv),w.push(L.sheenRoughnessMapUv),w.push(L.specularMapUv),w.push(L.specularColorMapUv),w.push(L.specularIntensityMapUv),w.push(L.transmissionMapUv),w.push(L.thicknessMapUv),w.push(L.combine),w.push(L.fogExp2),w.push(L.sizeAttenuation),w.push(L.morphTargetsCount),w.push(L.morphAttributeCount),w.push(L.numDirLights),w.push(L.numPointLights),w.push(L.numSpotLights),w.push(L.numSpotLightMaps),w.push(L.numHemiLights),w.push(L.numRectAreaLights),w.push(L.numDirLightShadows),w.push(L.numPointLightShadows),w.push(L.numSpotLightShadows),w.push(L.numSpotLightShadowsWithMaps),w.push(L.numLightProbes),w.push(L.shadowMapType),w.push(L.toneMapping),w.push(L.numClippingPlanes),w.push(L.numClipIntersection),w.push(L.depthPacking)}function M(w,L){o.disableAll(),L.isWebGL2&&o.enable(0),L.supportsVertexTextures&&o.enable(1),L.instancing&&o.enable(2),L.instancingColor&&o.enable(3),L.matcap&&o.enable(4),L.envMap&&o.enable(5),L.normalMapObjectSpace&&o.enable(6),L.normalMapTangentSpace&&o.enable(7),L.clearcoat&&o.enable(8),L.iridescence&&o.enable(9),L.alphaTest&&o.enable(10),L.vertexColors&&o.enable(11),L.vertexAlphas&&o.enable(12),L.vertexUv1s&&o.enable(13),L.vertexUv2s&&o.enable(14),L.vertexUv3s&&o.enable(15),L.vertexTangents&&o.enable(16),L.anisotropy&&o.enable(17),L.alphaHash&&o.enable(18),L.batching&&o.enable(19),w.push(o.mask),o.disableAll(),L.fog&&o.enable(0),L.useFog&&o.enable(1),L.flatShading&&o.enable(2),L.logarithmicDepthBuffer&&o.enable(3),L.skinning&&o.enable(4),L.morphTargets&&o.enable(5),L.morphNormals&&o.enable(6),L.morphColors&&o.enable(7),L.premultipliedAlpha&&o.enable(8),L.shadowMapEnabled&&o.enable(9),L.useLegacyLights&&o.enable(10),L.doubleSided&&o.enable(11),L.flipSided&&o.enable(12),L.useDepthPacking&&o.enable(13),L.dithering&&o.enable(14),L.transmission&&o.enable(15),L.sheen&&o.enable(16),L.opaque&&o.enable(17),L.pointsUvs&&o.enable(18),L.decodeVideoTexture&&o.enable(19),w.push(o.mask)}function U(w){let L=x[w.type],$;if(L){let ot=vi[L];$=Fl.clone(ot.uniforms)}else $=w.uniforms;return $}function W(w,L){let $;for(let ot=0,Mt=l.length;ot<Mt;ot++){let X=l[ot];if(X.cacheKey===L){$=X,++$.usedTimes;break}}return $===void 0&&($=new N_(i,L,w,r),l.push($)),$}function F(w){if(--w.usedTimes===0){let L=l.indexOf(w);l[L]=l[l.length-1],l.pop(),w.destroy()}}function B(w){c.remove(w)}function J(){c.dispose()}return{getParameters:_,getProgramCacheKey:m,getUniforms:U,acquireProgram:W,releaseProgram:F,releaseShaderCache:B,programs:l,dispose:J}}function B_(){let i=new WeakMap;function t(r){let a=i.get(r);return a===void 0&&(a={},i.set(r,a)),a}function e(r){i.delete(r)}function n(r,a,o){i.get(r)[a]=o}function s(){i=new WeakMap}return{get:t,remove:e,update:n,dispose:s}}function z_(i,t){return i.groupOrder!==t.groupOrder?i.groupOrder-t.groupOrder:i.renderOrder!==t.renderOrder?i.renderOrder-t.renderOrder:i.material.id!==t.material.id?i.material.id-t.material.id:i.z!==t.z?i.z-t.z:i.id-t.id}function qu(i,t){return i.groupOrder!==t.groupOrder?i.groupOrder-t.groupOrder:i.renderOrder!==t.renderOrder?i.renderOrder-t.renderOrder:i.z!==t.z?t.z-i.z:i.id-t.id}function Zu(){let i=[],t=0,e=[],n=[],s=[];function r(){t=0,e.length=0,n.length=0,s.length=0}function a(f,d,p,x,S,_){let m=i[t];return m===void 0?(m={id:f.id,object:f,geometry:d,material:p,groupOrder:x,renderOrder:f.renderOrder,z:S,group:_},i[t]=m):(m.id=f.id,m.object=f,m.geometry=d,m.material=p,m.groupOrder=x,m.renderOrder=f.renderOrder,m.z=S,m.group=_),t++,m}function o(f,d,p,x,S,_){let m=a(f,d,p,x,S,_);p.transmission>0?n.push(m):p.transparent===!0?s.push(m):e.push(m)}function c(f,d,p,x,S,_){let m=a(f,d,p,x,S,_);p.transmission>0?n.unshift(m):p.transparent===!0?s.unshift(m):e.unshift(m)}function l(f,d){e.length>1&&e.sort(f||z_),n.length>1&&n.sort(d||qu),s.length>1&&s.sort(d||qu)}function h(){for(let f=t,d=i.length;f<d;f++){let p=i[f];if(p.id===null)break;p.id=null,p.object=null,p.geometry=null,p.material=null,p.group=null}}return{opaque:e,transmissive:n,transparent:s,init:r,push:o,unshift:c,finish:h,sort:l}}function H_(){let i=new WeakMap;function t(n,s){let r=i.get(n),a;return r===void 0?(a=new Zu,i.set(n,[a])):s>=r.length?(a=new Zu,r.push(a)):a=r[s],a}function e(){i=new WeakMap}return{get:t,dispose:e}}function k_(){let i={};return{get:function(t){if(i[t.id]!==void 0)return i[t.id];let e;switch(t.type){case"DirectionalLight":e={direction:new O,color:new fe};break;case"SpotLight":e={position:new O,direction:new O,color:new fe,distance:0,coneCos:0,penumbraCos:0,decay:0};break;case"PointLight":e={position:new O,color:new fe,distance:0,decay:0};break;case"HemisphereLight":e={direction:new O,skyColor:new fe,groundColor:new fe};break;case"RectAreaLight":e={color:new fe,position:new O,halfWidth:new O,halfHeight:new O};break}return i[t.id]=e,e}}}function G_(){let i={};return{get:function(t){if(i[t.id]!==void 0)return i[t.id];let e;switch(t.type){case"DirectionalLight":e={shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new St};break;case"SpotLight":e={shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new St};break;case"PointLight":e={shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new St,shadowCameraNear:1,shadowCameraFar:1e3};break}return i[t.id]=e,e}}}var V_=0;function W_(i,t){return(t.castShadow?2:0)-(i.castShadow?2:0)+(t.map?1:0)-(i.map?1:0)}function X_(i,t){let e=new k_,n=G_(),s={version:0,hash:{directionalLength:-1,pointLength:-1,spotLength:-1,rectAreaLength:-1,hemiLength:-1,numDirectionalShadows:-1,numPointShadows:-1,numSpotShadows:-1,numSpotMaps:-1,numLightProbes:-1},ambient:[0,0,0],probe:[],directional:[],directionalShadow:[],directionalShadowMap:[],directionalShadowMatrix:[],spot:[],spotLightMap:[],spotShadow:[],spotShadowMap:[],spotLightMatrix:[],rectArea:[],rectAreaLTC1:null,rectAreaLTC2:null,point:[],pointShadow:[],pointShadowMap:[],pointShadowMatrix:[],hemi:[],numSpotLightShadowsWithMaps:0,numLightProbes:0};for(let h=0;h<9;h++)s.probe.push(new O);let r=new O,a=new Ue,o=new Ue;function c(h,f){let d=0,p=0,x=0;for(let ot=0;ot<9;ot++)s.probe[ot].set(0,0,0);let S=0,_=0,m=0,T=0,M=0,U=0,W=0,F=0,B=0,J=0,w=0;h.sort(W_);let L=f===!0?Math.PI:1;for(let ot=0,Mt=h.length;ot<Mt;ot++){let X=h[ot],K=X.color,tt=X.intensity,it=X.distance,ft=X.shadow&&X.shadow.map?X.shadow.map.texture:null;if(X.isAmbientLight)d+=K.r*tt*L,p+=K.g*tt*L,x+=K.b*tt*L;else if(X.isLightProbe){for(let nt=0;nt<9;nt++)s.probe[nt].addScaledVector(X.sh.coefficients[nt],tt);w++}else if(X.isDirectionalLight){let nt=e.get(X);if(nt.color.copy(X.color).multiplyScalar(X.intensity*L),X.castShadow){let ct=X.shadow,lt=n.get(X);lt.shadowBias=ct.bias,lt.shadowNormalBias=ct.normalBias,lt.shadowRadius=ct.radius,lt.shadowMapSize=ct.mapSize,s.directionalShadow[S]=lt,s.directionalShadowMap[S]=ft,s.directionalShadowMatrix[S]=X.shadow.matrix,U++}s.directional[S]=nt,S++}else if(X.isSpotLight){let nt=e.get(X);nt.position.setFromMatrixPosition(X.matrixWorld),nt.color.copy(K).multiplyScalar(tt*L),nt.distance=it,nt.coneCos=Math.cos(X.angle),nt.penumbraCos=Math.cos(X.angle*(1-X.penumbra)),nt.decay=X.decay,s.spot[m]=nt;let ct=X.shadow;if(X.map&&(s.spotLightMap[B]=X.map,B++,ct.updateMatrices(X),X.castShadow&&J++),s.spotLightMatrix[m]=ct.matrix,X.castShadow){let lt=n.get(X);lt.shadowBias=ct.bias,lt.shadowNormalBias=ct.normalBias,lt.shadowRadius=ct.radius,lt.shadowMapSize=ct.mapSize,s.spotShadow[m]=lt,s.spotShadowMap[m]=ft,F++}m++}else if(X.isRectAreaLight){let nt=e.get(X);nt.color.copy(K).multiplyScalar(tt),nt.halfWidth.set(X.width*.5,0,0),nt.halfHeight.set(0,X.height*.5,0),s.rectArea[T]=nt,T++}else if(X.isPointLight){let nt=e.get(X);if(nt.color.copy(X.color).multiplyScalar(X.intensity*L),nt.distance=X.distance,nt.decay=X.decay,X.castShadow){let ct=X.shadow,lt=n.get(X);lt.shadowBias=ct.bias,lt.shadowNormalBias=ct.normalBias,lt.shadowRadius=ct.radius,lt.shadowMapSize=ct.mapSize,lt.shadowCameraNear=ct.camera.near,lt.shadowCameraFar=ct.camera.far,s.pointShadow[_]=lt,s.pointShadowMap[_]=ft,s.pointShadowMatrix[_]=X.shadow.matrix,W++}s.point[_]=nt,_++}else if(X.isHemisphereLight){let nt=e.get(X);nt.skyColor.copy(X.color).multiplyScalar(tt*L),nt.groundColor.copy(X.groundColor).multiplyScalar(tt*L),s.hemi[M]=nt,M++}}T>0&&(t.isWebGL2?i.has("OES_texture_float_linear")===!0?(s.rectAreaLTC1=Pt.LTC_FLOAT_1,s.rectAreaLTC2=Pt.LTC_FLOAT_2):(s.rectAreaLTC1=Pt.LTC_HALF_1,s.rectAreaLTC2=Pt.LTC_HALF_2):i.has("OES_texture_float_linear")===!0?(s.rectAreaLTC1=Pt.LTC_FLOAT_1,s.rectAreaLTC2=Pt.LTC_FLOAT_2):i.has("OES_texture_half_float_linear")===!0?(s.rectAreaLTC1=Pt.LTC_HALF_1,s.rectAreaLTC2=Pt.LTC_HALF_2):console.error("THREE.WebGLRenderer: Unable to use RectAreaLight. Missing WebGL extensions.")),s.ambient[0]=d,s.ambient[1]=p,s.ambient[2]=x;let $=s.hash;($.directionalLength!==S||$.pointLength!==_||$.spotLength!==m||$.rectAreaLength!==T||$.hemiLength!==M||$.numDirectionalShadows!==U||$.numPointShadows!==W||$.numSpotShadows!==F||$.numSpotMaps!==B||$.numLightProbes!==w)&&(s.directional.length=S,s.spot.length=m,s.rectArea.length=T,s.point.length=_,s.hemi.length=M,s.directionalShadow.length=U,s.directionalShadowMap.length=U,s.pointShadow.length=W,s.pointShadowMap.length=W,s.spotShadow.length=F,s.spotShadowMap.length=F,s.directionalShadowMatrix.length=U,s.pointShadowMatrix.length=W,s.spotLightMatrix.length=F+B-J,s.spotLightMap.length=B,s.numSpotLightShadowsWithMaps=J,s.numLightProbes=w,$.directionalLength=S,$.pointLength=_,$.spotLength=m,$.rectAreaLength=T,$.hemiLength=M,$.numDirectionalShadows=U,$.numPointShadows=W,$.numSpotShadows=F,$.numSpotMaps=B,$.numLightProbes=w,s.version=V_++)}function l(h,f){let d=0,p=0,x=0,S=0,_=0,m=f.matrixWorldInverse;for(let T=0,M=h.length;T<M;T++){let U=h[T];if(U.isDirectionalLight){let W=s.directional[d];W.direction.setFromMatrixPosition(U.matrixWorld),r.setFromMatrixPosition(U.target.matrixWorld),W.direction.sub(r),W.direction.transformDirection(m),d++}else if(U.isSpotLight){let W=s.spot[x];W.position.setFromMatrixPosition(U.matrixWorld),W.position.applyMatrix4(m),W.direction.setFromMatrixPosition(U.matrixWorld),r.setFromMatrixPosition(U.target.matrixWorld),W.direction.sub(r),W.direction.transformDirection(m),x++}else if(U.isRectAreaLight){let W=s.rectArea[S];W.position.setFromMatrixPosition(U.matrixWorld),W.position.applyMatrix4(m),o.identity(),a.copy(U.matrixWorld),a.premultiply(m),o.extractRotation(a),W.halfWidth.set(U.width*.5,0,0),W.halfHeight.set(0,U.height*.5,0),W.halfWidth.applyMatrix4(o),W.halfHeight.applyMatrix4(o),S++}else if(U.isPointLight){let W=s.point[p];W.position.setFromMatrixPosition(U.matrixWorld),W.position.applyMatrix4(m),p++}else if(U.isHemisphereLight){let W=s.hemi[_];W.direction.setFromMatrixPosition(U.matrixWorld),W.direction.transformDirection(m),_++}}}return{setup:c,setupView:l,state:s}}function $u(i,t){let e=new X_(i,t),n=[],s=[];function r(){n.length=0,s.length=0}function a(f){n.push(f)}function o(f){s.push(f)}function c(f){e.setup(n,f)}function l(f){e.setupView(n,f)}return{init:r,state:{lightsArray:n,shadowsArray:s,lights:e},setupLights:c,setupLightsView:l,pushLight:a,pushShadow:o}}function Y_(i,t){let e=new WeakMap;function n(r,a=0){let o=e.get(r),c;return o===void 0?(c=new $u(i,t),e.set(r,[c])):a>=o.length?(c=new $u(i,t),o.push(c)):c=o[a],c}function s(){e=new WeakMap}return{get:n,dispose:s}}var nl=class extends yi{constructor(t){super(),this.isMeshDepthMaterial=!0,this.type="MeshDepthMaterial",this.depthPacking=Gd,this.map=null,this.alphaMap=null,this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.wireframe=!1,this.wireframeLinewidth=1,this.setValues(t)}copy(t){return super.copy(t),this.depthPacking=t.depthPacking,this.map=t.map,this.alphaMap=t.alphaMap,this.displacementMap=t.displacementMap,this.displacementScale=t.displacementScale,this.displacementBias=t.displacementBias,this.wireframe=t.wireframe,this.wireframeLinewidth=t.wireframeLinewidth,this}},il=class extends yi{constructor(t){super(),this.isMeshDistanceMaterial=!0,this.type="MeshDistanceMaterial",this.map=null,this.alphaMap=null,this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.setValues(t)}copy(t){return super.copy(t),this.map=t.map,this.alphaMap=t.alphaMap,this.displacementMap=t.displacementMap,this.displacementScale=t.displacementScale,this.displacementBias=t.displacementBias,this}},q_=`void main() {
	gl_Position = vec4( position, 1.0 );
}`,Z_=`uniform sampler2D shadow_pass;
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
}`;function $_(i,t,e){let n=new qr,s=new St,r=new St,a=new Je,o=new nl({depthPacking:Vd}),c=new il,l={},h=e.maxTextureSize,f={[es]:Tn,[Tn]:es,[ln]:ln},d=new Sn({defines:{VSM_SAMPLES:8},uniforms:{shadow_pass:{value:null},resolution:{value:new St},radius:{value:4}},vertexShader:q_,fragmentShader:Z_}),p=d.clone();p.defines.HORIZONTAL_PASS=1;let x=new Ke;x.setAttribute("position",new Mn(new Float32Array([-1,-1,.5,3,-1,.5,-1,3,.5]),3));let S=new Ne(x,d),_=this;this.enabled=!1,this.autoUpdate=!0,this.needsUpdate=!1,this.type=hf;let m=this.type;this.render=function(F,B,J){if(_.enabled===!1||_.autoUpdate===!1&&_.needsUpdate===!1||F.length===0)return;let w=i.getRenderTarget(),L=i.getActiveCubeFace(),$=i.getActiveMipmapLevel(),ot=i.state;ot.setBlending(Ki),ot.buffers.color.setClear(1,1,1,1),ot.buffers.depth.setTest(!0),ot.setScissorTest(!1);let Mt=m!==Ii&&this.type===Ii,X=m===Ii&&this.type!==Ii;for(let K=0,tt=F.length;K<tt;K++){let it=F[K],ft=it.shadow;if(ft===void 0){console.warn("THREE.WebGLShadowMap:",it,"has no shadow.");continue}if(ft.autoUpdate===!1&&ft.needsUpdate===!1)continue;s.copy(ft.mapSize);let nt=ft.getFrameExtents();if(s.multiply(nt),r.copy(ft.mapSize),(s.x>h||s.y>h)&&(s.x>h&&(r.x=Math.floor(h/nt.x),s.x=r.x*nt.x,ft.mapSize.x=r.x),s.y>h&&(r.y=Math.floor(h/nt.y),s.y=r.y*nt.y,ft.mapSize.y=r.y)),ft.map===null||Mt===!0||X===!0){let lt=this.type!==Ii?{minFilter:In,magFilter:In}:{};ft.map!==null&&ft.map.dispose(),ft.map=new Ni(s.x,s.y,lt),ft.map.texture.name=it.name+".shadowMap",ft.camera.updateProjectionMatrix()}i.setRenderTarget(ft.map),i.clear();let ct=ft.getViewportCount();for(let lt=0;lt<ct;lt++){let Dt=ft.getViewport(lt);a.set(r.x*Dt.x,r.y*Dt.y,r.x*Dt.z,r.y*Dt.w),ot.viewport(a),ft.updateMatrices(it,lt),n=ft.getFrustum(),U(B,J,ft.camera,it,this.type)}ft.isPointLightShadow!==!0&&this.type===Ii&&T(ft,J),ft.needsUpdate=!1}m=this.type,_.needsUpdate=!1,i.setRenderTarget(w,L,$)};function T(F,B){let J=t.update(S);d.defines.VSM_SAMPLES!==F.blurSamples&&(d.defines.VSM_SAMPLES=F.blurSamples,p.defines.VSM_SAMPLES=F.blurSamples,d.needsUpdate=!0,p.needsUpdate=!0),F.mapPass===null&&(F.mapPass=new Ni(s.x,s.y)),d.uniforms.shadow_pass.value=F.map.texture,d.uniforms.resolution.value=F.mapSize,d.uniforms.radius.value=F.radius,i.setRenderTarget(F.mapPass),i.clear(),i.renderBufferDirect(B,null,J,d,S,null),p.uniforms.shadow_pass.value=F.mapPass.texture,p.uniforms.resolution.value=F.mapSize,p.uniforms.radius.value=F.radius,i.setRenderTarget(F.map),i.clear(),i.renderBufferDirect(B,null,J,p,S,null)}function M(F,B,J,w){let L=null,$=J.isPointLight===!0?F.customDistanceMaterial:F.customDepthMaterial;if($!==void 0)L=$;else if(L=J.isPointLight===!0?c:o,i.localClippingEnabled&&B.clipShadows===!0&&Array.isArray(B.clippingPlanes)&&B.clippingPlanes.length!==0||B.displacementMap&&B.displacementScale!==0||B.alphaMap&&B.alphaTest>0||B.map&&B.alphaTest>0){let ot=L.uuid,Mt=B.uuid,X=l[ot];X===void 0&&(X={},l[ot]=X);let K=X[Mt];K===void 0&&(K=L.clone(),X[Mt]=K,B.addEventListener("dispose",W)),L=K}if(L.visible=B.visible,L.wireframe=B.wireframe,w===Ii?L.side=B.shadowSide!==null?B.shadowSide:B.side:L.side=B.shadowSide!==null?B.shadowSide:f[B.side],L.alphaMap=B.alphaMap,L.alphaTest=B.alphaTest,L.map=B.map,L.clipShadows=B.clipShadows,L.clippingPlanes=B.clippingPlanes,L.clipIntersection=B.clipIntersection,L.displacementMap=B.displacementMap,L.displacementScale=B.displacementScale,L.displacementBias=B.displacementBias,L.wireframeLinewidth=B.wireframeLinewidth,L.linewidth=B.linewidth,J.isPointLight===!0&&L.isMeshDistanceMaterial===!0){let ot=i.properties.get(L);ot.light=J}return L}function U(F,B,J,w,L){if(F.visible===!1)return;if(F.layers.test(B.layers)&&(F.isMesh||F.isLine||F.isPoints)&&(F.castShadow||F.receiveShadow&&L===Ii)&&(!F.frustumCulled||n.intersectsObject(F))){F.modelViewMatrix.multiplyMatrices(J.matrixWorldInverse,F.matrixWorld);let Mt=t.update(F),X=F.material;if(Array.isArray(X)){let K=Mt.groups;for(let tt=0,it=K.length;tt<it;tt++){let ft=K[tt],nt=X[ft.materialIndex];if(nt&&nt.visible){let ct=M(F,nt,w,L);F.onBeforeShadow(i,F,B,J,Mt,ct,ft),i.renderBufferDirect(J,null,Mt,ct,F,ft),F.onAfterShadow(i,F,B,J,Mt,ct,ft)}}}else if(X.visible){let K=M(F,X,w,L);F.onBeforeShadow(i,F,B,J,Mt,K,null),i.renderBufferDirect(J,null,Mt,K,F,null),F.onAfterShadow(i,F,B,J,Mt,K,null)}}let ot=F.children;for(let Mt=0,X=ot.length;Mt<X;Mt++)U(ot[Mt],B,J,w,L)}function W(F){F.target.removeEventListener("dispose",W);for(let J in l){let w=l[J],L=F.target.uuid;L in w&&(w[L].dispose(),delete w[L])}}}function J_(i,t,e){let n=e.isWebGL2;function s(){let k=!1,Rt=new Je,Ut=null,re=new Je(0,0,0,0);return{setMask:function(jt){Ut!==jt&&!k&&(i.colorMask(jt,jt,jt,jt),Ut=jt)},setLocked:function(jt){k=jt},setClear:function(jt,De,Fe,rn,xn){xn===!0&&(jt*=rn,De*=rn,Fe*=rn),Rt.set(jt,De,Fe,rn),re.equals(Rt)===!1&&(i.clearColor(jt,De,Fe,rn),re.copy(Rt))},reset:function(){k=!1,Ut=null,re.set(-1,0,0,0)}}}function r(){let k=!1,Rt=null,Ut=null,re=null;return{setTest:function(jt){jt?Jt(i.DEPTH_TEST):Wt(i.DEPTH_TEST)},setMask:function(jt){Rt!==jt&&!k&&(i.depthMask(jt),Rt=jt)},setFunc:function(jt){if(Ut!==jt){switch(jt){case vd:i.depthFunc(i.NEVER);break;case yd:i.depthFunc(i.ALWAYS);break;case Md:i.depthFunc(i.LESS);break;case ea:i.depthFunc(i.LEQUAL);break;case Sd:i.depthFunc(i.EQUAL);break;case bd:i.depthFunc(i.GEQUAL);break;case Ed:i.depthFunc(i.GREATER);break;case wd:i.depthFunc(i.NOTEQUAL);break;default:i.depthFunc(i.LEQUAL)}Ut=jt}},setLocked:function(jt){k=jt},setClear:function(jt){re!==jt&&(i.clearDepth(jt),re=jt)},reset:function(){k=!1,Rt=null,Ut=null,re=null}}}function a(){let k=!1,Rt=null,Ut=null,re=null,jt=null,De=null,Fe=null,rn=null,xn=null;return{setTest:function(Ce){k||(Ce?Jt(i.STENCIL_TEST):Wt(i.STENCIL_TEST))},setMask:function(Ce){Rt!==Ce&&!k&&(i.stencilMask(Ce),Rt=Ce)},setFunc:function(Ce,fn,Gn){(Ut!==Ce||re!==fn||jt!==Gn)&&(i.stencilFunc(Ce,fn,Gn),Ut=Ce,re=fn,jt=Gn)},setOp:function(Ce,fn,Gn){(De!==Ce||Fe!==fn||rn!==Gn)&&(i.stencilOp(Ce,fn,Gn),De=Ce,Fe=fn,rn=Gn)},setLocked:function(Ce){k=Ce},setClear:function(Ce){xn!==Ce&&(i.clearStencil(Ce),xn=Ce)},reset:function(){k=!1,Rt=null,Ut=null,re=null,jt=null,De=null,Fe=null,rn=null,xn=null}}}let o=new s,c=new r,l=new a,h=new WeakMap,f=new WeakMap,d={},p={},x=new WeakMap,S=[],_=null,m=!1,T=null,M=null,U=null,W=null,F=null,B=null,J=null,w=new fe(0,0,0),L=0,$=!1,ot=null,Mt=null,X=null,K=null,tt=null,it=i.getParameter(i.MAX_COMBINED_TEXTURE_IMAGE_UNITS),ft=!1,nt=0,ct=i.getParameter(i.VERSION);ct.indexOf("WebGL")!==-1?(nt=parseFloat(/^WebGL (\d)/.exec(ct)[1]),ft=nt>=1):ct.indexOf("OpenGL ES")!==-1&&(nt=parseFloat(/^OpenGL ES (\d)/.exec(ct)[1]),ft=nt>=2);let lt=null,Dt={},st=i.getParameter(i.SCISSOR_BOX),ut=i.getParameter(i.VIEWPORT),Nt=new Je().fromArray(st),Ft=new Je().fromArray(ut);function Bt(k,Rt,Ut,re){let jt=new Uint8Array(4),De=i.createTexture();i.bindTexture(k,De),i.texParameteri(k,i.TEXTURE_MIN_FILTER,i.NEAREST),i.texParameteri(k,i.TEXTURE_MAG_FILTER,i.NEAREST);for(let Fe=0;Fe<Ut;Fe++)n&&(k===i.TEXTURE_3D||k===i.TEXTURE_2D_ARRAY)?i.texImage3D(Rt,0,i.RGBA,1,1,re,0,i.RGBA,i.UNSIGNED_BYTE,jt):i.texImage2D(Rt+Fe,0,i.RGBA,1,1,0,i.RGBA,i.UNSIGNED_BYTE,jt);return De}let se={};se[i.TEXTURE_2D]=Bt(i.TEXTURE_2D,i.TEXTURE_2D,1),se[i.TEXTURE_CUBE_MAP]=Bt(i.TEXTURE_CUBE_MAP,i.TEXTURE_CUBE_MAP_POSITIVE_X,6),n&&(se[i.TEXTURE_2D_ARRAY]=Bt(i.TEXTURE_2D_ARRAY,i.TEXTURE_2D_ARRAY,1,1),se[i.TEXTURE_3D]=Bt(i.TEXTURE_3D,i.TEXTURE_3D,1,1)),o.setClear(0,0,0,1),c.setClear(1),l.setClear(0),Jt(i.DEPTH_TEST),c.setFunc(ea),It(!1),R(Ch),Jt(i.CULL_FACE),ht(Ki);function Jt(k){d[k]!==!0&&(i.enable(k),d[k]=!0)}function Wt(k){d[k]!==!1&&(i.disable(k),d[k]=!1)}function le(k,Rt){return p[k]!==Rt?(i.bindFramebuffer(k,Rt),p[k]=Rt,n&&(k===i.DRAW_FRAMEBUFFER&&(p[i.FRAMEBUFFER]=Rt),k===i.FRAMEBUFFER&&(p[i.DRAW_FRAMEBUFFER]=Rt)),!0):!1}function z(k,Rt){let Ut=S,re=!1;if(k)if(Ut=x.get(Rt),Ut===void 0&&(Ut=[],x.set(Rt,Ut)),k.isWebGLMultipleRenderTargets){let jt=k.texture;if(Ut.length!==jt.length||Ut[0]!==i.COLOR_ATTACHMENT0){for(let De=0,Fe=jt.length;De<Fe;De++)Ut[De]=i.COLOR_ATTACHMENT0+De;Ut.length=jt.length,re=!0}}else Ut[0]!==i.COLOR_ATTACHMENT0&&(Ut[0]=i.COLOR_ATTACHMENT0,re=!0);else Ut[0]!==i.BACK&&(Ut[0]=i.BACK,re=!0);re&&(e.isWebGL2?i.drawBuffers(Ut):t.get("WEBGL_draw_buffers").drawBuffersWEBGL(Ut))}function Tt(k){return _!==k?(i.useProgram(k),_=k,!0):!1}let rt={[xs]:i.FUNC_ADD,[sd]:i.FUNC_SUBTRACT,[rd]:i.FUNC_REVERSE_SUBTRACT};if(n)rt[Lh]=i.MIN,rt[Uh]=i.MAX;else{let k=t.get("EXT_blend_minmax");k!==null&&(rt[Lh]=k.MIN_EXT,rt[Uh]=k.MAX_EXT)}let bt={[od]:i.ZERO,[ad]:i.ONE,[cd]:i.SRC_COLOR,[zc]:i.SRC_ALPHA,[pd]:i.SRC_ALPHA_SATURATE,[fd]:i.DST_COLOR,[hd]:i.DST_ALPHA,[ld]:i.ONE_MINUS_SRC_COLOR,[Hc]:i.ONE_MINUS_SRC_ALPHA,[dd]:i.ONE_MINUS_DST_COLOR,[ud]:i.ONE_MINUS_DST_ALPHA,[md]:i.CONSTANT_COLOR,[gd]:i.ONE_MINUS_CONSTANT_COLOR,[_d]:i.CONSTANT_ALPHA,[xd]:i.ONE_MINUS_CONSTANT_ALPHA};function ht(k,Rt,Ut,re,jt,De,Fe,rn,xn,Ce){if(k===Ki){m===!0&&(Wt(i.BLEND),m=!1);return}if(m===!1&&(Jt(i.BLEND),m=!0),k!==id){if(k!==T||Ce!==$){if((M!==xs||F!==xs)&&(i.blendEquation(i.FUNC_ADD),M=xs,F=xs),Ce)switch(k){case ar:i.blendFuncSeparate(i.ONE,i.ONE_MINUS_SRC_ALPHA,i.ONE,i.ONE_MINUS_SRC_ALPHA);break;case hr:i.blendFunc(i.ONE,i.ONE);break;case Ph:i.blendFuncSeparate(i.ZERO,i.ONE_MINUS_SRC_COLOR,i.ZERO,i.ONE);break;case Ih:i.blendFuncSeparate(i.ZERO,i.SRC_COLOR,i.ZERO,i.SRC_ALPHA);break;default:console.error("THREE.WebGLState: Invalid blending: ",k);break}else switch(k){case ar:i.blendFuncSeparate(i.SRC_ALPHA,i.ONE_MINUS_SRC_ALPHA,i.ONE,i.ONE_MINUS_SRC_ALPHA);break;case hr:i.blendFunc(i.SRC_ALPHA,i.ONE);break;case Ph:i.blendFuncSeparate(i.ZERO,i.ONE_MINUS_SRC_COLOR,i.ZERO,i.ONE);break;case Ih:i.blendFunc(i.ZERO,i.SRC_COLOR);break;default:console.error("THREE.WebGLState: Invalid blending: ",k);break}U=null,W=null,B=null,J=null,w.set(0,0,0),L=0,T=k,$=Ce}return}jt=jt||Rt,De=De||Ut,Fe=Fe||re,(Rt!==M||jt!==F)&&(i.blendEquationSeparate(rt[Rt],rt[jt]),M=Rt,F=jt),(Ut!==U||re!==W||De!==B||Fe!==J)&&(i.blendFuncSeparate(bt[Ut],bt[re],bt[De],bt[Fe]),U=Ut,W=re,B=De,J=Fe),(rn.equals(w)===!1||xn!==L)&&(i.blendColor(rn.r,rn.g,rn.b,xn),w.copy(rn),L=xn),T=k,$=!1}function qt(k,Rt){k.side===ln?Wt(i.CULL_FACE):Jt(i.CULL_FACE);let Ut=k.side===Tn;Rt&&(Ut=!Ut),It(Ut),k.blending===ar&&k.transparent===!1?ht(Ki):ht(k.blending,k.blendEquation,k.blendSrc,k.blendDst,k.blendEquationAlpha,k.blendSrcAlpha,k.blendDstAlpha,k.blendColor,k.blendAlpha,k.premultipliedAlpha),c.setFunc(k.depthFunc),c.setTest(k.depthTest),c.setMask(k.depthWrite),o.setMask(k.colorWrite);let re=k.stencilWrite;l.setTest(re),re&&(l.setMask(k.stencilWriteMask),l.setFunc(k.stencilFunc,k.stencilRef,k.stencilFuncMask),l.setOp(k.stencilFail,k.stencilZFail,k.stencilZPass)),Y(k.polygonOffset,k.polygonOffsetFactor,k.polygonOffsetUnits),k.alphaToCoverage===!0?Jt(i.SAMPLE_ALPHA_TO_COVERAGE):Wt(i.SAMPLE_ALPHA_TO_COVERAGE)}function It(k){ot!==k&&(k?i.frontFace(i.CW):i.frontFace(i.CCW),ot=k)}function R(k){k!==ed?(Jt(i.CULL_FACE),k!==Mt&&(k===Ch?i.cullFace(i.BACK):k===nd?i.cullFace(i.FRONT):i.cullFace(i.FRONT_AND_BACK))):Wt(i.CULL_FACE),Mt=k}function b(k){k!==X&&(ft&&i.lineWidth(k),X=k)}function Y(k,Rt,Ut){k?(Jt(i.POLYGON_OFFSET_FILL),(K!==Rt||tt!==Ut)&&(i.polygonOffset(Rt,Ut),K=Rt,tt=Ut)):Wt(i.POLYGON_OFFSET_FILL)}function xt(k){k?Jt(i.SCISSOR_TEST):Wt(i.SCISSOR_TEST)}function mt(k){k===void 0&&(k=i.TEXTURE0+it-1),lt!==k&&(i.activeTexture(k),lt=k)}function gt(k,Rt,Ut){Ut===void 0&&(lt===null?Ut=i.TEXTURE0+it-1:Ut=lt);let re=Dt[Ut];re===void 0&&(re={type:void 0,texture:void 0},Dt[Ut]=re),(re.type!==k||re.texture!==Rt)&&(lt!==Ut&&(i.activeTexture(Ut),lt=Ut),i.bindTexture(k,Rt||se[k]),re.type=k,re.texture=Rt)}function Gt(){let k=Dt[lt];k!==void 0&&k.type!==void 0&&(i.bindTexture(k.type,null),k.type=void 0,k.texture=void 0)}function Lt(){try{i.compressedTexImage2D.apply(i,arguments)}catch(k){console.error("THREE.WebGLState:",k)}}function At(){try{i.compressedTexImage3D.apply(i,arguments)}catch(k){console.error("THREE.WebGLState:",k)}}function ee(){try{i.texSubImage2D.apply(i,arguments)}catch(k){console.error("THREE.WebGLState:",k)}}function pe(){try{i.texSubImage3D.apply(i,arguments)}catch(k){console.error("THREE.WebGLState:",k)}}function dt(){try{i.compressedTexSubImage2D.apply(i,arguments)}catch(k){console.error("THREE.WebGLState:",k)}}function Re(){try{i.compressedTexSubImage3D.apply(i,arguments)}catch(k){console.error("THREE.WebGLState:",k)}}function Se(){try{i.texStorage2D.apply(i,arguments)}catch(k){console.error("THREE.WebGLState:",k)}}function Zt(){try{i.texStorage3D.apply(i,arguments)}catch(k){console.error("THREE.WebGLState:",k)}}function Kt(){try{i.texImage2D.apply(i,arguments)}catch(k){console.error("THREE.WebGLState:",k)}}function Ht(){try{i.texImage3D.apply(i,arguments)}catch(k){console.error("THREE.WebGLState:",k)}}function ae(k){Nt.equals(k)===!1&&(i.scissor(k.x,k.y,k.z,k.w),Nt.copy(k))}function Ie(k){Ft.equals(k)===!1&&(i.viewport(k.x,k.y,k.z,k.w),Ft.copy(k))}function Ye(k,Rt){let Ut=f.get(Rt);Ut===void 0&&(Ut=new WeakMap,f.set(Rt,Ut));let re=Ut.get(k);re===void 0&&(re=i.getUniformBlockIndex(Rt,k.name),Ut.set(k,re))}function te(k,Rt){let re=f.get(Rt).get(k);h.get(Rt)!==re&&(i.uniformBlockBinding(Rt,re,k.__bindingPointIndex),h.set(Rt,re))}function wt(){i.disable(i.BLEND),i.disable(i.CULL_FACE),i.disable(i.DEPTH_TEST),i.disable(i.POLYGON_OFFSET_FILL),i.disable(i.SCISSOR_TEST),i.disable(i.STENCIL_TEST),i.disable(i.SAMPLE_ALPHA_TO_COVERAGE),i.blendEquation(i.FUNC_ADD),i.blendFunc(i.ONE,i.ZERO),i.blendFuncSeparate(i.ONE,i.ZERO,i.ONE,i.ZERO),i.blendColor(0,0,0,0),i.colorMask(!0,!0,!0,!0),i.clearColor(0,0,0,0),i.depthMask(!0),i.depthFunc(i.LESS),i.clearDepth(1),i.stencilMask(4294967295),i.stencilFunc(i.ALWAYS,0,4294967295),i.stencilOp(i.KEEP,i.KEEP,i.KEEP),i.clearStencil(0),i.cullFace(i.BACK),i.frontFace(i.CCW),i.polygonOffset(0,0),i.activeTexture(i.TEXTURE0),i.bindFramebuffer(i.FRAMEBUFFER,null),n===!0&&(i.bindFramebuffer(i.DRAW_FRAMEBUFFER,null),i.bindFramebuffer(i.READ_FRAMEBUFFER,null)),i.useProgram(null),i.lineWidth(1),i.scissor(0,0,i.canvas.width,i.canvas.height),i.viewport(0,0,i.canvas.width,i.canvas.height),d={},lt=null,Dt={},p={},x=new WeakMap,S=[],_=null,m=!1,T=null,M=null,U=null,W=null,F=null,B=null,J=null,w=new fe(0,0,0),L=0,$=!1,ot=null,Mt=null,X=null,K=null,tt=null,Nt.set(0,0,i.canvas.width,i.canvas.height),Ft.set(0,0,i.canvas.width,i.canvas.height),o.reset(),c.reset(),l.reset()}return{buffers:{color:o,depth:c,stencil:l},enable:Jt,disable:Wt,bindFramebuffer:le,drawBuffers:z,useProgram:Tt,setBlending:ht,setMaterial:qt,setFlipSided:It,setCullFace:R,setLineWidth:b,setPolygonOffset:Y,setScissorTest:xt,activeTexture:mt,bindTexture:gt,unbindTexture:Gt,compressedTexImage2D:Lt,compressedTexImage3D:At,texImage2D:Kt,texImage3D:Ht,updateUBOMapping:Ye,uniformBlockBinding:te,texStorage2D:Se,texStorage3D:Zt,texSubImage2D:ee,texSubImage3D:pe,compressedTexSubImage2D:dt,compressedTexSubImage3D:Re,scissor:ae,viewport:Ie,reset:wt}}function K_(i,t,e,n,s,r,a){let o=s.isWebGL2,c=t.has("WEBGL_multisampled_render_to_texture")?t.get("WEBGL_multisampled_render_to_texture"):null,l=typeof navigator=="undefined"?!1:/OculusBrowser/g.test(navigator.userAgent),h=new WeakMap,f,d=new WeakMap,p=!1;try{p=typeof OffscreenCanvas!="undefined"&&new OffscreenCanvas(1,1).getContext("2d")!==null}catch{}function x(R,b){return p?new OffscreenCanvas(R,b):Wr("canvas")}function S(R,b,Y,xt){let mt=1;if((R.width>xt||R.height>xt)&&(mt=xt/Math.max(R.width,R.height)),mt<1||b===!0)if(typeof HTMLImageElement!="undefined"&&R instanceof HTMLImageElement||typeof HTMLCanvasElement!="undefined"&&R instanceof HTMLCanvasElement||typeof ImageBitmap!="undefined"&&R instanceof ImageBitmap){let gt=b?ca:Math.floor,Gt=gt(mt*R.width),Lt=gt(mt*R.height);f===void 0&&(f=x(Gt,Lt));let At=Y?x(Gt,Lt):f;return At.width=Gt,At.height=Lt,At.getContext("2d").drawImage(R,0,0,Gt,Lt),console.warn("THREE.WebGLRenderer: Texture has been resized from ("+R.width+"x"+R.height+") to ("+Gt+"x"+Lt+")."),At}else return"data"in R&&console.warn("THREE.WebGLRenderer: Image in DataTexture is too big ("+R.width+"x"+R.height+")."),R;return R}function _(R){return Xc(R.width)&&Xc(R.height)}function m(R){return o?!1:R.wrapS!==Ln||R.wrapT!==Ln||R.minFilter!==In&&R.minFilter!==$n}function T(R,b){return R.generateMipmaps&&b&&R.minFilter!==In&&R.minFilter!==$n}function M(R){i.generateMipmap(R)}function U(R,b,Y,xt,mt=!1){if(o===!1)return b;if(R!==null){if(i[R]!==void 0)return i[R];console.warn("THREE.WebGLRenderer: Attempt to use non-existing WebGL internal format '"+R+"'")}let gt=b;if(b===i.RED&&(Y===i.FLOAT&&(gt=i.R32F),Y===i.HALF_FLOAT&&(gt=i.R16F),Y===i.UNSIGNED_BYTE&&(gt=i.R8)),b===i.RED_INTEGER&&(Y===i.UNSIGNED_BYTE&&(gt=i.R8UI),Y===i.UNSIGNED_SHORT&&(gt=i.R16UI),Y===i.UNSIGNED_INT&&(gt=i.R32UI),Y===i.BYTE&&(gt=i.R8I),Y===i.SHORT&&(gt=i.R16I),Y===i.INT&&(gt=i.R32I)),b===i.RG&&(Y===i.FLOAT&&(gt=i.RG32F),Y===i.HALF_FLOAT&&(gt=i.RG16F),Y===i.UNSIGNED_BYTE&&(gt=i.RG8)),b===i.RGBA){let Gt=mt?sa:Be.getTransfer(xt);Y===i.FLOAT&&(gt=i.RGBA32F),Y===i.HALF_FLOAT&&(gt=i.RGBA16F),Y===i.UNSIGNED_BYTE&&(gt=Gt===Xe?i.SRGB8_ALPHA8:i.RGBA8),Y===i.UNSIGNED_SHORT_4_4_4_4&&(gt=i.RGBA4),Y===i.UNSIGNED_SHORT_5_5_5_1&&(gt=i.RGB5_A1)}return(gt===i.R16F||gt===i.R32F||gt===i.RG16F||gt===i.RG32F||gt===i.RGBA16F||gt===i.RGBA32F)&&t.get("EXT_color_buffer_float"),gt}function W(R,b,Y){return T(R,Y)===!0||R.isFramebufferTexture&&R.minFilter!==In&&R.minFilter!==$n?Math.log2(Math.max(b.width,b.height))+1:R.mipmaps!==void 0&&R.mipmaps.length>0?R.mipmaps.length:R.isCompressedTexture&&Array.isArray(R.image)?b.mipmaps.length:1}function F(R){return R===In||R===Dh||R===rc?i.NEAREST:i.LINEAR}function B(R){let b=R.target;b.removeEventListener("dispose",B),w(b),b.isVideoTexture&&h.delete(b)}function J(R){let b=R.target;b.removeEventListener("dispose",J),$(b)}function w(R){let b=n.get(R);if(b.__webglInit===void 0)return;let Y=R.source,xt=d.get(Y);if(xt){let mt=xt[b.__cacheKey];mt.usedTimes--,mt.usedTimes===0&&L(R),Object.keys(xt).length===0&&d.delete(Y)}n.remove(R)}function L(R){let b=n.get(R);i.deleteTexture(b.__webglTexture);let Y=R.source,xt=d.get(Y);delete xt[b.__cacheKey],a.memory.textures--}function $(R){let b=R.texture,Y=n.get(R),xt=n.get(b);if(xt.__webglTexture!==void 0&&(i.deleteTexture(xt.__webglTexture),a.memory.textures--),R.depthTexture&&R.depthTexture.dispose(),R.isWebGLCubeRenderTarget)for(let mt=0;mt<6;mt++){if(Array.isArray(Y.__webglFramebuffer[mt]))for(let gt=0;gt<Y.__webglFramebuffer[mt].length;gt++)i.deleteFramebuffer(Y.__webglFramebuffer[mt][gt]);else i.deleteFramebuffer(Y.__webglFramebuffer[mt]);Y.__webglDepthbuffer&&i.deleteRenderbuffer(Y.__webglDepthbuffer[mt])}else{if(Array.isArray(Y.__webglFramebuffer))for(let mt=0;mt<Y.__webglFramebuffer.length;mt++)i.deleteFramebuffer(Y.__webglFramebuffer[mt]);else i.deleteFramebuffer(Y.__webglFramebuffer);if(Y.__webglDepthbuffer&&i.deleteRenderbuffer(Y.__webglDepthbuffer),Y.__webglMultisampledFramebuffer&&i.deleteFramebuffer(Y.__webglMultisampledFramebuffer),Y.__webglColorRenderbuffer)for(let mt=0;mt<Y.__webglColorRenderbuffer.length;mt++)Y.__webglColorRenderbuffer[mt]&&i.deleteRenderbuffer(Y.__webglColorRenderbuffer[mt]);Y.__webglDepthRenderbuffer&&i.deleteRenderbuffer(Y.__webglDepthRenderbuffer)}if(R.isWebGLMultipleRenderTargets)for(let mt=0,gt=b.length;mt<gt;mt++){let Gt=n.get(b[mt]);Gt.__webglTexture&&(i.deleteTexture(Gt.__webglTexture),a.memory.textures--),n.remove(b[mt])}n.remove(b),n.remove(R)}let ot=0;function Mt(){ot=0}function X(){let R=ot;return R>=s.maxTextures&&console.warn("THREE.WebGLTextures: Trying to use "+R+" texture units while this GPU supports only "+s.maxTextures),ot+=1,R}function K(R){let b=[];return b.push(R.wrapS),b.push(R.wrapT),b.push(R.wrapR||0),b.push(R.magFilter),b.push(R.minFilter),b.push(R.anisotropy),b.push(R.internalFormat),b.push(R.format),b.push(R.type),b.push(R.generateMipmaps),b.push(R.premultiplyAlpha),b.push(R.flipY),b.push(R.unpackAlignment),b.push(R.colorSpace),b.join()}function tt(R,b){let Y=n.get(R);if(R.isVideoTexture&&qt(R),R.isRenderTargetTexture===!1&&R.version>0&&Y.__version!==R.version){let xt=R.image;if(xt===null)console.warn("THREE.WebGLRenderer: Texture marked for update but no image data found.");else if(xt.complete===!1)console.warn("THREE.WebGLRenderer: Texture marked for update but image is incomplete");else{Nt(Y,R,b);return}}e.bindTexture(i.TEXTURE_2D,Y.__webglTexture,i.TEXTURE0+b)}function it(R,b){let Y=n.get(R);if(R.version>0&&Y.__version!==R.version){Nt(Y,R,b);return}e.bindTexture(i.TEXTURE_2D_ARRAY,Y.__webglTexture,i.TEXTURE0+b)}function ft(R,b){let Y=n.get(R);if(R.version>0&&Y.__version!==R.version){Nt(Y,R,b);return}e.bindTexture(i.TEXTURE_3D,Y.__webglTexture,i.TEXTURE0+b)}function nt(R,b){let Y=n.get(R);if(R.version>0&&Y.__version!==R.version){Ft(Y,R,b);return}e.bindTexture(i.TEXTURE_CUBE_MAP,Y.__webglTexture,i.TEXTURE0+b)}let ct={[bs]:i.REPEAT,[Ln]:i.CLAMP_TO_EDGE,[Vc]:i.MIRRORED_REPEAT},lt={[In]:i.NEAREST,[Dh]:i.NEAREST_MIPMAP_NEAREST,[rc]:i.NEAREST_MIPMAP_LINEAR,[$n]:i.LINEAR,[Ud]:i.LINEAR_MIPMAP_NEAREST,[kr]:i.LINEAR_MIPMAP_LINEAR},Dt={[Wd]:i.NEVER,[Jd]:i.ALWAYS,[Xd]:i.LESS,[Sf]:i.LEQUAL,[Yd]:i.EQUAL,[$d]:i.GEQUAL,[qd]:i.GREATER,[Zd]:i.NOTEQUAL};function st(R,b,Y){if(Y?(i.texParameteri(R,i.TEXTURE_WRAP_S,ct[b.wrapS]),i.texParameteri(R,i.TEXTURE_WRAP_T,ct[b.wrapT]),(R===i.TEXTURE_3D||R===i.TEXTURE_2D_ARRAY)&&i.texParameteri(R,i.TEXTURE_WRAP_R,ct[b.wrapR]),i.texParameteri(R,i.TEXTURE_MAG_FILTER,lt[b.magFilter]),i.texParameteri(R,i.TEXTURE_MIN_FILTER,lt[b.minFilter])):(i.texParameteri(R,i.TEXTURE_WRAP_S,i.CLAMP_TO_EDGE),i.texParameteri(R,i.TEXTURE_WRAP_T,i.CLAMP_TO_EDGE),(R===i.TEXTURE_3D||R===i.TEXTURE_2D_ARRAY)&&i.texParameteri(R,i.TEXTURE_WRAP_R,i.CLAMP_TO_EDGE),(b.wrapS!==Ln||b.wrapT!==Ln)&&console.warn("THREE.WebGLRenderer: Texture is not power of two. Texture.wrapS and Texture.wrapT should be set to THREE.ClampToEdgeWrapping."),i.texParameteri(R,i.TEXTURE_MAG_FILTER,F(b.magFilter)),i.texParameteri(R,i.TEXTURE_MIN_FILTER,F(b.minFilter)),b.minFilter!==In&&b.minFilter!==$n&&console.warn("THREE.WebGLRenderer: Texture is not power of two. Texture.minFilter should be set to THREE.NearestFilter or THREE.LinearFilter.")),b.compareFunction&&(i.texParameteri(R,i.TEXTURE_COMPARE_MODE,i.COMPARE_REF_TO_TEXTURE),i.texParameteri(R,i.TEXTURE_COMPARE_FUNC,Dt[b.compareFunction])),t.has("EXT_texture_filter_anisotropic")===!0){let xt=t.get("EXT_texture_filter_anisotropic");if(b.magFilter===In||b.minFilter!==rc&&b.minFilter!==kr||b.type===Ji&&t.has("OES_texture_float_linear")===!1||o===!1&&b.type===Gr&&t.has("OES_texture_half_float_linear")===!1)return;(b.anisotropy>1||n.get(b).__currentAnisotropy)&&(i.texParameterf(R,xt.TEXTURE_MAX_ANISOTROPY_EXT,Math.min(b.anisotropy,s.getMaxAnisotropy())),n.get(b).__currentAnisotropy=b.anisotropy)}}function ut(R,b){let Y=!1;R.__webglInit===void 0&&(R.__webglInit=!0,b.addEventListener("dispose",B));let xt=b.source,mt=d.get(xt);mt===void 0&&(mt={},d.set(xt,mt));let gt=K(b);if(gt!==R.__cacheKey){mt[gt]===void 0&&(mt[gt]={texture:i.createTexture(),usedTimes:0},a.memory.textures++,Y=!0),mt[gt].usedTimes++;let Gt=mt[R.__cacheKey];Gt!==void 0&&(mt[R.__cacheKey].usedTimes--,Gt.usedTimes===0&&L(b)),R.__cacheKey=gt,R.__webglTexture=mt[gt].texture}return Y}function Nt(R,b,Y){let xt=i.TEXTURE_2D;(b.isDataArrayTexture||b.isCompressedArrayTexture)&&(xt=i.TEXTURE_2D_ARRAY),b.isData3DTexture&&(xt=i.TEXTURE_3D);let mt=ut(R,b),gt=b.source;e.bindTexture(xt,R.__webglTexture,i.TEXTURE0+Y);let Gt=n.get(gt);if(gt.version!==Gt.__version||mt===!0){e.activeTexture(i.TEXTURE0+Y);let Lt=Be.getPrimaries(Be.workingColorSpace),At=b.colorSpace===Jn?null:Be.getPrimaries(b.colorSpace),ee=b.colorSpace===Jn||Lt===At?i.NONE:i.BROWSER_DEFAULT_WEBGL;i.pixelStorei(i.UNPACK_FLIP_Y_WEBGL,b.flipY),i.pixelStorei(i.UNPACK_PREMULTIPLY_ALPHA_WEBGL,b.premultiplyAlpha),i.pixelStorei(i.UNPACK_ALIGNMENT,b.unpackAlignment),i.pixelStorei(i.UNPACK_COLORSPACE_CONVERSION_WEBGL,ee);let pe=m(b)&&_(b.image)===!1,dt=S(b.image,pe,!1,s.maxTextureSize);dt=It(b,dt);let Re=_(dt)||o,Se=r.convert(b.format,b.colorSpace),Zt=r.convert(b.type),Kt=U(b.internalFormat,Se,Zt,b.colorSpace,b.isVideoTexture);st(xt,b,Re);let Ht,ae=b.mipmaps,Ie=o&&b.isVideoTexture!==!0&&Kt!==vf,Ye=Gt.__version===void 0||mt===!0,te=W(b,dt,Re);if(b.isDepthTexture)Kt=i.DEPTH_COMPONENT,o?b.type===Ji?Kt=i.DEPTH_COMPONENT32F:b.type===$i?Kt=i.DEPTH_COMPONENT24:b.type===ys?Kt=i.DEPTH24_STENCIL8:Kt=i.DEPTH_COMPONENT16:b.type===Ji&&console.error("WebGLRenderer: Floating point depth texture requires WebGL2."),b.format===Ms&&Kt===i.DEPTH_COMPONENT&&b.type!==Ll&&b.type!==$i&&(console.warn("THREE.WebGLRenderer: Use UnsignedShortType or UnsignedIntType for DepthFormat DepthTexture."),b.type=$i,Zt=r.convert(b.type)),b.format===dr&&Kt===i.DEPTH_COMPONENT&&(Kt=i.DEPTH_STENCIL,b.type!==ys&&(console.warn("THREE.WebGLRenderer: Use UnsignedInt248Type for DepthStencilFormat DepthTexture."),b.type=ys,Zt=r.convert(b.type))),Ye&&(Ie?e.texStorage2D(i.TEXTURE_2D,1,Kt,dt.width,dt.height):e.texImage2D(i.TEXTURE_2D,0,Kt,dt.width,dt.height,0,Se,Zt,null));else if(b.isDataTexture)if(ae.length>0&&Re){Ie&&Ye&&e.texStorage2D(i.TEXTURE_2D,te,Kt,ae[0].width,ae[0].height);for(let wt=0,k=ae.length;wt<k;wt++)Ht=ae[wt],Ie?e.texSubImage2D(i.TEXTURE_2D,wt,0,0,Ht.width,Ht.height,Se,Zt,Ht.data):e.texImage2D(i.TEXTURE_2D,wt,Kt,Ht.width,Ht.height,0,Se,Zt,Ht.data);b.generateMipmaps=!1}else Ie?(Ye&&e.texStorage2D(i.TEXTURE_2D,te,Kt,dt.width,dt.height),e.texSubImage2D(i.TEXTURE_2D,0,0,0,dt.width,dt.height,Se,Zt,dt.data)):e.texImage2D(i.TEXTURE_2D,0,Kt,dt.width,dt.height,0,Se,Zt,dt.data);else if(b.isCompressedTexture)if(b.isCompressedArrayTexture){Ie&&Ye&&e.texStorage3D(i.TEXTURE_2D_ARRAY,te,Kt,ae[0].width,ae[0].height,dt.depth);for(let wt=0,k=ae.length;wt<k;wt++)Ht=ae[wt],b.format!==hi?Se!==null?Ie?e.compressedTexSubImage3D(i.TEXTURE_2D_ARRAY,wt,0,0,0,Ht.width,Ht.height,dt.depth,Se,Ht.data,0,0):e.compressedTexImage3D(i.TEXTURE_2D_ARRAY,wt,Kt,Ht.width,Ht.height,dt.depth,0,Ht.data,0,0):console.warn("THREE.WebGLRenderer: Attempt to load unsupported compressed texture format in .uploadTexture()"):Ie?e.texSubImage3D(i.TEXTURE_2D_ARRAY,wt,0,0,0,Ht.width,Ht.height,dt.depth,Se,Zt,Ht.data):e.texImage3D(i.TEXTURE_2D_ARRAY,wt,Kt,Ht.width,Ht.height,dt.depth,0,Se,Zt,Ht.data)}else{Ie&&Ye&&e.texStorage2D(i.TEXTURE_2D,te,Kt,ae[0].width,ae[0].height);for(let wt=0,k=ae.length;wt<k;wt++)Ht=ae[wt],b.format!==hi?Se!==null?Ie?e.compressedTexSubImage2D(i.TEXTURE_2D,wt,0,0,Ht.width,Ht.height,Se,Ht.data):e.compressedTexImage2D(i.TEXTURE_2D,wt,Kt,Ht.width,Ht.height,0,Ht.data):console.warn("THREE.WebGLRenderer: Attempt to load unsupported compressed texture format in .uploadTexture()"):Ie?e.texSubImage2D(i.TEXTURE_2D,wt,0,0,Ht.width,Ht.height,Se,Zt,Ht.data):e.texImage2D(i.TEXTURE_2D,wt,Kt,Ht.width,Ht.height,0,Se,Zt,Ht.data)}else if(b.isDataArrayTexture)Ie?(Ye&&e.texStorage3D(i.TEXTURE_2D_ARRAY,te,Kt,dt.width,dt.height,dt.depth),e.texSubImage3D(i.TEXTURE_2D_ARRAY,0,0,0,0,dt.width,dt.height,dt.depth,Se,Zt,dt.data)):e.texImage3D(i.TEXTURE_2D_ARRAY,0,Kt,dt.width,dt.height,dt.depth,0,Se,Zt,dt.data);else if(b.isData3DTexture)Ie?(Ye&&e.texStorage3D(i.TEXTURE_3D,te,Kt,dt.width,dt.height,dt.depth),e.texSubImage3D(i.TEXTURE_3D,0,0,0,0,dt.width,dt.height,dt.depth,Se,Zt,dt.data)):e.texImage3D(i.TEXTURE_3D,0,Kt,dt.width,dt.height,dt.depth,0,Se,Zt,dt.data);else if(b.isFramebufferTexture){if(Ye)if(Ie)e.texStorage2D(i.TEXTURE_2D,te,Kt,dt.width,dt.height);else{let wt=dt.width,k=dt.height;for(let Rt=0;Rt<te;Rt++)e.texImage2D(i.TEXTURE_2D,Rt,Kt,wt,k,0,Se,Zt,null),wt>>=1,k>>=1}}else if(ae.length>0&&Re){Ie&&Ye&&e.texStorage2D(i.TEXTURE_2D,te,Kt,ae[0].width,ae[0].height);for(let wt=0,k=ae.length;wt<k;wt++)Ht=ae[wt],Ie?e.texSubImage2D(i.TEXTURE_2D,wt,0,0,Se,Zt,Ht):e.texImage2D(i.TEXTURE_2D,wt,Kt,Se,Zt,Ht);b.generateMipmaps=!1}else Ie?(Ye&&e.texStorage2D(i.TEXTURE_2D,te,Kt,dt.width,dt.height),e.texSubImage2D(i.TEXTURE_2D,0,0,0,Se,Zt,dt)):e.texImage2D(i.TEXTURE_2D,0,Kt,Se,Zt,dt);T(b,Re)&&M(xt),Gt.__version=gt.version,b.onUpdate&&b.onUpdate(b)}R.__version=b.version}function Ft(R,b,Y){if(b.image.length!==6)return;let xt=ut(R,b),mt=b.source;e.bindTexture(i.TEXTURE_CUBE_MAP,R.__webglTexture,i.TEXTURE0+Y);let gt=n.get(mt);if(mt.version!==gt.__version||xt===!0){e.activeTexture(i.TEXTURE0+Y);let Gt=Be.getPrimaries(Be.workingColorSpace),Lt=b.colorSpace===Jn?null:Be.getPrimaries(b.colorSpace),At=b.colorSpace===Jn||Gt===Lt?i.NONE:i.BROWSER_DEFAULT_WEBGL;i.pixelStorei(i.UNPACK_FLIP_Y_WEBGL,b.flipY),i.pixelStorei(i.UNPACK_PREMULTIPLY_ALPHA_WEBGL,b.premultiplyAlpha),i.pixelStorei(i.UNPACK_ALIGNMENT,b.unpackAlignment),i.pixelStorei(i.UNPACK_COLORSPACE_CONVERSION_WEBGL,At);let ee=b.isCompressedTexture||b.image[0].isCompressedTexture,pe=b.image[0]&&b.image[0].isDataTexture,dt=[];for(let wt=0;wt<6;wt++)!ee&&!pe?dt[wt]=S(b.image[wt],!1,!0,s.maxCubemapSize):dt[wt]=pe?b.image[wt].image:b.image[wt],dt[wt]=It(b,dt[wt]);let Re=dt[0],Se=_(Re)||o,Zt=r.convert(b.format,b.colorSpace),Kt=r.convert(b.type),Ht=U(b.internalFormat,Zt,Kt,b.colorSpace),ae=o&&b.isVideoTexture!==!0,Ie=gt.__version===void 0||xt===!0,Ye=W(b,Re,Se);st(i.TEXTURE_CUBE_MAP,b,Se);let te;if(ee){ae&&Ie&&e.texStorage2D(i.TEXTURE_CUBE_MAP,Ye,Ht,Re.width,Re.height);for(let wt=0;wt<6;wt++){te=dt[wt].mipmaps;for(let k=0;k<te.length;k++){let Rt=te[k];b.format!==hi?Zt!==null?ae?e.compressedTexSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+wt,k,0,0,Rt.width,Rt.height,Zt,Rt.data):e.compressedTexImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+wt,k,Ht,Rt.width,Rt.height,0,Rt.data):console.warn("THREE.WebGLRenderer: Attempt to load unsupported compressed texture format in .setTextureCube()"):ae?e.texSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+wt,k,0,0,Rt.width,Rt.height,Zt,Kt,Rt.data):e.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+wt,k,Ht,Rt.width,Rt.height,0,Zt,Kt,Rt.data)}}}else{te=b.mipmaps,ae&&Ie&&(te.length>0&&Ye++,e.texStorage2D(i.TEXTURE_CUBE_MAP,Ye,Ht,dt[0].width,dt[0].height));for(let wt=0;wt<6;wt++)if(pe){ae?e.texSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+wt,0,0,0,dt[wt].width,dt[wt].height,Zt,Kt,dt[wt].data):e.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+wt,0,Ht,dt[wt].width,dt[wt].height,0,Zt,Kt,dt[wt].data);for(let k=0;k<te.length;k++){let Ut=te[k].image[wt].image;ae?e.texSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+wt,k+1,0,0,Ut.width,Ut.height,Zt,Kt,Ut.data):e.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+wt,k+1,Ht,Ut.width,Ut.height,0,Zt,Kt,Ut.data)}}else{ae?e.texSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+wt,0,0,0,Zt,Kt,dt[wt]):e.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+wt,0,Ht,Zt,Kt,dt[wt]);for(let k=0;k<te.length;k++){let Rt=te[k];ae?e.texSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+wt,k+1,0,0,Zt,Kt,Rt.image[wt]):e.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+wt,k+1,Ht,Zt,Kt,Rt.image[wt])}}}T(b,Se)&&M(i.TEXTURE_CUBE_MAP),gt.__version=mt.version,b.onUpdate&&b.onUpdate(b)}R.__version=b.version}function Bt(R,b,Y,xt,mt,gt){let Gt=r.convert(Y.format,Y.colorSpace),Lt=r.convert(Y.type),At=U(Y.internalFormat,Gt,Lt,Y.colorSpace);if(!n.get(b).__hasExternalTextures){let pe=Math.max(1,b.width>>gt),dt=Math.max(1,b.height>>gt);mt===i.TEXTURE_3D||mt===i.TEXTURE_2D_ARRAY?e.texImage3D(mt,gt,At,pe,dt,b.depth,0,Gt,Lt,null):e.texImage2D(mt,gt,At,pe,dt,0,Gt,Lt,null)}e.bindFramebuffer(i.FRAMEBUFFER,R),ht(b)?c.framebufferTexture2DMultisampleEXT(i.FRAMEBUFFER,xt,mt,n.get(Y).__webglTexture,0,bt(b)):(mt===i.TEXTURE_2D||mt>=i.TEXTURE_CUBE_MAP_POSITIVE_X&&mt<=i.TEXTURE_CUBE_MAP_NEGATIVE_Z)&&i.framebufferTexture2D(i.FRAMEBUFFER,xt,mt,n.get(Y).__webglTexture,gt),e.bindFramebuffer(i.FRAMEBUFFER,null)}function se(R,b,Y){if(i.bindRenderbuffer(i.RENDERBUFFER,R),b.depthBuffer&&!b.stencilBuffer){let xt=o===!0?i.DEPTH_COMPONENT24:i.DEPTH_COMPONENT16;if(Y||ht(b)){let mt=b.depthTexture;mt&&mt.isDepthTexture&&(mt.type===Ji?xt=i.DEPTH_COMPONENT32F:mt.type===$i&&(xt=i.DEPTH_COMPONENT24));let gt=bt(b);ht(b)?c.renderbufferStorageMultisampleEXT(i.RENDERBUFFER,gt,xt,b.width,b.height):i.renderbufferStorageMultisample(i.RENDERBUFFER,gt,xt,b.width,b.height)}else i.renderbufferStorage(i.RENDERBUFFER,xt,b.width,b.height);i.framebufferRenderbuffer(i.FRAMEBUFFER,i.DEPTH_ATTACHMENT,i.RENDERBUFFER,R)}else if(b.depthBuffer&&b.stencilBuffer){let xt=bt(b);Y&&ht(b)===!1?i.renderbufferStorageMultisample(i.RENDERBUFFER,xt,i.DEPTH24_STENCIL8,b.width,b.height):ht(b)?c.renderbufferStorageMultisampleEXT(i.RENDERBUFFER,xt,i.DEPTH24_STENCIL8,b.width,b.height):i.renderbufferStorage(i.RENDERBUFFER,i.DEPTH_STENCIL,b.width,b.height),i.framebufferRenderbuffer(i.FRAMEBUFFER,i.DEPTH_STENCIL_ATTACHMENT,i.RENDERBUFFER,R)}else{let xt=b.isWebGLMultipleRenderTargets===!0?b.texture:[b.texture];for(let mt=0;mt<xt.length;mt++){let gt=xt[mt],Gt=r.convert(gt.format,gt.colorSpace),Lt=r.convert(gt.type),At=U(gt.internalFormat,Gt,Lt,gt.colorSpace),ee=bt(b);Y&&ht(b)===!1?i.renderbufferStorageMultisample(i.RENDERBUFFER,ee,At,b.width,b.height):ht(b)?c.renderbufferStorageMultisampleEXT(i.RENDERBUFFER,ee,At,b.width,b.height):i.renderbufferStorage(i.RENDERBUFFER,At,b.width,b.height)}}i.bindRenderbuffer(i.RENDERBUFFER,null)}function Jt(R,b){if(b&&b.isWebGLCubeRenderTarget)throw new Error("Depth Texture with cube render targets is not supported");if(e.bindFramebuffer(i.FRAMEBUFFER,R),!(b.depthTexture&&b.depthTexture.isDepthTexture))throw new Error("renderTarget.depthTexture must be an instance of THREE.DepthTexture");(!n.get(b.depthTexture).__webglTexture||b.depthTexture.image.width!==b.width||b.depthTexture.image.height!==b.height)&&(b.depthTexture.image.width=b.width,b.depthTexture.image.height=b.height,b.depthTexture.needsUpdate=!0),tt(b.depthTexture,0);let xt=n.get(b.depthTexture).__webglTexture,mt=bt(b);if(b.depthTexture.format===Ms)ht(b)?c.framebufferTexture2DMultisampleEXT(i.FRAMEBUFFER,i.DEPTH_ATTACHMENT,i.TEXTURE_2D,xt,0,mt):i.framebufferTexture2D(i.FRAMEBUFFER,i.DEPTH_ATTACHMENT,i.TEXTURE_2D,xt,0);else if(b.depthTexture.format===dr)ht(b)?c.framebufferTexture2DMultisampleEXT(i.FRAMEBUFFER,i.DEPTH_STENCIL_ATTACHMENT,i.TEXTURE_2D,xt,0,mt):i.framebufferTexture2D(i.FRAMEBUFFER,i.DEPTH_STENCIL_ATTACHMENT,i.TEXTURE_2D,xt,0);else throw new Error("Unknown depthTexture format")}function Wt(R){let b=n.get(R),Y=R.isWebGLCubeRenderTarget===!0;if(R.depthTexture&&!b.__autoAllocateDepthBuffer){if(Y)throw new Error("target.depthTexture not supported in Cube render targets");Jt(b.__webglFramebuffer,R)}else if(Y){b.__webglDepthbuffer=[];for(let xt=0;xt<6;xt++)e.bindFramebuffer(i.FRAMEBUFFER,b.__webglFramebuffer[xt]),b.__webglDepthbuffer[xt]=i.createRenderbuffer(),se(b.__webglDepthbuffer[xt],R,!1)}else e.bindFramebuffer(i.FRAMEBUFFER,b.__webglFramebuffer),b.__webglDepthbuffer=i.createRenderbuffer(),se(b.__webglDepthbuffer,R,!1);e.bindFramebuffer(i.FRAMEBUFFER,null)}function le(R,b,Y){let xt=n.get(R);b!==void 0&&Bt(xt.__webglFramebuffer,R,R.texture,i.COLOR_ATTACHMENT0,i.TEXTURE_2D,0),Y!==void 0&&Wt(R)}function z(R){let b=R.texture,Y=n.get(R),xt=n.get(b);R.addEventListener("dispose",J),R.isWebGLMultipleRenderTargets!==!0&&(xt.__webglTexture===void 0&&(xt.__webglTexture=i.createTexture()),xt.__version=b.version,a.memory.textures++);let mt=R.isWebGLCubeRenderTarget===!0,gt=R.isWebGLMultipleRenderTargets===!0,Gt=_(R)||o;if(mt){Y.__webglFramebuffer=[];for(let Lt=0;Lt<6;Lt++)if(o&&b.mipmaps&&b.mipmaps.length>0){Y.__webglFramebuffer[Lt]=[];for(let At=0;At<b.mipmaps.length;At++)Y.__webglFramebuffer[Lt][At]=i.createFramebuffer()}else Y.__webglFramebuffer[Lt]=i.createFramebuffer()}else{if(o&&b.mipmaps&&b.mipmaps.length>0){Y.__webglFramebuffer=[];for(let Lt=0;Lt<b.mipmaps.length;Lt++)Y.__webglFramebuffer[Lt]=i.createFramebuffer()}else Y.__webglFramebuffer=i.createFramebuffer();if(gt)if(s.drawBuffers){let Lt=R.texture;for(let At=0,ee=Lt.length;At<ee;At++){let pe=n.get(Lt[At]);pe.__webglTexture===void 0&&(pe.__webglTexture=i.createTexture(),a.memory.textures++)}}else console.warn("THREE.WebGLRenderer: WebGLMultipleRenderTargets can only be used with WebGL2 or WEBGL_draw_buffers extension.");if(o&&R.samples>0&&ht(R)===!1){let Lt=gt?b:[b];Y.__webglMultisampledFramebuffer=i.createFramebuffer(),Y.__webglColorRenderbuffer=[],e.bindFramebuffer(i.FRAMEBUFFER,Y.__webglMultisampledFramebuffer);for(let At=0;At<Lt.length;At++){let ee=Lt[At];Y.__webglColorRenderbuffer[At]=i.createRenderbuffer(),i.bindRenderbuffer(i.RENDERBUFFER,Y.__webglColorRenderbuffer[At]);let pe=r.convert(ee.format,ee.colorSpace),dt=r.convert(ee.type),Re=U(ee.internalFormat,pe,dt,ee.colorSpace,R.isXRRenderTarget===!0),Se=bt(R);i.renderbufferStorageMultisample(i.RENDERBUFFER,Se,Re,R.width,R.height),i.framebufferRenderbuffer(i.FRAMEBUFFER,i.COLOR_ATTACHMENT0+At,i.RENDERBUFFER,Y.__webglColorRenderbuffer[At])}i.bindRenderbuffer(i.RENDERBUFFER,null),R.depthBuffer&&(Y.__webglDepthRenderbuffer=i.createRenderbuffer(),se(Y.__webglDepthRenderbuffer,R,!0)),e.bindFramebuffer(i.FRAMEBUFFER,null)}}if(mt){e.bindTexture(i.TEXTURE_CUBE_MAP,xt.__webglTexture),st(i.TEXTURE_CUBE_MAP,b,Gt);for(let Lt=0;Lt<6;Lt++)if(o&&b.mipmaps&&b.mipmaps.length>0)for(let At=0;At<b.mipmaps.length;At++)Bt(Y.__webglFramebuffer[Lt][At],R,b,i.COLOR_ATTACHMENT0,i.TEXTURE_CUBE_MAP_POSITIVE_X+Lt,At);else Bt(Y.__webglFramebuffer[Lt],R,b,i.COLOR_ATTACHMENT0,i.TEXTURE_CUBE_MAP_POSITIVE_X+Lt,0);T(b,Gt)&&M(i.TEXTURE_CUBE_MAP),e.unbindTexture()}else if(gt){let Lt=R.texture;for(let At=0,ee=Lt.length;At<ee;At++){let pe=Lt[At],dt=n.get(pe);e.bindTexture(i.TEXTURE_2D,dt.__webglTexture),st(i.TEXTURE_2D,pe,Gt),Bt(Y.__webglFramebuffer,R,pe,i.COLOR_ATTACHMENT0+At,i.TEXTURE_2D,0),T(pe,Gt)&&M(i.TEXTURE_2D)}e.unbindTexture()}else{let Lt=i.TEXTURE_2D;if((R.isWebGL3DRenderTarget||R.isWebGLArrayRenderTarget)&&(o?Lt=R.isWebGL3DRenderTarget?i.TEXTURE_3D:i.TEXTURE_2D_ARRAY:console.error("THREE.WebGLTextures: THREE.Data3DTexture and THREE.DataArrayTexture only supported with WebGL2.")),e.bindTexture(Lt,xt.__webglTexture),st(Lt,b,Gt),o&&b.mipmaps&&b.mipmaps.length>0)for(let At=0;At<b.mipmaps.length;At++)Bt(Y.__webglFramebuffer[At],R,b,i.COLOR_ATTACHMENT0,Lt,At);else Bt(Y.__webglFramebuffer,R,b,i.COLOR_ATTACHMENT0,Lt,0);T(b,Gt)&&M(Lt),e.unbindTexture()}R.depthBuffer&&Wt(R)}function Tt(R){let b=_(R)||o,Y=R.isWebGLMultipleRenderTargets===!0?R.texture:[R.texture];for(let xt=0,mt=Y.length;xt<mt;xt++){let gt=Y[xt];if(T(gt,b)){let Gt=R.isWebGLCubeRenderTarget?i.TEXTURE_CUBE_MAP:i.TEXTURE_2D,Lt=n.get(gt).__webglTexture;e.bindTexture(Gt,Lt),M(Gt),e.unbindTexture()}}}function rt(R){if(o&&R.samples>0&&ht(R)===!1){let b=R.isWebGLMultipleRenderTargets?R.texture:[R.texture],Y=R.width,xt=R.height,mt=i.COLOR_BUFFER_BIT,gt=[],Gt=R.stencilBuffer?i.DEPTH_STENCIL_ATTACHMENT:i.DEPTH_ATTACHMENT,Lt=n.get(R),At=R.isWebGLMultipleRenderTargets===!0;if(At)for(let ee=0;ee<b.length;ee++)e.bindFramebuffer(i.FRAMEBUFFER,Lt.__webglMultisampledFramebuffer),i.framebufferRenderbuffer(i.FRAMEBUFFER,i.COLOR_ATTACHMENT0+ee,i.RENDERBUFFER,null),e.bindFramebuffer(i.FRAMEBUFFER,Lt.__webglFramebuffer),i.framebufferTexture2D(i.DRAW_FRAMEBUFFER,i.COLOR_ATTACHMENT0+ee,i.TEXTURE_2D,null,0);e.bindFramebuffer(i.READ_FRAMEBUFFER,Lt.__webglMultisampledFramebuffer),e.bindFramebuffer(i.DRAW_FRAMEBUFFER,Lt.__webglFramebuffer);for(let ee=0;ee<b.length;ee++){gt.push(i.COLOR_ATTACHMENT0+ee),R.depthBuffer&&gt.push(Gt);let pe=Lt.__ignoreDepthValues!==void 0?Lt.__ignoreDepthValues:!1;if(pe===!1&&(R.depthBuffer&&(mt|=i.DEPTH_BUFFER_BIT),R.stencilBuffer&&(mt|=i.STENCIL_BUFFER_BIT)),At&&i.framebufferRenderbuffer(i.READ_FRAMEBUFFER,i.COLOR_ATTACHMENT0,i.RENDERBUFFER,Lt.__webglColorRenderbuffer[ee]),pe===!0&&(i.invalidateFramebuffer(i.READ_FRAMEBUFFER,[Gt]),i.invalidateFramebuffer(i.DRAW_FRAMEBUFFER,[Gt])),At){let dt=n.get(b[ee]).__webglTexture;i.framebufferTexture2D(i.DRAW_FRAMEBUFFER,i.COLOR_ATTACHMENT0,i.TEXTURE_2D,dt,0)}i.blitFramebuffer(0,0,Y,xt,0,0,Y,xt,mt,i.NEAREST),l&&i.invalidateFramebuffer(i.READ_FRAMEBUFFER,gt)}if(e.bindFramebuffer(i.READ_FRAMEBUFFER,null),e.bindFramebuffer(i.DRAW_FRAMEBUFFER,null),At)for(let ee=0;ee<b.length;ee++){e.bindFramebuffer(i.FRAMEBUFFER,Lt.__webglMultisampledFramebuffer),i.framebufferRenderbuffer(i.FRAMEBUFFER,i.COLOR_ATTACHMENT0+ee,i.RENDERBUFFER,Lt.__webglColorRenderbuffer[ee]);let pe=n.get(b[ee]).__webglTexture;e.bindFramebuffer(i.FRAMEBUFFER,Lt.__webglFramebuffer),i.framebufferTexture2D(i.DRAW_FRAMEBUFFER,i.COLOR_ATTACHMENT0+ee,i.TEXTURE_2D,pe,0)}e.bindFramebuffer(i.DRAW_FRAMEBUFFER,Lt.__webglMultisampledFramebuffer)}}function bt(R){return Math.min(s.maxSamples,R.samples)}function ht(R){let b=n.get(R);return o&&R.samples>0&&t.has("WEBGL_multisampled_render_to_texture")===!0&&b.__useRenderToTexture!==!1}function qt(R){let b=a.render.frame;h.get(R)!==b&&(h.set(R,b),R.update())}function It(R,b){let Y=R.colorSpace,xt=R.format,mt=R.type;return R.isCompressedTexture===!0||R.isVideoTexture===!0||R.format===Wc||Y!==Di&&Y!==Jn&&(Be.getTransfer(Y)===Xe?o===!1?t.has("EXT_sRGB")===!0&&xt===hi?(R.format=Wc,R.minFilter=$n,R.generateMipmaps=!1):b=la.sRGBToLinear(b):(xt!==hi||mt!==Qi)&&console.warn("THREE.WebGLTextures: sRGB encoded textures have to use RGBAFormat and UnsignedByteType."):console.error("THREE.WebGLTextures: Unsupported texture color space:",Y)),b}this.allocateTextureUnit=X,this.resetTextureUnits=Mt,this.setTexture2D=tt,this.setTexture2DArray=it,this.setTexture3D=ft,this.setTextureCube=nt,this.rebindTextures=le,this.setupRenderTarget=z,this.updateRenderTargetMipmap=Tt,this.updateMultisampleRenderTarget=rt,this.setupDepthRenderbuffer=Wt,this.setupFrameBufferTexture=Bt,this.useMultisampledRTT=ht}function j_(i,t,e){let n=e.isWebGL2;function s(r,a=Jn){let o,c=Be.getTransfer(a);if(r===Qi)return i.UNSIGNED_BYTE;if(r===pf)return i.UNSIGNED_SHORT_4_4_4_4;if(r===mf)return i.UNSIGNED_SHORT_5_5_5_1;if(r===Dd)return i.BYTE;if(r===Nd)return i.SHORT;if(r===Ll)return i.UNSIGNED_SHORT;if(r===df)return i.INT;if(r===$i)return i.UNSIGNED_INT;if(r===Ji)return i.FLOAT;if(r===Gr)return n?i.HALF_FLOAT:(o=t.get("OES_texture_half_float"),o!==null?o.HALF_FLOAT_OES:null);if(r===Fd)return i.ALPHA;if(r===hi)return i.RGBA;if(r===Od)return i.LUMINANCE;if(r===Bd)return i.LUMINANCE_ALPHA;if(r===Ms)return i.DEPTH_COMPONENT;if(r===dr)return i.DEPTH_STENCIL;if(r===Wc)return o=t.get("EXT_sRGB"),o!==null?o.SRGB_ALPHA_EXT:null;if(r===zd)return i.RED;if(r===gf)return i.RED_INTEGER;if(r===Hd)return i.RG;if(r===_f)return i.RG_INTEGER;if(r===xf)return i.RGBA_INTEGER;if(r===oc||r===ac||r===cc||r===lc)if(c===Xe)if(o=t.get("WEBGL_compressed_texture_s3tc_srgb"),o!==null){if(r===oc)return o.COMPRESSED_SRGB_S3TC_DXT1_EXT;if(r===ac)return o.COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT;if(r===cc)return o.COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT;if(r===lc)return o.COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT}else return null;else if(o=t.get("WEBGL_compressed_texture_s3tc"),o!==null){if(r===oc)return o.COMPRESSED_RGB_S3TC_DXT1_EXT;if(r===ac)return o.COMPRESSED_RGBA_S3TC_DXT1_EXT;if(r===cc)return o.COMPRESSED_RGBA_S3TC_DXT3_EXT;if(r===lc)return o.COMPRESSED_RGBA_S3TC_DXT5_EXT}else return null;if(r===Nh||r===Fh||r===Oh||r===Bh)if(o=t.get("WEBGL_compressed_texture_pvrtc"),o!==null){if(r===Nh)return o.COMPRESSED_RGB_PVRTC_4BPPV1_IMG;if(r===Fh)return o.COMPRESSED_RGB_PVRTC_2BPPV1_IMG;if(r===Oh)return o.COMPRESSED_RGBA_PVRTC_4BPPV1_IMG;if(r===Bh)return o.COMPRESSED_RGBA_PVRTC_2BPPV1_IMG}else return null;if(r===vf)return o=t.get("WEBGL_compressed_texture_etc1"),o!==null?o.COMPRESSED_RGB_ETC1_WEBGL:null;if(r===zh||r===Hh)if(o=t.get("WEBGL_compressed_texture_etc"),o!==null){if(r===zh)return c===Xe?o.COMPRESSED_SRGB8_ETC2:o.COMPRESSED_RGB8_ETC2;if(r===Hh)return c===Xe?o.COMPRESSED_SRGB8_ALPHA8_ETC2_EAC:o.COMPRESSED_RGBA8_ETC2_EAC}else return null;if(r===kh||r===Gh||r===Vh||r===Wh||r===Xh||r===Yh||r===qh||r===Zh||r===$h||r===Jh||r===Kh||r===jh||r===Qh||r===tu)if(o=t.get("WEBGL_compressed_texture_astc"),o!==null){if(r===kh)return c===Xe?o.COMPRESSED_SRGB8_ALPHA8_ASTC_4x4_KHR:o.COMPRESSED_RGBA_ASTC_4x4_KHR;if(r===Gh)return c===Xe?o.COMPRESSED_SRGB8_ALPHA8_ASTC_5x4_KHR:o.COMPRESSED_RGBA_ASTC_5x4_KHR;if(r===Vh)return c===Xe?o.COMPRESSED_SRGB8_ALPHA8_ASTC_5x5_KHR:o.COMPRESSED_RGBA_ASTC_5x5_KHR;if(r===Wh)return c===Xe?o.COMPRESSED_SRGB8_ALPHA8_ASTC_6x5_KHR:o.COMPRESSED_RGBA_ASTC_6x5_KHR;if(r===Xh)return c===Xe?o.COMPRESSED_SRGB8_ALPHA8_ASTC_6x6_KHR:o.COMPRESSED_RGBA_ASTC_6x6_KHR;if(r===Yh)return c===Xe?o.COMPRESSED_SRGB8_ALPHA8_ASTC_8x5_KHR:o.COMPRESSED_RGBA_ASTC_8x5_KHR;if(r===qh)return c===Xe?o.COMPRESSED_SRGB8_ALPHA8_ASTC_8x6_KHR:o.COMPRESSED_RGBA_ASTC_8x6_KHR;if(r===Zh)return c===Xe?o.COMPRESSED_SRGB8_ALPHA8_ASTC_8x8_KHR:o.COMPRESSED_RGBA_ASTC_8x8_KHR;if(r===$h)return c===Xe?o.COMPRESSED_SRGB8_ALPHA8_ASTC_10x5_KHR:o.COMPRESSED_RGBA_ASTC_10x5_KHR;if(r===Jh)return c===Xe?o.COMPRESSED_SRGB8_ALPHA8_ASTC_10x6_KHR:o.COMPRESSED_RGBA_ASTC_10x6_KHR;if(r===Kh)return c===Xe?o.COMPRESSED_SRGB8_ALPHA8_ASTC_10x8_KHR:o.COMPRESSED_RGBA_ASTC_10x8_KHR;if(r===jh)return c===Xe?o.COMPRESSED_SRGB8_ALPHA8_ASTC_10x10_KHR:o.COMPRESSED_RGBA_ASTC_10x10_KHR;if(r===Qh)return c===Xe?o.COMPRESSED_SRGB8_ALPHA8_ASTC_12x10_KHR:o.COMPRESSED_RGBA_ASTC_12x10_KHR;if(r===tu)return c===Xe?o.COMPRESSED_SRGB8_ALPHA8_ASTC_12x12_KHR:o.COMPRESSED_RGBA_ASTC_12x12_KHR}else return null;if(r===hc||r===eu||r===nu)if(o=t.get("EXT_texture_compression_bptc"),o!==null){if(r===hc)return c===Xe?o.COMPRESSED_SRGB_ALPHA_BPTC_UNORM_EXT:o.COMPRESSED_RGBA_BPTC_UNORM_EXT;if(r===eu)return o.COMPRESSED_RGB_BPTC_SIGNED_FLOAT_EXT;if(r===nu)return o.COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_EXT}else return null;if(r===kd||r===iu||r===su||r===ru)if(o=t.get("EXT_texture_compression_rgtc"),o!==null){if(r===hc)return o.COMPRESSED_RED_RGTC1_EXT;if(r===iu)return o.COMPRESSED_SIGNED_RED_RGTC1_EXT;if(r===su)return o.COMPRESSED_RED_GREEN_RGTC2_EXT;if(r===ru)return o.COMPRESSED_SIGNED_RED_GREEN_RGTC2_EXT}else return null;return r===ys?n?i.UNSIGNED_INT_24_8:(o=t.get("WEBGL_depth_texture"),o!==null?o.UNSIGNED_INT_24_8_WEBGL:null):i[r]!==void 0?i[r]:null}return{convert:s}}var sl=class extends wn{constructor(t=[]){super(),this.isArrayCamera=!0,this.cameras=t}},rr=class extends An{constructor(){super(),this.isGroup=!0,this.type="Group"}},Q_={type:"move"},Br=class{constructor(){this._targetRay=null,this._grip=null,this._hand=null}getHandSpace(){return this._hand===null&&(this._hand=new rr,this._hand.matrixAutoUpdate=!1,this._hand.visible=!1,this._hand.joints={},this._hand.inputState={pinching:!1}),this._hand}getTargetRaySpace(){return this._targetRay===null&&(this._targetRay=new rr,this._targetRay.matrixAutoUpdate=!1,this._targetRay.visible=!1,this._targetRay.hasLinearVelocity=!1,this._targetRay.linearVelocity=new O,this._targetRay.hasAngularVelocity=!1,this._targetRay.angularVelocity=new O),this._targetRay}getGripSpace(){return this._grip===null&&(this._grip=new rr,this._grip.matrixAutoUpdate=!1,this._grip.visible=!1,this._grip.hasLinearVelocity=!1,this._grip.linearVelocity=new O,this._grip.hasAngularVelocity=!1,this._grip.angularVelocity=new O),this._grip}dispatchEvent(t){return this._targetRay!==null&&this._targetRay.dispatchEvent(t),this._grip!==null&&this._grip.dispatchEvent(t),this._hand!==null&&this._hand.dispatchEvent(t),this}connect(t){if(t&&t.hand){let e=this._hand;if(e)for(let n of t.hand.values())this._getHandJoint(e,n)}return this.dispatchEvent({type:"connected",data:t}),this}disconnect(t){return this.dispatchEvent({type:"disconnected",data:t}),this._targetRay!==null&&(this._targetRay.visible=!1),this._grip!==null&&(this._grip.visible=!1),this._hand!==null&&(this._hand.visible=!1),this}update(t,e,n){let s=null,r=null,a=null,o=this._targetRay,c=this._grip,l=this._hand;if(t&&e.session.visibilityState!=="visible-blurred"){if(l&&t.hand){a=!0;for(let S of t.hand.values()){let _=e.getJointPose(S,n),m=this._getHandJoint(l,S);_!==null&&(m.matrix.fromArray(_.transform.matrix),m.matrix.decompose(m.position,m.rotation,m.scale),m.matrixWorldNeedsUpdate=!0,m.jointRadius=_.radius),m.visible=_!==null}let h=l.joints["index-finger-tip"],f=l.joints["thumb-tip"],d=h.position.distanceTo(f.position),p=.02,x=.005;l.inputState.pinching&&d>p+x?(l.inputState.pinching=!1,this.dispatchEvent({type:"pinchend",handedness:t.handedness,target:this})):!l.inputState.pinching&&d<=p-x&&(l.inputState.pinching=!0,this.dispatchEvent({type:"pinchstart",handedness:t.handedness,target:this}))}else c!==null&&t.gripSpace&&(r=e.getPose(t.gripSpace,n),r!==null&&(c.matrix.fromArray(r.transform.matrix),c.matrix.decompose(c.position,c.rotation,c.scale),c.matrixWorldNeedsUpdate=!0,r.linearVelocity?(c.hasLinearVelocity=!0,c.linearVelocity.copy(r.linearVelocity)):c.hasLinearVelocity=!1,r.angularVelocity?(c.hasAngularVelocity=!0,c.angularVelocity.copy(r.angularVelocity)):c.hasAngularVelocity=!1));o!==null&&(s=e.getPose(t.targetRaySpace,n),s===null&&r!==null&&(s=r),s!==null&&(o.matrix.fromArray(s.transform.matrix),o.matrix.decompose(o.position,o.rotation,o.scale),o.matrixWorldNeedsUpdate=!0,s.linearVelocity?(o.hasLinearVelocity=!0,o.linearVelocity.copy(s.linearVelocity)):o.hasLinearVelocity=!1,s.angularVelocity?(o.hasAngularVelocity=!0,o.angularVelocity.copy(s.angularVelocity)):o.hasAngularVelocity=!1,this.dispatchEvent(Q_)))}return o!==null&&(o.visible=s!==null),c!==null&&(c.visible=r!==null),l!==null&&(l.visible=a!==null),this}_getHandJoint(t,e){if(t.joints[e.jointName]===void 0){let n=new rr;n.matrixAutoUpdate=!1,n.visible=!1,t.joints[e.jointName]=n,t.add(n)}return t.joints[e.jointName]}},rl=class extends ns{constructor(t,e){super();let n=this,s=null,r=1,a=null,o="local-floor",c=1,l=null,h=null,f=null,d=null,p=null,x=null,S=e.getContextAttributes(),_=null,m=null,T=[],M=[],U=new St,W=null,F=new wn;F.layers.enable(1),F.viewport=new Je;let B=new wn;B.layers.enable(2),B.viewport=new Je;let J=[F,B],w=new sl;w.layers.enable(1),w.layers.enable(2);let L=null,$=null;this.cameraAutoUpdate=!0,this.enabled=!1,this.isPresenting=!1,this.getController=function(st){let ut=T[st];return ut===void 0&&(ut=new Br,T[st]=ut),ut.getTargetRaySpace()},this.getControllerGrip=function(st){let ut=T[st];return ut===void 0&&(ut=new Br,T[st]=ut),ut.getGripSpace()},this.getHand=function(st){let ut=T[st];return ut===void 0&&(ut=new Br,T[st]=ut),ut.getHandSpace()};function ot(st){let ut=M.indexOf(st.inputSource);if(ut===-1)return;let Nt=T[ut];Nt!==void 0&&(Nt.update(st.inputSource,st.frame,l||a),Nt.dispatchEvent({type:st.type,data:st.inputSource}))}function Mt(){s.removeEventListener("select",ot),s.removeEventListener("selectstart",ot),s.removeEventListener("selectend",ot),s.removeEventListener("squeeze",ot),s.removeEventListener("squeezestart",ot),s.removeEventListener("squeezeend",ot),s.removeEventListener("end",Mt),s.removeEventListener("inputsourceschange",X);for(let st=0;st<T.length;st++){let ut=M[st];ut!==null&&(M[st]=null,T[st].disconnect(ut))}L=null,$=null,t.setRenderTarget(_),p=null,d=null,f=null,s=null,m=null,Dt.stop(),n.isPresenting=!1,t.setPixelRatio(W),t.setSize(U.width,U.height,!1),n.dispatchEvent({type:"sessionend"})}this.setFramebufferScaleFactor=function(st){r=st,n.isPresenting===!0&&console.warn("THREE.WebXRManager: Cannot change framebuffer scale while presenting.")},this.setReferenceSpaceType=function(st){o=st,n.isPresenting===!0&&console.warn("THREE.WebXRManager: Cannot change reference space type while presenting.")},this.getReferenceSpace=function(){return l||a},this.setReferenceSpace=function(st){l=st},this.getBaseLayer=function(){return d!==null?d:p},this.getBinding=function(){return f},this.getFrame=function(){return x},this.getSession=function(){return s},this.setSession=async function(st){if(s=st,s!==null){if(_=t.getRenderTarget(),s.addEventListener("select",ot),s.addEventListener("selectstart",ot),s.addEventListener("selectend",ot),s.addEventListener("squeeze",ot),s.addEventListener("squeezestart",ot),s.addEventListener("squeezeend",ot),s.addEventListener("end",Mt),s.addEventListener("inputsourceschange",X),S.xrCompatible!==!0&&await e.makeXRCompatible(),W=t.getPixelRatio(),t.getSize(U),s.renderState.layers===void 0||t.capabilities.isWebGL2===!1){let ut={antialias:s.renderState.layers===void 0?S.antialias:!0,alpha:!0,depth:S.depth,stencil:S.stencil,framebufferScaleFactor:r};p=new XRWebGLLayer(s,e,ut),s.updateRenderState({baseLayer:p}),t.setPixelRatio(1),t.setSize(p.framebufferWidth,p.framebufferHeight,!1),m=new Ni(p.framebufferWidth,p.framebufferHeight,{format:hi,type:Qi,colorSpace:t.outputColorSpace,stencilBuffer:S.stencil})}else{let ut=null,Nt=null,Ft=null;S.depth&&(Ft=S.stencil?e.DEPTH24_STENCIL8:e.DEPTH_COMPONENT24,ut=S.stencil?dr:Ms,Nt=S.stencil?ys:$i);let Bt={colorFormat:e.RGBA8,depthFormat:Ft,scaleFactor:r};f=new XRWebGLBinding(s,e),d=f.createProjectionLayer(Bt),s.updateRenderState({layers:[d]}),t.setPixelRatio(1),t.setSize(d.textureWidth,d.textureHeight,!1),m=new Ni(d.textureWidth,d.textureHeight,{format:hi,type:Qi,depthTexture:new _a(d.textureWidth,d.textureHeight,Nt,void 0,void 0,void 0,void 0,void 0,void 0,ut),stencilBuffer:S.stencil,colorSpace:t.outputColorSpace,samples:S.antialias?4:0});let se=t.properties.get(m);se.__ignoreDepthValues=d.ignoreDepthValues}m.isXRRenderTarget=!0,this.setFoveation(c),l=null,a=await s.requestReferenceSpace(o),Dt.setContext(s),Dt.start(),n.isPresenting=!0,n.dispatchEvent({type:"sessionstart"})}},this.getEnvironmentBlendMode=function(){if(s!==null)return s.environmentBlendMode};function X(st){for(let ut=0;ut<st.removed.length;ut++){let Nt=st.removed[ut],Ft=M.indexOf(Nt);Ft>=0&&(M[Ft]=null,T[Ft].disconnect(Nt))}for(let ut=0;ut<st.added.length;ut++){let Nt=st.added[ut],Ft=M.indexOf(Nt);if(Ft===-1){for(let se=0;se<T.length;se++)if(se>=M.length){M.push(Nt),Ft=se;break}else if(M[se]===null){M[se]=Nt,Ft=se;break}if(Ft===-1)break}let Bt=T[Ft];Bt&&Bt.connect(Nt)}}let K=new O,tt=new O;function it(st,ut,Nt){K.setFromMatrixPosition(ut.matrixWorld),tt.setFromMatrixPosition(Nt.matrixWorld);let Ft=K.distanceTo(tt),Bt=ut.projectionMatrix.elements,se=Nt.projectionMatrix.elements,Jt=Bt[14]/(Bt[10]-1),Wt=Bt[14]/(Bt[10]+1),le=(Bt[9]+1)/Bt[5],z=(Bt[9]-1)/Bt[5],Tt=(Bt[8]-1)/Bt[0],rt=(se[8]+1)/se[0],bt=Jt*Tt,ht=Jt*rt,qt=Ft/(-Tt+rt),It=qt*-Tt;ut.matrixWorld.decompose(st.position,st.quaternion,st.scale),st.translateX(It),st.translateZ(qt),st.matrixWorld.compose(st.position,st.quaternion,st.scale),st.matrixWorldInverse.copy(st.matrixWorld).invert();let R=Jt+qt,b=Wt+qt,Y=bt-It,xt=ht+(Ft-It),mt=le*Wt/b*R,gt=z*Wt/b*R;st.projectionMatrix.makePerspective(Y,xt,mt,gt,R,b),st.projectionMatrixInverse.copy(st.projectionMatrix).invert()}function ft(st,ut){ut===null?st.matrixWorld.copy(st.matrix):st.matrixWorld.multiplyMatrices(ut.matrixWorld,st.matrix),st.matrixWorldInverse.copy(st.matrixWorld).invert()}this.updateCamera=function(st){if(s===null)return;w.near=B.near=F.near=st.near,w.far=B.far=F.far=st.far,(L!==w.near||$!==w.far)&&(s.updateRenderState({depthNear:w.near,depthFar:w.far}),L=w.near,$=w.far);let ut=st.parent,Nt=w.cameras;ft(w,ut);for(let Ft=0;Ft<Nt.length;Ft++)ft(Nt[Ft],ut);Nt.length===2?it(w,F,B):w.projectionMatrix.copy(F.projectionMatrix),nt(st,w,ut)};function nt(st,ut,Nt){Nt===null?st.matrix.copy(ut.matrixWorld):(st.matrix.copy(Nt.matrixWorld),st.matrix.invert(),st.matrix.multiply(ut.matrixWorld)),st.matrix.decompose(st.position,st.quaternion,st.scale),st.updateMatrixWorld(!0),st.projectionMatrix.copy(ut.projectionMatrix),st.projectionMatrixInverse.copy(ut.projectionMatrixInverse),st.isPerspectiveCamera&&(st.fov=Vr*2*Math.atan(1/st.projectionMatrix.elements[5]),st.zoom=1)}this.getCamera=function(){return w},this.getFoveation=function(){if(!(d===null&&p===null))return c},this.setFoveation=function(st){c=st,d!==null&&(d.fixedFoveation=st),p!==null&&p.fixedFoveation!==void 0&&(p.fixedFoveation=st)};let ct=null;function lt(st,ut){if(h=ut.getViewerPose(l||a),x=ut,h!==null){let Nt=h.views;p!==null&&(t.setRenderTargetFramebuffer(m,p.framebuffer),t.setRenderTarget(m));let Ft=!1;Nt.length!==w.cameras.length&&(w.cameras.length=0,Ft=!0);for(let Bt=0;Bt<Nt.length;Bt++){let se=Nt[Bt],Jt=null;if(p!==null)Jt=p.getViewport(se);else{let le=f.getViewSubImage(d,se);Jt=le.viewport,Bt===0&&(t.setRenderTargetTextures(m,le.colorTexture,d.ignoreDepthValues?void 0:le.depthStencilTexture),t.setRenderTarget(m))}let Wt=J[Bt];Wt===void 0&&(Wt=new wn,Wt.layers.enable(Bt),Wt.viewport=new Je,J[Bt]=Wt),Wt.matrix.fromArray(se.transform.matrix),Wt.matrix.decompose(Wt.position,Wt.quaternion,Wt.scale),Wt.projectionMatrix.fromArray(se.projectionMatrix),Wt.projectionMatrixInverse.copy(Wt.projectionMatrix).invert(),Wt.viewport.set(Jt.x,Jt.y,Jt.width,Jt.height),Bt===0&&(w.matrix.copy(Wt.matrix),w.matrix.decompose(w.position,w.quaternion,w.scale)),Ft===!0&&w.cameras.push(Wt)}}for(let Nt=0;Nt<T.length;Nt++){let Ft=M[Nt],Bt=T[Nt];Ft!==null&&Bt!==void 0&&Bt.update(Ft,ut,l||a)}ct&&ct(st,ut),ut.detectedPlanes&&n.dispatchEvent({type:"planesdetected",data:ut}),x=null}let Dt=new Tf;Dt.setAnimationLoop(lt),this.setAnimationLoop=function(st){ct=st},this.dispose=function(){}}};function tx(i,t){function e(_,m){_.matrixAutoUpdate===!0&&_.updateMatrix(),m.value.copy(_.matrix)}function n(_,m){m.color.getRGB(_.fogColor.value,wf(i)),m.isFog?(_.fogNear.value=m.near,_.fogFar.value=m.far):m.isFogExp2&&(_.fogDensity.value=m.density)}function s(_,m,T,M,U){m.isMeshBasicMaterial||m.isMeshLambertMaterial?r(_,m):m.isMeshToonMaterial?(r(_,m),f(_,m)):m.isMeshPhongMaterial?(r(_,m),h(_,m)):m.isMeshStandardMaterial?(r(_,m),d(_,m),m.isMeshPhysicalMaterial&&p(_,m,U)):m.isMeshMatcapMaterial?(r(_,m),x(_,m)):m.isMeshDepthMaterial?r(_,m):m.isMeshDistanceMaterial?(r(_,m),S(_,m)):m.isMeshNormalMaterial?r(_,m):m.isLineBasicMaterial?(a(_,m),m.isLineDashedMaterial&&o(_,m)):m.isPointsMaterial?c(_,m,T,M):m.isSpriteMaterial?l(_,m):m.isShadowMaterial?(_.color.value.copy(m.color),_.opacity.value=m.opacity):m.isShaderMaterial&&(m.uniformsNeedUpdate=!1)}function r(_,m){_.opacity.value=m.opacity,m.color&&_.diffuse.value.copy(m.color),m.emissive&&_.emissive.value.copy(m.emissive).multiplyScalar(m.emissiveIntensity),m.map&&(_.map.value=m.map,e(m.map,_.mapTransform)),m.alphaMap&&(_.alphaMap.value=m.alphaMap,e(m.alphaMap,_.alphaMapTransform)),m.bumpMap&&(_.bumpMap.value=m.bumpMap,e(m.bumpMap,_.bumpMapTransform),_.bumpScale.value=m.bumpScale,m.side===Tn&&(_.bumpScale.value*=-1)),m.normalMap&&(_.normalMap.value=m.normalMap,e(m.normalMap,_.normalMapTransform),_.normalScale.value.copy(m.normalScale),m.side===Tn&&_.normalScale.value.negate()),m.displacementMap&&(_.displacementMap.value=m.displacementMap,e(m.displacementMap,_.displacementMapTransform),_.displacementScale.value=m.displacementScale,_.displacementBias.value=m.displacementBias),m.emissiveMap&&(_.emissiveMap.value=m.emissiveMap,e(m.emissiveMap,_.emissiveMapTransform)),m.specularMap&&(_.specularMap.value=m.specularMap,e(m.specularMap,_.specularMapTransform)),m.alphaTest>0&&(_.alphaTest.value=m.alphaTest);let T=t.get(m).envMap;if(T&&(_.envMap.value=T,_.flipEnvMap.value=T.isCubeTexture&&T.isRenderTargetTexture===!1?-1:1,_.reflectivity.value=m.reflectivity,_.ior.value=m.ior,_.refractionRatio.value=m.refractionRatio),m.lightMap){_.lightMap.value=m.lightMap;let M=i._useLegacyLights===!0?Math.PI:1;_.lightMapIntensity.value=m.lightMapIntensity*M,e(m.lightMap,_.lightMapTransform)}m.aoMap&&(_.aoMap.value=m.aoMap,_.aoMapIntensity.value=m.aoMapIntensity,e(m.aoMap,_.aoMapTransform))}function a(_,m){_.diffuse.value.copy(m.color),_.opacity.value=m.opacity,m.map&&(_.map.value=m.map,e(m.map,_.mapTransform))}function o(_,m){_.dashSize.value=m.dashSize,_.totalSize.value=m.dashSize+m.gapSize,_.scale.value=m.scale}function c(_,m,T,M){_.diffuse.value.copy(m.color),_.opacity.value=m.opacity,_.size.value=m.size*T,_.scale.value=M*.5,m.map&&(_.map.value=m.map,e(m.map,_.uvTransform)),m.alphaMap&&(_.alphaMap.value=m.alphaMap,e(m.alphaMap,_.alphaMapTransform)),m.alphaTest>0&&(_.alphaTest.value=m.alphaTest)}function l(_,m){_.diffuse.value.copy(m.color),_.opacity.value=m.opacity,_.rotation.value=m.rotation,m.map&&(_.map.value=m.map,e(m.map,_.mapTransform)),m.alphaMap&&(_.alphaMap.value=m.alphaMap,e(m.alphaMap,_.alphaMapTransform)),m.alphaTest>0&&(_.alphaTest.value=m.alphaTest)}function h(_,m){_.specular.value.copy(m.specular),_.shininess.value=Math.max(m.shininess,1e-4)}function f(_,m){m.gradientMap&&(_.gradientMap.value=m.gradientMap)}function d(_,m){_.metalness.value=m.metalness,m.metalnessMap&&(_.metalnessMap.value=m.metalnessMap,e(m.metalnessMap,_.metalnessMapTransform)),_.roughness.value=m.roughness,m.roughnessMap&&(_.roughnessMap.value=m.roughnessMap,e(m.roughnessMap,_.roughnessMapTransform)),t.get(m).envMap&&(_.envMapIntensity.value=m.envMapIntensity)}function p(_,m,T){_.ior.value=m.ior,m.sheen>0&&(_.sheenColor.value.copy(m.sheenColor).multiplyScalar(m.sheen),_.sheenRoughness.value=m.sheenRoughness,m.sheenColorMap&&(_.sheenColorMap.value=m.sheenColorMap,e(m.sheenColorMap,_.sheenColorMapTransform)),m.sheenRoughnessMap&&(_.sheenRoughnessMap.value=m.sheenRoughnessMap,e(m.sheenRoughnessMap,_.sheenRoughnessMapTransform))),m.clearcoat>0&&(_.clearcoat.value=m.clearcoat,_.clearcoatRoughness.value=m.clearcoatRoughness,m.clearcoatMap&&(_.clearcoatMap.value=m.clearcoatMap,e(m.clearcoatMap,_.clearcoatMapTransform)),m.clearcoatRoughnessMap&&(_.clearcoatRoughnessMap.value=m.clearcoatRoughnessMap,e(m.clearcoatRoughnessMap,_.clearcoatRoughnessMapTransform)),m.clearcoatNormalMap&&(_.clearcoatNormalMap.value=m.clearcoatNormalMap,e(m.clearcoatNormalMap,_.clearcoatNormalMapTransform),_.clearcoatNormalScale.value.copy(m.clearcoatNormalScale),m.side===Tn&&_.clearcoatNormalScale.value.negate())),m.iridescence>0&&(_.iridescence.value=m.iridescence,_.iridescenceIOR.value=m.iridescenceIOR,_.iridescenceThicknessMinimum.value=m.iridescenceThicknessRange[0],_.iridescenceThicknessMaximum.value=m.iridescenceThicknessRange[1],m.iridescenceMap&&(_.iridescenceMap.value=m.iridescenceMap,e(m.iridescenceMap,_.iridescenceMapTransform)),m.iridescenceThicknessMap&&(_.iridescenceThicknessMap.value=m.iridescenceThicknessMap,e(m.iridescenceThicknessMap,_.iridescenceThicknessMapTransform))),m.transmission>0&&(_.transmission.value=m.transmission,_.transmissionSamplerMap.value=T.texture,_.transmissionSamplerSize.value.set(T.width,T.height),m.transmissionMap&&(_.transmissionMap.value=m.transmissionMap,e(m.transmissionMap,_.transmissionMapTransform)),_.thickness.value=m.thickness,m.thicknessMap&&(_.thicknessMap.value=m.thicknessMap,e(m.thicknessMap,_.thicknessMapTransform)),_.attenuationDistance.value=m.attenuationDistance,_.attenuationColor.value.copy(m.attenuationColor)),m.anisotropy>0&&(_.anisotropyVector.value.set(m.anisotropy*Math.cos(m.anisotropyRotation),m.anisotropy*Math.sin(m.anisotropyRotation)),m.anisotropyMap&&(_.anisotropyMap.value=m.anisotropyMap,e(m.anisotropyMap,_.anisotropyMapTransform))),_.specularIntensity.value=m.specularIntensity,_.specularColor.value.copy(m.specularColor),m.specularColorMap&&(_.specularColorMap.value=m.specularColorMap,e(m.specularColorMap,_.specularColorMapTransform)),m.specularIntensityMap&&(_.specularIntensityMap.value=m.specularIntensityMap,e(m.specularIntensityMap,_.specularIntensityMapTransform))}function x(_,m){m.matcap&&(_.matcap.value=m.matcap)}function S(_,m){let T=t.get(m).light;_.referencePosition.value.setFromMatrixPosition(T.matrixWorld),_.nearDistance.value=T.shadow.camera.near,_.farDistance.value=T.shadow.camera.far}return{refreshFogUniforms:n,refreshMaterialUniforms:s}}function ex(i,t,e,n){let s={},r={},a=[],o=e.isWebGL2?i.getParameter(i.MAX_UNIFORM_BUFFER_BINDINGS):0;function c(T,M){let U=M.program;n.uniformBlockBinding(T,U)}function l(T,M){let U=s[T.id];U===void 0&&(x(T),U=h(T),s[T.id]=U,T.addEventListener("dispose",_));let W=M.program;n.updateUBOMapping(T,W);let F=t.render.frame;r[T.id]!==F&&(d(T),r[T.id]=F)}function h(T){let M=f();T.__bindingPointIndex=M;let U=i.createBuffer(),W=T.__size,F=T.usage;return i.bindBuffer(i.UNIFORM_BUFFER,U),i.bufferData(i.UNIFORM_BUFFER,W,F),i.bindBuffer(i.UNIFORM_BUFFER,null),i.bindBufferBase(i.UNIFORM_BUFFER,M,U),U}function f(){for(let T=0;T<o;T++)if(a.indexOf(T)===-1)return a.push(T),T;return console.error("THREE.WebGLRenderer: Maximum number of simultaneously usable uniforms groups reached."),0}function d(T){let M=s[T.id],U=T.uniforms,W=T.__cache;i.bindBuffer(i.UNIFORM_BUFFER,M);for(let F=0,B=U.length;F<B;F++){let J=Array.isArray(U[F])?U[F]:[U[F]];for(let w=0,L=J.length;w<L;w++){let $=J[w];if(p($,F,w,W)===!0){let ot=$.__offset,Mt=Array.isArray($.value)?$.value:[$.value],X=0;for(let K=0;K<Mt.length;K++){let tt=Mt[K],it=S(tt);typeof tt=="number"||typeof tt=="boolean"?($.__data[0]=tt,i.bufferSubData(i.UNIFORM_BUFFER,ot+X,$.__data)):tt.isMatrix3?($.__data[0]=tt.elements[0],$.__data[1]=tt.elements[1],$.__data[2]=tt.elements[2],$.__data[3]=0,$.__data[4]=tt.elements[3],$.__data[5]=tt.elements[4],$.__data[6]=tt.elements[5],$.__data[7]=0,$.__data[8]=tt.elements[6],$.__data[9]=tt.elements[7],$.__data[10]=tt.elements[8],$.__data[11]=0):(tt.toArray($.__data,X),X+=it.storage/Float32Array.BYTES_PER_ELEMENT)}i.bufferSubData(i.UNIFORM_BUFFER,ot,$.__data)}}}i.bindBuffer(i.UNIFORM_BUFFER,null)}function p(T,M,U,W){let F=T.value,B=M+"_"+U;if(W[B]===void 0)return typeof F=="number"||typeof F=="boolean"?W[B]=F:W[B]=F.clone(),!0;{let J=W[B];if(typeof F=="number"||typeof F=="boolean"){if(J!==F)return W[B]=F,!0}else if(J.equals(F)===!1)return J.copy(F),!0}return!1}function x(T){let M=T.uniforms,U=0,W=16;for(let B=0,J=M.length;B<J;B++){let w=Array.isArray(M[B])?M[B]:[M[B]];for(let L=0,$=w.length;L<$;L++){let ot=w[L],Mt=Array.isArray(ot.value)?ot.value:[ot.value];for(let X=0,K=Mt.length;X<K;X++){let tt=Mt[X],it=S(tt),ft=U%W;ft!==0&&W-ft<it.boundary&&(U+=W-ft),ot.__data=new Float32Array(it.storage/Float32Array.BYTES_PER_ELEMENT),ot.__offset=U,U+=it.storage}}}let F=U%W;return F>0&&(U+=W-F),T.__size=U,T.__cache={},this}function S(T){let M={boundary:0,storage:0};return typeof T=="number"||typeof T=="boolean"?(M.boundary=4,M.storage=4):T.isVector2?(M.boundary=8,M.storage=8):T.isVector3||T.isColor?(M.boundary=16,M.storage=12):T.isVector4?(M.boundary=16,M.storage=16):T.isMatrix3?(M.boundary=48,M.storage=48):T.isMatrix4?(M.boundary=64,M.storage=64):T.isTexture?console.warn("THREE.WebGLRenderer: Texture samplers can not be part of an uniforms group."):console.warn("THREE.WebGLRenderer: Unsupported uniform value type.",T),M}function _(T){let M=T.target;M.removeEventListener("dispose",_);let U=a.indexOf(M.__bindingPointIndex);a.splice(U,1),i.deleteBuffer(s[M.id]),delete s[M.id],delete r[M.id]}function m(){for(let T in s)i.deleteBuffer(s[T]);a=[],s={},r={}}return{bind:c,update:l,dispose:m}}var Zr=class{constructor(t={}){let{canvas:e=up(),context:n=null,depth:s=!0,stencil:r=!0,alpha:a=!1,antialias:o=!1,premultipliedAlpha:c=!0,preserveDrawingBuffer:l=!1,powerPreference:h="default",failIfMajorPerformanceCaveat:f=!1}=t;this.isWebGLRenderer=!0;let d;n!==null?d=n.getContextAttributes().alpha:d=a;let p=new Uint32Array(4),x=new Int32Array(4),S=null,_=null,m=[],T=[];this.domElement=e,this.debug={checkShaderErrors:!0,onShaderError:null},this.autoClear=!0,this.autoClearColor=!0,this.autoClearDepth=!0,this.autoClearStencil=!0,this.sortObjects=!0,this.clippingPlanes=[],this.localClippingEnabled=!1,this._outputColorSpace=sn,this._useLegacyLights=!1,this.toneMapping=ji,this.toneMappingExposure=1;let M=this,U=!1,W=0,F=0,B=null,J=-1,w=null,L=new Je,$=new Je,ot=null,Mt=new fe(0),X=0,K=e.width,tt=e.height,it=1,ft=null,nt=null,ct=new Je(0,0,K,tt),lt=new Je(0,0,K,tt),Dt=!1,st=new qr,ut=!1,Nt=!1,Ft=null,Bt=new Ue,se=new St,Jt=new O,Wt={background:null,fog:null,environment:null,overrideMaterial:null,isScene:!0};function le(){return B===null?it:1}let z=n;function Tt(P,Z){for(let j=0;j<P.length;j++){let et=P[j],q=e.getContext(et,Z);if(q!==null)return q}return null}try{let P={alpha:!0,depth:s,stencil:r,antialias:o,premultipliedAlpha:c,preserveDrawingBuffer:l,powerPreference:h,failIfMajorPerformanceCaveat:f};if("setAttribute"in e&&e.setAttribute("data-engine","three.js r160"),e.addEventListener("webglcontextlost",wt,!1),e.addEventListener("webglcontextrestored",k,!1),e.addEventListener("webglcontextcreationerror",Rt,!1),z===null){let Z=["webgl2","webgl","experimental-webgl"];if(M.isWebGL1Renderer===!0&&Z.shift(),z=Tt(Z,P),z===null)throw Tt(Z)?new Error("Error creating WebGL context with your selected attributes."):new Error("Error creating WebGL context.")}typeof WebGLRenderingContext!="undefined"&&z instanceof WebGLRenderingContext&&console.warn("THREE.WebGLRenderer: WebGL 1 support was deprecated in r153 and will be removed in r163."),z.getShaderPrecisionFormat===void 0&&(z.getShaderPrecisionFormat=function(){return{rangeMin:1,rangeMax:1,precision:1}})}catch(P){throw console.error("THREE.WebGLRenderer: "+P.message),P}let rt,bt,ht,qt,It,R,b,Y,xt,mt,gt,Gt,Lt,At,ee,pe,dt,Re,Se,Zt,Kt,Ht,ae,Ie;function Ye(){rt=new yg(z),bt=new pg(z,rt,t),rt.init(bt),Ht=new j_(z,rt,bt),ht=new J_(z,rt,bt),qt=new bg(z),It=new B_,R=new K_(z,rt,ht,It,bt,Ht,qt),b=new gg(M),Y=new vg(M),xt=new Ip(z,bt),ae=new fg(z,rt,xt,bt),mt=new Mg(z,xt,qt,ae),gt=new Ag(z,mt,xt,qt),Se=new Tg(z,bt,R),pe=new mg(It),Gt=new O_(M,b,Y,rt,bt,ae,pe),Lt=new tx(M,It),At=new H_,ee=new Y_(rt,bt),Re=new ug(M,b,Y,ht,gt,d,c),dt=new $_(M,gt,bt),Ie=new ex(z,qt,bt,ht),Zt=new dg(z,rt,qt,bt),Kt=new Sg(z,rt,qt,bt),qt.programs=Gt.programs,M.capabilities=bt,M.extensions=rt,M.properties=It,M.renderLists=At,M.shadowMap=dt,M.state=ht,M.info=qt}Ye();let te=new rl(M,z);this.xr=te,this.getContext=function(){return z},this.getContextAttributes=function(){return z.getContextAttributes()},this.forceContextLoss=function(){let P=rt.get("WEBGL_lose_context");P&&P.loseContext()},this.forceContextRestore=function(){let P=rt.get("WEBGL_lose_context");P&&P.restoreContext()},this.getPixelRatio=function(){return it},this.setPixelRatio=function(P){P!==void 0&&(it=P,this.setSize(K,tt,!1))},this.getSize=function(P){return P.set(K,tt)},this.setSize=function(P,Z,j=!0){if(te.isPresenting){console.warn("THREE.WebGLRenderer: Can't change size while VR device is presenting.");return}K=P,tt=Z,e.width=Math.floor(P*it),e.height=Math.floor(Z*it),j===!0&&(e.style.width=P+"px",e.style.height=Z+"px"),this.setViewport(0,0,P,Z)},this.getDrawingBufferSize=function(P){return P.set(K*it,tt*it).floor()},this.setDrawingBufferSize=function(P,Z,j){K=P,tt=Z,it=j,e.width=Math.floor(P*j),e.height=Math.floor(Z*j),this.setViewport(0,0,P,Z)},this.getCurrentViewport=function(P){return P.copy(L)},this.getViewport=function(P){return P.copy(ct)},this.setViewport=function(P,Z,j,et){P.isVector4?ct.set(P.x,P.y,P.z,P.w):ct.set(P,Z,j,et),ht.viewport(L.copy(ct).multiplyScalar(it).floor())},this.getScissor=function(P){return P.copy(lt)},this.setScissor=function(P,Z,j,et){P.isVector4?lt.set(P.x,P.y,P.z,P.w):lt.set(P,Z,j,et),ht.scissor($.copy(lt).multiplyScalar(it).floor())},this.getScissorTest=function(){return Dt},this.setScissorTest=function(P){ht.setScissorTest(Dt=P)},this.setOpaqueSort=function(P){ft=P},this.setTransparentSort=function(P){nt=P},this.getClearColor=function(P){return P.copy(Re.getClearColor())},this.setClearColor=function(){Re.setClearColor.apply(Re,arguments)},this.getClearAlpha=function(){return Re.getClearAlpha()},this.setClearAlpha=function(){Re.setClearAlpha.apply(Re,arguments)},this.clear=function(P=!0,Z=!0,j=!0){let et=0;if(P){let q=!1;if(B!==null){let C=B.texture.format;q=C===xf||C===_f||C===gf}if(q){let C=B.texture.type,Xt=C===Qi||C===$i||C===Ll||C===ys||C===pf||C===mf,Qt=Re.getClearColor(),ie=Re.getClearAlpha(),me=Qt.r,ue=Qt.g,ge=Qt.b;Xt?(p[0]=me,p[1]=ue,p[2]=ge,p[3]=ie,z.clearBufferuiv(z.COLOR,0,p)):(x[0]=me,x[1]=ue,x[2]=ge,x[3]=ie,z.clearBufferiv(z.COLOR,0,x))}else et|=z.COLOR_BUFFER_BIT}Z&&(et|=z.DEPTH_BUFFER_BIT),j&&(et|=z.STENCIL_BUFFER_BIT,this.state.buffers.stencil.setMask(4294967295)),z.clear(et)},this.clearColor=function(){this.clear(!0,!1,!1)},this.clearDepth=function(){this.clear(!1,!0,!1)},this.clearStencil=function(){this.clear(!1,!1,!0)},this.dispose=function(){e.removeEventListener("webglcontextlost",wt,!1),e.removeEventListener("webglcontextrestored",k,!1),e.removeEventListener("webglcontextcreationerror",Rt,!1),At.dispose(),ee.dispose(),It.dispose(),b.dispose(),Y.dispose(),gt.dispose(),ae.dispose(),Ie.dispose(),Gt.dispose(),te.dispose(),te.removeEventListener("sessionstart",xn),te.removeEventListener("sessionend",Ce),Ft&&(Ft.dispose(),Ft=null),fn.stop()};function wt(P){P.preventDefault(),console.log("THREE.WebGLRenderer: Context Lost."),U=!0}function k(){console.log("THREE.WebGLRenderer: Context Restored."),U=!1;let P=qt.autoReset,Z=dt.enabled,j=dt.autoUpdate,et=dt.needsUpdate,q=dt.type;Ye(),qt.autoReset=P,dt.enabled=Z,dt.autoUpdate=j,dt.needsUpdate=et,dt.type=q}function Rt(P){console.error("THREE.WebGLRenderer: A WebGL context could not be created. Reason: ",P.statusMessage)}function Ut(P){let Z=P.target;Z.removeEventListener("dispose",Ut),re(Z)}function re(P){jt(P),It.remove(P)}function jt(P){let Z=It.get(P).programs;Z!==void 0&&(Z.forEach(function(j){Gt.releaseProgram(j)}),P.isShaderMaterial&&Gt.releaseShaderCache(P))}this.renderBufferDirect=function(P,Z,j,et,q,C){Z===null&&(Z=Wt);let Xt=q.isMesh&&q.matrixWorld.determinant()<0,Qt=He(P,Z,j,et,q);ht.setMaterial(et,Xt);let ie=j.index,me=1;if(et.wireframe===!0){if(ie=mt.getWireframeAttribute(j),ie===void 0)return;me=2}let ue=j.drawRange,ge=j.attributes.position,yt=ue.start*me,Ot=(ue.start+ue.count)*me;C!==null&&(yt=Math.max(yt,C.start*me),Ot=Math.min(Ot,(C.start+C.count)*me)),ie!==null?(yt=Math.max(yt,0),Ot=Math.min(Ot,ie.count)):ge!=null&&(yt=Math.max(yt,0),Ot=Math.min(Ot,ge.count));let zt=Ot-yt;if(zt<0||zt===1/0)return;ae.setup(q,et,Qt,j,ie);let en,ke=Zt;if(ie!==null&&(en=xt.get(ie),ke=Kt,ke.setIndex(en)),q.isMesh)et.wireframe===!0?(ht.setLineWidth(et.wireframeLinewidth*le()),ke.setMode(z.LINES)):ke.setMode(z.TRIANGLES);else if(q.isLine){let ce=et.linewidth;ce===void 0&&(ce=1),ht.setLineWidth(ce*le()),q.isLineSegments?ke.setMode(z.LINES):q.isLineLoop?ke.setMode(z.LINE_LOOP):ke.setMode(z.LINE_STRIP)}else q.isPoints?ke.setMode(z.POINTS):q.isSprite&&ke.setMode(z.TRIANGLES);if(q.isBatchedMesh)ke.renderMultiDraw(q._multiDrawStarts,q._multiDrawCounts,q._multiDrawCount);else if(q.isInstancedMesh)ke.renderInstances(yt,zt,q.count);else if(j.isInstancedBufferGeometry){let ce=j._maxInstanceCount!==void 0?j._maxInstanceCount:1/0,dn=Math.min(j.instanceCount,ce);ke.renderInstances(yt,zt,dn)}else ke.render(yt,zt)};function De(P,Z,j){P.transparent===!0&&P.side===ln&&P.forceSinglePass===!1?(P.side=Tn,P.needsUpdate=!0,Ds(P,Z,j),P.side=es,P.needsUpdate=!0,Ds(P,Z,j),P.side=ln):Ds(P,Z,j)}this.compile=function(P,Z,j=null){j===null&&(j=P),_=ee.get(j),_.init(),T.push(_),j.traverseVisible(function(q){q.isLight&&q.layers.test(Z.layers)&&(_.pushLight(q),q.castShadow&&_.pushShadow(q))}),P!==j&&P.traverseVisible(function(q){q.isLight&&q.layers.test(Z.layers)&&(_.pushLight(q),q.castShadow&&_.pushShadow(q))}),_.setupLights(M._useLegacyLights);let et=new Set;return P.traverse(function(q){let C=q.material;if(C)if(Array.isArray(C))for(let Xt=0;Xt<C.length;Xt++){let Qt=C[Xt];De(Qt,j,q),et.add(Qt)}else De(C,j,q),et.add(C)}),T.pop(),_=null,et},this.compileAsync=function(P,Z,j=null){let et=this.compile(P,Z,j);return new Promise(q=>{function C(){if(et.forEach(function(Xt){It.get(Xt).currentProgram.isReady()&&et.delete(Xt)}),et.size===0){q(P);return}setTimeout(C,10)}rt.get("KHR_parallel_shader_compile")!==null?C():setTimeout(C,10)})};let Fe=null;function rn(P){Fe&&Fe(P)}function xn(){fn.stop()}function Ce(){fn.start()}let fn=new Tf;fn.setAnimationLoop(rn),typeof self!="undefined"&&fn.setContext(self),this.setAnimationLoop=function(P){Fe=P,te.setAnimationLoop(P),P===null?fn.stop():fn.start()},te.addEventListener("sessionstart",xn),te.addEventListener("sessionend",Ce),this.render=function(P,Z){if(Z!==void 0&&Z.isCamera!==!0){console.error("THREE.WebGLRenderer.render: camera is not an instance of THREE.Camera.");return}if(U===!0)return;P.matrixWorldAutoUpdate===!0&&P.updateMatrixWorld(),Z.parent===null&&Z.matrixWorldAutoUpdate===!0&&Z.updateMatrixWorld(),te.enabled===!0&&te.isPresenting===!0&&(te.cameraAutoUpdate===!0&&te.updateCamera(Z),Z=te.getCamera()),P.isScene===!0&&P.onBeforeRender(M,P,Z,B),_=ee.get(P,T.length),_.init(),T.push(_),Bt.multiplyMatrices(Z.projectionMatrix,Z.matrixWorldInverse),st.setFromProjectionMatrix(Bt),Nt=this.localClippingEnabled,ut=pe.init(this.clippingPlanes,Nt),S=At.get(P,m.length),S.init(),m.push(S),Gn(P,Z,0,M.sortObjects),S.finish(),M.sortObjects===!0&&S.sort(ft,nt),this.info.render.frame++,ut===!0&&pe.beginShadows();let j=_.state.shadowsArray;if(dt.render(j,P,Z),ut===!0&&pe.endShadows(),this.info.autoReset===!0&&this.info.reset(),Re.render(S,P),_.setupLights(M._useLegacyLights),Z.isArrayCamera){let et=Z.cameras;for(let q=0,C=et.length;q<C;q++){let Xt=et[q];as(S,P,Xt,Xt.viewport)}}else as(S,P,Z);B!==null&&(R.updateMultisampleRenderTarget(B),R.updateRenderTargetMipmap(B)),P.isScene===!0&&P.onAfterRender(M,P,Z),ae.resetDefaultState(),J=-1,w=null,T.pop(),T.length>0?_=T[T.length-1]:_=null,m.pop(),m.length>0?S=m[m.length-1]:S=null};function Gn(P,Z,j,et){if(P.visible===!1)return;if(P.layers.test(Z.layers)){if(P.isGroup)j=P.renderOrder;else if(P.isLOD)P.autoUpdate===!0&&P.update(Z);else if(P.isLight)_.pushLight(P),P.castShadow&&_.pushShadow(P);else if(P.isSprite){if(!P.frustumCulled||st.intersectsSprite(P)){et&&Jt.setFromMatrixPosition(P.matrixWorld).applyMatrix4(Bt);let Xt=gt.update(P),Qt=P.material;Qt.visible&&S.push(P,Xt,Qt,j,Jt.z,null)}}else if((P.isMesh||P.isLine||P.isPoints)&&(!P.frustumCulled||st.intersectsObject(P))){let Xt=gt.update(P),Qt=P.material;if(et&&(P.boundingSphere!==void 0?(P.boundingSphere===null&&P.computeBoundingSphere(),Jt.copy(P.boundingSphere.center)):(Xt.boundingSphere===null&&Xt.computeBoundingSphere(),Jt.copy(Xt.boundingSphere.center)),Jt.applyMatrix4(P.matrixWorld).applyMatrix4(Bt)),Array.isArray(Qt)){let ie=Xt.groups;for(let me=0,ue=ie.length;me<ue;me++){let ge=ie[me],yt=Qt[ge.materialIndex];yt&&yt.visible&&S.push(P,Xt,yt,j,Jt.z,ge)}}else Qt.visible&&S.push(P,Xt,Qt,j,Jt.z,null)}}let C=P.children;for(let Xt=0,Qt=C.length;Xt<Qt;Xt++)Gn(C[Xt],Z,j,et)}function as(P,Z,j,et){let q=P.opaque,C=P.transmissive,Xt=P.transparent;_.setupLightsView(j),ut===!0&&pe.setGlobalState(M.clippingPlanes,j),C.length>0&&Ba(q,C,Z,j),et&&ht.viewport(L.copy(et)),q.length>0&&Mi(q,Z,j),C.length>0&&Mi(C,Z,j),Xt.length>0&&Mi(Xt,Z,j),ht.buffers.depth.setTest(!0),ht.buffers.depth.setMask(!0),ht.buffers.color.setMask(!0),ht.setPolygonOffset(!1)}function Ba(P,Z,j,et){if((j.isScene===!0?j.overrideMaterial:null)!==null)return;let C=bt.isWebGL2;Ft===null&&(Ft=new Ni(1,1,{generateMipmaps:!0,type:rt.has("EXT_color_buffer_half_float")?Gr:Qi,minFilter:kr,samples:C?4:0})),M.getDrawingBufferSize(se),C?Ft.setSize(se.x,se.y):Ft.setSize(ca(se.x),ca(se.y));let Xt=M.getRenderTarget();M.setRenderTarget(Ft),M.getClearColor(Mt),X=M.getClearAlpha(),X<1&&M.setClearColor(16777215,.5),M.clear();let Qt=M.toneMapping;M.toneMapping=ji,Mi(P,j,et),R.updateMultisampleRenderTarget(Ft),R.updateRenderTargetMipmap(Ft);let ie=!1;for(let me=0,ue=Z.length;me<ue;me++){let ge=Z[me],yt=ge.object,Ot=ge.geometry,zt=ge.material,en=ge.group;if(zt.side===ln&&yt.layers.test(et.layers)){let ke=zt.side;zt.side=Tn,zt.needsUpdate=!0,cs(yt,j,et,Ot,zt,en),zt.side=ke,zt.needsUpdate=!0,ie=!0}}ie===!0&&(R.updateMultisampleRenderTarget(Ft),R.updateRenderTargetMipmap(Ft)),M.setRenderTarget(Xt),M.setClearColor(Mt,X),M.toneMapping=Qt}function Mi(P,Z,j){let et=Z.isScene===!0?Z.overrideMaterial:null;for(let q=0,C=P.length;q<C;q++){let Xt=P[q],Qt=Xt.object,ie=Xt.geometry,me=et===null?Xt.material:et,ue=Xt.group;Qt.layers.test(j.layers)&&cs(Qt,Z,j,ie,me,ue)}}function cs(P,Z,j,et,q,C){P.onBeforeRender(M,Z,j,et,q,C),P.modelViewMatrix.multiplyMatrices(j.matrixWorldInverse,P.matrixWorld),P.normalMatrix.getNormalMatrix(P.modelViewMatrix),q.onBeforeRender(M,Z,j,et,P,C),q.transparent===!0&&q.side===ln&&q.forceSinglePass===!1?(q.side=Tn,q.needsUpdate=!0,M.renderBufferDirect(j,Z,et,q,P,C),q.side=es,q.needsUpdate=!0,M.renderBufferDirect(j,Z,et,q,P,C),q.side=ln):M.renderBufferDirect(j,Z,et,q,P,C),P.onAfterRender(M,Z,j,et,q,C)}function Ds(P,Z,j){Z.isScene!==!0&&(Z=Wt);let et=It.get(P),q=_.state.lights,C=_.state.shadowsArray,Xt=q.state.version,Qt=Gt.getParameters(P,q.state,C,Z,j),ie=Gt.getProgramCacheKey(Qt),me=et.programs;et.environment=P.isMeshStandardMaterial?Z.environment:null,et.fog=Z.fog,et.envMap=(P.isMeshStandardMaterial?Y:b).get(P.envMap||et.environment),me===void 0&&(P.addEventListener("dispose",Ut),me=new Map,et.programs=me);let ue=me.get(ie);if(ue!==void 0){if(et.currentProgram===ue&&et.lightsStateVersion===Xt)return ho(P,Qt),ue}else Qt.uniforms=Gt.getUniforms(P),P.onBuild(j,Qt,M),P.onBeforeCompile(Qt,M),ue=Gt.acquireProgram(Qt,ie),me.set(ie,ue),et.uniforms=Qt.uniforms;let ge=et.uniforms;return(!P.isShaderMaterial&&!P.isRawShaderMaterial||P.clipping===!0)&&(ge.clippingPlanes=pe.uniform),ho(P,Qt),et.needsLights=uo(P),et.lightsStateVersion=Xt,et.needsLights&&(ge.ambientLightColor.value=q.state.ambient,ge.lightProbe.value=q.state.probe,ge.directionalLights.value=q.state.directional,ge.directionalLightShadows.value=q.state.directionalShadow,ge.spotLights.value=q.state.spot,ge.spotLightShadows.value=q.state.spotShadow,ge.rectAreaLights.value=q.state.rectArea,ge.ltc_1.value=q.state.rectAreaLTC1,ge.ltc_2.value=q.state.rectAreaLTC2,ge.pointLights.value=q.state.point,ge.pointLightShadows.value=q.state.pointShadow,ge.hemisphereLights.value=q.state.hemi,ge.directionalShadowMap.value=q.state.directionalShadowMap,ge.directionalShadowMatrix.value=q.state.directionalShadowMatrix,ge.spotShadowMap.value=q.state.spotShadowMap,ge.spotLightMatrix.value=q.state.spotLightMatrix,ge.spotLightMap.value=q.state.spotLightMap,ge.pointShadowMap.value=q.state.pointShadowMap,ge.pointShadowMatrix.value=q.state.pointShadowMatrix),et.currentProgram=ue,et.uniformsList=null,ue}function Si(P){if(P.uniformsList===null){let Z=P.currentProgram.getUniforms();P.uniformsList=lr.seqWithValue(Z.seq,P.uniforms)}return P.uniformsList}function ho(P,Z){let j=It.get(P);j.outputColorSpace=Z.outputColorSpace,j.batching=Z.batching,j.instancing=Z.instancing,j.instancingColor=Z.instancingColor,j.skinning=Z.skinning,j.morphTargets=Z.morphTargets,j.morphNormals=Z.morphNormals,j.morphColors=Z.morphColors,j.morphTargetsCount=Z.morphTargetsCount,j.numClippingPlanes=Z.numClippingPlanes,j.numIntersection=Z.numClipIntersection,j.vertexAlphas=Z.vertexAlphas,j.vertexTangents=Z.vertexTangents,j.toneMapping=Z.toneMapping}function He(P,Z,j,et,q){Z.isScene!==!0&&(Z=Wt),R.resetTextureUnits();let C=Z.fog,Xt=et.isMeshStandardMaterial?Z.environment:null,Qt=B===null?M.outputColorSpace:B.isXRRenderTarget===!0?B.texture.colorSpace:Di,ie=(et.isMeshStandardMaterial?Y:b).get(et.envMap||Xt),me=et.vertexColors===!0&&!!j.attributes.color&&j.attributes.color.itemSize===4,ue=!!j.attributes.tangent&&(!!et.normalMap||et.anisotropy>0),ge=!!j.morphAttributes.position,yt=!!j.morphAttributes.normal,Ot=!!j.morphAttributes.color,zt=ji;et.toneMapped&&(B===null||B.isXRRenderTarget===!0)&&(zt=M.toneMapping);let en=j.morphAttributes.position||j.morphAttributes.normal||j.morphAttributes.color,ke=en!==void 0?en.length:0,ce=It.get(et),dn=_.state.lights;if(ut===!0&&(Nt===!0||P!==w)){let vn=P===w&&et.id===J;pe.setState(et,P,vn)}let Le=!1;et.version===ce.__version?(ce.needsLights&&ce.lightsStateVersion!==dn.state.version||ce.outputColorSpace!==Qt||q.isBatchedMesh&&ce.batching===!1||!q.isBatchedMesh&&ce.batching===!0||q.isInstancedMesh&&ce.instancing===!1||!q.isInstancedMesh&&ce.instancing===!0||q.isSkinnedMesh&&ce.skinning===!1||!q.isSkinnedMesh&&ce.skinning===!0||q.isInstancedMesh&&ce.instancingColor===!0&&q.instanceColor===null||q.isInstancedMesh&&ce.instancingColor===!1&&q.instanceColor!==null||ce.envMap!==ie||et.fog===!0&&ce.fog!==C||ce.numClippingPlanes!==void 0&&(ce.numClippingPlanes!==pe.numPlanes||ce.numIntersection!==pe.numIntersection)||ce.vertexAlphas!==me||ce.vertexTangents!==ue||ce.morphTargets!==ge||ce.morphNormals!==yt||ce.morphColors!==Ot||ce.toneMapping!==zt||bt.isWebGL2===!0&&ce.morphTargetsCount!==ke)&&(Le=!0):(Le=!0,ce.__version=et.version);let fi=ce.currentProgram;Le===!0&&(fi=Ds(et,Z,q));let ki=!1,bi=!1,Ns=!1,qe=fi.getUniforms(),ti=ce.uniforms;if(ht.useProgram(fi.program)&&(ki=!0,bi=!0,Ns=!0),et.id!==J&&(J=et.id,bi=!0),ki||w!==P){qe.setValue(z,"projectionMatrix",P.projectionMatrix),qe.setValue(z,"viewMatrix",P.matrixWorldInverse);let vn=qe.map.cameraPosition;vn!==void 0&&vn.setValue(z,Jt.setFromMatrixPosition(P.matrixWorld)),bt.logarithmicDepthBuffer&&qe.setValue(z,"logDepthBufFC",2/(Math.log(P.far+1)/Math.LN2)),(et.isMeshPhongMaterial||et.isMeshToonMaterial||et.isMeshLambertMaterial||et.isMeshBasicMaterial||et.isMeshStandardMaterial||et.isShaderMaterial)&&qe.setValue(z,"isOrthographic",P.isOrthographicCamera===!0),w!==P&&(w=P,bi=!0,Ns=!0)}if(q.isSkinnedMesh){qe.setOptional(z,q,"bindMatrix"),qe.setOptional(z,q,"bindMatrixInverse");let vn=q.skeleton;vn&&(bt.floatVertexTextures?(vn.boneTexture===null&&vn.computeBoneTexture(),qe.setValue(z,"boneTexture",vn.boneTexture,R)):console.warn("THREE.WebGLRenderer: SkinnedMesh can only be used with WebGL 2. With WebGL 1 OES_texture_float and vertex textures support is required."))}q.isBatchedMesh&&(qe.setOptional(z,q,"batchingTexture"),qe.setValue(z,"batchingTexture",q._matricesTexture,R));let Gi=j.morphAttributes;if((Gi.position!==void 0||Gi.normal!==void 0||Gi.color!==void 0&&bt.isWebGL2===!0)&&Se.update(q,j,fi),(bi||ce.receiveShadow!==q.receiveShadow)&&(ce.receiveShadow=q.receiveShadow,qe.setValue(z,"receiveShadow",q.receiveShadow)),et.isMeshGouraudMaterial&&et.envMap!==null&&(ti.envMap.value=ie,ti.flipEnvMap.value=ie.isCubeTexture&&ie.isRenderTargetTexture===!1?-1:1),bi&&(qe.setValue(z,"toneMappingExposure",M.toneMappingExposure),ce.needsLights&&Vn(ti,Ns),C&&et.fog===!0&&Lt.refreshFogUniforms(ti,C),Lt.refreshMaterialUniforms(ti,et,it,tt,Ft),lr.upload(z,Si(ce),ti,R)),et.isShaderMaterial&&et.uniformsNeedUpdate===!0&&(lr.upload(z,Si(ce),ti,R),et.uniformsNeedUpdate=!1),et.isSpriteMaterial&&qe.setValue(z,"center",q.center),qe.setValue(z,"modelViewMatrix",q.modelViewMatrix),qe.setValue(z,"normalMatrix",q.normalMatrix),qe.setValue(z,"modelMatrix",q.matrixWorld),et.isShaderMaterial||et.isRawShaderMaterial){let vn=et.uniformsGroups;for(let ze=0,ei=vn.length;ze<ei;ze++)if(bt.isWebGL2){let Vi=vn[ze];Ie.update(Vi,fi),Ie.bind(Vi,fi)}else console.warn("THREE.WebGLRenderer: Uniform Buffer Objects can only be used with WebGL 2.")}return fi}function Vn(P,Z){P.ambientLightColor.needsUpdate=Z,P.lightProbe.needsUpdate=Z,P.directionalLights.needsUpdate=Z,P.directionalLightShadows.needsUpdate=Z,P.pointLights.needsUpdate=Z,P.pointLightShadows.needsUpdate=Z,P.spotLights.needsUpdate=Z,P.spotLightShadows.needsUpdate=Z,P.rectAreaLights.needsUpdate=Z,P.hemisphereLights.needsUpdate=Z}function uo(P){return P.isMeshLambertMaterial||P.isMeshToonMaterial||P.isMeshPhongMaterial||P.isMeshStandardMaterial||P.isShadowMaterial||P.isShaderMaterial&&P.lights===!0}this.getActiveCubeFace=function(){return W},this.getActiveMipmapLevel=function(){return F},this.getRenderTarget=function(){return B},this.setRenderTargetTextures=function(P,Z,j){It.get(P.texture).__webglTexture=Z,It.get(P.depthTexture).__webglTexture=j;let et=It.get(P);et.__hasExternalTextures=!0,et.__hasExternalTextures&&(et.__autoAllocateDepthBuffer=j===void 0,et.__autoAllocateDepthBuffer||rt.has("WEBGL_multisampled_render_to_texture")===!0&&(console.warn("THREE.WebGLRenderer: Render-to-texture extension was disabled because an external texture was provided"),et.__useRenderToTexture=!1))},this.setRenderTargetFramebuffer=function(P,Z){let j=It.get(P);j.__webglFramebuffer=Z,j.__useDefaultFramebuffer=Z===void 0},this.setRenderTarget=function(P,Z=0,j=0){B=P,W=Z,F=j;let et=!0,q=null,C=!1,Xt=!1;if(P){let ie=It.get(P);ie.__useDefaultFramebuffer!==void 0?(ht.bindFramebuffer(z.FRAMEBUFFER,null),et=!1):ie.__webglFramebuffer===void 0?R.setupRenderTarget(P):ie.__hasExternalTextures&&R.rebindTextures(P,It.get(P.texture).__webglTexture,It.get(P.depthTexture).__webglTexture);let me=P.texture;(me.isData3DTexture||me.isDataArrayTexture||me.isCompressedArrayTexture)&&(Xt=!0);let ue=It.get(P).__webglFramebuffer;P.isWebGLCubeRenderTarget?(Array.isArray(ue[Z])?q=ue[Z][j]:q=ue[Z],C=!0):bt.isWebGL2&&P.samples>0&&R.useMultisampledRTT(P)===!1?q=It.get(P).__webglMultisampledFramebuffer:Array.isArray(ue)?q=ue[j]:q=ue,L.copy(P.viewport),$.copy(P.scissor),ot=P.scissorTest}else L.copy(ct).multiplyScalar(it).floor(),$.copy(lt).multiplyScalar(it).floor(),ot=Dt;if(ht.bindFramebuffer(z.FRAMEBUFFER,q)&&bt.drawBuffers&&et&&ht.drawBuffers(P,q),ht.viewport(L),ht.scissor($),ht.setScissorTest(ot),C){let ie=It.get(P.texture);z.framebufferTexture2D(z.FRAMEBUFFER,z.COLOR_ATTACHMENT0,z.TEXTURE_CUBE_MAP_POSITIVE_X+Z,ie.__webglTexture,j)}else if(Xt){let ie=It.get(P.texture),me=Z||0;z.framebufferTextureLayer(z.FRAMEBUFFER,z.COLOR_ATTACHMENT0,ie.__webglTexture,j||0,me)}J=-1},this.readRenderTargetPixels=function(P,Z,j,et,q,C,Xt){if(!(P&&P.isWebGLRenderTarget)){console.error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not THREE.WebGLRenderTarget.");return}let Qt=It.get(P).__webglFramebuffer;if(P.isWebGLCubeRenderTarget&&Xt!==void 0&&(Qt=Qt[Xt]),Qt){ht.bindFramebuffer(z.FRAMEBUFFER,Qt);try{let ie=P.texture,me=ie.format,ue=ie.type;if(me!==hi&&Ht.convert(me)!==z.getParameter(z.IMPLEMENTATION_COLOR_READ_FORMAT)){console.error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not in RGBA or implementation defined format.");return}let ge=ue===Gr&&(rt.has("EXT_color_buffer_half_float")||bt.isWebGL2&&rt.has("EXT_color_buffer_float"));if(ue!==Qi&&Ht.convert(ue)!==z.getParameter(z.IMPLEMENTATION_COLOR_READ_TYPE)&&!(ue===Ji&&(bt.isWebGL2||rt.has("OES_texture_float")||rt.has("WEBGL_color_buffer_float")))&&!ge){console.error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not in UnsignedByteType or implementation defined type.");return}Z>=0&&Z<=P.width-et&&j>=0&&j<=P.height-q&&z.readPixels(Z,j,et,q,Ht.convert(me),Ht.convert(ue),C)}finally{let ie=B!==null?It.get(B).__webglFramebuffer:null;ht.bindFramebuffer(z.FRAMEBUFFER,ie)}}},this.copyFramebufferToTexture=function(P,Z,j=0){let et=Math.pow(2,-j),q=Math.floor(Z.image.width*et),C=Math.floor(Z.image.height*et);R.setTexture2D(Z,0),z.copyTexSubImage2D(z.TEXTURE_2D,j,0,0,P.x,P.y,q,C),ht.unbindTexture()},this.copyTextureToTexture=function(P,Z,j,et=0){let q=Z.image.width,C=Z.image.height,Xt=Ht.convert(j.format),Qt=Ht.convert(j.type);R.setTexture2D(j,0),z.pixelStorei(z.UNPACK_FLIP_Y_WEBGL,j.flipY),z.pixelStorei(z.UNPACK_PREMULTIPLY_ALPHA_WEBGL,j.premultiplyAlpha),z.pixelStorei(z.UNPACK_ALIGNMENT,j.unpackAlignment),Z.isDataTexture?z.texSubImage2D(z.TEXTURE_2D,et,P.x,P.y,q,C,Xt,Qt,Z.image.data):Z.isCompressedTexture?z.compressedTexSubImage2D(z.TEXTURE_2D,et,P.x,P.y,Z.mipmaps[0].width,Z.mipmaps[0].height,Xt,Z.mipmaps[0].data):z.texSubImage2D(z.TEXTURE_2D,et,P.x,P.y,Xt,Qt,Z.image),et===0&&j.generateMipmaps&&z.generateMipmap(z.TEXTURE_2D),ht.unbindTexture()},this.copyTextureToTexture3D=function(P,Z,j,et,q=0){if(M.isWebGL1Renderer){console.warn("THREE.WebGLRenderer.copyTextureToTexture3D: can only be used with WebGL2.");return}let C=P.max.x-P.min.x+1,Xt=P.max.y-P.min.y+1,Qt=P.max.z-P.min.z+1,ie=Ht.convert(et.format),me=Ht.convert(et.type),ue;if(et.isData3DTexture)R.setTexture3D(et,0),ue=z.TEXTURE_3D;else if(et.isDataArrayTexture||et.isCompressedArrayTexture)R.setTexture2DArray(et,0),ue=z.TEXTURE_2D_ARRAY;else{console.warn("THREE.WebGLRenderer.copyTextureToTexture3D: only supports THREE.DataTexture3D and THREE.DataTexture2DArray.");return}z.pixelStorei(z.UNPACK_FLIP_Y_WEBGL,et.flipY),z.pixelStorei(z.UNPACK_PREMULTIPLY_ALPHA_WEBGL,et.premultiplyAlpha),z.pixelStorei(z.UNPACK_ALIGNMENT,et.unpackAlignment);let ge=z.getParameter(z.UNPACK_ROW_LENGTH),yt=z.getParameter(z.UNPACK_IMAGE_HEIGHT),Ot=z.getParameter(z.UNPACK_SKIP_PIXELS),zt=z.getParameter(z.UNPACK_SKIP_ROWS),en=z.getParameter(z.UNPACK_SKIP_IMAGES),ke=j.isCompressedTexture?j.mipmaps[q]:j.image;z.pixelStorei(z.UNPACK_ROW_LENGTH,ke.width),z.pixelStorei(z.UNPACK_IMAGE_HEIGHT,ke.height),z.pixelStorei(z.UNPACK_SKIP_PIXELS,P.min.x),z.pixelStorei(z.UNPACK_SKIP_ROWS,P.min.y),z.pixelStorei(z.UNPACK_SKIP_IMAGES,P.min.z),j.isDataTexture||j.isData3DTexture?z.texSubImage3D(ue,q,Z.x,Z.y,Z.z,C,Xt,Qt,ie,me,ke.data):j.isCompressedArrayTexture?(console.warn("THREE.WebGLRenderer.copyTextureToTexture3D: untested support for compressed srcTexture."),z.compressedTexSubImage3D(ue,q,Z.x,Z.y,Z.z,C,Xt,Qt,ie,ke.data)):z.texSubImage3D(ue,q,Z.x,Z.y,Z.z,C,Xt,Qt,ie,me,ke),z.pixelStorei(z.UNPACK_ROW_LENGTH,ge),z.pixelStorei(z.UNPACK_IMAGE_HEIGHT,yt),z.pixelStorei(z.UNPACK_SKIP_PIXELS,Ot),z.pixelStorei(z.UNPACK_SKIP_ROWS,zt),z.pixelStorei(z.UNPACK_SKIP_IMAGES,en),q===0&&et.generateMipmaps&&z.generateMipmap(ue),ht.unbindTexture()},this.initTexture=function(P){P.isCubeTexture?R.setTextureCube(P,0):P.isData3DTexture?R.setTexture3D(P,0):P.isDataArrayTexture||P.isCompressedArrayTexture?R.setTexture2DArray(P,0):R.setTexture2D(P,0),ht.unbindTexture()},this.resetState=function(){W=0,F=0,B=null,ht.reset(),ae.reset()},typeof __THREE_DEVTOOLS__!="undefined"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("observe",{detail:this}))}get coordinateSystem(){return Ui}get outputColorSpace(){return this._outputColorSpace}set outputColorSpace(t){this._outputColorSpace=t;let e=this.getContext();e.drawingBufferColorSpace=t===Dl?"display-p3":"srgb",e.unpackColorSpace=Be.workingColorSpace===Da?"display-p3":"srgb"}get outputEncoding(){return console.warn("THREE.WebGLRenderer: Property .outputEncoding has been removed. Use .outputColorSpace instead."),this.outputColorSpace===sn?Ss:yf}set outputEncoding(t){console.warn("THREE.WebGLRenderer: Property .outputEncoding has been removed. Use .outputColorSpace instead."),this.outputColorSpace=t===Ss?sn:Di}get useLegacyLights(){return console.warn("THREE.WebGLRenderer: The property .useLegacyLights has been deprecated. Migrate your lighting according to the following guide: https://discourse.threejs.org/t/updates-to-lighting-in-three-js-r155/53733."),this._useLegacyLights}set useLegacyLights(t){console.warn("THREE.WebGLRenderer: The property .useLegacyLights has been deprecated. Migrate your lighting according to the following guide: https://discourse.threejs.org/t/updates-to-lighting-in-three-js-r155/53733."),this._useLegacyLights=t}},ol=class extends Zr{};ol.prototype.isWebGL1Renderer=!0;var xa=class i{constructor(t,e=25e-5){this.isFogExp2=!0,this.name="",this.color=new fe(t),this.density=e}clone(){return new i(this.color,this.density)}toJSON(){return{type:"FogExp2",name:this.name,color:this.color.getHex(),density:this.density}}};var $r=class extends An{constructor(){super(),this.isScene=!0,this.type="Scene",this.background=null,this.environment=null,this.fog=null,this.backgroundBlurriness=0,this.backgroundIntensity=1,this.overrideMaterial=null,typeof __THREE_DEVTOOLS__!="undefined"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("observe",{detail:this}))}copy(t,e){return super.copy(t,e),t.background!==null&&(this.background=t.background.clone()),t.environment!==null&&(this.environment=t.environment.clone()),t.fog!==null&&(this.fog=t.fog.clone()),this.backgroundBlurriness=t.backgroundBlurriness,this.backgroundIntensity=t.backgroundIntensity,t.overrideMaterial!==null&&(this.overrideMaterial=t.overrideMaterial.clone()),this.matrixAutoUpdate=t.matrixAutoUpdate,this}toJSON(t){let e=super.toJSON(t);return this.fog!==null&&(e.object.fog=this.fog.toJSON()),this.backgroundBlurriness>0&&(e.object.backgroundBlurriness=this.backgroundBlurriness),this.backgroundIntensity!==1&&(e.object.backgroundIntensity=this.backgroundIntensity),e}};var Oi=class extends Mn{constructor(t,e,n,s=1){super(t,e,n),this.isInstancedBufferAttribute=!0,this.meshPerAttribute=s}copy(t){return super.copy(t),this.meshPerAttribute=t.meshPerAttribute,this}toJSON(){let t=super.toJSON();return t.meshPerAttribute=this.meshPerAttribute,t.isInstancedBufferAttribute=!0,t}},tr=new Ue,Ju=new Ue,Zo=[],Ku=new Fi,nx=new Ue,Lr=new Ne,Ur=new is,Jr=class extends Ne{constructor(t,e,n){super(t,e),this.isInstancedMesh=!0,this.instanceMatrix=new Oi(new Float32Array(n*16),16),this.instanceColor=null,this.count=n,this.boundingBox=null,this.boundingSphere=null;for(let s=0;s<n;s++)this.setMatrixAt(s,nx)}computeBoundingBox(){let t=this.geometry,e=this.count;this.boundingBox===null&&(this.boundingBox=new Fi),t.boundingBox===null&&t.computeBoundingBox(),this.boundingBox.makeEmpty();for(let n=0;n<e;n++)this.getMatrixAt(n,tr),Ku.copy(t.boundingBox).applyMatrix4(tr),this.boundingBox.union(Ku)}computeBoundingSphere(){let t=this.geometry,e=this.count;this.boundingSphere===null&&(this.boundingSphere=new is),t.boundingSphere===null&&t.computeBoundingSphere(),this.boundingSphere.makeEmpty();for(let n=0;n<e;n++)this.getMatrixAt(n,tr),Ur.copy(t.boundingSphere).applyMatrix4(tr),this.boundingSphere.union(Ur)}copy(t,e){return super.copy(t,e),this.instanceMatrix.copy(t.instanceMatrix),t.instanceColor!==null&&(this.instanceColor=t.instanceColor.clone()),this.count=t.count,t.boundingBox!==null&&(this.boundingBox=t.boundingBox.clone()),t.boundingSphere!==null&&(this.boundingSphere=t.boundingSphere.clone()),this}getColorAt(t,e){e.fromArray(this.instanceColor.array,t*3)}getMatrixAt(t,e){e.fromArray(this.instanceMatrix.array,t*16)}raycast(t,e){let n=this.matrixWorld,s=this.count;if(Lr.geometry=this.geometry,Lr.material=this.material,Lr.material!==void 0&&(this.boundingSphere===null&&this.computeBoundingSphere(),Ur.copy(this.boundingSphere),Ur.applyMatrix4(n),t.ray.intersectsSphere(Ur)!==!1))for(let r=0;r<s;r++){this.getMatrixAt(r,tr),Ju.multiplyMatrices(n,tr),Lr.matrixWorld=Ju,Lr.raycast(t,Zo);for(let a=0,o=Zo.length;a<o;a++){let c=Zo[a];c.instanceId=r,c.object=this,e.push(c)}Zo.length=0}}setColorAt(t,e){this.instanceColor===null&&(this.instanceColor=new Oi(new Float32Array(this.instanceMatrix.count*3),3)),e.toArray(this.instanceColor.array,t*3)}setMatrixAt(t,e){e.toArray(this.instanceMatrix.array,t*16)}updateMorphTargets(){}dispose(){this.dispatchEvent({type:"dispose"})}};var Kr=class extends yi{constructor(t){super(),this.isPointsMaterial=!0,this.type="PointsMaterial",this.color=new fe(16777215),this.map=null,this.alphaMap=null,this.size=1,this.sizeAttenuation=!0,this.fog=!0,this.setValues(t)}copy(t){return super.copy(t),this.color.copy(t.color),this.map=t.map,this.alphaMap=t.alphaMap,this.size=t.size,this.sizeAttenuation=t.sizeAttenuation,this.fog=t.fog,this}},ju=new Ue,al=new Xr,$o=new is,Jo=new O,va=class extends An{constructor(t=new Ke,e=new Kr){super(),this.isPoints=!0,this.type="Points",this.geometry=t,this.material=e,this.updateMorphTargets()}copy(t,e){return super.copy(t,e),this.material=Array.isArray(t.material)?t.material.slice():t.material,this.geometry=t.geometry,this}raycast(t,e){let n=this.geometry,s=this.matrixWorld,r=t.params.Points.threshold,a=n.drawRange;if(n.boundingSphere===null&&n.computeBoundingSphere(),$o.copy(n.boundingSphere),$o.applyMatrix4(s),$o.radius+=r,t.ray.intersectsSphere($o)===!1)return;ju.copy(s).invert(),al.copy(t.ray).applyMatrix4(ju);let o=r/((this.scale.x+this.scale.y+this.scale.z)/3),c=o*o,l=n.index,f=n.attributes.position;if(l!==null){let d=Math.max(0,a.start),p=Math.min(l.count,a.start+a.count);for(let x=d,S=p;x<S;x++){let _=l.getX(x);Jo.fromBufferAttribute(f,_),Qu(Jo,_,c,s,t,e,this)}}else{let d=Math.max(0,a.start),p=Math.min(f.count,a.start+a.count);for(let x=d,S=p;x<S;x++)Jo.fromBufferAttribute(f,x),Qu(Jo,x,c,s,t,e,this)}}updateMorphTargets(){let e=this.geometry.morphAttributes,n=Object.keys(e);if(n.length>0){let s=e[n[0]];if(s!==void 0){this.morphTargetInfluences=[],this.morphTargetDictionary={};for(let r=0,a=s.length;r<a;r++){let o=s[r].name||String(r);this.morphTargetInfluences.push(0),this.morphTargetDictionary[o]=r}}}}};function Qu(i,t,e,n,s,r,a){let o=al.distanceSqToPoint(i);if(o<e){let c=new O;al.closestPointToPoint(i,c),c.applyMatrix4(n);let l=s.ray.origin.distanceTo(c);if(l<s.near||l>s.far)return;r.push({distance:l,distanceToRay:Math.sqrt(o),point:c,index:t,face:null,object:a})}}var ya=class extends Hn{constructor(t,e,n,s,r,a,o,c,l){super(t,e,n,s,r,a,o,c,l),this.isCanvasTexture=!0,this.needsUpdate=!0}},Kn=class{constructor(){this.type="Curve",this.arcLengthDivisions=200}getPoint(){return console.warn("THREE.Curve: .getPoint() not implemented."),null}getPointAt(t,e){let n=this.getUtoTmapping(t);return this.getPoint(n,e)}getPoints(t=5){let e=[];for(let n=0;n<=t;n++)e.push(this.getPoint(n/t));return e}getSpacedPoints(t=5){let e=[];for(let n=0;n<=t;n++)e.push(this.getPointAt(n/t));return e}getLength(){let t=this.getLengths();return t[t.length-1]}getLengths(t=this.arcLengthDivisions){if(this.cacheArcLengths&&this.cacheArcLengths.length===t+1&&!this.needsUpdate)return this.cacheArcLengths;this.needsUpdate=!1;let e=[],n,s=this.getPoint(0),r=0;e.push(0);for(let a=1;a<=t;a++)n=this.getPoint(a/t),r+=n.distanceTo(s),e.push(r),s=n;return this.cacheArcLengths=e,e}updateArcLengths(){this.needsUpdate=!0,this.getLengths()}getUtoTmapping(t,e){let n=this.getLengths(),s=0,r=n.length,a;e?a=e:a=t*n[r-1];let o=0,c=r-1,l;for(;o<=c;)if(s=Math.floor(o+(c-o)/2),l=n[s]-a,l<0)o=s+1;else if(l>0)c=s-1;else{c=s;break}if(s=c,n[s]===a)return s/(r-1);let h=n[s],d=n[s+1]-h,p=(a-h)/d;return(s+p)/(r-1)}getTangent(t,e){let s=t-1e-4,r=t+1e-4;s<0&&(s=0),r>1&&(r=1);let a=this.getPoint(s),o=this.getPoint(r),c=e||(a.isVector2?new St:new O);return c.copy(o).sub(a).normalize(),c}getTangentAt(t,e){let n=this.getUtoTmapping(t);return this.getTangent(n,e)}computeFrenetFrames(t,e){let n=new O,s=[],r=[],a=[],o=new O,c=new Ue;for(let p=0;p<=t;p++){let x=p/t;s[p]=this.getTangentAt(x,new O)}r[0]=new O,a[0]=new O;let l=Number.MAX_VALUE,h=Math.abs(s[0].x),f=Math.abs(s[0].y),d=Math.abs(s[0].z);h<=l&&(l=h,n.set(1,0,0)),f<=l&&(l=f,n.set(0,1,0)),d<=l&&n.set(0,0,1),o.crossVectors(s[0],n).normalize(),r[0].crossVectors(s[0],o),a[0].crossVectors(s[0],r[0]);for(let p=1;p<=t;p++){if(r[p]=r[p-1].clone(),a[p]=a[p-1].clone(),o.crossVectors(s[p-1],s[p]),o.length()>Number.EPSILON){o.normalize();let x=Math.acos(gn(s[p-1].dot(s[p]),-1,1));r[p].applyMatrix4(c.makeRotationAxis(o,x))}a[p].crossVectors(s[p],r[p])}if(e===!0){let p=Math.acos(gn(r[0].dot(r[t]),-1,1));p/=t,s[0].dot(o.crossVectors(r[0],r[t]))>0&&(p=-p);for(let x=1;x<=t;x++)r[x].applyMatrix4(c.makeRotationAxis(s[x],p*x)),a[x].crossVectors(s[x],r[x])}return{tangents:s,normals:r,binormals:a}}clone(){return new this.constructor().copy(this)}copy(t){return this.arcLengthDivisions=t.arcLengthDivisions,this}toJSON(){let t={metadata:{version:4.6,type:"Curve",generator:"Curve.toJSON"}};return t.arcLengthDivisions=this.arcLengthDivisions,t.type=this.type,t}fromJSON(t){return this.arcLengthDivisions=t.arcLengthDivisions,this}},jr=class extends Kn{constructor(t=0,e=0,n=1,s=1,r=0,a=Math.PI*2,o=!1,c=0){super(),this.isEllipseCurve=!0,this.type="EllipseCurve",this.aX=t,this.aY=e,this.xRadius=n,this.yRadius=s,this.aStartAngle=r,this.aEndAngle=a,this.aClockwise=o,this.aRotation=c}getPoint(t,e){let n=e||new St,s=Math.PI*2,r=this.aEndAngle-this.aStartAngle,a=Math.abs(r)<Number.EPSILON;for(;r<0;)r+=s;for(;r>s;)r-=s;r<Number.EPSILON&&(a?r=0:r=s),this.aClockwise===!0&&!a&&(r===s?r=-s:r=r-s);let o=this.aStartAngle+t*r,c=this.aX+this.xRadius*Math.cos(o),l=this.aY+this.yRadius*Math.sin(o);if(this.aRotation!==0){let h=Math.cos(this.aRotation),f=Math.sin(this.aRotation),d=c-this.aX,p=l-this.aY;c=d*h-p*f+this.aX,l=d*f+p*h+this.aY}return n.set(c,l)}copy(t){return super.copy(t),this.aX=t.aX,this.aY=t.aY,this.xRadius=t.xRadius,this.yRadius=t.yRadius,this.aStartAngle=t.aStartAngle,this.aEndAngle=t.aEndAngle,this.aClockwise=t.aClockwise,this.aRotation=t.aRotation,this}toJSON(){let t=super.toJSON();return t.aX=this.aX,t.aY=this.aY,t.xRadius=this.xRadius,t.yRadius=this.yRadius,t.aStartAngle=this.aStartAngle,t.aEndAngle=this.aEndAngle,t.aClockwise=this.aClockwise,t.aRotation=this.aRotation,t}fromJSON(t){return super.fromJSON(t),this.aX=t.aX,this.aY=t.aY,this.xRadius=t.xRadius,this.yRadius=t.yRadius,this.aStartAngle=t.aStartAngle,this.aEndAngle=t.aEndAngle,this.aClockwise=t.aClockwise,this.aRotation=t.aRotation,this}},cl=class extends jr{constructor(t,e,n,s,r,a){super(t,e,n,n,s,r,a),this.isArcCurve=!0,this.type="ArcCurve"}};function Bl(){let i=0,t=0,e=0,n=0;function s(r,a,o,c){i=r,t=o,e=-3*r+3*a-2*o-c,n=2*r-2*a+o+c}return{initCatmullRom:function(r,a,o,c,l){s(a,o,l*(o-r),l*(c-a))},initNonuniformCatmullRom:function(r,a,o,c,l,h,f){let d=(a-r)/l-(o-r)/(l+h)+(o-a)/h,p=(o-a)/h-(c-a)/(h+f)+(c-o)/f;d*=h,p*=h,s(a,o,d,p)},calc:function(r){let a=r*r,o=a*r;return i+t*r+e*a+n*o}}}var Ko=new O,Dc=new Bl,Nc=new Bl,Fc=new Bl,ll=class extends Kn{constructor(t=[],e=!1,n="centripetal",s=.5){super(),this.isCatmullRomCurve3=!0,this.type="CatmullRomCurve3",this.points=t,this.closed=e,this.curveType=n,this.tension=s}getPoint(t,e=new O){let n=e,s=this.points,r=s.length,a=(r-(this.closed?0:1))*t,o=Math.floor(a),c=a-o;this.closed?o+=o>0?0:(Math.floor(Math.abs(o)/r)+1)*r:c===0&&o===r-1&&(o=r-2,c=1);let l,h;this.closed||o>0?l=s[(o-1)%r]:(Ko.subVectors(s[0],s[1]).add(s[0]),l=Ko);let f=s[o%r],d=s[(o+1)%r];if(this.closed||o+2<r?h=s[(o+2)%r]:(Ko.subVectors(s[r-1],s[r-2]).add(s[r-1]),h=Ko),this.curveType==="centripetal"||this.curveType==="chordal"){let p=this.curveType==="chordal"?.5:.25,x=Math.pow(l.distanceToSquared(f),p),S=Math.pow(f.distanceToSquared(d),p),_=Math.pow(d.distanceToSquared(h),p);S<1e-4&&(S=1),x<1e-4&&(x=S),_<1e-4&&(_=S),Dc.initNonuniformCatmullRom(l.x,f.x,d.x,h.x,x,S,_),Nc.initNonuniformCatmullRom(l.y,f.y,d.y,h.y,x,S,_),Fc.initNonuniformCatmullRom(l.z,f.z,d.z,h.z,x,S,_)}else this.curveType==="catmullrom"&&(Dc.initCatmullRom(l.x,f.x,d.x,h.x,this.tension),Nc.initCatmullRom(l.y,f.y,d.y,h.y,this.tension),Fc.initCatmullRom(l.z,f.z,d.z,h.z,this.tension));return n.set(Dc.calc(c),Nc.calc(c),Fc.calc(c)),n}copy(t){super.copy(t),this.points=[];for(let e=0,n=t.points.length;e<n;e++){let s=t.points[e];this.points.push(s.clone())}return this.closed=t.closed,this.curveType=t.curveType,this.tension=t.tension,this}toJSON(){let t=super.toJSON();t.points=[];for(let e=0,n=this.points.length;e<n;e++){let s=this.points[e];t.points.push(s.toArray())}return t.closed=this.closed,t.curveType=this.curveType,t.tension=this.tension,t}fromJSON(t){super.fromJSON(t),this.points=[];for(let e=0,n=t.points.length;e<n;e++){let s=t.points[e];this.points.push(new O().fromArray(s))}return this.closed=t.closed,this.curveType=t.curveType,this.tension=t.tension,this}};function tf(i,t,e,n,s){let r=(n-t)*.5,a=(s-e)*.5,o=i*i,c=i*o;return(2*e-2*n+r+a)*c+(-3*e+3*n-2*r-a)*o+r*i+e}function ix(i,t){let e=1-i;return e*e*t}function sx(i,t){return 2*(1-i)*i*t}function rx(i,t){return i*i*t}function zr(i,t,e,n){return ix(i,t)+sx(i,e)+rx(i,n)}function ox(i,t){let e=1-i;return e*e*e*t}function ax(i,t){let e=1-i;return 3*e*e*i*t}function cx(i,t){return 3*(1-i)*i*i*t}function lx(i,t){return i*i*i*t}function Hr(i,t,e,n,s){return ox(i,t)+ax(i,e)+cx(i,n)+lx(i,s)}var Ma=class extends Kn{constructor(t=new St,e=new St,n=new St,s=new St){super(),this.isCubicBezierCurve=!0,this.type="CubicBezierCurve",this.v0=t,this.v1=e,this.v2=n,this.v3=s}getPoint(t,e=new St){let n=e,s=this.v0,r=this.v1,a=this.v2,o=this.v3;return n.set(Hr(t,s.x,r.x,a.x,o.x),Hr(t,s.y,r.y,a.y,o.y)),n}copy(t){return super.copy(t),this.v0.copy(t.v0),this.v1.copy(t.v1),this.v2.copy(t.v2),this.v3.copy(t.v3),this}toJSON(){let t=super.toJSON();return t.v0=this.v0.toArray(),t.v1=this.v1.toArray(),t.v2=this.v2.toArray(),t.v3=this.v3.toArray(),t}fromJSON(t){return super.fromJSON(t),this.v0.fromArray(t.v0),this.v1.fromArray(t.v1),this.v2.fromArray(t.v2),this.v3.fromArray(t.v3),this}},hl=class extends Kn{constructor(t=new O,e=new O,n=new O,s=new O){super(),this.isCubicBezierCurve3=!0,this.type="CubicBezierCurve3",this.v0=t,this.v1=e,this.v2=n,this.v3=s}getPoint(t,e=new O){let n=e,s=this.v0,r=this.v1,a=this.v2,o=this.v3;return n.set(Hr(t,s.x,r.x,a.x,o.x),Hr(t,s.y,r.y,a.y,o.y),Hr(t,s.z,r.z,a.z,o.z)),n}copy(t){return super.copy(t),this.v0.copy(t.v0),this.v1.copy(t.v1),this.v2.copy(t.v2),this.v3.copy(t.v3),this}toJSON(){let t=super.toJSON();return t.v0=this.v0.toArray(),t.v1=this.v1.toArray(),t.v2=this.v2.toArray(),t.v3=this.v3.toArray(),t}fromJSON(t){return super.fromJSON(t),this.v0.fromArray(t.v0),this.v1.fromArray(t.v1),this.v2.fromArray(t.v2),this.v3.fromArray(t.v3),this}},Sa=class extends Kn{constructor(t=new St,e=new St){super(),this.isLineCurve=!0,this.type="LineCurve",this.v1=t,this.v2=e}getPoint(t,e=new St){let n=e;return t===1?n.copy(this.v2):(n.copy(this.v2).sub(this.v1),n.multiplyScalar(t).add(this.v1)),n}getPointAt(t,e){return this.getPoint(t,e)}getTangent(t,e=new St){return e.subVectors(this.v2,this.v1).normalize()}getTangentAt(t,e){return this.getTangent(t,e)}copy(t){return super.copy(t),this.v1.copy(t.v1),this.v2.copy(t.v2),this}toJSON(){let t=super.toJSON();return t.v1=this.v1.toArray(),t.v2=this.v2.toArray(),t}fromJSON(t){return super.fromJSON(t),this.v1.fromArray(t.v1),this.v2.fromArray(t.v2),this}},ul=class extends Kn{constructor(t=new O,e=new O){super(),this.isLineCurve3=!0,this.type="LineCurve3",this.v1=t,this.v2=e}getPoint(t,e=new O){let n=e;return t===1?n.copy(this.v2):(n.copy(this.v2).sub(this.v1),n.multiplyScalar(t).add(this.v1)),n}getPointAt(t,e){return this.getPoint(t,e)}getTangent(t,e=new O){return e.subVectors(this.v2,this.v1).normalize()}getTangentAt(t,e){return this.getTangent(t,e)}copy(t){return super.copy(t),this.v1.copy(t.v1),this.v2.copy(t.v2),this}toJSON(){let t=super.toJSON();return t.v1=this.v1.toArray(),t.v2=this.v2.toArray(),t}fromJSON(t){return super.fromJSON(t),this.v1.fromArray(t.v1),this.v2.fromArray(t.v2),this}},ba=class extends Kn{constructor(t=new St,e=new St,n=new St){super(),this.isQuadraticBezierCurve=!0,this.type="QuadraticBezierCurve",this.v0=t,this.v1=e,this.v2=n}getPoint(t,e=new St){let n=e,s=this.v0,r=this.v1,a=this.v2;return n.set(zr(t,s.x,r.x,a.x),zr(t,s.y,r.y,a.y)),n}copy(t){return super.copy(t),this.v0.copy(t.v0),this.v1.copy(t.v1),this.v2.copy(t.v2),this}toJSON(){let t=super.toJSON();return t.v0=this.v0.toArray(),t.v1=this.v1.toArray(),t.v2=this.v2.toArray(),t}fromJSON(t){return super.fromJSON(t),this.v0.fromArray(t.v0),this.v1.fromArray(t.v1),this.v2.fromArray(t.v2),this}},fl=class extends Kn{constructor(t=new O,e=new O,n=new O){super(),this.isQuadraticBezierCurve3=!0,this.type="QuadraticBezierCurve3",this.v0=t,this.v1=e,this.v2=n}getPoint(t,e=new O){let n=e,s=this.v0,r=this.v1,a=this.v2;return n.set(zr(t,s.x,r.x,a.x),zr(t,s.y,r.y,a.y),zr(t,s.z,r.z,a.z)),n}copy(t){return super.copy(t),this.v0.copy(t.v0),this.v1.copy(t.v1),this.v2.copy(t.v2),this}toJSON(){let t=super.toJSON();return t.v0=this.v0.toArray(),t.v1=this.v1.toArray(),t.v2=this.v2.toArray(),t}fromJSON(t){return super.fromJSON(t),this.v0.fromArray(t.v0),this.v1.fromArray(t.v1),this.v2.fromArray(t.v2),this}},Ea=class extends Kn{constructor(t=[]){super(),this.isSplineCurve=!0,this.type="SplineCurve",this.points=t}getPoint(t,e=new St){let n=e,s=this.points,r=(s.length-1)*t,a=Math.floor(r),o=r-a,c=s[a===0?a:a-1],l=s[a],h=s[a>s.length-2?s.length-1:a+1],f=s[a>s.length-3?s.length-1:a+2];return n.set(tf(o,c.x,l.x,h.x,f.x),tf(o,c.y,l.y,h.y,f.y)),n}copy(t){super.copy(t),this.points=[];for(let e=0,n=t.points.length;e<n;e++){let s=t.points[e];this.points.push(s.clone())}return this}toJSON(){let t=super.toJSON();t.points=[];for(let e=0,n=this.points.length;e<n;e++){let s=this.points[e];t.points.push(s.toArray())}return t}fromJSON(t){super.fromJSON(t),this.points=[];for(let e=0,n=t.points.length;e<n;e++){let s=t.points[e];this.points.push(new St().fromArray(s))}return this}},dl=Object.freeze({__proto__:null,ArcCurve:cl,CatmullRomCurve3:ll,CubicBezierCurve:Ma,CubicBezierCurve3:hl,EllipseCurve:jr,LineCurve:Sa,LineCurve3:ul,QuadraticBezierCurve:ba,QuadraticBezierCurve3:fl,SplineCurve:Ea}),pl=class extends Kn{constructor(){super(),this.type="CurvePath",this.curves=[],this.autoClose=!1}add(t){this.curves.push(t)}closePath(){let t=this.curves[0].getPoint(0),e=this.curves[this.curves.length-1].getPoint(1);if(!t.equals(e)){let n=t.isVector2===!0?"LineCurve":"LineCurve3";this.curves.push(new dl[n](e,t))}return this}getPoint(t,e){let n=t*this.getLength(),s=this.getCurveLengths(),r=0;for(;r<s.length;){if(s[r]>=n){let a=s[r]-n,o=this.curves[r],c=o.getLength(),l=c===0?0:1-a/c;return o.getPointAt(l,e)}r++}return null}getLength(){let t=this.getCurveLengths();return t[t.length-1]}updateArcLengths(){this.needsUpdate=!0,this.cacheLengths=null,this.getCurveLengths()}getCurveLengths(){if(this.cacheLengths&&this.cacheLengths.length===this.curves.length)return this.cacheLengths;let t=[],e=0;for(let n=0,s=this.curves.length;n<s;n++)e+=this.curves[n].getLength(),t.push(e);return this.cacheLengths=t,t}getSpacedPoints(t=40){let e=[];for(let n=0;n<=t;n++)e.push(this.getPoint(n/t));return this.autoClose&&e.push(e[0]),e}getPoints(t=12){let e=[],n;for(let s=0,r=this.curves;s<r.length;s++){let a=r[s],o=a.isEllipseCurve?t*2:a.isLineCurve||a.isLineCurve3?1:a.isSplineCurve?t*a.points.length:t,c=a.getPoints(o);for(let l=0;l<c.length;l++){let h=c[l];n&&n.equals(h)||(e.push(h),n=h)}}return this.autoClose&&e.length>1&&!e[e.length-1].equals(e[0])&&e.push(e[0]),e}copy(t){super.copy(t),this.curves=[];for(let e=0,n=t.curves.length;e<n;e++){let s=t.curves[e];this.curves.push(s.clone())}return this.autoClose=t.autoClose,this}toJSON(){let t=super.toJSON();t.autoClose=this.autoClose,t.curves=[];for(let e=0,n=this.curves.length;e<n;e++){let s=this.curves[e];t.curves.push(s.toJSON())}return t}fromJSON(t){super.fromJSON(t),this.autoClose=t.autoClose,this.curves=[];for(let e=0,n=t.curves.length;e<n;e++){let s=t.curves[e];this.curves.push(new dl[s.type]().fromJSON(s))}return this}},ws=class extends pl{constructor(t){super(),this.type="Path",this.currentPoint=new St,t&&this.setFromPoints(t)}setFromPoints(t){this.moveTo(t[0].x,t[0].y);for(let e=1,n=t.length;e<n;e++)this.lineTo(t[e].x,t[e].y);return this}moveTo(t,e){return this.currentPoint.set(t,e),this}lineTo(t,e){let n=new Sa(this.currentPoint.clone(),new St(t,e));return this.curves.push(n),this.currentPoint.set(t,e),this}quadraticCurveTo(t,e,n,s){let r=new ba(this.currentPoint.clone(),new St(t,e),new St(n,s));return this.curves.push(r),this.currentPoint.set(n,s),this}bezierCurveTo(t,e,n,s,r,a){let o=new Ma(this.currentPoint.clone(),new St(t,e),new St(n,s),new St(r,a));return this.curves.push(o),this.currentPoint.set(r,a),this}splineThru(t){let e=[this.currentPoint.clone()].concat(t),n=new Ea(e);return this.curves.push(n),this.currentPoint.copy(t[t.length-1]),this}arc(t,e,n,s,r,a){let o=this.currentPoint.x,c=this.currentPoint.y;return this.absarc(t+o,e+c,n,s,r,a),this}absarc(t,e,n,s,r,a){return this.absellipse(t,e,n,n,s,r,a),this}ellipse(t,e,n,s,r,a,o,c){let l=this.currentPoint.x,h=this.currentPoint.y;return this.absellipse(t+l,e+h,n,s,r,a,o,c),this}absellipse(t,e,n,s,r,a,o,c){let l=new jr(t,e,n,s,r,a,o,c);if(this.curves.length>0){let f=l.getPoint(0);f.equals(this.currentPoint)||this.lineTo(f.x,f.y)}this.curves.push(l);let h=l.getPoint(1);return this.currentPoint.copy(h),this}copy(t){return super.copy(t),this.currentPoint.copy(t.currentPoint),this}toJSON(){let t=super.toJSON();return t.currentPoint=this.currentPoint.toArray(),t}fromJSON(t){return super.fromJSON(t),this.currentPoint.fromArray(t.currentPoint),this}},Ts=class i extends Ke{constructor(t=[new St(0,-.5),new St(.5,0),new St(0,.5)],e=12,n=0,s=Math.PI*2){super(),this.type="LatheGeometry",this.parameters={points:t,segments:e,phiStart:n,phiLength:s},e=Math.floor(e),s=gn(s,0,Math.PI*2);let r=[],a=[],o=[],c=[],l=[],h=1/e,f=new O,d=new St,p=new O,x=new O,S=new O,_=0,m=0;for(let T=0;T<=t.length-1;T++)switch(T){case 0:_=t[T+1].x-t[T].x,m=t[T+1].y-t[T].y,p.x=m*1,p.y=-_,p.z=m*0,S.copy(p),p.normalize(),c.push(p.x,p.y,p.z);break;case t.length-1:c.push(S.x,S.y,S.z);break;default:_=t[T+1].x-t[T].x,m=t[T+1].y-t[T].y,p.x=m*1,p.y=-_,p.z=m*0,x.copy(p),p.x+=S.x,p.y+=S.y,p.z+=S.z,p.normalize(),c.push(p.x,p.y,p.z),S.copy(x)}for(let T=0;T<=e;T++){let M=n+T*h*s,U=Math.sin(M),W=Math.cos(M);for(let F=0;F<=t.length-1;F++){f.x=t[F].x*U,f.y=t[F].y,f.z=t[F].x*W,a.push(f.x,f.y,f.z),d.x=T/e,d.y=F/(t.length-1),o.push(d.x,d.y);let B=c[3*F+0]*U,J=c[3*F+1],w=c[3*F+0]*W;l.push(B,J,w)}}for(let T=0;T<e;T++)for(let M=0;M<t.length-1;M++){let U=M+T*t.length,W=U,F=U+t.length,B=U+t.length+1,J=U+1;r.push(W,F,J),r.push(B,J,F)}this.setIndex(r),this.setAttribute("position",new de(a,3)),this.setAttribute("uv",new de(o,2)),this.setAttribute("normal",new de(l,3))}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.points,t.segments,t.phiStart,t.phiLength)}},As=class i extends Ts{constructor(t=1,e=1,n=4,s=8){let r=new ws;r.absarc(0,-e/2,t,Math.PI*1.5,0),r.absarc(0,e/2,t,0,Math.PI*.5),super(r.getPoints(n),s),this.type="CapsuleGeometry",this.parameters={radius:t,length:e,capSegments:n,radialSegments:s}}static fromJSON(t){return new i(t.radius,t.length,t.capSegments,t.radialSegments)}},gr=class i extends Ke{constructor(t=1,e=32,n=0,s=Math.PI*2){super(),this.type="CircleGeometry",this.parameters={radius:t,segments:e,thetaStart:n,thetaLength:s},e=Math.max(3,e);let r=[],a=[],o=[],c=[],l=new O,h=new St;a.push(0,0,0),o.push(0,0,1),c.push(.5,.5);for(let f=0,d=3;f<=e;f++,d+=3){let p=n+f/e*s;l.x=t*Math.cos(p),l.y=t*Math.sin(p),a.push(l.x,l.y,l.z),o.push(0,0,1),h.x=(a[d]/t+1)/2,h.y=(a[d+1]/t+1)/2,c.push(h.x,h.y)}for(let f=1;f<=e;f++)r.push(f,f+1,0);this.setIndex(r),this.setAttribute("position",new de(a,3)),this.setAttribute("normal",new de(o,3)),this.setAttribute("uv",new de(c,2))}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.radius,t.segments,t.thetaStart,t.thetaLength)}},tn=class i extends Ke{constructor(t=1,e=1,n=1,s=32,r=1,a=!1,o=0,c=Math.PI*2){super(),this.type="CylinderGeometry",this.parameters={radiusTop:t,radiusBottom:e,height:n,radialSegments:s,heightSegments:r,openEnded:a,thetaStart:o,thetaLength:c};let l=this;s=Math.floor(s),r=Math.floor(r);let h=[],f=[],d=[],p=[],x=0,S=[],_=n/2,m=0;T(),a===!1&&(t>0&&M(!0),e>0&&M(!1)),this.setIndex(h),this.setAttribute("position",new de(f,3)),this.setAttribute("normal",new de(d,3)),this.setAttribute("uv",new de(p,2));function T(){let U=new O,W=new O,F=0,B=(e-t)/n;for(let J=0;J<=r;J++){let w=[],L=J/r,$=L*(e-t)+t;for(let ot=0;ot<=s;ot++){let Mt=ot/s,X=Mt*c+o,K=Math.sin(X),tt=Math.cos(X);W.x=$*K,W.y=-L*n+_,W.z=$*tt,f.push(W.x,W.y,W.z),U.set(K,B,tt).normalize(),d.push(U.x,U.y,U.z),p.push(Mt,1-L),w.push(x++)}S.push(w)}for(let J=0;J<s;J++)for(let w=0;w<r;w++){let L=S[w][J],$=S[w+1][J],ot=S[w+1][J+1],Mt=S[w][J+1];h.push(L,$,Mt),h.push($,ot,Mt),F+=6}l.addGroup(m,F,0),m+=F}function M(U){let W=x,F=new St,B=new O,J=0,w=U===!0?t:e,L=U===!0?1:-1;for(let ot=1;ot<=s;ot++)f.push(0,_*L,0),d.push(0,L,0),p.push(.5,.5),x++;let $=x;for(let ot=0;ot<=s;ot++){let X=ot/s*c+o,K=Math.cos(X),tt=Math.sin(X);B.x=w*tt,B.y=_*L,B.z=w*K,f.push(B.x,B.y,B.z),d.push(0,L,0),F.x=K*.5+.5,F.y=tt*.5*L+.5,p.push(F.x,F.y),x++}for(let ot=0;ot<s;ot++){let Mt=W+ot,X=$+ot;U===!0?h.push(X,X+1,Mt):h.push(X+1,X,Mt),J+=3}l.addGroup(m,J,U===!0?1:2),m+=J}}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.radiusTop,t.radiusBottom,t.height,t.radialSegments,t.heightSegments,t.openEnded,t.thetaStart,t.thetaLength)}},Qr=class i extends tn{constructor(t=1,e=1,n=32,s=1,r=!1,a=0,o=Math.PI*2){super(0,t,e,n,s,r,a,o),this.type="ConeGeometry",this.parameters={radius:t,height:e,radialSegments:n,heightSegments:s,openEnded:r,thetaStart:a,thetaLength:o}}static fromJSON(t){return new i(t.radius,t.height,t.radialSegments,t.heightSegments,t.openEnded,t.thetaStart,t.thetaLength)}},to=class i extends Ke{constructor(t=[],e=[],n=1,s=0){super(),this.type="PolyhedronGeometry",this.parameters={vertices:t,indices:e,radius:n,detail:s};let r=[],a=[];o(s),l(n),h(),this.setAttribute("position",new de(r,3)),this.setAttribute("normal",new de(r.slice(),3)),this.setAttribute("uv",new de(a,2)),s===0?this.computeVertexNormals():this.normalizeNormals();function o(T){let M=new O,U=new O,W=new O;for(let F=0;F<e.length;F+=3)p(e[F+0],M),p(e[F+1],U),p(e[F+2],W),c(M,U,W,T)}function c(T,M,U,W){let F=W+1,B=[];for(let J=0;J<=F;J++){B[J]=[];let w=T.clone().lerp(U,J/F),L=M.clone().lerp(U,J/F),$=F-J;for(let ot=0;ot<=$;ot++)ot===0&&J===F?B[J][ot]=w:B[J][ot]=w.clone().lerp(L,ot/$)}for(let J=0;J<F;J++)for(let w=0;w<2*(F-J)-1;w++){let L=Math.floor(w/2);w%2===0?(d(B[J][L+1]),d(B[J+1][L]),d(B[J][L])):(d(B[J][L+1]),d(B[J+1][L+1]),d(B[J+1][L]))}}function l(T){let M=new O;for(let U=0;U<r.length;U+=3)M.x=r[U+0],M.y=r[U+1],M.z=r[U+2],M.normalize().multiplyScalar(T),r[U+0]=M.x,r[U+1]=M.y,r[U+2]=M.z}function h(){let T=new O;for(let M=0;M<r.length;M+=3){T.x=r[M+0],T.y=r[M+1],T.z=r[M+2];let U=_(T)/2/Math.PI+.5,W=m(T)/Math.PI+.5;a.push(U,1-W)}x(),f()}function f(){for(let T=0;T<a.length;T+=6){let M=a[T+0],U=a[T+2],W=a[T+4],F=Math.max(M,U,W),B=Math.min(M,U,W);F>.9&&B<.1&&(M<.2&&(a[T+0]+=1),U<.2&&(a[T+2]+=1),W<.2&&(a[T+4]+=1))}}function d(T){r.push(T.x,T.y,T.z)}function p(T,M){let U=T*3;M.x=t[U+0],M.y=t[U+1],M.z=t[U+2]}function x(){let T=new O,M=new O,U=new O,W=new O,F=new St,B=new St,J=new St;for(let w=0,L=0;w<r.length;w+=9,L+=6){T.set(r[w+0],r[w+1],r[w+2]),M.set(r[w+3],r[w+4],r[w+5]),U.set(r[w+6],r[w+7],r[w+8]),F.set(a[L+0],a[L+1]),B.set(a[L+2],a[L+3]),J.set(a[L+4],a[L+5]),W.copy(T).add(M).add(U).divideScalar(3);let $=_(W);S(F,L+0,T,$),S(B,L+2,M,$),S(J,L+4,U,$)}}function S(T,M,U,W){W<0&&T.x===1&&(a[M]=T.x-1),U.x===0&&U.z===0&&(a[M]=W/2/Math.PI+.5)}function _(T){return Math.atan2(T.z,-T.x)}function m(T){return Math.atan2(-T.y,Math.sqrt(T.x*T.x+T.z*T.z))}}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.vertices,t.indices,t.radius,t.details)}},eo=class i extends to{constructor(t=1,e=0){let n=(1+Math.sqrt(5))/2,s=1/n,r=[-1,-1,-1,-1,-1,1,-1,1,-1,-1,1,1,1,-1,-1,1,-1,1,1,1,-1,1,1,1,0,-s,-n,0,-s,n,0,s,-n,0,s,n,-s,-n,0,-s,n,0,s,-n,0,s,n,0,-n,0,-s,n,0,-s,-n,0,s,n,0,s],a=[3,11,7,3,7,15,3,15,13,7,19,17,7,17,6,7,6,15,17,4,8,17,8,10,17,10,6,8,0,16,8,16,2,8,2,10,0,12,1,0,1,18,0,18,16,6,10,2,6,2,13,6,13,15,2,16,18,2,18,3,2,3,13,18,1,9,18,9,11,18,11,3,4,14,12,4,12,0,4,0,8,11,9,5,11,5,19,11,19,7,19,5,14,19,14,4,19,4,17,1,12,14,1,14,5,1,5,9];super(r,a,t,e),this.type="DodecahedronGeometry",this.parameters={radius:t,detail:e}}static fromJSON(t){return new i(t.radius,t.detail)}};var jn=class extends ws{constructor(t){super(t),this.uuid=Is(),this.type="Shape",this.holes=[]}getPointsHoles(t){let e=[];for(let n=0,s=this.holes.length;n<s;n++)e[n]=this.holes[n].getPoints(t);return e}extractPoints(t){return{shape:this.getPoints(t),holes:this.getPointsHoles(t)}}copy(t){super.copy(t),this.holes=[];for(let e=0,n=t.holes.length;e<n;e++){let s=t.holes[e];this.holes.push(s.clone())}return this}toJSON(){let t=super.toJSON();t.uuid=this.uuid,t.holes=[];for(let e=0,n=this.holes.length;e<n;e++){let s=this.holes[e];t.holes.push(s.toJSON())}return t}fromJSON(t){super.fromJSON(t),this.uuid=t.uuid,this.holes=[];for(let e=0,n=t.holes.length;e<n;e++){let s=t.holes[e];this.holes.push(new ws().fromJSON(s))}return this}},hx={triangulate:function(i,t,e=2){let n=t&&t.length,s=n?t[0]*e:i.length,r=Lf(i,0,s,e,!0),a=[];if(!r||r.next===r.prev)return a;let o,c,l,h,f,d,p;if(n&&(r=mx(i,t,r,e)),i.length>80*e){o=l=i[0],c=h=i[1];for(let x=e;x<s;x+=e)f=i[x],d=i[x+1],f<o&&(o=f),d<c&&(c=d),f>l&&(l=f),d>h&&(h=d);p=Math.max(l-o,h-c),p=p!==0?32767/p:0}return no(r,a,e,o,c,p,0),a}};function Lf(i,t,e,n,s){let r,a;if(s===Tx(i,t,e,n)>0)for(r=t;r<e;r+=n)a=ef(r,i[r],i[r+1],a);else for(r=e-n;r>=t;r-=n)a=ef(r,i[r],i[r+1],a);return a&&Fa(a,a.next)&&(so(a),a=a.next),a}function Rs(i,t){if(!i)return i;t||(t=i);let e=i,n;do if(n=!1,!e.steiner&&(Fa(e,e.next)||Qe(e.prev,e,e.next)===0)){if(so(e),e=t=e.prev,e===e.next)break;n=!0}else e=e.next;while(n||e!==t);return t}function no(i,t,e,n,s,r,a){if(!i)return;!a&&r&&yx(i,n,s,r);let o=i,c,l;for(;i.prev!==i.next;){if(c=i.prev,l=i.next,r?fx(i,n,s,r):ux(i)){t.push(c.i/e|0),t.push(i.i/e|0),t.push(l.i/e|0),so(i),i=l.next,o=l.next;continue}if(i=l,i===o){a?a===1?(i=dx(Rs(i),t,e),no(i,t,e,n,s,r,2)):a===2&&px(i,t,e,n,s,r):no(Rs(i),t,e,n,s,r,1);break}}}function ux(i){let t=i.prev,e=i,n=i.next;if(Qe(t,e,n)>=0)return!1;let s=t.x,r=e.x,a=n.x,o=t.y,c=e.y,l=n.y,h=s<r?s<a?s:a:r<a?r:a,f=o<c?o<l?o:l:c<l?c:l,d=s>r?s>a?s:a:r>a?r:a,p=o>c?o>l?o:l:c>l?c:l,x=n.next;for(;x!==t;){if(x.x>=h&&x.x<=d&&x.y>=f&&x.y<=p&&or(s,o,r,c,a,l,x.x,x.y)&&Qe(x.prev,x,x.next)>=0)return!1;x=x.next}return!0}function fx(i,t,e,n){let s=i.prev,r=i,a=i.next;if(Qe(s,r,a)>=0)return!1;let o=s.x,c=r.x,l=a.x,h=s.y,f=r.y,d=a.y,p=o<c?o<l?o:l:c<l?c:l,x=h<f?h<d?h:d:f<d?f:d,S=o>c?o>l?o:l:c>l?c:l,_=h>f?h>d?h:d:f>d?f:d,m=ml(p,x,t,e,n),T=ml(S,_,t,e,n),M=i.prevZ,U=i.nextZ;for(;M&&M.z>=m&&U&&U.z<=T;){if(M.x>=p&&M.x<=S&&M.y>=x&&M.y<=_&&M!==s&&M!==a&&or(o,h,c,f,l,d,M.x,M.y)&&Qe(M.prev,M,M.next)>=0||(M=M.prevZ,U.x>=p&&U.x<=S&&U.y>=x&&U.y<=_&&U!==s&&U!==a&&or(o,h,c,f,l,d,U.x,U.y)&&Qe(U.prev,U,U.next)>=0))return!1;U=U.nextZ}for(;M&&M.z>=m;){if(M.x>=p&&M.x<=S&&M.y>=x&&M.y<=_&&M!==s&&M!==a&&or(o,h,c,f,l,d,M.x,M.y)&&Qe(M.prev,M,M.next)>=0)return!1;M=M.prevZ}for(;U&&U.z<=T;){if(U.x>=p&&U.x<=S&&U.y>=x&&U.y<=_&&U!==s&&U!==a&&or(o,h,c,f,l,d,U.x,U.y)&&Qe(U.prev,U,U.next)>=0)return!1;U=U.nextZ}return!0}function dx(i,t,e){let n=i;do{let s=n.prev,r=n.next.next;!Fa(s,r)&&Uf(s,n,n.next,r)&&io(s,r)&&io(r,s)&&(t.push(s.i/e|0),t.push(n.i/e|0),t.push(r.i/e|0),so(n),so(n.next),n=i=r),n=n.next}while(n!==i);return Rs(n)}function px(i,t,e,n,s,r){let a=i;do{let o=a.next.next;for(;o!==a.prev;){if(a.i!==o.i&&bx(a,o)){let c=Df(a,o);a=Rs(a,a.next),c=Rs(c,c.next),no(a,t,e,n,s,r,0),no(c,t,e,n,s,r,0);return}o=o.next}a=a.next}while(a!==i)}function mx(i,t,e,n){let s=[],r,a,o,c,l;for(r=0,a=t.length;r<a;r++)o=t[r]*n,c=r<a-1?t[r+1]*n:i.length,l=Lf(i,o,c,n,!1),l===l.next&&(l.steiner=!0),s.push(Sx(l));for(s.sort(gx),r=0;r<s.length;r++)e=_x(s[r],e);return e}function gx(i,t){return i.x-t.x}function _x(i,t){let e=xx(i,t);if(!e)return t;let n=Df(e,i);return Rs(n,n.next),Rs(e,e.next)}function xx(i,t){let e=t,n=-1/0,s,r=i.x,a=i.y;do{if(a<=e.y&&a>=e.next.y&&e.next.y!==e.y){let d=e.x+(a-e.y)*(e.next.x-e.x)/(e.next.y-e.y);if(d<=r&&d>n&&(n=d,s=e.x<e.next.x?e:e.next,d===r))return s}e=e.next}while(e!==t);if(!s)return null;let o=s,c=s.x,l=s.y,h=1/0,f;e=s;do r>=e.x&&e.x>=c&&r!==e.x&&or(a<l?r:n,a,c,l,a<l?n:r,a,e.x,e.y)&&(f=Math.abs(a-e.y)/(r-e.x),io(e,i)&&(f<h||f===h&&(e.x>s.x||e.x===s.x&&vx(s,e)))&&(s=e,h=f)),e=e.next;while(e!==o);return s}function vx(i,t){return Qe(i.prev,i,t.prev)<0&&Qe(t.next,i,i.next)<0}function yx(i,t,e,n){let s=i;do s.z===0&&(s.z=ml(s.x,s.y,t,e,n)),s.prevZ=s.prev,s.nextZ=s.next,s=s.next;while(s!==i);s.prevZ.nextZ=null,s.prevZ=null,Mx(s)}function Mx(i){let t,e,n,s,r,a,o,c,l=1;do{for(e=i,i=null,r=null,a=0;e;){for(a++,n=e,o=0,t=0;t<l&&(o++,n=n.nextZ,!!n);t++);for(c=l;o>0||c>0&&n;)o!==0&&(c===0||!n||e.z<=n.z)?(s=e,e=e.nextZ,o--):(s=n,n=n.nextZ,c--),r?r.nextZ=s:i=s,s.prevZ=r,r=s;e=n}r.nextZ=null,l*=2}while(a>1);return i}function ml(i,t,e,n,s){return i=(i-e)*s|0,t=(t-n)*s|0,i=(i|i<<8)&16711935,i=(i|i<<4)&252645135,i=(i|i<<2)&858993459,i=(i|i<<1)&1431655765,t=(t|t<<8)&16711935,t=(t|t<<4)&252645135,t=(t|t<<2)&858993459,t=(t|t<<1)&1431655765,i|t<<1}function Sx(i){let t=i,e=i;do(t.x<e.x||t.x===e.x&&t.y<e.y)&&(e=t),t=t.next;while(t!==i);return e}function or(i,t,e,n,s,r,a,o){return(s-a)*(t-o)>=(i-a)*(r-o)&&(i-a)*(n-o)>=(e-a)*(t-o)&&(e-a)*(r-o)>=(s-a)*(n-o)}function bx(i,t){return i.next.i!==t.i&&i.prev.i!==t.i&&!Ex(i,t)&&(io(i,t)&&io(t,i)&&wx(i,t)&&(Qe(i.prev,i,t.prev)||Qe(i,t.prev,t))||Fa(i,t)&&Qe(i.prev,i,i.next)>0&&Qe(t.prev,t,t.next)>0)}function Qe(i,t,e){return(t.y-i.y)*(e.x-t.x)-(t.x-i.x)*(e.y-t.y)}function Fa(i,t){return i.x===t.x&&i.y===t.y}function Uf(i,t,e,n){let s=Qo(Qe(i,t,e)),r=Qo(Qe(i,t,n)),a=Qo(Qe(e,n,i)),o=Qo(Qe(e,n,t));return!!(s!==r&&a!==o||s===0&&jo(i,e,t)||r===0&&jo(i,n,t)||a===0&&jo(e,i,n)||o===0&&jo(e,t,n))}function jo(i,t,e){return t.x<=Math.max(i.x,e.x)&&t.x>=Math.min(i.x,e.x)&&t.y<=Math.max(i.y,e.y)&&t.y>=Math.min(i.y,e.y)}function Qo(i){return i>0?1:i<0?-1:0}function Ex(i,t){let e=i;do{if(e.i!==i.i&&e.next.i!==i.i&&e.i!==t.i&&e.next.i!==t.i&&Uf(e,e.next,i,t))return!0;e=e.next}while(e!==i);return!1}function io(i,t){return Qe(i.prev,i,i.next)<0?Qe(i,t,i.next)>=0&&Qe(i,i.prev,t)>=0:Qe(i,t,i.prev)<0||Qe(i,i.next,t)<0}function wx(i,t){let e=i,n=!1,s=(i.x+t.x)/2,r=(i.y+t.y)/2;do e.y>r!=e.next.y>r&&e.next.y!==e.y&&s<(e.next.x-e.x)*(r-e.y)/(e.next.y-e.y)+e.x&&(n=!n),e=e.next;while(e!==i);return n}function Df(i,t){let e=new gl(i.i,i.x,i.y),n=new gl(t.i,t.x,t.y),s=i.next,r=t.prev;return i.next=t,t.prev=i,e.next=s,s.prev=e,n.next=e,e.prev=n,r.next=n,n.prev=r,n}function ef(i,t,e,n){let s=new gl(i,t,e);return n?(s.next=n.next,s.prev=n,n.next.prev=s,n.next=s):(s.prev=s,s.next=s),s}function so(i){i.next.prev=i.prev,i.prev.next=i.next,i.prevZ&&(i.prevZ.nextZ=i.nextZ),i.nextZ&&(i.nextZ.prevZ=i.prevZ)}function gl(i,t,e){this.i=i,this.x=t,this.y=e,this.prev=null,this.next=null,this.z=0,this.prevZ=null,this.nextZ=null,this.steiner=!1}function Tx(i,t,e,n){let s=0;for(let r=t,a=e-n;r<e;r+=n)s+=(i[a]-i[r])*(i[r+1]+i[a+1]),a=r;return s}var ts=class i{static area(t){let e=t.length,n=0;for(let s=e-1,r=0;r<e;s=r++)n+=t[s].x*t[r].y-t[r].x*t[s].y;return n*.5}static isClockWise(t){return i.area(t)<0}static triangulateShape(t,e){let n=[],s=[],r=[];nf(t),sf(n,t);let a=t.length;e.forEach(nf);for(let c=0;c<e.length;c++)s.push(a),a+=e[c].length,sf(n,e[c]);let o=hx.triangulate(n,s);for(let c=0;c<o.length;c+=3)r.push(o.slice(c,c+3));return r}};function nf(i){let t=i.length;t>2&&i[t-1].equals(i[0])&&i.pop()}function sf(i,t){for(let e=0;e<t.length;e++)i.push(t[e].x),i.push(t[e].y)}var Bi=class i extends Ke{constructor(t=new jn([new St(.5,.5),new St(-.5,.5),new St(-.5,-.5),new St(.5,-.5)]),e={}){super(),this.type="ExtrudeGeometry",this.parameters={shapes:t,options:e},t=Array.isArray(t)?t:[t];let n=this,s=[],r=[];for(let o=0,c=t.length;o<c;o++){let l=t[o];a(l)}this.setAttribute("position",new de(s,3)),this.setAttribute("uv",new de(r,2)),this.computeVertexNormals();function a(o){let c=[],l=e.curveSegments!==void 0?e.curveSegments:12,h=e.steps!==void 0?e.steps:1,f=e.depth!==void 0?e.depth:1,d=e.bevelEnabled!==void 0?e.bevelEnabled:!0,p=e.bevelThickness!==void 0?e.bevelThickness:.2,x=e.bevelSize!==void 0?e.bevelSize:p-.1,S=e.bevelOffset!==void 0?e.bevelOffset:0,_=e.bevelSegments!==void 0?e.bevelSegments:3,m=e.extrudePath,T=e.UVGenerator!==void 0?e.UVGenerator:Ax,M,U=!1,W,F,B,J;m&&(M=m.getSpacedPoints(h),U=!0,d=!1,W=m.computeFrenetFrames(h,!1),F=new O,B=new O,J=new O),d||(_=0,p=0,x=0,S=0);let w=o.extractPoints(l),L=w.shape,$=w.holes;if(!ts.isClockWise(L)){L=L.reverse();for(let z=0,Tt=$.length;z<Tt;z++){let rt=$[z];ts.isClockWise(rt)&&($[z]=rt.reverse())}}let Mt=ts.triangulateShape(L,$),X=L;for(let z=0,Tt=$.length;z<Tt;z++){let rt=$[z];L=L.concat(rt)}function K(z,Tt,rt){return Tt||console.error("THREE.ExtrudeGeometry: vec does not exist"),z.clone().addScaledVector(Tt,rt)}let tt=L.length,it=Mt.length;function ft(z,Tt,rt){let bt,ht,qt,It=z.x-Tt.x,R=z.y-Tt.y,b=rt.x-z.x,Y=rt.y-z.y,xt=It*It+R*R,mt=It*Y-R*b;if(Math.abs(mt)>Number.EPSILON){let gt=Math.sqrt(xt),Gt=Math.sqrt(b*b+Y*Y),Lt=Tt.x-R/gt,At=Tt.y+It/gt,ee=rt.x-Y/Gt,pe=rt.y+b/Gt,dt=((ee-Lt)*Y-(pe-At)*b)/(It*Y-R*b);bt=Lt+It*dt-z.x,ht=At+R*dt-z.y;let Re=bt*bt+ht*ht;if(Re<=2)return new St(bt,ht);qt=Math.sqrt(Re/2)}else{let gt=!1;It>Number.EPSILON?b>Number.EPSILON&&(gt=!0):It<-Number.EPSILON?b<-Number.EPSILON&&(gt=!0):Math.sign(R)===Math.sign(Y)&&(gt=!0),gt?(bt=-R,ht=It,qt=Math.sqrt(xt)):(bt=It,ht=R,qt=Math.sqrt(xt/2))}return new St(bt/qt,ht/qt)}let nt=[];for(let z=0,Tt=X.length,rt=Tt-1,bt=z+1;z<Tt;z++,rt++,bt++)rt===Tt&&(rt=0),bt===Tt&&(bt=0),nt[z]=ft(X[z],X[rt],X[bt]);let ct=[],lt,Dt=nt.concat();for(let z=0,Tt=$.length;z<Tt;z++){let rt=$[z];lt=[];for(let bt=0,ht=rt.length,qt=ht-1,It=bt+1;bt<ht;bt++,qt++,It++)qt===ht&&(qt=0),It===ht&&(It=0),lt[bt]=ft(rt[bt],rt[qt],rt[It]);ct.push(lt),Dt=Dt.concat(lt)}for(let z=0;z<_;z++){let Tt=z/_,rt=p*Math.cos(Tt*Math.PI/2),bt=x*Math.sin(Tt*Math.PI/2)+S;for(let ht=0,qt=X.length;ht<qt;ht++){let It=K(X[ht],nt[ht],bt);Bt(It.x,It.y,-rt)}for(let ht=0,qt=$.length;ht<qt;ht++){let It=$[ht];lt=ct[ht];for(let R=0,b=It.length;R<b;R++){let Y=K(It[R],lt[R],bt);Bt(Y.x,Y.y,-rt)}}}let st=x+S;for(let z=0;z<tt;z++){let Tt=d?K(L[z],Dt[z],st):L[z];U?(B.copy(W.normals[0]).multiplyScalar(Tt.x),F.copy(W.binormals[0]).multiplyScalar(Tt.y),J.copy(M[0]).add(B).add(F),Bt(J.x,J.y,J.z)):Bt(Tt.x,Tt.y,0)}for(let z=1;z<=h;z++)for(let Tt=0;Tt<tt;Tt++){let rt=d?K(L[Tt],Dt[Tt],st):L[Tt];U?(B.copy(W.normals[z]).multiplyScalar(rt.x),F.copy(W.binormals[z]).multiplyScalar(rt.y),J.copy(M[z]).add(B).add(F),Bt(J.x,J.y,J.z)):Bt(rt.x,rt.y,f/h*z)}for(let z=_-1;z>=0;z--){let Tt=z/_,rt=p*Math.cos(Tt*Math.PI/2),bt=x*Math.sin(Tt*Math.PI/2)+S;for(let ht=0,qt=X.length;ht<qt;ht++){let It=K(X[ht],nt[ht],bt);Bt(It.x,It.y,f+rt)}for(let ht=0,qt=$.length;ht<qt;ht++){let It=$[ht];lt=ct[ht];for(let R=0,b=It.length;R<b;R++){let Y=K(It[R],lt[R],bt);U?Bt(Y.x,Y.y+M[h-1].y,M[h-1].x+rt):Bt(Y.x,Y.y,f+rt)}}}ut(),Nt();function ut(){let z=s.length/3;if(d){let Tt=0,rt=tt*Tt;for(let bt=0;bt<it;bt++){let ht=Mt[bt];se(ht[2]+rt,ht[1]+rt,ht[0]+rt)}Tt=h+_*2,rt=tt*Tt;for(let bt=0;bt<it;bt++){let ht=Mt[bt];se(ht[0]+rt,ht[1]+rt,ht[2]+rt)}}else{for(let Tt=0;Tt<it;Tt++){let rt=Mt[Tt];se(rt[2],rt[1],rt[0])}for(let Tt=0;Tt<it;Tt++){let rt=Mt[Tt];se(rt[0]+tt*h,rt[1]+tt*h,rt[2]+tt*h)}}n.addGroup(z,s.length/3-z,0)}function Nt(){let z=s.length/3,Tt=0;Ft(X,Tt),Tt+=X.length;for(let rt=0,bt=$.length;rt<bt;rt++){let ht=$[rt];Ft(ht,Tt),Tt+=ht.length}n.addGroup(z,s.length/3-z,1)}function Ft(z,Tt){let rt=z.length;for(;--rt>=0;){let bt=rt,ht=rt-1;ht<0&&(ht=z.length-1);for(let qt=0,It=h+_*2;qt<It;qt++){let R=tt*qt,b=tt*(qt+1),Y=Tt+bt+R,xt=Tt+ht+R,mt=Tt+ht+b,gt=Tt+bt+b;Jt(Y,xt,mt,gt)}}}function Bt(z,Tt,rt){c.push(z),c.push(Tt),c.push(rt)}function se(z,Tt,rt){Wt(z),Wt(Tt),Wt(rt);let bt=s.length/3,ht=T.generateTopUV(n,s,bt-3,bt-2,bt-1);le(ht[0]),le(ht[1]),le(ht[2])}function Jt(z,Tt,rt,bt){Wt(z),Wt(Tt),Wt(bt),Wt(Tt),Wt(rt),Wt(bt);let ht=s.length/3,qt=T.generateSideWallUV(n,s,ht-6,ht-3,ht-2,ht-1);le(qt[0]),le(qt[1]),le(qt[3]),le(qt[1]),le(qt[2]),le(qt[3])}function Wt(z){s.push(c[z*3+0]),s.push(c[z*3+1]),s.push(c[z*3+2])}function le(z){r.push(z.x),r.push(z.y)}}}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}toJSON(){let t=super.toJSON(),e=this.parameters.shapes,n=this.parameters.options;return Rx(e,n,t)}static fromJSON(t,e){let n=[];for(let r=0,a=t.shapes.length;r<a;r++){let o=e[t.shapes[r]];n.push(o)}let s=t.options.extrudePath;return s!==void 0&&(t.options.extrudePath=new dl[s.type]().fromJSON(s)),new i(n,t.options)}},Ax={generateTopUV:function(i,t,e,n,s){let r=t[e*3],a=t[e*3+1],o=t[n*3],c=t[n*3+1],l=t[s*3],h=t[s*3+1];return[new St(r,a),new St(o,c),new St(l,h)]},generateSideWallUV:function(i,t,e,n,s,r){let a=t[e*3],o=t[e*3+1],c=t[e*3+2],l=t[n*3],h=t[n*3+1],f=t[n*3+2],d=t[s*3],p=t[s*3+1],x=t[s*3+2],S=t[r*3],_=t[r*3+1],m=t[r*3+2];return Math.abs(o-h)<Math.abs(a-l)?[new St(a,1-c),new St(l,1-f),new St(d,1-x),new St(S,1-m)]:[new St(o,1-c),new St(h,1-f),new St(p,1-x),new St(_,1-m)]}};function Rx(i,t,e){if(e.shapes=[],Array.isArray(i))for(let n=0,s=i.length;n<s;n++){let r=i[n];e.shapes.push(r.uuid)}else e.shapes.push(i.uuid);return e.options=Object.assign({},t),t.extrudePath!==void 0&&(e.options.extrudePath=t.extrudePath.toJSON()),e}var wa=class i extends to{constructor(t=1,e=0){let n=(1+Math.sqrt(5))/2,s=[-1,n,0,1,n,0,-1,-n,0,1,-n,0,0,-1,n,0,1,n,0,-1,-n,0,1,-n,n,0,-1,n,0,1,-n,0,-1,-n,0,1],r=[0,11,5,0,5,1,0,1,7,0,7,10,0,10,11,1,5,9,5,11,4,11,10,2,10,7,6,7,1,8,3,9,4,3,4,2,3,2,6,3,6,8,3,8,9,4,9,5,2,4,11,6,2,10,8,6,7,9,8,1];super(s,r,t,e),this.type="IcosahedronGeometry",this.parameters={radius:t,detail:e}}static fromJSON(t){return new i(t.radius,t.detail)}},Ta=class i extends to{constructor(t=1,e=0){let n=[1,0,0,-1,0,0,0,1,0,0,-1,0,0,0,1,0,0,-1],s=[0,2,4,0,4,3,0,3,5,0,5,2,1,2,5,1,5,3,1,3,4,1,4,2];super(n,s,t,e),this.type="OctahedronGeometry",this.parameters={radius:t,detail:e}}static fromJSON(t){return new i(t.radius,t.detail)}};var Aa=class i extends Ke{constructor(t=new jn([new St(0,.5),new St(-.5,-.5),new St(.5,-.5)]),e=12){super(),this.type="ShapeGeometry",this.parameters={shapes:t,curveSegments:e};let n=[],s=[],r=[],a=[],o=0,c=0;if(Array.isArray(t)===!1)l(t);else for(let h=0;h<t.length;h++)l(t[h]),this.addGroup(o,c,h),o+=c,c=0;this.setIndex(n),this.setAttribute("position",new de(s,3)),this.setAttribute("normal",new de(r,3)),this.setAttribute("uv",new de(a,2));function l(h){let f=s.length/3,d=h.extractPoints(e),p=d.shape,x=d.holes;ts.isClockWise(p)===!1&&(p=p.reverse());for(let _=0,m=x.length;_<m;_++){let T=x[_];ts.isClockWise(T)===!0&&(x[_]=T.reverse())}let S=ts.triangulateShape(p,x);for(let _=0,m=x.length;_<m;_++){let T=x[_];p=p.concat(T)}for(let _=0,m=p.length;_<m;_++){let T=p[_];s.push(T.x,T.y,0),r.push(0,0,1),a.push(T.x,T.y)}for(let _=0,m=S.length;_<m;_++){let T=S[_],M=T[0]+f,U=T[1]+f,W=T[2]+f;n.push(M,U,W),c+=3}}}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}toJSON(){let t=super.toJSON(),e=this.parameters.shapes;return Cx(e,t)}static fromJSON(t,e){let n=[];for(let s=0,r=t.shapes.length;s<r;s++){let a=e[t.shapes[s]];n.push(a)}return new i(n,t.curveSegments)}};function Cx(i,t){if(t.shapes=[],Array.isArray(i))for(let e=0,n=i.length;e<n;e++){let s=i[e];t.shapes.push(s.uuid)}else t.shapes.push(i.uuid);return t}var Un=class i extends Ke{constructor(t=1,e=32,n=16,s=0,r=Math.PI*2,a=0,o=Math.PI){super(),this.type="SphereGeometry",this.parameters={radius:t,widthSegments:e,heightSegments:n,phiStart:s,phiLength:r,thetaStart:a,thetaLength:o},e=Math.max(3,Math.floor(e)),n=Math.max(2,Math.floor(n));let c=Math.min(a+o,Math.PI),l=0,h=[],f=new O,d=new O,p=[],x=[],S=[],_=[];for(let m=0;m<=n;m++){let T=[],M=m/n,U=0;m===0&&a===0?U=.5/e:m===n&&c===Math.PI&&(U=-.5/e);for(let W=0;W<=e;W++){let F=W/e;f.x=-t*Math.cos(s+F*r)*Math.sin(a+M*o),f.y=t*Math.cos(a+M*o),f.z=t*Math.sin(s+F*r)*Math.sin(a+M*o),x.push(f.x,f.y,f.z),d.copy(f).normalize(),S.push(d.x,d.y,d.z),_.push(F+U,1-M),T.push(l++)}h.push(T)}for(let m=0;m<n;m++)for(let T=0;T<e;T++){let M=h[m][T+1],U=h[m][T],W=h[m+1][T],F=h[m+1][T+1];(m!==0||a>0)&&p.push(M,U,F),(m!==n-1||c<Math.PI)&&p.push(U,W,F)}this.setIndex(p),this.setAttribute("position",new de(x,3)),this.setAttribute("normal",new de(S,3)),this.setAttribute("uv",new de(_,2))}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.radius,t.widthSegments,t.heightSegments,t.phiStart,t.phiLength,t.thetaStart,t.thetaLength)}};var ro=class i extends Ke{constructor(t=1,e=.4,n=12,s=48,r=Math.PI*2){super(),this.type="TorusGeometry",this.parameters={radius:t,tube:e,radialSegments:n,tubularSegments:s,arc:r},n=Math.floor(n),s=Math.floor(s);let a=[],o=[],c=[],l=[],h=new O,f=new O,d=new O;for(let p=0;p<=n;p++)for(let x=0;x<=s;x++){let S=x/s*r,_=p/n*Math.PI*2;f.x=(t+e*Math.cos(_))*Math.cos(S),f.y=(t+e*Math.cos(_))*Math.sin(S),f.z=e*Math.sin(_),o.push(f.x,f.y,f.z),h.x=t*Math.cos(S),h.y=t*Math.sin(S),d.subVectors(f,h).normalize(),c.push(d.x,d.y,d.z),l.push(x/s),l.push(p/n)}for(let p=1;p<=n;p++)for(let x=1;x<=s;x++){let S=(s+1)*p+x-1,_=(s+1)*(p-1)+x-1,m=(s+1)*(p-1)+x,T=(s+1)*p+x;a.push(S,_,T),a.push(_,m,T)}this.setIndex(a),this.setAttribute("position",new de(o,3)),this.setAttribute("normal",new de(c,3)),this.setAttribute("uv",new de(l,2))}copy(t){return super.copy(t),this.parameters=Object.assign({},t.parameters),this}static fromJSON(t){return new i(t.radius,t.tube,t.radialSegments,t.tubularSegments,t.arc)}};var Qn=class extends yi{constructor(t){super(),this.isMeshStandardMaterial=!0,this.defines={STANDARD:""},this.type="MeshStandardMaterial",this.color=new fe(16777215),this.roughness=1,this.metalness=0,this.map=null,this.lightMap=null,this.lightMapIntensity=1,this.aoMap=null,this.aoMapIntensity=1,this.emissive=new fe(0),this.emissiveIntensity=1,this.emissiveMap=null,this.bumpMap=null,this.bumpScale=1,this.normalMap=null,this.normalMapType=Mf,this.normalScale=new St(1,1),this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.roughnessMap=null,this.metalnessMap=null,this.alphaMap=null,this.envMap=null,this.envMapIntensity=1,this.wireframe=!1,this.wireframeLinewidth=1,this.wireframeLinecap="round",this.wireframeLinejoin="round",this.flatShading=!1,this.fog=!0,this.setValues(t)}copy(t){return super.copy(t),this.defines={STANDARD:""},this.color.copy(t.color),this.roughness=t.roughness,this.metalness=t.metalness,this.map=t.map,this.lightMap=t.lightMap,this.lightMapIntensity=t.lightMapIntensity,this.aoMap=t.aoMap,this.aoMapIntensity=t.aoMapIntensity,this.emissive.copy(t.emissive),this.emissiveMap=t.emissiveMap,this.emissiveIntensity=t.emissiveIntensity,this.bumpMap=t.bumpMap,this.bumpScale=t.bumpScale,this.normalMap=t.normalMap,this.normalMapType=t.normalMapType,this.normalScale.copy(t.normalScale),this.displacementMap=t.displacementMap,this.displacementScale=t.displacementScale,this.displacementBias=t.displacementBias,this.roughnessMap=t.roughnessMap,this.metalnessMap=t.metalnessMap,this.alphaMap=t.alphaMap,this.envMap=t.envMap,this.envMapIntensity=t.envMapIntensity,this.wireframe=t.wireframe,this.wireframeLinewidth=t.wireframeLinewidth,this.wireframeLinecap=t.wireframeLinecap,this.wireframeLinejoin=t.wireframeLinejoin,this.flatShading=t.flatShading,this.fog=t.fog,this}};function ta(i,t,e){return!i||!e&&i.constructor===t?i:typeof t.BYTES_PER_ELEMENT=="number"?new t(i):Array.prototype.slice.call(i)}function Px(i){return ArrayBuffer.isView(i)&&!(i instanceof DataView)}var _r=class{constructor(t,e,n,s){this.parameterPositions=t,this._cachedIndex=0,this.resultBuffer=s!==void 0?s:new e.constructor(n),this.sampleValues=e,this.valueSize=n,this.settings=null,this.DefaultSettings_={}}evaluate(t){let e=this.parameterPositions,n=this._cachedIndex,s=e[n],r=e[n-1];n:{t:{let a;e:{i:if(!(t<s)){for(let o=n+2;;){if(s===void 0){if(t<r)break i;return n=e.length,this._cachedIndex=n,this.copySampleValue_(n-1)}if(n===o)break;if(r=s,s=e[++n],t<s)break t}a=e.length;break e}if(!(t>=r)){let o=e[1];t<o&&(n=2,r=o);for(let c=n-2;;){if(r===void 0)return this._cachedIndex=0,this.copySampleValue_(0);if(n===c)break;if(s=r,r=e[--n-1],t>=r)break t}a=n,n=0;break e}break n}for(;n<a;){let o=n+a>>>1;t<e[o]?a=o:n=o+1}if(s=e[n],r=e[n-1],r===void 0)return this._cachedIndex=0,this.copySampleValue_(0);if(s===void 0)return n=e.length,this._cachedIndex=n,this.copySampleValue_(n-1)}this._cachedIndex=n,this.intervalChanged_(n,r,s)}return this.interpolate_(n,r,t,s)}getSettings_(){return this.settings||this.DefaultSettings_}copySampleValue_(t){let e=this.resultBuffer,n=this.sampleValues,s=this.valueSize,r=t*s;for(let a=0;a!==s;++a)e[a]=n[r+a];return e}interpolate_(){throw new Error("call to abstract method")}intervalChanged_(){}},_l=class extends _r{constructor(t,e,n,s){super(t,e,n,s),this._weightPrev=-0,this._offsetPrev=-0,this._weightNext=-0,this._offsetNext=-0,this.DefaultSettings_={endingStart:ou,endingEnd:ou}}intervalChanged_(t,e,n){let s=this.parameterPositions,r=t-2,a=t+1,o=s[r],c=s[a];if(o===void 0)switch(this.getSettings_().endingStart){case au:r=t,o=2*e-n;break;case cu:r=s.length-2,o=e+s[r]-s[r+1];break;default:r=t,o=n}if(c===void 0)switch(this.getSettings_().endingEnd){case au:a=t,c=2*n-e;break;case cu:a=1,c=n+s[1]-s[0];break;default:a=t-1,c=e}let l=(n-e)*.5,h=this.valueSize;this._weightPrev=l/(e-o),this._weightNext=l/(c-n),this._offsetPrev=r*h,this._offsetNext=a*h}interpolate_(t,e,n,s){let r=this.resultBuffer,a=this.sampleValues,o=this.valueSize,c=t*o,l=c-o,h=this._offsetPrev,f=this._offsetNext,d=this._weightPrev,p=this._weightNext,x=(n-e)/(s-e),S=x*x,_=S*x,m=-d*_+2*d*S-d*x,T=(1+d)*_+(-1.5-2*d)*S+(-.5+d)*x+1,M=(-1-p)*_+(1.5+p)*S+.5*x,U=p*_-p*S;for(let W=0;W!==o;++W)r[W]=m*a[h+W]+T*a[l+W]+M*a[c+W]+U*a[f+W];return r}},xl=class extends _r{constructor(t,e,n,s){super(t,e,n,s)}interpolate_(t,e,n,s){let r=this.resultBuffer,a=this.sampleValues,o=this.valueSize,c=t*o,l=c-o,h=(n-e)/(s-e),f=1-h;for(let d=0;d!==o;++d)r[d]=a[l+d]*f+a[c+d]*h;return r}},vl=class extends _r{constructor(t,e,n,s){super(t,e,n,s)}interpolate_(t){return this.copySampleValue_(t-1)}},ui=class{constructor(t,e,n,s){if(t===void 0)throw new Error("THREE.KeyframeTrack: track name is undefined");if(e===void 0||e.length===0)throw new Error("THREE.KeyframeTrack: no keyframes in track named "+t);this.name=t,this.times=ta(e,this.TimeBufferType),this.values=ta(n,this.ValueBufferType),this.setInterpolation(s||this.DefaultInterpolation)}static toJSON(t){let e=t.constructor,n;if(e.toJSON!==this.toJSON)n=e.toJSON(t);else{n={name:t.name,times:ta(t.times,Array),values:ta(t.values,Array)};let s=t.getInterpolation();s!==t.DefaultInterpolation&&(n.interpolation=s)}return n.type=t.ValueTypeName,n}InterpolantFactoryMethodDiscrete(t){return new vl(this.times,this.values,this.getValueSize(),t)}InterpolantFactoryMethodLinear(t){return new xl(this.times,this.values,this.getValueSize(),t)}InterpolantFactoryMethodSmooth(t){return new _l(this.times,this.values,this.getValueSize(),t)}setInterpolation(t){let e;switch(t){case na:e=this.InterpolantFactoryMethodDiscrete;break;case ia:e=this.InterpolantFactoryMethodLinear;break;case uc:e=this.InterpolantFactoryMethodSmooth;break}if(e===void 0){let n="unsupported interpolation for "+this.ValueTypeName+" keyframe track named "+this.name;if(this.createInterpolant===void 0)if(t!==this.DefaultInterpolation)this.setInterpolation(this.DefaultInterpolation);else throw new Error(n);return console.warn("THREE.KeyframeTrack:",n),this}return this.createInterpolant=e,this}getInterpolation(){switch(this.createInterpolant){case this.InterpolantFactoryMethodDiscrete:return na;case this.InterpolantFactoryMethodLinear:return ia;case this.InterpolantFactoryMethodSmooth:return uc}}getValueSize(){return this.values.length/this.times.length}shift(t){if(t!==0){let e=this.times;for(let n=0,s=e.length;n!==s;++n)e[n]+=t}return this}scale(t){if(t!==1){let e=this.times;for(let n=0,s=e.length;n!==s;++n)e[n]*=t}return this}trim(t,e){let n=this.times,s=n.length,r=0,a=s-1;for(;r!==s&&n[r]<t;)++r;for(;a!==-1&&n[a]>e;)--a;if(++a,r!==0||a!==s){r>=a&&(a=Math.max(a,1),r=a-1);let o=this.getValueSize();this.times=n.slice(r,a),this.values=this.values.slice(r*o,a*o)}return this}validate(){let t=!0,e=this.getValueSize();e-Math.floor(e)!==0&&(console.error("THREE.KeyframeTrack: Invalid value size in track.",this),t=!1);let n=this.times,s=this.values,r=n.length;r===0&&(console.error("THREE.KeyframeTrack: Track is empty.",this),t=!1);let a=null;for(let o=0;o!==r;o++){let c=n[o];if(typeof c=="number"&&isNaN(c)){console.error("THREE.KeyframeTrack: Time is not a valid number.",this,o,c),t=!1;break}if(a!==null&&a>c){console.error("THREE.KeyframeTrack: Out of order keys.",this,o,c,a),t=!1;break}a=c}if(s!==void 0&&Px(s))for(let o=0,c=s.length;o!==c;++o){let l=s[o];if(isNaN(l)){console.error("THREE.KeyframeTrack: Value is not a valid number.",this,o,l),t=!1;break}}return t}optimize(){let t=this.times.slice(),e=this.values.slice(),n=this.getValueSize(),s=this.getInterpolation()===uc,r=t.length-1,a=1;for(let o=1;o<r;++o){let c=!1,l=t[o],h=t[o+1];if(l!==h&&(o!==1||l!==t[0]))if(s)c=!0;else{let f=o*n,d=f-n,p=f+n;for(let x=0;x!==n;++x){let S=e[f+x];if(S!==e[d+x]||S!==e[p+x]){c=!0;break}}}if(c){if(o!==a){t[a]=t[o];let f=o*n,d=a*n;for(let p=0;p!==n;++p)e[d+p]=e[f+p]}++a}}if(r>0){t[a]=t[r];for(let o=r*n,c=a*n,l=0;l!==n;++l)e[c+l]=e[o+l];++a}return a!==t.length?(this.times=t.slice(0,a),this.values=e.slice(0,a*n)):(this.times=t,this.values=e),this}clone(){let t=this.times.slice(),e=this.values.slice(),n=this.constructor,s=new n(this.name,t,e);return s.createInterpolant=this.createInterpolant,s}};ui.prototype.TimeBufferType=Float32Array;ui.prototype.ValueBufferType=Float32Array;ui.prototype.DefaultInterpolation=ia;var Cs=class extends ui{};Cs.prototype.ValueTypeName="bool";Cs.prototype.ValueBufferType=Array;Cs.prototype.DefaultInterpolation=na;Cs.prototype.InterpolantFactoryMethodLinear=void 0;Cs.prototype.InterpolantFactoryMethodSmooth=void 0;var yl=class extends ui{};yl.prototype.ValueTypeName="color";var Ml=class extends ui{};Ml.prototype.ValueTypeName="number";var Sl=class extends _r{constructor(t,e,n,s){super(t,e,n,s)}interpolate_(t,e,n,s){let r=this.resultBuffer,a=this.sampleValues,o=this.valueSize,c=(n-e)/(s-e),l=t*o;for(let h=l+o;l!==h;l+=4)kn.slerpFlat(r,0,a,l-o,a,l,c);return r}},oo=class extends ui{InterpolantFactoryMethodLinear(t){return new Sl(this.times,this.values,this.getValueSize(),t)}};oo.prototype.ValueTypeName="quaternion";oo.prototype.DefaultInterpolation=ia;oo.prototype.InterpolantFactoryMethodSmooth=void 0;var Ps=class extends ui{};Ps.prototype.ValueTypeName="string";Ps.prototype.ValueBufferType=Array;Ps.prototype.DefaultInterpolation=na;Ps.prototype.InterpolantFactoryMethodLinear=void 0;Ps.prototype.InterpolantFactoryMethodSmooth=void 0;var bl=class extends ui{};bl.prototype.ValueTypeName="vector";var rf={enabled:!1,files:{},add:function(i,t){this.enabled!==!1&&(this.files[i]=t)},get:function(i){if(this.enabled!==!1)return this.files[i]},remove:function(i){delete this.files[i]},clear:function(){this.files={}}},El=class{constructor(t,e,n){let s=this,r=!1,a=0,o=0,c,l=[];this.onStart=void 0,this.onLoad=t,this.onProgress=e,this.onError=n,this.itemStart=function(h){o++,r===!1&&s.onStart!==void 0&&s.onStart(h,a,o),r=!0},this.itemEnd=function(h){a++,s.onProgress!==void 0&&s.onProgress(h,a,o),a===o&&(r=!1,s.onLoad!==void 0&&s.onLoad())},this.itemError=function(h){s.onError!==void 0&&s.onError(h)},this.resolveURL=function(h){return c?c(h):h},this.setURLModifier=function(h){return c=h,this},this.addHandler=function(h,f){return l.push(h,f),this},this.removeHandler=function(h){let f=l.indexOf(h);return f!==-1&&l.splice(f,2),this},this.getHandler=function(h){for(let f=0,d=l.length;f<d;f+=2){let p=l[f],x=l[f+1];if(p.global&&(p.lastIndex=0),p.test(h))return x}return null}}},Ix=new El,ao=class{constructor(t){this.manager=t!==void 0?t:Ix,this.crossOrigin="anonymous",this.withCredentials=!1,this.path="",this.resourcePath="",this.requestHeader={}}load(){}loadAsync(t,e){let n=this;return new Promise(function(s,r){n.load(t,s,e,r)})}parse(){}setCrossOrigin(t){return this.crossOrigin=t,this}setWithCredentials(t){return this.withCredentials=t,this}setPath(t){return this.path=t,this}setResourcePath(t){return this.resourcePath=t,this}setRequestHeader(t){return this.requestHeader=t,this}};ao.DEFAULT_MATERIAL_NAME="__DEFAULT";var wl=class extends ao{constructor(t){super(t)}load(t,e,n,s){this.path!==void 0&&(t=this.path+t),t=this.manager.resolveURL(t);let r=this,a=rf.get(t);if(a!==void 0)return r.manager.itemStart(t),setTimeout(function(){e&&e(a),r.manager.itemEnd(t)},0),a;let o=Wr("img");function c(){h(),rf.add(t,this),e&&e(this),r.manager.itemEnd(t)}function l(f){h(),s&&s(f),r.manager.itemError(t),r.manager.itemEnd(t)}function h(){o.removeEventListener("load",c,!1),o.removeEventListener("error",l,!1)}return o.addEventListener("load",c,!1),o.addEventListener("error",l,!1),t.slice(0,5)!=="data:"&&this.crossOrigin!==void 0&&(o.crossOrigin=this.crossOrigin),r.manager.itemStart(t),o.src=t,o}};var Ra=class extends ao{constructor(t){super(t)}load(t,e,n,s){let r=new Hn,a=new wl(this.manager);return a.setCrossOrigin(this.crossOrigin),a.setPath(this.path),a.load(t,function(o){r.image=o,r.needsUpdate=!0,e!==void 0&&e(r)},n,s),r}},co=class extends An{constructor(t,e=1){super(),this.isLight=!0,this.type="Light",this.color=new fe(t),this.intensity=e}dispose(){}copy(t,e){return super.copy(t,e),this.color.copy(t.color),this.intensity=t.intensity,this}toJSON(t){let e=super.toJSON(t);return e.object.color=this.color.getHex(),e.object.intensity=this.intensity,this.groundColor!==void 0&&(e.object.groundColor=this.groundColor.getHex()),this.distance!==void 0&&(e.object.distance=this.distance),this.angle!==void 0&&(e.object.angle=this.angle),this.decay!==void 0&&(e.object.decay=this.decay),this.penumbra!==void 0&&(e.object.penumbra=this.penumbra),this.shadow!==void 0&&(e.object.shadow=this.shadow.toJSON()),e}},Ca=class extends co{constructor(t,e,n){super(t,n),this.isHemisphereLight=!0,this.type="HemisphereLight",this.position.copy(An.DEFAULT_UP),this.updateMatrix(),this.groundColor=new fe(e)}copy(t,e){return super.copy(t,e),this.groundColor.copy(t.groundColor),this}},Oc=new Ue,of=new O,af=new O,Pa=class{constructor(t){this.camera=t,this.bias=0,this.normalBias=0,this.radius=1,this.blurSamples=8,this.mapSize=new St(512,512),this.map=null,this.mapPass=null,this.matrix=new Ue,this.autoUpdate=!0,this.needsUpdate=!1,this._frustum=new qr,this._frameExtents=new St(1,1),this._viewportCount=1,this._viewports=[new Je(0,0,1,1)]}getViewportCount(){return this._viewportCount}getFrustum(){return this._frustum}updateMatrices(t){let e=this.camera,n=this.matrix;of.setFromMatrixPosition(t.matrixWorld),e.position.copy(of),af.setFromMatrixPosition(t.target.matrixWorld),e.lookAt(af),e.updateMatrixWorld(),Oc.multiplyMatrices(e.projectionMatrix,e.matrixWorldInverse),this._frustum.setFromProjectionMatrix(Oc),n.set(.5,0,0,.5,0,.5,0,.5,0,0,.5,.5,0,0,0,1),n.multiply(Oc)}getViewport(t){return this._viewports[t]}getFrameExtents(){return this._frameExtents}dispose(){this.map&&this.map.dispose(),this.mapPass&&this.mapPass.dispose()}copy(t){return this.camera=t.camera.clone(),this.bias=t.bias,this.radius=t.radius,this.mapSize.copy(t.mapSize),this}clone(){return new this.constructor().copy(this)}toJSON(){let t={};return this.bias!==0&&(t.bias=this.bias),this.normalBias!==0&&(t.normalBias=this.normalBias),this.radius!==1&&(t.radius=this.radius),(this.mapSize.x!==512||this.mapSize.y!==512)&&(t.mapSize=this.mapSize.toArray()),t.camera=this.camera.toJSON(!1).object,delete t.camera.matrix,t}};var cf=new Ue,Dr=new O,Bc=new O,Tl=class extends Pa{constructor(){super(new wn(90,1,.5,500)),this.isPointLightShadow=!0,this._frameExtents=new St(4,2),this._viewportCount=6,this._viewports=[new Je(2,1,1,1),new Je(0,1,1,1),new Je(3,1,1,1),new Je(1,1,1,1),new Je(3,0,1,1),new Je(1,0,1,1)],this._cubeDirections=[new O(1,0,0),new O(-1,0,0),new O(0,0,1),new O(0,0,-1),new O(0,1,0),new O(0,-1,0)],this._cubeUps=[new O(0,1,0),new O(0,1,0),new O(0,1,0),new O(0,1,0),new O(0,0,1),new O(0,0,-1)]}updateMatrices(t,e=0){let n=this.camera,s=this.matrix,r=t.distance||n.far;r!==n.far&&(n.far=r,n.updateProjectionMatrix()),Dr.setFromMatrixPosition(t.matrixWorld),n.position.copy(Dr),Bc.copy(n.position),Bc.add(this._cubeDirections[e]),n.up.copy(this._cubeUps[e]),n.lookAt(Bc),n.updateMatrixWorld(),s.makeTranslation(-Dr.x,-Dr.y,-Dr.z),cf.multiplyMatrices(n.projectionMatrix,n.matrixWorldInverse),this._frustum.setFromProjectionMatrix(cf)}},rs=class extends co{constructor(t,e,n=0,s=2){super(t,e),this.isPointLight=!0,this.type="PointLight",this.distance=n,this.decay=s,this.shadow=new Tl}get power(){return this.intensity*4*Math.PI}set power(t){this.intensity=t/(4*Math.PI)}dispose(){this.shadow.dispose()}copy(t,e){return super.copy(t,e),this.distance=t.distance,this.decay=t.decay,this.shadow=t.shadow.clone(),this}},Al=class extends Pa{constructor(){super(new ga(-5,5,5,-5,.5,500)),this.isDirectionalLightShadow=!0}},Ia=class extends co{constructor(t,e){super(t,e),this.isDirectionalLight=!0,this.type="DirectionalLight",this.position.copy(An.DEFAULT_UP),this.updateMatrix(),this.target=new An,this.shadow=new Al}dispose(){this.shadow.dispose()}copy(t){return super.copy(t),this.target=t.target.clone(),this.shadow=t.shadow.clone(),this}};var lo=class extends Ke{constructor(){super(),this.isInstancedBufferGeometry=!0,this.type="InstancedBufferGeometry",this.instanceCount=1/0}copy(t){return super.copy(t),this.instanceCount=t.instanceCount,this}toJSON(){let t=super.toJSON();return t.instanceCount=this.instanceCount,t.isInstancedBufferGeometry=!0,t}};var zl="\\[\\]\\.:\\/",Lx=new RegExp("["+zl+"]","g"),Hl="[^"+zl+"]",Ux="[^"+zl.replace("\\.","")+"]",Dx=/((?:WC+[\/:])*)/.source.replace("WC",Hl),Nx=/(WCOD+)?/.source.replace("WCOD",Ux),Fx=/(?:\.(WC+)(?:\[(.+)\])?)?/.source.replace("WC",Hl),Ox=/\.(WC+)(?:\[(.+)\])?/.source.replace("WC",Hl),Bx=new RegExp("^"+Dx+Nx+Fx+Ox+"$"),zx=["material","materials","bones","map"],Rl=class{constructor(t,e,n){let s=n||$e.parseTrackName(e);this._targetGroup=t,this._bindings=t.subscribe_(e,s)}getValue(t,e){this.bind();let n=this._targetGroup.nCachedObjects_,s=this._bindings[n];s!==void 0&&s.getValue(t,e)}setValue(t,e){let n=this._bindings;for(let s=this._targetGroup.nCachedObjects_,r=n.length;s!==r;++s)n[s].setValue(t,e)}bind(){let t=this._bindings;for(let e=this._targetGroup.nCachedObjects_,n=t.length;e!==n;++e)t[e].bind()}unbind(){let t=this._bindings;for(let e=this._targetGroup.nCachedObjects_,n=t.length;e!==n;++e)t[e].unbind()}},$e=class i{constructor(t,e,n){this.path=e,this.parsedPath=n||i.parseTrackName(e),this.node=i.findNode(t,this.parsedPath.nodeName),this.rootNode=t,this.getValue=this._getValue_unbound,this.setValue=this._setValue_unbound}static create(t,e,n){return t&&t.isAnimationObjectGroup?new i.Composite(t,e,n):new i(t,e,n)}static sanitizeNodeName(t){return t.replace(/\s/g,"_").replace(Lx,"")}static parseTrackName(t){let e=Bx.exec(t);if(e===null)throw new Error("PropertyBinding: Cannot parse trackName: "+t);let n={nodeName:e[2],objectName:e[3],objectIndex:e[4],propertyName:e[5],propertyIndex:e[6]},s=n.nodeName&&n.nodeName.lastIndexOf(".");if(s!==void 0&&s!==-1){let r=n.nodeName.substring(s+1);zx.indexOf(r)!==-1&&(n.nodeName=n.nodeName.substring(0,s),n.objectName=r)}if(n.propertyName===null||n.propertyName.length===0)throw new Error("PropertyBinding: can not parse propertyName from trackName: "+t);return n}static findNode(t,e){if(e===void 0||e===""||e==="."||e===-1||e===t.name||e===t.uuid)return t;if(t.skeleton){let n=t.skeleton.getBoneByName(e);if(n!==void 0)return n}if(t.children){let n=function(r){for(let a=0;a<r.length;a++){let o=r[a];if(o.name===e||o.uuid===e)return o;let c=n(o.children);if(c)return c}return null},s=n(t.children);if(s)return s}return null}_getValue_unavailable(){}_setValue_unavailable(){}_getValue_direct(t,e){t[e]=this.targetObject[this.propertyName]}_getValue_array(t,e){let n=this.resolvedProperty;for(let s=0,r=n.length;s!==r;++s)t[e++]=n[s]}_getValue_arrayElement(t,e){t[e]=this.resolvedProperty[this.propertyIndex]}_getValue_toArray(t,e){this.resolvedProperty.toArray(t,e)}_setValue_direct(t,e){this.targetObject[this.propertyName]=t[e]}_setValue_direct_setNeedsUpdate(t,e){this.targetObject[this.propertyName]=t[e],this.targetObject.needsUpdate=!0}_setValue_direct_setMatrixWorldNeedsUpdate(t,e){this.targetObject[this.propertyName]=t[e],this.targetObject.matrixWorldNeedsUpdate=!0}_setValue_array(t,e){let n=this.resolvedProperty;for(let s=0,r=n.length;s!==r;++s)n[s]=t[e++]}_setValue_array_setNeedsUpdate(t,e){let n=this.resolvedProperty;for(let s=0,r=n.length;s!==r;++s)n[s]=t[e++];this.targetObject.needsUpdate=!0}_setValue_array_setMatrixWorldNeedsUpdate(t,e){let n=this.resolvedProperty;for(let s=0,r=n.length;s!==r;++s)n[s]=t[e++];this.targetObject.matrixWorldNeedsUpdate=!0}_setValue_arrayElement(t,e){this.resolvedProperty[this.propertyIndex]=t[e]}_setValue_arrayElement_setNeedsUpdate(t,e){this.resolvedProperty[this.propertyIndex]=t[e],this.targetObject.needsUpdate=!0}_setValue_arrayElement_setMatrixWorldNeedsUpdate(t,e){this.resolvedProperty[this.propertyIndex]=t[e],this.targetObject.matrixWorldNeedsUpdate=!0}_setValue_fromArray(t,e){this.resolvedProperty.fromArray(t,e)}_setValue_fromArray_setNeedsUpdate(t,e){this.resolvedProperty.fromArray(t,e),this.targetObject.needsUpdate=!0}_setValue_fromArray_setMatrixWorldNeedsUpdate(t,e){this.resolvedProperty.fromArray(t,e),this.targetObject.matrixWorldNeedsUpdate=!0}_getValue_unbound(t,e){this.bind(),this.getValue(t,e)}_setValue_unbound(t,e){this.bind(),this.setValue(t,e)}bind(){let t=this.node,e=this.parsedPath,n=e.objectName,s=e.propertyName,r=e.propertyIndex;if(t||(t=i.findNode(this.rootNode,e.nodeName),this.node=t),this.getValue=this._getValue_unavailable,this.setValue=this._setValue_unavailable,!t){console.warn("THREE.PropertyBinding: No target node found for track: "+this.path+".");return}if(n){let l=e.objectIndex;switch(n){case"materials":if(!t.material){console.error("THREE.PropertyBinding: Can not bind to material as node does not have a material.",this);return}if(!t.material.materials){console.error("THREE.PropertyBinding: Can not bind to material.materials as node.material does not have a materials array.",this);return}t=t.material.materials;break;case"bones":if(!t.skeleton){console.error("THREE.PropertyBinding: Can not bind to bones as node does not have a skeleton.",this);return}t=t.skeleton.bones;for(let h=0;h<t.length;h++)if(t[h].name===l){l=h;break}break;case"map":if("map"in t){t=t.map;break}if(!t.material){console.error("THREE.PropertyBinding: Can not bind to material as node does not have a material.",this);return}if(!t.material.map){console.error("THREE.PropertyBinding: Can not bind to material.map as node.material does not have a map.",this);return}t=t.material.map;break;default:if(t[n]===void 0){console.error("THREE.PropertyBinding: Can not bind to objectName of node undefined.",this);return}t=t[n]}if(l!==void 0){if(t[l]===void 0){console.error("THREE.PropertyBinding: Trying to bind to objectIndex of objectName, but is undefined.",this,t);return}t=t[l]}}let a=t[s];if(a===void 0){let l=e.nodeName;console.error("THREE.PropertyBinding: Trying to update property for track: "+l+"."+s+" but it wasn't found.",t);return}let o=this.Versioning.None;this.targetObject=t,t.needsUpdate!==void 0?o=this.Versioning.NeedsUpdate:t.matrixWorldNeedsUpdate!==void 0&&(o=this.Versioning.MatrixWorldNeedsUpdate);let c=this.BindingType.Direct;if(r!==void 0){if(s==="morphTargetInfluences"){if(!t.geometry){console.error("THREE.PropertyBinding: Can not bind to morphTargetInfluences because node does not have a geometry.",this);return}if(!t.geometry.morphAttributes){console.error("THREE.PropertyBinding: Can not bind to morphTargetInfluences because node does not have a geometry.morphAttributes.",this);return}t.morphTargetDictionary[r]!==void 0&&(r=t.morphTargetDictionary[r])}c=this.BindingType.ArrayElement,this.resolvedProperty=a,this.propertyIndex=r}else a.fromArray!==void 0&&a.toArray!==void 0?(c=this.BindingType.HasFromToArray,this.resolvedProperty=a):Array.isArray(a)?(c=this.BindingType.EntireArray,this.resolvedProperty=a):this.propertyName=s;this.getValue=this.GetterByBindingType[c],this.setValue=this.SetterByBindingTypeAndVersioning[c][o]}unbind(){this.node=null,this.getValue=this._getValue_unbound,this.setValue=this._setValue_unbound}};$e.Composite=Rl;$e.prototype.BindingType={Direct:0,EntireArray:1,ArrayElement:2,HasFromToArray:3};$e.prototype.Versioning={None:0,NeedsUpdate:1,MatrixWorldNeedsUpdate:2};$e.prototype.GetterByBindingType=[$e.prototype._getValue_direct,$e.prototype._getValue_array,$e.prototype._getValue_arrayElement,$e.prototype._getValue_toArray];$e.prototype.SetterByBindingTypeAndVersioning=[[$e.prototype._setValue_direct,$e.prototype._setValue_direct_setNeedsUpdate,$e.prototype._setValue_direct_setMatrixWorldNeedsUpdate],[$e.prototype._setValue_array,$e.prototype._setValue_array_setNeedsUpdate,$e.prototype._setValue_array_setMatrixWorldNeedsUpdate],[$e.prototype._setValue_arrayElement,$e.prototype._setValue_arrayElement_setNeedsUpdate,$e.prototype._setValue_arrayElement_setMatrixWorldNeedsUpdate],[$e.prototype._setValue_fromArray,$e.prototype._setValue_fromArray_setNeedsUpdate,$e.prototype._setValue_fromArray_setMatrixWorldNeedsUpdate]];var Vx=new Float32Array(1);var La=class{constructor(t,e,n=0,s=1/0){this.ray=new Xr(t,e),this.near=n,this.far=s,this.camera=null,this.layers=new Yr,this.params={Mesh:{},Line:{threshold:1},LOD:{},Points:{threshold:1},Sprite:{}}}set(t,e){this.ray.set(t,e)}setFromCamera(t,e){e.isPerspectiveCamera?(this.ray.origin.setFromMatrixPosition(e.matrixWorld),this.ray.direction.set(t.x,t.y,.5).unproject(e).sub(this.ray.origin).normalize(),this.camera=e):e.isOrthographicCamera?(this.ray.origin.set(t.x,t.y,(e.near+e.far)/(e.near-e.far)).unproject(e),this.ray.direction.set(0,0,-1).transformDirection(e.matrixWorld),this.camera=e):console.error("THREE.Raycaster: Unsupported camera type: "+e.type)}intersectObject(t,e=!0,n=[]){return Cl(t,this,n,e),n.sort(lf),n}intersectObjects(t,e=!0,n=[]){for(let s=0,r=t.length;s<r;s++)Cl(t[s],this,n,e);return n.sort(lf),n}};function lf(i,t){return i.distance-t.distance}function Cl(i,t,e,n){if(i.layers.test(t.layers)&&i.raycast(t,e),n===!0){let s=i.children;for(let r=0,a=s.length;r<a;r++)Cl(s[r],t,e,!0)}}typeof __THREE_DEVTOOLS__!="undefined"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("register",{detail:{revision:"160"}}));typeof window!="undefined"&&(window.__THREE__?console.warn("WARNING: Multiple instances of Three.js being imported."):window.__THREE__="160");function Ls(i,t=!1){let e=i[0].index!==null,n=new Set(Object.keys(i[0].attributes)),s=new Set(Object.keys(i[0].morphAttributes)),r={},a={},o=i[0].morphTargetsRelative,c=new Ke,l=0;for(let h=0;h<i.length;++h){let f=i[h],d=0;if(e!==(f.index!==null))return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed with geometry at index "+h+". All geometries must have compatible attributes; make sure index attribute exists among all geometries, or in none of them."),null;for(let p in f.attributes){if(!n.has(p))return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed with geometry at index "+h+'. All geometries must have compatible attributes; make sure "'+p+'" attribute exists among all geometries, or in none of them.'),null;r[p]===void 0&&(r[p]=[]),r[p].push(f.attributes[p]),d++}if(d!==n.size)return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed with geometry at index "+h+". Make sure all geometries have the same number of attributes."),null;if(o!==f.morphTargetsRelative)return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed with geometry at index "+h+". .morphTargetsRelative must be consistent throughout all geometries."),null;for(let p in f.morphAttributes){if(!s.has(p))return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed with geometry at index "+h+".  .morphAttributes must be consistent throughout all geometries."),null;a[p]===void 0&&(a[p]=[]),a[p].push(f.morphAttributes[p])}if(t){let p;if(e)p=f.index.count;else if(f.attributes.position!==void 0)p=f.attributes.position.count;else return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed with geometry at index "+h+". The geometry must have either an index or a position attribute"),null;c.addGroup(l,p,h),l+=p}}if(e){let h=0,f=[];for(let d=0;d<i.length;++d){let p=i[d].index;for(let x=0;x<p.count;++x)f.push(p.getX(x)+h);h+=i[d].attributes.position.count}c.setIndex(f)}for(let h in r){let f=Nf(r[h]);if(!f)return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed while trying to merge the "+h+" attribute."),null;c.setAttribute(h,f)}for(let h in a){let f=a[h][0].length;if(f===0)break;c.morphAttributes=c.morphAttributes||{},c.morphAttributes[h]=[];for(let d=0;d<f;++d){let p=[];for(let S=0;S<a[h].length;++S)p.push(a[h][S][d]);let x=Nf(p);if(!x)return console.error("THREE.BufferGeometryUtils: .mergeGeometries() failed while trying to merge the "+h+" morphAttribute."),null;c.morphAttributes[h].push(x)}}return c}function Nf(i){let t,e,n,s=-1,r=0;for(let l=0;l<i.length;++l){let h=i[l];if(h.isInterleavedBufferAttribute)return console.error("THREE.BufferGeometryUtils: .mergeAttributes() failed. InterleavedBufferAttributes are not supported."),null;if(t===void 0&&(t=h.array.constructor),t!==h.array.constructor)return console.error("THREE.BufferGeometryUtils: .mergeAttributes() failed. BufferAttribute.array must be of consistent array types across matching attributes."),null;if(e===void 0&&(e=h.itemSize),e!==h.itemSize)return console.error("THREE.BufferGeometryUtils: .mergeAttributes() failed. BufferAttribute.itemSize must be consistent across matching attributes."),null;if(n===void 0&&(n=h.normalized),n!==h.normalized)return console.error("THREE.BufferGeometryUtils: .mergeAttributes() failed. BufferAttribute.normalized must be consistent across matching attributes."),null;if(s===-1&&(s=h.gpuType),s!==h.gpuType)return console.error("THREE.BufferGeometryUtils: .mergeAttributes() failed. BufferAttribute.gpuType must be consistent across matching attributes."),null;r+=h.array.length}let a=new t(r),o=0;for(let l=0;l<i.length;++l)a.set(i[l].array,o),o+=i[l].array.length;let c=new Mn(a,e,n);return s!==void 0&&(c.gpuType=s),c}var vr=class i extends Ne{constructor(){let t=i.SkyShader,e=new Sn({name:t.name,uniforms:Fl.clone(t.uniforms),vertexShader:t.vertexShader,fragmentShader:t.fragmentShader,side:Tn,depthWrite:!1});super(new Pe(1,1,1),e),this.isSky=!0}};vr.SkyShader={name:"SkyShader",uniforms:{turbidity:{value:2},rayleigh:{value:1},mieCoefficient:{value:.005},mieDirectionalG:{value:.8},sunPosition:{value:new O},up:{value:new O(0,1,0)}},vertexShader:`
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

		}`};var yr={gate:[[55,4],[10,2.5,-4]],hall:[[-13.4,-11.2],[-28,2.3,-12]],hearth:[[-16.4,-14.6],[-19.6,.5,-12]],seat:[[-23.2,-12],[-28,2.1,-12]],chamber:[[-4.6,-18.2],[3.2,.9,-21.6]],kitchen:[[-20.6,14.6],[-27,1.1,13.6]],stables:[[10,12.5],[6,1.6,23]],wall:[[60,-44],[19300,950,10400]],sands:[[-50,44],[-2600,-52,3600]]},os=[228,17],Oa=48.9,Hi=32e3;function kx(i){return function(){i|=0,i=i+1831565813|0;let t=Math.imul(i^i>>>15,1|i);return t=t+Math.imul(t^t>>>7,61|t)^t,((t^t>>>14)>>>0)/4294967296}}var Us=(i,t,e)=>{let n=Math.max(0,Math.min(1,(e-i)/(t-i)));return n*n*(3-2*n)},On=(i,t,e)=>Math.max(t,Math.min(e,i));async function ev(i,t){let e=!!t.cy,n=u=>e?u[1]:u[0],s=Math.min(screen.width,screen.height)<=600,r=matchMedia("(pointer: coarse)").matches,a=matchMedia("(prefers-reduced-motion: reduce)").matches,o=kx(1237),c=u=>new URL(u,document.baseURI).href,l=document.createElement("canvas");l.className="ll-canvas",l.tabIndex=0,l.setAttribute("role","img"),l.setAttribute("aria-label",n(t.ui.canvas)),i.appendChild(l);let h;try{h=new Zr({canvas:l,antialias:!s,powerPreference:"high-performance",logarithmicDepthBuffer:!0})}catch{i.classList.add("fail"),l.remove();return}let f=Math.min(devicePixelRatio||1,s?1.6:2),d=s?Math.min(f,1.25):f;h.setPixelRatio(d),h.outputColorSpace=sn,h.toneMapping=Il,h.toneMappingExposure=.62,h.shadowMap.enabled=!0,h.shadowMap.type=Pl;let p=Math.min(8,h.capabilities.getMaxAnisotropy()),x={grass:s?2600:9e3,fireShadow:!s,shadow:s?1024:2048},S=s?"-m":"",_=new Ra,m=(u,g)=>new Promise((y,v)=>_.load(c(u),E=>{g&&(E.colorSpace=sn),E.anisotropy=p,y(E)},void 0,v)),T=u=>new Promise((g,y)=>{let v=new Image;v.onload=()=>g(v),v.onerror=y,v.src=c(u)}),M;try{M=await Promise.all([T("llys-h.png"),m(`llys-n${S}.webp`),m(`llys-c${S}.webp`,!0),m(`stone${S}.webp`,!0),m(`stone-n${S}.webp`)])}catch{i.classList.add("fail"),l.remove();return}let[U,W,F,B,J]=M,w=U.width,L=document.createElement("canvas");L.width=L.height=w;let $=L.getContext("2d",{willReadFrequently:!0});$.drawImage(U,0,0);let ot=$.getImageData(0,0,w,w).data,Mt=new Float32Array(w*w);for(let u=0;u<w*w;u++)Mt[u]=(ot[u*4]*256+ot[u*4+1])/20-50;function X(u,g){let y=On((u+Hi)/(2*Hi)*w-.5,0,w-1.001),v=On((g+Hi)/(2*Hi)*w-.5,0,w-1.001),E=Math.floor(y),A=Math.floor(v),D=y-E,N=v-A,I=A*w+E;return Mt[I]*(1-D)*(1-N)+Mt[I+1]*D*(1-N)+Mt[I+w]*(1-D)*N+Mt[I+w+1]*D*N}let K=u=>u*u/(2*6371e3*1.15);function tt(u,g){let y=Math.hypot(u,g),E=(.6*Math.sin(u*.031+1.3)*Math.cos(g*.027)+.35*Math.sin(u*.07+g*.05)+.15*Math.sin(u*.19-g*.13))*Us(48,110,Math.max(Math.abs(u)*1.25,Math.abs(g)*1.6)),A=Us(220,760,y);return E*(1-A)+(X(u,g)-Oa)*A-K(y)}let it=new $r,ft=new fe(9676733);it.fog=new xa(ft,21e-6);let nt=new wn(s?68:60,1,.1,8e4);nt.rotation.order="YXZ";let ct=u=>{let g=document.createElement("canvas");return g.width=g.height=u,[g,g.getContext("2d")]};function lt(u,g,y=!0){let v=new ya(u);return v.wrapS=v.wrapT=bs,v.anisotropy=p,y&&(v.colorSpace=sn),g&&v.repeat.set(g[0],g[1]),v}function Dt(u,g=2){let y=u.width,v=u.getContext("2d").getImageData(0,0,y,y).data,[E,A]=ct(y),D=A.createImageData(y,y),N=D.data,I=(V,H)=>v[((H+y)%y*y+(V+y)%y)*4]/255;for(let V=0;V<y;V++)for(let H=0;H<y;H++){let G=(I(H+1,V)-I(H-1,V))*g,Q=(I(H,V+1)-I(H,V-1))*g,vt=Math.hypot(G,Q,1),pt=(V*y+H)*4;N[pt]=(-G/vt*.5+.5)*255,N[pt+1]=(Q/vt*.5+.5)*255,N[pt+2]=(1/vt*.5+.5)*255,N[pt+3]=255}return A.putImageData(D,0,0),lt(E,null,!1)}let st=(u,g,y,v,E,A,D,N)=>{for(let I=0;I<y;I++){u.fillStyle=`rgba(${v},${E+o()*(A-E)})`;let V=D+o()*(N-D);u.fillRect(o()*g,o()*g,V,V)}},ut=(u,g,y,v,E,A,D)=>{for(let N=0;N<y;N++){let I=o()*g,V=o()*g,H=A+o()*(D-A);for(let G of[-g,0,g])for(let Q of[-g,0,g]){let vt=u.createRadialGradient(I+G,V+Q,0,I+G,V+Q,H);vt.addColorStop(0,`rgba(${v},${E})`),vt.addColorStop(1,`rgba(${v},0)`),u.fillStyle=vt,u.fillRect(I+G-H,V+Q-H,2*H,2*H)}}},[Nt,Ft]=ct(512);Ft.fillStyle="#e8e2d4",Ft.fillRect(0,0,512,512),ut(Ft,512,60,"214,205,186",.35,30,120),ut(Ft,512,40,"246,243,236",.5,20,90),ut(Ft,512,14,"180,178,160",.12,40,140),st(Ft,512,5e3,"120,110,95",.02,.1,1,3);for(let u=0;u<70;u++){Ft.strokeStyle=`rgba(150,140,120,${.03+o()*.05})`,Ft.lineWidth=1+o()*3;let g=o()*512,y=o()*512;Ft.beginPath(),Ft.moveTo(g,y),Ft.lineTo(g+(o()-.5)*6,y+40+o()*90),Ft.stroke()}let Bt=lt(Nt),[se,Jt]=ct(256);Jt.drawImage(Nt,0,0,256,256),Jt.strokeStyle="rgba(150,48,30,.85)",Jt.lineWidth=2.2;for(let u=0;u<4;u++){Jt.beginPath(),Jt.moveTo(0,u*64+1),Jt.lineTo(256,u*64+1),Jt.stroke();for(let g=0;g<3;g++){let y=g*96+u%2*48;Jt.beginPath(),Jt.moveTo(y,u*64),Jt.lineTo(y,u*64+64),Jt.stroke()}}let Wt=lt(se),[le,z]=ct(512),[Tt,rt]=ct(512);z.fillStyle="#6d5a3e",z.fillRect(0,0,512,512),rt.fillStyle="#555",rt.fillRect(0,0,512,512);for(let u=0;u<9e3;u++){let g=o()*512,y=o()*512,v=18+o()*34,E=.6+o()*1.6,A=o(),D=A<.45?[118+o()*40,100+o()*30,70+o()*20]:A<.85?[150+o()*50,122+o()*35,72+o()*25]:[110,108,100];for(let N of[-512,0,512])for(let I of[-512,0,512]){z.strokeStyle=`rgba(${D[0]|0},${D[1]|0},${D[2]|0},.75)`,z.lineWidth=E,z.beginPath(),z.moveTo(g+N,y+I),z.lineTo(g+N+(o()-.5)*3,y+I+v),z.stroke();let V=110+A*120;rt.strokeStyle=`rgba(${V},${V},${V},.7)`,rt.lineWidth=E,rt.beginPath(),rt.moveTo(g+N,y+I),rt.lineTo(g+N+(o()-.5)*3,y+I+v),rt.stroke()}}for(let u=0;u<512;u+=64){let g=z.createLinearGradient(0,u,0,u+64);g.addColorStop(0,"rgba(30,22,12,.0)"),g.addColorStop(.85,"rgba(30,22,12,.12)"),g.addColorStop(1,"rgba(30,22,12,.4)"),z.fillStyle=g,z.fillRect(0,u,512,64);let y=rt.createLinearGradient(0,u,0,u+64);y.addColorStop(0,"rgba(255,255,255,.15)"),y.addColorStop(1,"rgba(0,0,0,.45)"),rt.fillStyle=y,rt.fillRect(0,u,512,64)}ut(z,512,16,"70,72,60",.25,30,90);let bt=lt(le),ht=Dt(Tt,3),[qt,It]=ct(256);It.fillStyle="#2a2119",It.fillRect(0,0,256,256);for(let u=0;u<2500;u++){let g=30+o()*45;It.strokeStyle=`rgba(${g+10},${g},${g-8},.6)`,It.lineWidth=.5+o();let y=o()*256,v=o()*256;It.beginPath(),It.moveTo(y,v),It.lineTo(y+(o()-.5)*2,v+10+o()*16),It.stroke()}let R=lt(qt),[b,Y]=ct(512),[xt,mt]=ct(512);Y.fillStyle="#6a5440",Y.fillRect(0,0,512,512),mt.fillStyle="#808080",mt.fillRect(0,0,512,512);for(let u=0;u<700;u++){let g=o()*512,y=o()<.2?50:25,v=.08+o()*.25,E=.5+o()*2.5,A=(o()-.5)*16;Y.strokeStyle=`rgba(${y+20},${y+8},${y-5},${v})`,mt.strokeStyle=`rgba(40,40,40,${v})`,Y.lineWidth=mt.lineWidth=E;for(let D of[Y,mt])for(let N of[-512,0,512])D.beginPath(),D.moveTo(0,g+N),D.bezierCurveTo(170,g+N+A,340,g+N-A,512,g+N),D.stroke()}ut(Y,512,20,"140,118,92",.18,20,80),ut(Y,512,12,"40,30,22",.2,10,50);for(let u=0;u<26;u++){let g=o()*512,y=o()*512;Y.fillStyle="rgba(35,25,15,.5)",Y.beginPath(),Y.ellipse(g,y,5+o()*6,2+o()*3,0,0,7),Y.fill()}let gt=lt(b),Gt=Dt(xt,1.5),[Lt,At]=ct(256);At.fillStyle="#e6dfcf",At.fillRect(0,0,256,256),At.fillStyle="#93331f";for(let u=-1;u<5;u++){let g=u*64;At.beginPath(),At.moveTo(0,g),At.lineTo(128,g+40),At.lineTo(256,g),At.lineTo(256,g+32),At.lineTo(128,g+72),At.lineTo(0,g+32),At.closePath(),At.fill()}At.globalAlpha=.25,At.drawImage(b,0,0,256,256),At.globalAlpha=1,st(At,256,900,"60,40,30",.03,.12,1,3);let ee=lt(Lt),[pe,dt]=ct(512);dt.fillStyle="#4e3f2e",dt.fillRect(0,0,512,512),ut(dt,512,50,"70,58,42",.5,20,70),ut(dt,512,30,"38,30,22",.45,15,60);for(let u=0;u<2600;u++){let g=o()*512,y=o()*512,v=o()*Math.PI,E=14+o()*30,A=o();dt.strokeStyle=A<.6?`rgba(${150+o()*40},${140+o()*30},${70+o()*20},.75)`:`rgba(${90+o()*30},${110+o()*30},50,.7)`,dt.lineWidth=.8+o()*1.4,dt.beginPath(),dt.moveTo(g,y),dt.lineTo(g+Math.cos(v)*E,y+Math.sin(v)*E),dt.stroke()}let Re=lt(pe),[Se,Zt]=ct(512);Zt.fillStyle="#58693c",Zt.fillRect(0,0,512,512),ut(Zt,512,40,"90,104,58",.45,20,80),ut(Zt,512,30,"66,80,42",.4,20,70),ut(Zt,512,10,"120,120,60",.25,30,90);for(let u=0;u<16e3;u++){let g=o()*512,y=o()*512,v=o();Zt.strokeStyle=v<.5?`rgba(${76+o()*44},${96+o()*40},${42+o()*20},.55)`:v<.9?`rgba(${40+o()*30},${60+o()*30},20,.5)`:`rgba(${150+o()*40},${150+o()*30},90,.5)`,Zt.lineWidth=.7+o(),Zt.beginPath(),Zt.moveTo(g,y),Zt.lineTo(g+(o()-.5)*5,y-4-o()*8),Zt.stroke()}let Kt=lt(Se),[Ht,ae]=ct(256);ae.fillStyle="#6b5a44",ae.fillRect(0,0,256,256),ut(ae,256,40,"92,78,58",.5,10,40),ut(ae,256,20,"60,50,38",.5,10,30),st(ae,256,3e3,"150,140,120",.1,.4,1,3),st(ae,256,1500,"40,32,24",.1,.4,1,2);let Ie=lt(Ht),[Ye,te]=ct(512),wt=160,k=u=>(u+wt/2)/wt*512;te.fillStyle="#000",te.fillRect(0,0,512,512),te.lineCap="round",te.lineJoin="round",te.strokeStyle="rgba(255,255,255,.9)";let Rt=(u,g)=>{te.lineWidth=g/wt*512,te.beginPath(),u.forEach(([y,v],E)=>E?te.lineTo(k(y),k(v)):te.moveTo(k(y),k(v))),te.stroke()};Rt([[75,6],[44,1],[20,2],[0,-2],[-14.5,-5.5]],4.2),Rt([[0,-2],[-4,-15.5]],2.6),Rt([[20,2],[10,14],[8,19.5]],3.2),Rt([[0,-2],[-12,8],[-18.5,13.5]],2.8),Rt([[20,2],[22,-15.5]],3),Rt([[20,2],[30,11]],2),Rt([[8,2.5],[8,2.5]],7);for(let[u,g,y]of[[42,1,7],[-14.5,-5,4],[-14.5,-18.5,3.5],[8,19,6],[-18,14,4],[22,-15,5]]){let v=te.createRadialGradient(k(u),k(g),0,k(u),k(g),y/wt*512);v.addColorStop(0,"rgba(255,255,255,.85)"),v.addColorStop(1,"rgba(255,255,255,0)"),te.fillStyle=v,te.fillRect(0,0,512,512)}let Ut=te.getImageData(0,0,512,512).data,re=(u,g)=>{let y=On(Math.round(k(u)),0,511),v=On(Math.round(k(g)),0,511);return Ut[(v*512+y)*4]/255},jt=lt(Ye,null,!1);jt.wrapS=jt.wrapT=Ln,jt.flipY=!1;function De(u,g,y,v){let[E,A]=ct(256);A.fillStyle=u,A.fillRect(0,0,256,256);for(let D=0;D<4;D++)for(let N=0;N<4;N++){let I=32+N*64,V=32+D*64;A.fillStyle=g,A.beginPath(),A.moveTo(I,V-26),A.lineTo(I+26,V),A.lineTo(I,V+26),A.lineTo(I-26,V),A.closePath(),A.fill(),A.fillStyle=u,A.beginPath(),A.moveTo(I,V-20),A.lineTo(I+20,V),A.lineTo(I,V+20),A.lineTo(I-20,V),A.closePath(),A.fill(),A.fillStyle=y,v==="cross"?(A.fillRect(I-3,V-12,6,24),A.fillRect(I-12,V-3,24,6)):(A.beginPath(),A.arc(I,V,8,0,7),A.fill(),A.fillStyle=g,A.beginPath(),A.arc(I,V,3.5,0,7),A.fill())}for(let D=0;D<2600;D++)A.fillStyle=`rgba(0,0,0,${o()*.08})`,A.fillRect(o()*256,o()*256,1,3);return lt(E)}let Fe=De("#7d1d1a","#c9962e","#2f5a3a","cross"),rn=De("#2c4a35","#c9962e","#8e2a20","ring"),[xn,Ce]=ct(128);Ce.fillStyle="#d8d1c0",Ce.fillRect(0,0,128,128);for(let u=0;u<128;u+=2)Ce.fillStyle="rgba(160,150,130,.12)",Ce.fillRect(u,0,1,128),Ce.fillRect(0,u,128,1);ut(Ce,128,6,"200,190,170",.25,10,30);let fn=lt(xn),[Gn,as]=ct(512);function Ba(u,g,y,v,E,A){u.save(),u.translate(g,y),u.scale(v,v),u.fillStyle=E,u.strokeStyle=E,u.lineCap="round",u.lineJoin="round",u.beginPath(),u.moveTo(-34,-6),u.bezierCurveTo(-30,-16,10,-16,20,-12),u.bezierCurveTo(26,-10,28,-2,24,6),u.bezierCurveTo(10,10,-20,10,-32,6),u.closePath(),u.fill(),u.beginPath(),u.arc(24,-18,11,0,7),u.fill(),u.beginPath();for(let D=0;D<18;D++){let N=D%2?12:17,I=D/18*Math.PI*2;u.lineTo(24+Math.cos(I)*N,-18+Math.sin(I)*N)}u.closePath(),u.fill(),u.lineWidth=6,[[-26,4,-32,26],[-16,6,-14,26],[10,6,8,26],[20,2,34,6]].forEach(([D,N,I,V])=>{u.beginPath(),u.moveTo(D,N),u.lineTo(I,V),u.stroke()}),u.lineWidth=4,u.beginPath(),u.moveTo(-33,-4),u.bezierCurveTo(-52,-10,-46,-40,-30,-36),u.stroke(),u.beginPath(),u.moveTo(-30,-36),u.lineTo(-20,-44),u.lineTo(-24,-30),u.closePath(),u.fill(),u.fillStyle=A,u.beginPath(),u.arc(20,-20,2.4,0,7),u.arc(28,-20,2.4,0,7),u.fill(),u.fillRect(19,-12,10,2),u.restore()}let Mi="#d4a22a",cs="#a51f1b";[[0,0,Mi,cs],[256,0,cs,Mi],[0,256,cs,Mi],[256,256,Mi,cs]].forEach(([u,g,y,v])=>{as.fillStyle=y,as.fillRect(u,g,256,256),Ba(as,u+128,g+140,2.9,v,y)}),st(as,512,4e3,"0,0,0",.02,.08,1,3);let Ds=lt(Gn),Si=1800,[ho,He]=ct(1024),Vn=u=>(u+Si/2)/Si*1024,uo=[];{let g=Si/14,y=[];for(let E=0;E<15;E++){y.push([]);for(let A=0;A<15;A++)y[E].push([-Si/2+E*g+(E&&E<14?(o()-.5)*g*.5:0),-Si/2+A*g+(A&&A<14?(o()-.5)*g*.5:0)])}He.fillStyle="#5b7a36",He.fillRect(0,0,1024,1024);let v=[["#587a34",0],["#62843a",0],["#4f6f2e",0],["#a39a52",1],["#b4a65c",1],["#8c9248",1],["#7b8a44",2],["#7a6648",3]];for(let E=0;E<14;E++)for(let A=0;A<14;A++){let D=[y[E][A],y[E+1][A],y[E+1][A+1],y[E][A+1]],N=D.reduce((G,Q)=>G+Q[0],0)/4,I=D.reduce((G,Q)=>G+Q[1],0)/4;if(Math.hypot(N,I)<110)continue;let[V,H]=v[Math.floor(o()*v.length)];if(He.save(),He.beginPath(),D.forEach(([G,Q],vt)=>vt?He.lineTo(Vn(G),Vn(Q)):He.moveTo(Vn(G),Vn(Q))),He.closePath(),He.clip(),He.fillStyle=V,He.fillRect(0,0,1024,1024),H===1||H===3){let G=Math.atan2(D[1][1]-D[0][1],D[1][0]-D[0][0])+(o()<.5?0:Math.PI/2);He.translate(Vn(N),Vn(I)),He.rotate(G);for(let Q=-40;Q<40;Q++)He.fillStyle=`rgba(${o()<.5?"255,240,200":"40,50,20"},${.04+o()*.1})`,He.fillRect(-200,Q*5.7,400,5.7*(.5+o()*.5))}He.restore(),He.strokeStyle="rgba(48,58,30,.9)",He.lineWidth=2.2,He.beginPath(),D.forEach(([G,Q],vt)=>vt?He.lineTo(Vn(G),Vn(Q)):He.moveTo(Vn(G),Vn(Q))),He.closePath(),He.stroke(),uo.push(D)}ut(He,1024,70,"120,110,70",.08,20,80),ut(He,1024,60,"30,50,20",.08,20,70)}let P=lt(ho,null);P.wrapS=P.wrapT=Ln,P.flipY=!1;let[Z,j]=ct(128);j.fillStyle="#cfc6b2",j.fillRect(0,0,128,128);for(let u=0;u<900;u++){let g=o()*128,y=o()*128,v=1.5+o()*3,E=o();j.strokeStyle=E<.5?"rgba(255,250,236,.55)":"rgba(120,108,88,.45)",j.lineWidth=.8+o(),j.beginPath(),j.arc(g,y,v,o()*6,o()*6+3.5),j.stroke()}let et=lt(Z),q=u=>new Qn(Object.assign({roughness:.9,vertexColors:!0},u)),C={stone:q({map:B,normalMap:J,normalScale:new St(1.1,1.1),roughness:.95}),lime:q({map:Bt,normalMap:J,normalScale:new St(.45,.45),roughness:.93}),ash:q({map:Wt,normalMap:J,normalScale:new St(.25,.25)}),thatch:q({map:bt,normalMap:ht,normalScale:new St(1.4,1.4),roughness:1}),soot:q({map:R,roughness:1}),oak:q({map:gt,normalMap:Gt,roughness:.8}),chev:q({map:ee,normalMap:Gt,normalScale:new St(.4,.4),roughness:.75}),floor:q({map:Re,roughness:1}),linen:q({map:fn,roughness:.95}),hangR:q({map:Fe,roughness:.95,side:ln}),hangG:q({map:rn,roughness:.95,side:ln}),arms:q({map:Ds,roughness:.9,side:ln}),red:q({color:9052186,roughness:.9}),green:q({color:3034419,roughness:.9}),iron:q({color:2828840,roughness:.55,metalness:.7}),gold:q({color:13146666,roughness:.35,metalness:.85}),clay:q({color:10185285,roughness:.8}),glaze:q({color:7305781,roughness:.35}),horn:q({color:10519631,roughness:.45}),straw:q({map:bt,color:14205066,roughness:1}),wattle:q({map:gt,color:10127986,roughness:1}),daub:q({map:Bt,color:13352870,normalMap:J,normalScale:new St(.3,.3)}),bread:q({color:11039802,roughness:.9}),turf:q({map:Kt,color:12108954,roughness:1}),cloth:q({map:fn,roughness:.95,side:ln}),skin:q({color:13145978,roughness:.62}),coat:q({roughness:.72}),wool:q({map:et,roughness:1})},Xt=Object.values(C);C.stone.map.wrapS=C.stone.map.wrapT=bs,J.wrapS=J.wrapT=bs;let Qt=new Map,ie=[],me=(u,g,y=0)=>ie.find(v=>u>v[0]-y&&u<v[2]+y&&g>v[1]-y&&g<v[3]+y),ue=(u,g,y)=>{let v=u[2]-u[0]>=u[3]-u[1],E=v?(u[3]-u[1])/2:(u[2]-u[0])/2,A=Math.abs(v?y-(u[1]+u[3])/2:g-(u[0]+u[2])/2);return u[4]+(u[5]-u[4])*(1-A/E)};function ge(u,g,y,v,E,A){let D=1,N=u+v*.3,I=g+E*.3,V=y+A*.3,H=me(N,V);if(H&&I<ue(H,N,V)-.2){D*=1-.62*Us(1.6,H[5],g);let G=Math.min(u-H[0],H[2]-u,y-H[1],H[3]-y);D*=.78+.22*Us(0,1.6,G),D*=.86+.14*Us(0,.8,g)}else E<.5&&(D*=.74+.26*Us(0,1.1,g));return D}function yt(u,g,y,v,E){y&&u.applyMatrix4(y),u.index&&(u=u.toNonIndexed()),u.attributes.normal||u.computeVertexNormals(),u.attributes.uv||u.setAttribute("uv",new de(new Float32Array(u.attributes.position.count*2),2));let A=u.attributes.position,D=u.attributes.normal,N=new Float32Array(A.count*3);for(let I=0;I<A.count;I++){let V=v?1:ge(A.getX(I),A.getY(I),A.getZ(I),D.getX(I),D.getY(I),D.getZ(I));N[I*3]=V*(E?E.r:1),N[I*3+1]=V*(E?E.g:1),N[I*3+2]=V*(E?E.b:1)}u.setAttribute("color",new de(N,3));for(let I of Object.keys(u.attributes))["position","normal","uv","color"].includes(I)||u.deleteAttribute(I);u.clearGroups(),Qt.has(g)||Qt.set(g,[]),Qt.get(g).push(u)}let Ot=(u,g,y,v=0,E=0,A=0,D=1)=>new Ue().compose(new O(u,g,y),new kn().setFromEuler(new ss(E,v,A,"YXZ")),new O(D,D,D));function zt(u,g,y,v,E,A,D,N=0,I=2,V=1){let H=new Pe(u,g,y,1,V,1),G=H.attributes.uv,Q=[[y,g],[y,g],[u,y],[u,y],[u,g],[u,g]],vt=G.count/6;for(let pt=0;pt<6;pt++)for(let Yt=0;Yt<vt;Yt++){let _t=pt*vt+Yt;G.setXY(_t,G.getX(_t)*Q[pt][0]/I,G.getY(_t)*Q[pt][1]/I)}yt(H,v,Ot(E,A,D,N))}function en(u,g,y,v,E,A,D,N=8,I=0,V=0,H=0,G=1){let Q=new tn(u,g,y,N,1),vt=Q.attributes.uv;for(let pt=0;pt<vt.count;pt++)vt.setXY(pt,vt.getX(pt)*Math.PI*(u+g)/G,vt.getY(pt)*y/G);yt(Q,v,Ot(E,A,D,V,I,H))}function ke(u){let g=u.index?u.toNonIndexed():u,y=[],v=u.groups.length?u.groups:[{start:0,count:g.attributes.position.count,materialIndex:0}];for(let E of v){let A=new Ke;for(let D of["position","normal","uv"]){let N=g.attributes[D];N&&A.setAttribute(D,new de(N.array.slice(E.start*N.itemSize,(E.start+E.count)*N.itemSize),N.itemSize))}y[E.materialIndex]=y[E.materialIndex]?Ls([y[E.materialIndex],A]):A}return y}let ce=[],dn=[],Le=(u,g,y,v,E=0)=>{let A=Math.cos(E),D=Math.sin(E),N=[[-y/2,-v/2],[y/2,-v/2],[y/2,v/2],[-y/2,v/2]].map(([I,V])=>[u+I*A+V*D,g-I*D+V*A]);for(let I=0;I<4;I++)ce.push([...N[I],...N[(I+1)%4],.05])};function fi(u,g,y){let v=new jn;u.forEach(([N,I],V)=>V?v.lineTo(N,I):v.moveTo(N,I)),v.closePath();for(let N of g){let I=new ws,V=N.at-N.w/2,H=N.at+N.w/2,G=N.y+N.h;I.moveTo(V,N.y),I.lineTo(H,N.y),N.arch?(I.lineTo(H,G-N.w/2),I.absarc(N.at,G-N.w/2,N.w/2,0,Math.PI,!1)):(I.lineTo(H,G),I.lineTo(V,G)),I.closePath(),v.holes.push(I)}let E=new Bi(v,{depth:y,bevelEnabled:!1,curveSegments:12});E.translate(0,0,-y/2);let[A,D]=ke(E);for(let N of[A,D])if(N){let I=N.attributes.uv;for(let V=0;V<I.count;V++)I.setXY(V,I.getX(V)/2.2,I.getY(V)/2.2)}return[A,D]}function ki(u,g,y,v,E,A,D,N=[],I=null,V=C.ash){let H=Math.hypot(y-u,v-g),G=-Math.atan2(v-g,y-u),Q=Ot(u,0,g,G),vt=(at,Ct,kt=0,ne=0,$t=0)=>{at&&yt(at,Ct,Q.clone().multiply(Ot(kt,ne,$t)))},pt=N.filter(at=>!at.y).sort((at,Ct)=>at.at-Ct.at),Yt=N.filter(at=>at.y),_t=Yt.filter(at=>at.y+at.h<=E-.15),Vt=Yt.filter(at=>at.y+at.h>E-.15),ye=0,oe=[];for(let at of pt)oe.push([ye,at.at-at.w/2]),ye=at.at+at.w/2;oe.push([ye,H]);for(let[at,Ct]of oe){if(Ct-at<.02)continue;let[kt,ne]=fi([[0,0],[Ct-at,0],[Ct-at,E],[0,E]],_t.filter($t=>$t.at>at&&$t.at<Ct).map($t=>Object.assign({},$t,{at:$t.at-at})),A);if(vt(kt,D,at),vt(ne,V,at),ce.push([u+(y-u)*at/H,g+(v-g)*at/H,u+(y-u)*Ct/H,g+(v-g)*Ct/H,A/2]),D!==C.stone){let $t=new Pe(Ct-at,.42,A+.14);$t.translate((at+Ct)/2,.21,0);let he=$t.attributes.uv,Ge=Math.max(Ct-at,A)/2.2;for(let Ze=0;Ze<he.count;Ze++)he.setXY(Ze,he.getX(Ze)*Ge,he.getY(Ze)*.2);yt($t,C.stone,Q.clone())}}for(let at of pt){let Ct=at.at-at.w/2,kt=at.at+at.w/2,ne=at.w/2;if(at.arch){let $t=new jn;$t.moveTo(Ct,at.h-ne),$t.absarc(at.at,at.h-ne,ne,Math.PI,0,!0),$t.lineTo(kt,E),$t.lineTo(Ct,E),$t.closePath();let he=new Bi($t,{depth:A,bevelEnabled:!1,curveSegments:12});he.translate(0,0,-A/2);let[Ge,Ze]=ke(he);for(let Ve of[Ge,Ze]){let We=Ve.attributes.uv;for(let Fn=0;Fn<We.count;Fn++)We.setXY(Fn,We.getX(Fn)/2.2,We.getY(Fn)/2.2)}vt(Ge,D),vt(Ze,V);let on=new jn;on.moveTo(Ct-.3,at.h-ne),on.absarc(at.at,at.h-ne,ne+.3,Math.PI,0,!0),on.lineTo(kt,at.h-ne),on.absarc(at.at,at.h-ne,ne,0,Math.PI,!1),on.closePath();let cn=new Bi(on,{depth:A+.04,bevelEnabled:!1,curveSegments:12});cn.translate(0,0,-A/2-.02);let ve=cn.attributes.uv;for(let Ve=0;Ve<ve.count;Ve++)ve.setXY(Ve,ve.getX(Ve)/1.2,ve.getY(Ve)/1.2);yt(cn,D===C.lime?C.ash:C.stone,Q.clone())}else{let $t=new Pe(at.w+.02,E-at.h,A);$t.translate(at.at,at.h+(E-at.h)/2,0),yt($t,D,Q.clone());let he=new Pe(at.w+.5,.2,A+.06);he.translate(at.at,at.h+.1,0),yt(he,C.oak,Q.clone())}if(at.leaf!==!1){let $t=at.w-.04,he=at.arch?at.h-ne*.25:at.h,Ge=-1,Ze=Ge*-1.3,on=Q.clone().multiply(Ot(Ct+.03,0,Ge*(A/2-.06),Ze)),cn=new Pe($t,he,.07);cn.translate($t/2,he/2,0),yt(cn,C.oak,on.clone());for(let ve of[.45,he-.5]){let Ve=new Pe($t*.8,.06,.09);Ve.translate($t*.4,ve,0),yt(Ve,C.iron,on.clone())}}}for(let at of _t.concat(Vt)){for(let Ct of[-1,1]){let kt=new Pe(at.w/2,at.h-at.w/2,.05);kt.translate(-Ct*at.w/4,0,0),yt(kt,C.oak,Q.clone().multiply(Ot(at.at+Ct*at.w/2,at.y+(at.h-at.w/2)/2,-A/2-.04,-Ct*1.35)))}bi.push({x:u+(y-u)*at.at/H,z:g+(v-g)*at.at/H,y:at.y+at.h/2,w:at.w,h:at.h,nx:-(v-g)/H,nz:(y-u)/H})}for(let at of pt)bi.push({x:u+(y-u)*at.at/H,z:g+(v-g)*at.at/H,y:at.h/2,w:at.w,h:at.h,nx:-(v-g)/H,nz:(y-u)/H,door:!0});if(I){let[at,Ct]=I,[kt,ne]=fi([[0,E],[H,E],[H/2+Ct,at],[H/2-Ct,at]],Vt,A);vt(kt,D),vt(ne,V)}return{L:H,ry:G}}let bi=[];function Ns(u,g,y,v,E,A,D,N=!1,I=null){let H=v/2+.55,G=y/2+(N?.55:.35),Q=.42,vt=E-.55*(A-E)/(v/2),pt=A-vt,Yt=Math.hypot(H,pt),_t=N?Math.max(.4,G-H*.95):G,Vt=D?Ot(u,0,g,Math.PI/2):Ot(u,0,g),ye=(Ct,kt,ne,$t,he,Ge)=>{let Ze=new Ke,on=[Ct,kt,ne],cn=he;new O().subVectors(new O(...kt),new O(...Ct)).cross(new O().subVectors(new O(...ne),new O(...Ct))).dot(Ge)<0&&(on=[Ct,ne,kt],cn=[he[0],he[2],he[1]]),Ze.setAttribute("position",new de(on.flat(),3)),Ze.setAttribute("uv",new de(cn.flat(),2)),Ze.computeVertexNormals(),yt(Ze,$t,Vt.clone())};for(let Ct of[1,-1]){let kt=new _n(2,1,10,6),ne=kt.attributes.position,$t=kt.attributes.uv;for(let ve=0;ve<ne.count;ve++){let Ve=ne.getX(ve),We=ne.getY(ve)+.5,Fn=G+(_t-G)*We,Rh=Ve*Fn,td=Math.sin(We*Math.PI)*.09*(1-Math.abs(Ve)*.5)+(o()-.5)*.035;ne.setXYZ(ve,Rh,vt+pt*We-td+Q/2,Ct*H*(1-We)),$t.setXY(ve,Rh/1.6,We*Yt/1.6)}Ct<0&&kt.index.array.reverse(),kt.computeVertexNormals(),yt(kt,C.thatch,Vt.clone());let he=new _n(2,1,1,4),Ge=he.attributes.position,Ze=he.attributes.uv;for(let ve=0;ve<Ge.count;ve++){let Ve=Ge.getX(ve),We=Ge.getY(ve)+.5,Fn=Ve*(G-.1+(_t-G)*We);Ge.setXYZ(ve,Fn,vt+pt*We-Q/2,Ct*(H-.05)*(1-We)),Ze.setXY(ve,Fn,We*Yt)}Ct>0&&he.index.array.reverse(),he.computeVertexNormals(),yt(he,C.soot,Vt.clone());let on=new Pe(2*G,Q*1.15,.32,6,1,1);on.translate(0,vt,Ct*(H-.12));let cn=on.attributes.uv;for(let ve=0;ve<cn.count;ve++)cn.setXY(ve,cn.getX(ve)*G,cn.getY(ve)*.3);yt(on,C.thatch,Vt.clone());for(let ve=-G+.5;ve<G-.3;ve+=.6){let Ve=Math.max(0,(Math.abs(ve)-_t)/(G-_t||1));if(N&&Ve>.98)continue;let We=new Pe(.11,.14,Yt*(1-Ve)-.2);We.rotateX(Ct*Math.atan2(pt,H)),We.translate(ve,vt+pt*(1-Ve)/2-Q/2-.09,Ct*H*(1-(1-Ve)/2)),yt(We,C.oak,Vt.clone())}for(let ve of[.33,.66]){let Ve=new Pe(2*(G+(_t-G)*ve)-.4,.2,.2);Ve.translate(0,vt+pt*ve-Q/2-.26,Ct*H*(1-ve)),yt(Ve,C.oak,Vt.clone())}}if(N)for(let Ct of[-1,1]){let kt=[Ct*G,vt+Q/2,-H],ne=[Ct*G,vt+Q/2,H],$t=[Ct*_t,A+Q/2,0],he=new O(Ct,1,0);ye(kt,ne,$t,C.thatch,[[-H/1.6,0],[H/1.6,0],[0,Yt/1.6]],he),ye([kt[0]-Ct*.1,vt-Q/2,kt[2]+.05],[ne[0]-Ct*.1,vt-Q/2,ne[2]-.05],[$t[0],A-Q/2,0],C.soot,[[0,0],[H,0],[H/2,Yt]],new O(-Ct,-1,0));let Ge=new Pe(.32,Q*1.15,2*H);Ge.translate(Ct*(G-.12),vt,0),yt(Ge,C.thatch,Vt.clone())}let oe=new tn(.3,.3,2*_t+.3,10,1);oe.rotateZ(Math.PI/2),oe.translate(0,A+Q/2-.12,0);let at=oe.attributes.uv;for(let Ct=0;Ct<at.count;Ct++)at.setXY(Ct,at.getX(Ct)*1.3,at.getY(Ct)*_t/.8);if(yt(oe,C.thatch,Vt.clone()),!N)for(let Ct of[-1,1]){let kt=new jn;kt.moveTo(-H,vt-Q*.6),kt.lineTo(0,A-Q*.6+.2),kt.lineTo(H,vt-Q*.6),kt.lineTo(H,vt+Q*.6),kt.lineTo(0,A+Q*.6+.2),kt.lineTo(-H,vt+Q*.6),kt.closePath();let ne=new Bi(kt,{depth:.3,bevelEnabled:!1});ne.rotateY(Math.PI/2),ne.translate(Ct*G-(Ct>0?.3:0),0,0);let $t=ne.attributes.uv;for(let he=0;he<$t.count;he++)$t.setXY(he,$t.getX(he)/1.6,$t.getY(he)/1.6);yt(ne,C.thatch,Vt.clone())}if(I!=null){let Ct=I,kt=D?[u,g+Ct]:[u+Ct,g];zt(1.3,1,1.3,C.oak,kt[0],A+.45,kt[1],0,1);for(let $t=-1;$t<=1;$t+=2)zt(1.34,.08,.04,C.soot,kt[0],A+.3+$t*.2,kt[1]+.66,0,1);let ne=new Qr(1.2,.85,4,1);ne.rotateY(Math.PI/4),ne.translate(kt[0],A+1.35,kt[1]),yt(ne,C.thatch)}return{ey:vt,hw:H,hl:G}}function qe(u){let{cx:g,cz:y,w:v,d:E,h:A,ridge:D,t:N=.9,mat:I=C.lime}=u,V=g-v/2,H=g+v/2,G=y-E/2,Q=y+E/2,vt=(at,Ct)=>(u.open||[]).filter(kt=>kt.side===at).map(kt=>Object.assign({arch:!0,y:0},kt,{at:Ct/2+(at==="n"||at==="e"?-kt.at:kt.at)}));u.noRoom||ie.push([V,G,H,Q,A,D]);let pt=I===C.lime?C.ash:I,Yt=D-.5,_t=.25;ki(V+N/2,Q-N/2,H-N/2,Q-N/2,A,N,I,vt("s",v-N),null,pt),ki(H-N/2,G+N/2,V+N/2,G+N/2,A,N,I,vt("n",v-N),null,pt),ki(V+N/2,G+N/2,V+N/2,Q-N/2,A,N,I,vt("w",E-N),u.hips?null:[Yt,_t],pt),ki(H-N/2,Q-N/2,H-N/2,G+N/2,A,N,I,vt("e",E-N),u.hips?null:[Yt,_t],pt);let Vt=new _n(v-N*2+.1,E-N*2+.1);Vt.rotateX(-Math.PI/2),Vt.translate(g,.025,y);let ye=Vt.attributes.uv;for(let at=0;at<ye.count;at++)ye.setXY(at,ye.getX(at)*(v-2*N)/3,ye.getY(at)*(E-2*N)/3);yt(Vt,u.floor||C.floor);let oe=Ns(g,y,v,E,A,D,!1,u.hips,u.louvre);return{x0:V,x1:H,z0:G,z1:Q,t:N,h:A,ridge:D,ix0:V+N,ix1:H-N,iz0:G+N,iz1:Q-N,ey:oe.ey}}let ti=[[-44,-31],[41,-33],[43,32],[-42,34]];for(let u=0;u<4;u++){let[g,y]=[ti[u],ti[(u+1)%4]],v=Math.hypot(y[0]-g[0],y[1]-g[1]),E=u===1?[{at:Math.hypot(42.03-41,.45+33),w:3.6,h:2.2,y:0,arch:!1,leaf:!1}]:[];ki(g[0],g[1],y[0],y[1],2.2,1.3,C.stone,E);let A=new Pe(v,.14,1.45);A.translate(v/2,2.27,0);let D=A.attributes.uv;for(let N=0;N<D.count;N++)D.setXY(N,D.getX(N)*v/2.2,D.getY(N)*.66);E.length||yt(A,C.stone,Ot(g[0],0,g[1],-Math.atan2(y[1]-g[1],y[0]-g[0]))),zt(1.8,2.5,1.8,C.stone,g[0],1.25,g[1],-Math.atan2(y[1]-g[1],y[0]-g[0]),2.2)}let Gi=42.03,vn=.45;zt(1.6,3.8,1.6,C.stone,Gi,1.9,vn-2.7),zt(1.6,3.8,1.6,C.stone,Gi,1.9,vn+2.7),Ns(Gi,vn,7.2,3.6,3.8,5.6,!0);for(let u of[-1,1]){let g=new Pe(.08,2.9,1.75);g.translate(0,1.45,u*.88),yt(g,C.oak,Ot(Gi-.6,0,vn+u*1.75,u*-1.2))}let ze=qe({cx:-20,cz:-12,w:17,d:11,h:3.6,ridge:9.4,louvre:.5,open:[{side:"s",at:5.5,w:1.7,h:3},{side:"n",at:5.5,w:1.7,h:3},{side:"s",at:-4.5,w:.62,h:1.3,y:1.55},{side:"s",at:.5,w:.62,h:1.3,y:1.55},{side:"n",at:-2,w:.62,h:1.3,y:1.55},{side:"w",at:0,w:.7,h:1.6,y:4.3},{side:"e",at:0,w:.62,h:1.4,y:4}]}),ei=qe({cx:-1,cz:-20,w:13,d:7.5,h:3.3,ridge:7.8,open:[{side:"s",at:-3.4,w:1.3,h:2.5},{side:"s",at:1.8,w:.6,h:1.2,y:1.4},{side:"s",at:4.6,w:.6,h:1.2,y:1.4},{side:"w",at:0,w:.55,h:1.2,y:1.5}]}),Vi=qe({cx:-24,cz:14,w:10,d:6.5,h:2.9,ridge:6.6,mat:C.stone,louvre:-1.5,open:[{side:"e",at:-.4,w:1.4,h:2.3},{side:"s",at:1.5,w:.55,h:.9,y:1.4}]}),Dn=qe({cx:8,cz:24,w:22,d:6.5,h:2.6,ridge:6.2,mat:C.daub,hips:!0,open:[{side:"n",at:-6,w:2.2,h:2.3,arch:!1,leaf:!1},{side:"n",at:2,w:2.2,h:2.3,arch:!1,leaf:!1},{side:"n",at:7.5,w:.55,h:.8,y:1.3,arch:!1}]}),za=qe({cx:24,cz:-20,w:16,d:8,h:3,ridge:7.6,mat:C.daub,hips:!0,open:[{side:"s",at:0,w:3.2,h:2.9,arch:!1,leaf:!1},{side:"n",at:0,w:3.2,h:2.9,arch:!1,leaf:!1}]});qe({cx:33,cz:16,w:5.5,d:4,h:2,ridge:4.2,mat:C.daub,hips:!0,open:[{side:"w",at:0,w:1,h:1.5,arch:!1,leaf:!1}]}),qe({cx:-37.5,cz:-25.5,w:3,d:2.6,h:2.1,ridge:3.8,mat:C.daub,hips:!0,open:[{side:"s",at:0,w:.9,h:1.8,arch:!1}]});for(let u of[Dn,za]){for(let g=u.x0+.3;g<=u.x1-.2;g+=2.2)for(let y of[u.z0-.02,u.z1+.02])zt(.22,u.h,.08,C.oak,g,u.h/2,y,0,1);for(let g of[u.z0-.02,u.z1+.02])zt(u.x1-u.x0,.22,.08,C.oak,(u.x0+u.x1)/2,u.h-.15,g,0,1)}let xe=-12,Wn=-19.6,di=[xe-2.7,xe+2.7],Nn=[-26,-22.4,-18.8,-15.2],Ei=5;for(let u of Nn)for(let g of di)en(.19,.21,Ei,C.chev,u,Ei/2,g,8,0,0,0,.62),dn.push([u,g,.3]);for(let u of di)zt(Nn[3]-Nn[0]+1.2,.3,.3,C.oak,(Nn[0]+Nn[3])/2,Ei+.15,u,0,2);function kl(u,g,y,v,E,A=.22,D=.26){let N=Math.hypot(y-u,v-g),I=N/2,V=new jn;V.moveTo(-I,E-I-.2),V.lineTo(-I,E-I),V.absarc(0,E-I,I,Math.PI,0,!0),V.lineTo(I,E-I-.2),V.lineTo(I-D,E-I-.2),V.lineTo(I-D,E-I),V.absarc(0,E-I,I-D,0,Math.PI,!1),V.lineTo(-I+D,E-I-.2),V.closePath();let H=new Bi(V,{depth:A,bevelEnabled:!1,curveSegments:18});H.translate(0,0,-A/2);let G=H.attributes.uv;for(let Q=0;Q<G.count;Q++)G.setXY(Q,G.getX(Q)/1.4,G.getY(Q)/1.4);yt(H,C.ash,Ot((u+y)/2,0,(g+v)/2,-Math.atan2(v-g,y-u)))}for(let u=0;u<3;u++)for(let g of di)kl(Nn[u],g,Nn[u+1],g,Ei);for(let u of Nn){kl(u,di[0],u,di[1],Ei+1.35,.26,.3),zt(.28,.3,ze.iz1-ze.iz0,C.oak,u,Ei+1.5,xe,0,2);for(let g of[-1,1]){let y=new Pe(.2,.2,1.9);y.rotateX(g*.55),y.translate(u,Ei-.75,xe+g*3.7),yt(y,C.oak)}zt(.18,ze.ridge-Ei-2,.18,C.oak,u,(ze.ridge+Ei+1.4)/2-.5,xe,0,1)}let Gx=[Wn,xe];for(let u=0;u<22;u++){let g=u/22*Math.PI*2,y=new eo(.2+o()*.07,0);y.scale(1.3,.7,1);let v=y.attributes.uv;for(let E=0;E<v.count;E++)v.setXY(E,v.getX(E)*.4,v.getY(E)*.4);yt(y,C.stone,Ot(Wn+Math.cos(g)*1.15*1.25,.09,xe+Math.sin(g)*1.15,g+o(),o()*.3,o()*.3))}dn.push([Wn,xe,1.25]);let Xn=ze.ix0,fo=3.4;zt(fo,.32,ze.iz1-ze.iz0,C.oak,Xn+fo/2,.16,xe,0,1.6),zt(.08,.32,ze.iz1-ze.iz0,C.oak,Xn+fo,.16,xe,0,1);let ls=Xn+.9;zt(.75,.5,.7,C.oak,ls,.57,xe,0,1),zt(.12,1.9,.82,C.oak,ls-.38,1.27,xe,0,1);for(let u of[-1,1])zt(.7,.1,.1,C.oak,ls+.02,1.1,xe+u*.38,0,1),en(.06,.06,.9,C.oak,ls+.35,.77,xe+u*.38,6);zt(.6,.14,.62,C.red,ls+.04,.88,xe),zt(.06,.9,.6,C.red,ls-.3,1.45,xe);for(let u of[-1,1]){let g=new Un(.09,10,8);yt(g,C.gold,Ot(ls-.38,2.27,xe+u*.34))}{let u=new _n(ze.iz1-ze.iz0-.2,2.6);u.rotateY(Math.PI/2);let g=u.attributes.uv;for(let y=0;y<g.count;y++)g.setXY(y,g.getX(y)*3.6,g.getY(y));yt(u,C.hangR,Ot(Xn+.04,1.65,xe))}{let u=new _n(1.7,2.1,6,6),g=u.attributes.position;for(let y=0;y<g.count;y++)g.setZ(y,Math.sin(g.getX(y)*3.4)*.04);u.computeVertexNormals(),u.rotateY(Math.PI/2),yt(u,C.arms,Ot(Xn+.1,3.95,xe),!0)}en(.03,.03,1.9,C.oak,Xn+.14,5,xe,6,Math.PI/2);for(let u of[ze.iz0+.03,ze.iz1-.03])for(let[g,y]of[[-25.4,C.hangG],[-21.6,C.hangR]]){let v=new _n(2.6,1.9),E=v.attributes.uv;for(let A=0;A<E.count;A++)E.setXY(A,E.getX(A)*2.6,E.getY(A)*1.9);yt(v,y,Ot(g,2.35,u,u<xe?0:Math.PI))}let Gl=(()=>{let u=new jn;return u.moveTo(-.3,.32),u.lineTo(.3,.32),u.quadraticCurveTo(.32,-.1,0,-.42),u.quadraticCurveTo(-.32,-.1,-.3,.32),new Bi(u,{depth:.04,bevelEnabled:!0,bevelSize:.015,bevelThickness:.015,bevelSegments:1})})(),Vl=[C.arms,C.red,C.green,C.arms,C.red,C.green,C.arms,C.red],Ff=0;for(let u of Nn)for(let g of di){let y=g<xe?1:-1,v=Gl.clone(),E=v.attributes.uv;for(let A=0;A<E.count;A++)E.setXY(A,E.getX(A)*1.4+.5,E.getY(A)*1.4+.5);yt(v,Vl[Ff++%Vl.length],Ot(u,3.1,g+y*.23,y>0?0:Math.PI,-.12))}function Wl(u,g,y,v,E){let[A,D]=v?[y,.85]:[.85,y];if(zt(A,.07,D,C.oak,u,.78,g,0,1.4),E){zt(A+.02,.01,D+.2,C.linen,u,.82,g,0,1.2);for(let N of[-1,1])zt(v?A+.02:.01,.32,v?.01:D+.02,C.linen,v?u:u+N*.52,.66,v?g+N*.52:g,0,1.2)}for(let N of[-.38,.38])zt(v?.08:.7,.74,v?.7:.08,C.oak,v?u+N*y:u,.37,v?g:g+N*y,0,1);Le(u,g,A,D)}Wl(Xn+2.35,xe,6.6,!1,!0);for(let u of[-1,1])zt(.36,.44,2,C.oak,Xn+1.55,.54,xe+u*2.15,0,1);for(let u of[-1,1]){let g=xe+u*4.1;Wl(-19.9,g,6.4,!0,u<0),zt(6.4,.42,.32,C.oak,-19.9,.21,g-u*.75,0,1.4),Le(-19.9,g-u*.75,6.4,.32)}let Xl=new tn(.045,.035,.12,10),Ha=new Un(.12,12,6,0,Math.PI*2,Math.PI/2,Math.PI/2),Yl=new Ts([[0,0],[.08,0],[.11,.08],[.1,.2],[.06,.28],[.065,.33],[0,.33]].map(([u,g])=>new St(u,g)),12),po=new Un(.1,10,6);po.scale(1.3,.55,1),Ha.rotateX(Math.PI);let ka=(u,g,y,v)=>{for(let E=0;E<y;E++){let A=(E+.5)/y-.5,D=v?u+A*5.8:u+(o()-.5)*.3,N=v?g+(o()-.5)*.3:g+A*6.2,I=o();I<.4?yt(Xl.clone(),o()<.5?C.horn:C.clay,Ot(D,.88,N)):I<.65?yt(Ha.clone(),C.oak,Ot(D,.94,N)):I<.85?yt(po.clone(),C.bread,Ot(D,.86,N,o()*3)):yt(Yl.clone(),C.glaze,Ot(D,.82,N))}};ka(Xn+2.35,xe,10,!1),ka(-19.9,xe-4.1,9,!0),ka(-19.9,xe+4.1,7,!0);for(let u=0;u<5;u++)yt(Xl.clone(),C.gold,Ot(Xn+2.2,.88,xe-1.6+u*.8));{let u=Ot(-17.3,0,-13.6,-.6),g=new tn(.2,.22,.45,8);g.translate(0,.225,0),yt(g,C.oak,u.clone());let y=(v,E,A,D,N)=>{let I=Math.hypot(E[0]-v[0],E[1]-v[1]),V=new Pe(I,A,D);V.rotateZ(Math.atan2(E[1]-v[1],E[0]-v[0])),V.translate((v[0]+E[0])/2,(v[1]+E[1])/2,0),yt(V,N,u.clone())};y([0,.47],[.16,1.4],.13,.12,C.oak),y([.16,1.4],[.36,1.36],.07,.05,C.oak),y([.36,1.36],[.6,1.2],.07,.05,C.oak),y([.6,1.2],[.1,.5],.05,.05,C.oak);for(let v=0;v<10;v++){let E=(v+1)/11,A=.02+E*.14,D=.55+E*.82,N=.16+E*.44,I=1.39-E*.19,V=new tn(.003,.003,1,3),H=Math.hypot(N-A,I-D);V.scale(1,H,1),V.rotateZ(-Math.atan2(N-A,I-D)),V.translate((A+N)/2,(D+I)/2,0),yt(V,C.gold,u.clone(),!0)}zt(.5,.04,.5,C.oak,-13.4,.55,-12.4,.3,.5),zt(.3,.55,.3,C.oak,-13.4,.27,-12.4,.3,.5),dn.push([-13.4,-12.4,.4]);for(let v=0;v<7;v++)for(let E=0;E<7;E++)(v+E)%2&&zt(.06,.006,.06,C.soot,-13.4+(v-3)*.062,.573,-12.4+(E-3)*.062,0,.5);for(let v=0;v<9;v++)en(.014,.014,.05,v?C.oak:C.gold,-13.4+(o()-.5)*.38,.6,-12.4+(o()-.5)*.38,6)}let ql=[[Nn[0],di[0]+.25],[Nn[0],di[1]-.25],[Nn[2],di[0]+.25],[Nn[2],di[1]-.25]];for(let[u,g]of ql)en(.025,.02,.5,C.iron,u,2.75,g,5),en(.04,.03,.45,C.oak,u,3.05,g,6);{zt(2.2,.5,1.7,C.oak,3,.3,-21.4,0,1),zt(2.15,.22,1.65,C.red,3,.62,-21.4,0,1),zt(.5,.14,1.5,C.linen,3+.8,.78,-21.4,0,1);for(let[E,A]of[[-1.1,-.85],[1.1,-.85],[-1.1,.85],[1.1,.85]])en(.05,.05,2.4,C.oak,3+E,1.2,-21.4+A,6);zt(2.3,.06,1.8,C.oak,3,2.4,-21.4,0,1);for(let[E,A,D,N]of[[2.3,.02,0,-.88],[.02,1.8,1.12,0]])zt(E,1.6,A,C.green,3+D,1.6,-21.4+N,0,1);for(let E of[-1,1]){let A=new _n(.6,1.9,4,1),D=A.attributes.position;for(let N=0;N<D.count;N++)D.setZ(N,Math.sin(D.getX(N)*18)*.04);A.computeVertexNormals(),yt(A,C.green,Ot(3-1.12+.3,1.42,-21.4+E*.87))}Le(3,-21.4,2.3,1.8),zt(1.1,.6,.6,C.oak,-1.8,.3,ei.iz0+.4,0,.8),zt(1.12,.06,.62,C.iron,-1.8,.58,ei.iz0+.4,0,.8),Le(-1.8,ei.iz0+.4,1.1,.6),zt(.9,.5,.5,C.oak,-6,.25,ei.iz1-.35,0,.8),Le(-6,ei.iz1-.35,.9,.5),zt(.55,.45,.5,C.oak,0,.45,-19.5,0,.8),zt(.08,1.1,.5,C.oak,-.24,.9,-19.5,0,.8),zt(.5,.1,.5,C.red,.02,.73,-19.5);let y=new _n(3,1.8);yt(y,C.hangG,Ot(-1.2,1.9,ei.iz0+.03));let v=new tn(.35,.2,.3,10,1,!0);yt(v,C.iron,Ot(-2.4,.55,-19.4)),en(.03,.03,.45,C.iron,-2.4,.2,-19.4,4)}let pi=-26.8,mi=14;for(let u=0;u<12;u++){let g=u/12*Math.PI*2,y=new eo(.17,0);yt(y,C.stone,Ot(pi+Math.cos(g)*.7,.08,mi+Math.sin(g)*.7,o()*3))}dn.push([pi,mi,.9]);{let u=new Un(.38,14,8,0,Math.PI*2,Math.PI*.35,Math.PI*.65);yt(u,C.iron,Ot(pi,.95,mi)),en(.012,.012,1.6,C.iron,pi,2.1,mi,3);for(let g of[0,2.1,4.2]){let y=new tn(.04,.05,3.2,5);y.rotateZ(.32),y.translate(.5,1.5,0),yt(y,C.oak,Ot(pi,0,mi,g))}}zt(2.4,.08,.9,C.oak,-23.4,.82,12.1,0,1.2);for(let u of[-1,1])zt(.08,.78,.7,C.oak,-23.4+u*1,.39,12.1,0,1);Le(-23.4,12.1,2.4,.9),yt(po.clone(),C.bread,Ot(-23,.9,12.1)),yt(po.clone(),C.bread,Ot(-23.4,.9,12.2,1)),yt(Ha.clone(),C.oak,Ot(-24,.97,12));let Of=new Ts([[0,0],[.27,0],[.32,.2],[.34,.4],[.32,.6],[.27,.8],[0,.8]].map(([u,g])=>new St(u,g)),14);for(let u=0;u<3;u++)yt(Of.clone(),C.oak,Ot(-20.4+u*.1,0,15.9-u*.75-0,o())),dn.push([-20.4+u*.1,15.9-u*.75,.35]);for(let u=0;u<4;u++){let g=new Un(.3,10,8);g.scale(1,1.25,.9),yt(g,C.straw,Ot(-27.5+u*.55,.35,15.9,o()*3))}zt(.9,.5,.7,C.stone,-20.6,.25,19.4,0,1);{let u=new Un(1.3,18,10,0,Math.PI*2,0,Math.PI/2),g=u.attributes.uv;for(let y=0;y<g.count;y++)g.setXY(y,g.getX(y)*4,g.getY(y)*1.2);yt(u,C.daub,Ot(-17,0,19.5)),dn.push([-17,19.5,1.4])}for(let u=Dn.ix0+2.2;u<Dn.ix1-1;u+=2.2)zt(.1,1.3,2.4,C.oak,u,.65,Dn.iz1-1.2,0,1);zt(Dn.ix1-Dn.ix0-.4,.5,.4,C.oak,(Dn.ix0+Dn.ix1)/2,1.5,Dn.iz1-.3,0,1.2),zt(Dn.ix1-Dn.ix0-.4,.2,.3,C.straw,(Dn.ix0+Dn.ix1)/2,1.85,Dn.iz1-.3,0,1);for(let u=0;u<26;u++){let g=new tn(.16,.2,.9,7);yt(g,C.straw,Ot(za.ix0+.6+u%13*.5,.45+Math.floor(u/13)*0,za.iz0+.4+Math.floor(u/13)*.45,0,.1*(o()-.5)))}{let u=new tn(.95,1,.8,16,1,!0),g=u.attributes.uv;for(let v=0;v<g.count;v++)g.setXY(v,g.getX(v)*3,g.getY(v)*.4);yt(u,C.stone,Ot(8,.4,2.5)),yt(new gr(.95,16).rotateX(-Math.PI/2),C.iron,Ot(8,.5,2.5),!0);for(let v of[-1,1])zt(.14,1.7,.14,C.oak,8+v*1.05,.85,2.5,0,1);en(.08,.08,2.3,C.oak,8,1.55,2.5,8,0,0,Math.PI/2),dn.push([8,2.5,1.2]);let y=new tn(.16,.13,.3,10);yt(y,C.oak,Ot(8.6,.65,3.3))}for(let u=0;u<30;u++){let g=new tn(.09+o()*.05,.1+o()*.05,1.1,7);yt(g,C.oak,Ot(-9+u%8*.24,.12+Math.floor(u/8)*.2,5+(o()-.5)*.1,0,Math.PI/2))}Le(-8.2,5,2.2,1.2);{let u=new tn(.2,2.1,1.8,14),g=u.attributes.uv;for(let E=0;E<g.count;E++)g.setXY(E,g.getX(E)*5,g.getY(E));yt(u,C.straw,Ot(33,3.2,-6));let y=new tn(2.1,2.2,2.3,14),v=y.attributes.uv;for(let E=0;E<v.count;E++)v.setXY(E,v.getX(E)*5,v.getY(E)*1.2);yt(y,C.straw,Ot(33,1.15,-6)),dn.push([33,-6,2.3])}{let u=Ot(20,0,6,.5),g=new Pe(2.6,.1,1.4);g.translate(0,.78,0),yt(g,C.oak,u.clone());for(let E of[-1,1]){let A=new Pe(2.6,.4,.06);A.translate(0,1,E*.7),yt(A,C.oak,u.clone());let D=new ro(.55,.06,6,18);D.translate(-.3,.58,E*.82),yt(D,C.oak,u.clone())}let y=new Pe(2.2,.08,.08);y.translate(2.3,.55,.35),yt(y,C.oak,u.clone());let v=y.clone();v.translate(0,0,-.7),yt(v,C.oak,u.clone()),dn.push([20,6,1.5])}zt(1,.7,1,C.stone,37.5,.35,4.5,.1,1);function Zl(u,g=1.1){for(let y=0;y<u.length-1;y++){let[v,E]=[u[y],u[y+1]],A=Math.hypot(E[0]-v[0],E[1]-v[1]),D=new Pe(A,g,.08);D.translate(A/2,g/2,0);let N=D.attributes.uv;for(let I=0;I<N.count;I++)N.setXY(I,N.getX(I)*A*2,N.getY(I)*g);yt(D,C.wattle,Ot(v[0],0,v[1],-Math.atan2(E[1]-v[1],E[0]-v[0]))),ce.push([v[0],v[1],E[0],E[1],.06]);for(let I=0;I<=A;I+=.6)en(.035,.035,g+.15,C.oak,v[0]+(E[0]-v[0])*I/A,(g+.15)/2,v[1]+(E[1]-v[1])*I/A,5)}}Zl([[30.2,18],[30.2,22.5],[36,22.5],[36,18.2]]),Zl([[-36,18],[-36,26],[-30,26]],.95);let $l=[[-120,-60,.3],[-150,-20,1.1],[-128,82,-.4],[-160,60,.7],[110,-95,.2],[-60,-120,1.4]];for(let[u,g,y]of $l){let v=tt(u,g),E=Ot(u,v,g,y),A=new Pe(7,2,4.2);A.translate(0,1,0);let D=A.attributes.uv;for(let V=0;V<D.count;V++)D.setXY(V,D.getX(V)*3,D.getY(V));yt(A,C.daub,E.clone(),!0);let N=new Qr(4.4,3,4,1);N.rotateY(Math.PI/4),N.scale(1.25,1,.78),N.translate(0,3.4,0);let I=N.attributes.uv;for(let V=0;V<I.count;V++)I.setXY(V,I.getX(V)*6,I.getY(V)*3);yt(N,C.thatch,E.clone(),!0),ce.push([u-4,g,u+4,g,2.4])}let je=u=>new fe(u),Ee=(u,g,y,v,E=7)=>{let A=new O(...u),D=new O(...g),N=A.distanceTo(D),I=new tn(v,y,N,E);return I.applyQuaternion(new kn().setFromUnitVectors(new O(0,1,0),D.clone().sub(A).normalize())),I.translate((u[0]+g[0])/2,(u[1]+g[1])/2,(u[2]+g[2])/2),I},pn=(u,g,y,v,E=1,A=1,D=1,N=10)=>{let I=new Un(u,N,Math.max(6,N*.7|0));return I.scale(E,A,D),I.translate(g,y,v),I},mo=(u,g,y,v,E,A)=>{let D=new Pe(u,g,y);return D.translate(v,E,A),D},go=(u,g=12)=>new Ts(u.map(([y,v])=>new St(y,v)),g),Me={madder:10108716,woad:4875920,weld:10261584,fawn:10916719,grey:8814711,brown:6967352,green:5072448,black:3486254,linen:14867661,rust:9065778,plum:6175306},Jl=[2826006,4008475,5913634,7232064,9075304,2300436,8014374],_o=je(4008734);function ni(u,g,y,v={}){let E=v.y!=null?v.y:tt(u,g),A=Ot(u,E,g,y,0,0,v.h||1),D=(pt,Yt,_t)=>yt(pt,Yt,A.clone(),!1,_t),N=je(v.tunic||Me.fawn),I=je(v.hose||Me.brown),V=je(v.hair||Jl[o()*Jl.length|0]),H=v.sit||0,G=H?H-.75:0;if(v.woman&&!H)D(go([[0,.02],[.3,.02],[.27,.3],[.22,.7],[.17,.98],[.2,1.2],[.21,1.34],[.16,1.44],[.07,1.5],[0,1.5]]),C.cloth,N);else{for(let _t of[-.09,.09])H?(D(Ee([_t,H+.07,-.02],[_t*1.1,H+.08,.44],.1,.08),C.cloth,N),D(Ee([_t*1.1,H+.05,.44],[_t*1.1,.08,.47],.062,.052),C.cloth,v.woman?N:I),D(mo(.1,.08,.22,_t*1.1,.04,.52),C.coat,_o)):(D(Ee([_t,.06,0],[_t,.62,0],.052,.066),C.cloth,I),D(mo(.1,.08,.23,_t,.04,.05),C.coat,_o));let Yt=go((H?[[0,.82],[.21,.82],[.19,.95],[.18,1],[.2,1.2],[.22,1.36],[.17,1.45],[.07,1.5],[0,1.5]]:[[0,.5],[.26,.5],[.23,.62],[.2,.85],[.18,1],[.2,1.2],[.22,1.36],[.17,1.45],[.07,1.5],[0,1.5]]).map(([_t,Vt])=>[_t,Vt+(H?G:0)]));if(Yt.scale(1,1,.74),D(Yt,C.cloth,N),!v.woman){let _t=new ro(.185,.018,5,16);_t.rotateX(Math.PI/2),_t.scale(1,1,.74),_t.translate(0,1+G,0),D(_t,C.coat,_o)}}if(v.woman&&H){let pt=go([[0,.82],[.22,.82],[.18,1],[.2,1.2],[.21,1.34],[.16,1.44],[.07,1.5],[0,1.5]].map(([Yt,_t])=>[Yt,_t+G]));pt.scale(1,1,.74),D(pt,C.cloth,N)}let Q=(pt,Yt,_t)=>{let Vt=[pt*.2,1.38+G,0];D(Ee(Vt,Yt,.058,.05),C.cloth,N),D(Ee(Yt,_t,.048,.04),C.cloth,N),D(pn(.045,..._t),C.skin)},vt=v.arms||(H?"table":"down");for(let pt of[-1,1])vt==="table"?Q(pt,[pt*.25,.86,.18],[pt*.14,.87,.44]):vt==="work"?Q(pt,[pt*.25,1.12+G,.16],[pt*.1,1+G,.4]):vt==="spear"?Q(pt,pt>0?[.27,1.1,.1]:[-.27,1.1,.08],pt>0?[.3,1.2,.24]:[-.24,1.02,.26]):vt==="hold"&&pt>0?Q(pt,[.26,1.1+G,.14],[.24,1.18+G,.36]):Q(pt,[pt*.25,1.1+G,.02],[pt*.25,.86+G,.05]);if(D(Ee([0,1.47+G,0],[0,1.58+G,.01],.05,.048),C.skin),D(pn(.1,0,1.67+G,.015,.92,1.12,1),C.skin),D(pn(.024,0,1.655+G,.108),C.skin),v.woman){let pt=new Un(.118,12,9,Math.PI/2+1.05,Math.PI*2-2.1,0,2.3);pt.scale(.95,1.1,1),pt.translate(0,1.69+G,-.005),D(pt,C.cloth,je(v.veil||Me.linen)),D(Ee([0,1.62+G,-.05],[0,1.4+G,-.1],.1,.17,10),C.cloth,je(v.veil||Me.linen))}else if(v.hood){let pt=new Un(.125,12,9,Math.PI/2+.95,Math.PI*2-1.9,0,2.2);pt.scale(.95,1.1,1),pt.translate(0,1.69+G,-.01),D(pt,C.cloth,je(v.hood)),D(go([[.24,1.32],[.2,1.42],[.12,1.52],[0,1.55]].map(([Yt,_t])=>[Yt,_t+G])),C.cloth,je(v.hood))}else{D(new Un(.106,12,6,0,Math.PI*2,0,1).scale(.95,1.1,1).translate(0,1.685+G,.005),C.coat,V);let pt=new Un(.108,12,8,Math.PI/2+.95,Math.PI*2-1.9,0,2);pt.scale(.95,1.1,1),pt.translate(0,1.685+G,0),D(pt,C.coat,V),v.beard&&D(pn(.068,0,1.6+G,.055,1,1.15,.8),C.coat,V)}if(v.cloak){let pt=H?.72:1.02,Yt=new tn(.205,H?.27:.33,pt,16,1,!0,Math.PI*.36,Math.PI*1.28);Yt.scale(1,1,.82),Yt.translate(0,1.44+G-pt/2,-.02),D(Yt,C.cloth,je(v.cloak)),D(pn(.025,.16,1.42+G,.1),C.gold)}if(vt==="spear"){D(Ee([.3,.02,.27],[.3,2.35,.27],.02,.018),C.oak),D(Ee([.3,2.35,.27],[.3,2.58,.27],.03,.002,5),C.iron);let pt=Gl.clone();pt.scale(1.15,1.15,1),pt.translate(-.28,1,.2),D(pt,v.shield||C.arms)}vt==="hold"&&v.jug&&D(Yl.clone().translate(.24,1.02+G,.38),C.glaze),v.free||dn.push([u,g,H?.26:.3])}function xo(u,g,y,v,E){let A=Ot(u,tt(u,g),g,y),D=je(v),N=je(1972501),I=(H,G,Q)=>yt(H,G,A.clone(),!1,Q),V=new As(.3,.85,4,12);V.rotateX(Math.PI/2),V.scale(1,1.12,1),V.translate(0,1.04,0),I(V,C.coat,D),I(pn(.3,0,1.08,.45,.95,1.05,1),C.coat,D),I(pn(.31,0,1.07,-.45,1,1.02,1),C.coat,D),I(Ee([0,1.15,.55],[0,1.58,.88],.21,.13,9),C.coat,D),I(Ee([0,1.66,.86],[0,1.36,1.13],.1,.07,9),C.coat,D),I(pn(.075,0,1.36,1.13,1,.9,1.1),C.coat,je(2761244));for(let H of[-1,1])I(Ee([H*.05,1.7,.84],[H*.06,1.82,.82],.03,.005,5),C.coat,D);I(Ee([0,1.28,.5],[0,1.74,.83],.045,.035,5),C.coat,N);for(let[H,G]of[[-.15,.48],[.15,.48],[-.15,-.5],[.15,-.5]])I(Ee([H,.98,G],[H,.5,G+(G<0?-.04:0)],.085,.055),C.coat,D),I(Ee([H,.5,G+(G<0?-.04:0)],[H,.06,G],.045,.042),C.coat,G>0&&v===7028002?je(1840658):D),I(pn(.055,H,.04,G+.01,1,.7,1.1),C.coat,N);I(Ee([0,1.25,-.78],[0,.58,-.9],.07,.03),C.coat,N),E&&(I(mo(.66,.04,.7,0,1.36,-.02),C.cloth,je(Me.madder)),I(mo(.5,.12,.56,0,1.42,-.02),C.coat,_o)),dn.push([u+Math.sin(y)*.2,g+Math.cos(y)*.2,.65])}function Mr(u,g,y,v,E,A){let D=Ot(u,A!=null?A:tt(u,g),g,y),N=je(v),I=(H,G)=>yt(H,G,D.clone(),!1,N);if(E){let H=new As(.14,.42,4,10);H.rotateX(Math.PI/2),H.scale(1.15,.85,1),H.translate(0,.14,0),I(H,C.coat),I(Ee([-.08,.07,.2],[-.06,.05,.5],.035,.03),C.coat),I(Ee([.08,.07,.2],[.06,.05,.5],.035,.03),C.coat),I(pn(.17,.03,.17,-.24,1.1,.9,1.1),C.coat),I(pn(.16,0,.19,.2,1,1,1),C.coat),I(Ee([0,.22,.3],[0,.2,.46],.08,.07),C.coat),I(pn(.085,0,.17,.5,1,.9,1.1),C.coat),I(Ee([0,.15,.54],[0,.1,.7],.055,.025),C.coat);for(let G of[-1,1])I(Ee([G*.05,.22,.48],[G*.1,.16,.42],.035,.01,4),C.coat);I(Ee([.05,.12,-.34],[.2,.05,-.6],.03,.015),C.coat);return}let V=new As(.13,.42,4,10);V.rotateX(Math.PI/2),V.translate(0,.55,0),I(V,C.coat),I(pn(.16,0,.53,.2,.85,1.15,1),C.coat),I(Ee([0,.6,.3],[0,.8,.42],.075,.06),C.coat),I(Ee([0,.82,.4],[0,.74,.62],.07,.028),C.coat);for(let H of[-1,1])I(Ee([H*.04,.86,.41],[H*.07,.84,.34],.03,.01,4),C.coat);for(let[H,G]of[[-.07,.22],[.07,.22],[-.07,-.25],[.07,-.25]])I(Ee([H,.52,G],[H,.02,G+(G<0?-.05:.02)],.04,.022),C.coat);I(Ee([0,.58,-.36],[0,.3,-.58],.025,.012),C.coat),dn.push([u,g,.35])}function Bf(u,g,y,v){let E=Ot(u,tt(u,g),g,y,0,0,.9+o()*.2),A=je(v<.12?4864556:v<.2?10853e3:15920351),D=je(v<.12?2760986:11838860),N=(V,H,G)=>yt(V,H,E.clone(),!0,G);N(pn(.4,0,.55,0,.82,.78,1.15,12),C.wool,A);let I=o()<.6;N(Ee([0,.62,.3],I?[0,.42,.5]:[0,.72,.5],.16,.12),C.wool,A),N(Ee(I?[0,.42,.5]:[0,.72,.5],I?[0,.2,.64]:[0,.74,.66],.085,.055),C.coat,D),N(pn(.075,0,I?.2:.74,I?.64:.66,.85,.9,1.1),C.coat,D);for(let V of[-1,1])N(Ee([V*.05,I?.4:.78,I?.52:.55],[V*.13,I?.38:.76,I?.5:.52],.022,.01,4),C.coat,D);for(let[V,H]of[[-.13,.22],[.13,.22],[-.13,-.24],[.13,-.24]])N(Ee([V,.35,H],[V,.01,H],.04,.03,5),C.coat,je(2761760))}function zf(u,g,y){let v=Ot(u,tt(u,g),g,y),E=je(2038810),A=(I,V,H)=>yt(I,V,v.clone(),!0,H||E),D=new As(.4,1,4,12);D.rotateX(Math.PI/2),D.scale(1,1.08,1),D.translate(0,.98,0),A(D,C.coat);let N=o()<.5;A(Ee([0,1.05,.7],N?[0,.45,1.05]:[0,1,1.05],.24,.17,9),C.coat),A(pn(.15,0,N?.35:.92,N?1.12:1.18,.9,1,1.25),C.coat);for(let I of[-1,1])A(Ee([I*.1,N?.52:1.08,N?1.04:1.08],[I*.3,N?.6:1.2,N?1:1.04],.03,.01,5),C.coat,je(14076848));for(let[I,V]of[[-.2,.5],[.2,.5],[-.2,-.52],[.2,-.52]])A(Ee([I,.8,V],[I,.02,V],.085,.055),C.coat);A(Ee([0,1.2,-.85],[0,.45,-.95],.04,.03,5),C.coat)}function Hf(u,g,y){let v=Ot(u,tt(u,g),g,y,0,0,.9+o()*.2),E=(D,N,I)=>yt(D,N,v.clone(),!0,I),A=je(o()<.7?15921126:10130570);E(pn(.2,0,.3,0,.78,.72,1.25),C.coat,A),E(Ee([0,.36,.18],[0,.62,.25],.05,.04),C.coat,A),E(pn(.055,0,.65,.27),C.coat,A),E(Ee([0,.64,.3],[0,.62,.38],.022,.006,5),C.coat,je(14715434));for(let D of[-1,1])E(Ee([D*.06,.16,0],[D*.06,0,.02],.015,.012,4),C.coat,je(14715434))}let Ga=xe;ni(44.4,-1.75,Math.PI/2,{arms:"spear",tunic:Me.madder,hose:Me.black,cloak:Me.woad,beard:!0,h:1.03}),ni(44.4,2.65,Math.PI/2,{arms:"spear",tunic:Me.woad,hose:Me.brown,cloak:Me.green,shield:C.red,h:1}),xo(36.2,6.6,-2.2,5912608,!0);let Va=(u,g,y,v,E)=>ni(u,g,y,{sit:E?.76:.42,y:0,tunic:[Me.madder,Me.woad,Me.green,Me.weld,Me.rust,Me.plum][v%6],hose:Me.black,cloak:E&&v%2?[Me.woad,Me.madder][v%2]:v%3===0?Me.fawn:0,beard:v%3===1,woman:!E&&v%4===2,veil:v%8===2?Me.linen:14274488});[-21.7,-20.7,-19.7,-17.9,-17].forEach((u,g)=>Va(u,Ga-4.1+.75,Math.PI,g)),[-21.4,-20.4,-17.6].forEach((u,g)=>Va(u,Ga+4.1-.75,0,g+5)),[-2.55,-1.75,1.75,2.55].forEach((u,g)=>Va(Xn+1.55,Ga+u,Math.PI/2,g,!0)),ni(-16.8,-9.6,-Math.PI/2-.3,{arms:"hold",jug:!0,tunic:Me.fawn,hose:Me.grey}),ni(-14.6,-13.9,-Math.PI/2+.5,{tunic:Me.green,cloak:Me.madder,beard:!0,hair:9075304}),Mr(-17.4,-11,-2.3,9401428,!0,0),Mr(-21.3,-12.6,1.2,4865846,!0,0),ni(-25.95,13.35,Math.atan2(-.85,.65),{arms:"work",tunic:Me.brown,hose:Me.grey,hood:Me.fawn}),ni(-23.4,12.85,Math.PI,{arms:"work",woman:!0,tunic:Me.weld,veil:14274488}),xo(4.6,18.6,Math.PI/2,7028002),xo(12.4,18.9,-Math.PI/2+.2,9407104),xo(15.2,18.7,-Math.PI/2-.15,2827296),ni(10.6,18.3,Math.PI/2+.3,{tunic:Me.fawn,hose:Me.brown,hood:Me.green}),ni(9.25,3.55,-2.5,{woman:!0,tunic:Me.woad,veil:14274488}),yt(new tn(.14,.11,.26,10),C.oak,Ot(9.55,.13,3.95)),ni(-8.2,6.35,Math.PI,{arms:"work",tunic:Me.rust,hose:Me.brown}),Mr(32,20,.6,14208440),Mr(34.2,19.4,-1.9,5917244),Mr(33.4,21.5,2.6,11569760,!0);for(let u=0;u<7;u++)Hf(-34.6+o()*3.6,19.6+o()*5,o()*6.3);for(let u=0;u<46;u++){let g=o()*6.3,y=Math.sqrt(o())*26;Bf(-82+Math.cos(g)*y*1.3,58+Math.sin(g)*y,o()*6.3,o())}ni(-70,46,-.9,{tunic:Me.grey,hose:Me.brown,cloak:Me.fawn,hood:Me.brown,free:!0});for(let u=0;u<9;u++)zf(98+o()*26,-62+o()*16,o()*6.3);{let u=new Set;for(let g of uo)for(let y=0;y<4;y++){let v=g[y],E=g[(y+1)%4],A=[v,E].map(Q=>Q.map(vt=>vt.toFixed(1)).join(",")).sort().join("|");if(u.has(A))continue;u.add(A);let D=(v[0]+E[0])/2,N=(v[1]+E[1])/2;if(Math.hypot(D,N)>480||Math.hypot(D,N)<100)continue;let I=(Math.atan2(D,-N)*180/Math.PI+360)%360;if(o()<.45||I>95&&I<135||I>200&&I<250)continue;let V=Math.hypot(E[0]-v[0],E[1]-v[1]),H=-Math.atan2(E[1]-v[1],E[0]-v[0]),G=Math.ceil(V/8);for(let Q=0;Q<G;Q++){let vt=Q/G,pt=(Q+1)/G,Yt=v[0]+(E[0]-v[0])*vt,_t=v[1]+(E[1]-v[1])*vt,Vt=v[0]+(E[0]-v[0])*pt,ye=v[1]+(E[1]-v[1])*pt,oe=(tt(Yt,_t)+tt(Vt,ye))/2,at=V/G+.05,Ct=new Pe(at,1,1.3),kt=Ct.attributes.uv;for(let $t=0;$t<kt.count;$t++)kt.setXY($t,kt.getX($t)*at/2.2,kt.getY($t)*.45);yt(Ct,C.stone,Ot((Yt+Vt)/2,oe+.32,(_t+ye)/2,H),!0);let ne=new Pe(at,.3,1.2);yt(ne,C.turf,Ot((Yt+Vt)/2,oe+.92,(_t+ye)/2,H),!0)}ce.push([v[0],v[1],E[0],E[1],.65])}}for(let[u,g]of Qt){let y=Ls(g,!1);if(!y)continue;let v=new Ne(y,u);v.castShadow=v.receiveShadow=!0,v.matrixAutoUpdate=!1,it.add(v)}Qt.clear();{let u=[],g=s?96:160,y=0,v=.9;for(;y<900;)u.push(y),y+=v,v*=y<60?1:1.045;u.push(900);let E=[],A=[],D=[];for(let G=0;G<u.length;G++)for(let Q=0;Q<(G?g:1);Q++){let vt=Q/g*Math.PI*2,pt=Math.cos(vt)*u[G],Yt=Math.sin(vt)*u[G];E.push(pt,tt(pt,Yt),Yt),A.push(pt/3,Yt/3)}let N=(G,Q)=>G===0?0:1+(G-1)*g+Q%g;for(let G=0;G<u.length-1;G++)for(let Q=0;Q<g;Q++)G===0?D.push(0,N(1,Q+1),N(1,Q)):D.push(N(G,Q),N(G,Q+1),N(G+1,Q),N(G,Q+1),N(G+1,Q+1),N(G+1,Q));let I=new Ke;I.setAttribute("position",new de(E,3)),I.setAttribute("uv",new de(A,2)),I.setIndex(D),I.computeVertexNormals();let V=new Qn({map:Kt,roughness:1});V.onBeforeCompile=G=>{G.uniforms.splat={value:jt},G.uniforms.earth={value:Ie},G.uniforms.landC={value:F},G.uniforms.fields={value:P},G.vertexShader=G.vertexShader.replace("#include <common>",`#include <common>
varying vec3 vW;`).replace("#include <worldpos_vertex>",`#include <worldpos_vertex>
vW = (modelMatrix * vec4(transformed, 1.)).xyz;`),G.fragmentShader=G.fragmentShader.replace("#include <common>",`#include <common>
varying vec3 vW; uniform sampler2D splat, earth, landC, fields;`).replace("#include <map_fragment>",`
          vec2 suv = vW.xz / ${wt.toFixed(1)} + .5;
          float wornA = texture2D(splat, suv).r * step(0., suv.x) * step(suv.x, 1.) * step(0., suv.y) * step(suv.y, 1.);
          vec3 g1 = texture2D(map, vMapUv).rgb, g2 = texture2D(map, vMapUv * .21 + .37).rgb, e = texture2D(earth, vMapUv * .8).rgb;
          vec3 gr = mix(g1, g2, .45) * (0.86 + .28 * texture2D(map, vMapUv * .031).g);
          gr = mix(vec3(dot(gr, vec3(.3, .55, .15))), gr, .8);
          float d = length(vW.xz);
          vec3 far = texture2D(landC, vec2(vW.x, -vW.z) / ${(2*Hi).toFixed(1)} + .5).rgb * 1.08;
          vec3 fc = texture2D(fields, vW.xz / ${Si.toFixed(1)} + .5).rgb;
          float lum = dot(mix(g1, g2, .45), vec3(.3, .55, .15)) / .36;
          vec3 fld = fc * mix(1., lum, .55) * 1.1;
          vec3 c = mix(gr, fld, smoothstep(70., 130., d));
          c = mix(c, e, smoothstep(.15, .7, wornA));
          c = mix(c, far, smoothstep(620., 880., d));
          diffuseColor.rgb *= c;`)};let H=new Ne(I,V);H.receiveShadow=!0,it.add(H)}{let u=s?192:384,g=new _n(2*Hi,2*Hi,u-1,u-1);g.rotateX(-Math.PI/2);let y=g.attributes.position;for(let A=0;A<y.count;A++){let D=y.getX(A),N=y.getZ(A),I=Math.hypot(D,N),V=X(D,N)-Oa-K(I);V-=4*(1-Us(820,1100,I)),y.setY(A,Math.max(V,-Oa-K(I)-25))}g.computeVertexNormals();let v=new Qn({map:F,normalMap:W,normalMapType:Ul,roughness:1}),E=new Ne(g,v);it.add(E)}let gi=new O().setFromSphericalCoords(1,zi.degToRad(90-os[1]),Math.PI-zi.degToRad(os[0]));gi.set(Math.sin(zi.degToRad(os[0]))*Math.cos(zi.degToRad(os[1])),Math.sin(zi.degToRad(os[1])),-Math.cos(zi.degToRad(os[0]))*Math.cos(zi.degToRad(os[1])));let Kl={time:{value:0},sunDir:{value:gi},deep:{value:new fe(1520711)},skyC:{value:new fe(7310246)},fogC:{value:ft},fogD:{value:it.fog.density}};{let u=new _n(2*Hi*2.5,2*Hi*2.5,200,200);u.rotateX(-Math.PI/2);{let v=u.attributes.position;for(let E=0;E<v.count;E++)v.setY(E,-K(Math.hypot(v.getX(E),v.getZ(E))))}let g=new Sn({uniforms:Kl,transparent:!0,depthWrite:!0,vertexShader:`#include <common>
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
        }`}),y=new Ne(u,g);y.position.y=-Oa+.3,y.renderOrder=-1,it.add(y)}let Sr=new vr;Sr.scale.setScalar(7e4);let br=Sr.material.uniforms;br.turbidity.value=2.6,br.rayleigh.value=1.7,br.mieCoefficient.value=.0028,br.mieDirectionalG.value=.8,br.sunPosition.value.copy(gi),Sr.renderOrder=-2,Sr.material.depthTest=!1,it.add(Sr);{let u=new mr(h),g=new $r,y=new vr;y.scale.setScalar(60),y.material.uniforms.sunPosition.value.copy(gi),y.material.uniforms.turbidity.value=2.6,y.material.uniforms.rayleigh.value=1.7,y.material.uniforms.mieCoefficient.value=.0028,g.add(y);let v=new Ne(new gr(50,24).rotateX(-Math.PI/2),new Es({color:3951148}));v.position.y=-1,g.add(v),it.environment=u.fromScene(g,.04).texture,u.dispose()}let jl={time:{value:0},sunDir:{value:gi}};{let u=new _n(12e4,12e4);u.rotateX(Math.PI/2);let g=new Sn({uniforms:jl,transparent:!0,depthWrite:!1,side:ln,fog:!1,vertexShader:`#include <common>
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
        }`}),y=new Ne(u,g);y.position.y=1500,y.renderOrder=1,it.add(y)}let Ql=u=>{u.fragmentShader=u.fragmentShader.replace("#include <normal_fragment_begin>",_e.normal_fragment_begin.replace("normal *= faceDirection;",""))},th={time:{value:0}};{let[u,g]=ct(128),[y,v]=ct(128);g.fillStyle="#76844f",g.fillRect(0,0,128,128),v.fillStyle="#000",v.fillRect(0,0,128,128);for(let _t=0;_t<70;_t++){let Vt=6+o()*116,ye=(o()-.5)*34,oe=50+o()*74,at=130+o()*90;g.strokeStyle=`rgb(${at*.68|0},${at*.82|0},${at*.46|0})`,g.lineWidth=v.lineWidth=1.2+o()*2,v.strokeStyle="#fff";for(let Ct of[g,v])Ct.beginPath(),Ct.moveTo(Vt,128),Ct.quadraticCurveTo(Vt+ye*.3,128-oe*.6,Vt+ye,128-oe),Ct.stroke()}for(let _t=0;_t<6;_t++){g.fillStyle=`rgb(${170+o()*50},${150+o()*40},90)`;let Vt=10+o()*108,ye=10+o()*40;v.fillStyle="#fff";for(let oe of[g,v])oe.beginPath(),oe.ellipse(Vt,ye,2.5,7,o()-.5,0,7),oe.fill()}let E=lt(u),A=lt(y,null,!1);E.wrapS=E.wrapT=A.wrapS=A.wrapT=Ln;let D=new _n(.6,.42);D.translate(0,.2,0);let N=D.clone().rotateY(Math.PI/2),I=D.clone().rotateY(Math.PI/4),V=Ls([D,N,I]);V.setAttribute("normal",new de(new Float32Array(V.attributes.position.count*3).map((_t,Vt)=>Vt%3===1?1:0),3));let H=new Qn({map:E,alphaMap:A,alphaTest:.5,side:ln,roughness:1});H.onBeforeCompile=_t=>{_t.uniforms.time=th.time,Ql(_t),_t.vertexShader=_t.vertexShader.replace("#include <common>",`#include <common>
uniform float time;`).replace("#include <begin_vertex>",`#include <begin_vertex>
        vec4 ip = instanceMatrix * vec4(0.,0.,0.,1.);
        float sw = sin(time * 1.7 + ip.x * .23 + ip.z * .17) * .5 + sin(time * 3.1 + ip.x * .7) * .25;
        transformed.x += sw * .12 * position.y; transformed.z += sw * .06 * position.y;`)};let G=new Jr(V,H,x.grass),Q=new Ue,vt=new fe,pt=0,Yt=0;for(;pt<x.grass&&Yt++<x.grass*6;){let _t=5+Math.pow(o(),1.6)*70,Vt=o()*Math.PI*2,ye=Math.cos(Vt)*_t,oe=Math.sin(Vt)*_t;if(re(ye,oe)>.25||me(ye,oe,1.2)||ce.some(([Ct,kt,ne,$t,he])=>{let Ge=ne-Ct,Ze=$t-kt,on=Ge*Ge+Ze*Ze||1,cn=On(((ye-Ct)*Ge+(oe-kt)*Ze)/on,0,1);return Math.hypot(ye-Ct-Ge*cn,oe-kt-Ze*cn)<he+.5}))continue;let at=.6+o()*.9;Q.compose(new O(ye,tt(ye,oe)-.02,oe),new kn().setFromEuler(new ss(0,o()*6.3,0)),new O(at,at*(.7+o()*.6),at)),G.setMatrixAt(pt,Q),G.setColorAt(pt,vt.setHSL(.19+o()*.05,.25+o()*.15,.42+o()*.16)),pt++}G.count=pt,G.receiveShadow=!0,it.add(G)}{let[u,g]=ct(128),[y,v]=ct(128);g.fillStyle="#4d6a2c",g.fillRect(0,0,128,128),v.fillStyle="#000",v.fillRect(0,0,128,128);for(let _t=0;_t<1500;_t++){let Vt=80+o()*100,ye=o()*6.28,oe=Math.sqrt(o())*60,at=64+Math.cos(ye)*oe,Ct=64+Math.sin(ye)*oe,kt=3+o()*3,ne=1.5+o()*2,$t=o()*3;g.fillStyle=`rgb(${Vt*.58|0},${Vt*.9|0},${Vt*.34|0})`,v.fillStyle="#fff";for(let he of[g,v])he.beginPath(),he.ellipse(at,Ct,kt,ne,$t,0,7),he.fill()}let E=lt(u),A=lt(y,null,!1),D=new Qn({map:E,alphaMap:A,alphaTest:.5,side:ln,roughness:.9});D.onBeforeCompile=Ql;let N=new wa(1,2),I=[],V=[],H=[[62,-60],[70,-20],[-75,-55],[-85,20],[-104,72],[40,75],[95,40],[-110,-15],[20,-85],[-30,90],[120,-40],[-140,-70],[150,62],[-60,-95],[85,85],[-96,44],[58,98],[130,70],[-120,100],[10,120]],G=[Math.cos(zi.degToRad(os[0]))*0+.5,.35];for(let[_t,Vt]of H){let ye=tt(_t,Vt),oe=2.2+o()*2.2,at=_t+G[0]*oe*.45,Ct=Vt-G[1]*oe*.45,kt=ye+oe*1,ne=new tn(.12*oe/2.4,.3*oe/2.4,oe*1.05,6);ne.translate(0,oe*.52,0),ne.rotateZ(-.28),ne.rotateY(.6),ne.translate(_t,ye,Vt),V.push(ne);for(let $t=0;$t<12;$t++){let he=N.clone(),Ge=oe*(.38+o()*.3),Ze=(o()-.35)*oe*1,on=(o()-.35)*oe*.75,cn=(o()-.5)*oe*1;he.scale(Ge*1.1,Ge*.95,Ge*1.1),he.translate(at+Ze,kt+on,Ct+cn);let ve=he.attributes.position,Ve=new Float32Array(ve.count*3);for(let We=0;We<ve.count;We++){let Fn=new O(ve.getX(We)-at,(ve.getY(We)-kt)*1.4,ve.getZ(We)-Ct).normalize();Ve.set([Fn.x,Fn.y,Fn.z],We*3)}he.setAttribute("normal",new Mn(Ve,3)),I.push(he)}}let Q=Ls(I.map(_t=>_t.index?_t.toNonIndexed():_t)),vt=Q.attributes.uv;for(let _t=0;_t<vt.count;_t++)vt.setXY(_t,vt.getX(_t)*3,vt.getY(_t)*3);let pt=new Ne(Q,D);pt.castShadow=pt.receiveShadow=!0,it.add(pt);let Yt=new Ne(Ls(V),new Qn({map:gt,color:9076848,roughness:.9}));Yt.castShadow=!0,it.add(Yt);for(let[_t,Vt]of H)dn.push([_t,Vt,.5])}let eh=s?7:12,Er=[],nh=[];{let u=new Qn({color:15790057,roughness:.7,side:ln}),g=new jn;g.moveTo(0,.13),g.lineTo(.3,.11),g.lineTo(.74,-.03),g.lineTo(.6,-.08),g.lineTo(.3,-.1),g.lineTo(0,-.1);let y=new Aa(g);y.rotateX(Math.PI/2);let v=y.clone();v.scale(-1,1,1);let E=new fe(3815996),A=new fe(1,1,1);for(let I of[y,v]){let V=I.attributes.position,H=new Float32Array(V.count*3);for(let G=0;G<V.count;G++){let Q=Math.abs(V.getX(G))>.58?E:A;H.set([Q.r,Q.g,Q.b],G*3)}I.setAttribute("color",new de(H,3))}let D=u.clone();D.vertexColors=!0;let N=new Un(.065,8,6);N.scale(1,.9,3.4);for(let[I,V]of[[N,u],[y,D],[v,D]]){let H=new Jr(I,V,eh);H.frustumCulled=!1,it.add(H),Er.push(H)}for(let I=0;I<eh;I++)nh.push({c:[(o()-.5)*140,16+o()*34,(o()-.5)*140],r:25+o()*70,w:(o()<.5?-1:1)*(.09+o()*.08),a:o()*6.3,ph:o()*9})}let vo=new Ue,ih=new Ue,sh=new kn,kf=new ss,rh=new O,Gf=new O(1.4,1.4,1.4);function Vf(u){nh.forEach((g,y)=>{let v=g.a+u*g.w,E=Math.sign(g.w);rh.set(g.c[0]+Math.cos(v)*g.r,g.c[1]+Math.sin(u*.3+g.ph)*3,g.c[2]+Math.sin(v)*g.r),sh.setFromEuler(kf.set(0,Math.atan2(-Math.sin(v)*E,Math.cos(v)*E),-E*.32,"YXZ")),vo.compose(rh,sh,Gf),Er[0].setMatrixAt(y,vo);let A=Math.sin(u*7.5+g.ph)*.5*(Math.sin(u*.5+g.ph)>.25?1:.12)+.1;Er[1].setMatrixAt(y,ih.makeRotationZ(A).premultiply(vo)),Er[2].setMatrixAt(y,ih.makeRotationZ(-A).premultiply(vo))});for(let g of Er)g.instanceMatrix.needsUpdate=!0}let Yn=new Ia(16769723,3.3);Yn.position.copy(gi).multiplyScalar(120),it.add(Yn,Yn.target),Yn.castShadow=!0,Yn.shadow.mapSize.set(x.shadow,x.shadow),Object.assign(Yn.shadow.camera,{left:-38,right:38,top:38,bottom:-38,near:1,far:300}),Yn.shadow.bias=-5e-4,Yn.shadow.normalBias=.04,Yn.shadow.radius=3;let oh=new Ca(12374783,4998195,.15);it.add(oh);let ii=new rs(16747068,60,0,2);ii.position.set(Wn,1,xe),it.add(ii),x.fireShadow&&(ii.castShadow=!0,ii.shadow.mapSize.set(512,512),ii.shadow.bias=-.004,ii.shadow.camera.near=.3,ii.shadow.camera.far=22,ii.shadow.radius=4);let ah=new rs(16754784,9,0,2);ah.position.set(Xn+2.4,2.4,xe),it.add(ah);let Wa=new rs(16751178,6,0,2);Wa.position.set(Nn[2],3.4,xe),it.add(Wa);let Xa=new rs(16747068,22,0,2);Xa.position.set(pi,.9,mi),it.add(Xa);let Ya=new rs(16749638,9,0,2);Ya.position.set(-2.4,1.1,-19.4),it.add(Ya);let ch={time:{value:0}},Wf=new Sn({uniforms:ch,transparent:!0,depthWrite:!1,blending:hr,vertexShader:`#include <common>
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
      }`});function Xf(u,g){let y=new lo,v=new _n(1,1);v.translate(0,.5,0),y.setIndex(v.index),y.setAttribute("position",v.attributes.position),y.setAttribute("uv",v.attributes.uv),y.setAttribute("off",new Oi(new Float32Array(u.flat()),4)),y.instanceCount=u.length;let E=new Ne(y,g);return E.frustumCulled=!1,E.renderOrder=3,it.add(E),E}let wr=[];for(let u=0;u<6;u++)wr.push([Wn+(o()-.5)*.7,.02,xe+(o()-.5)*.5,.7+o()*.4]);for(let u=0;u<3;u++)wr.push([pi+(o()-.5)*.4,.02,mi+(o()-.5)*.4,.45+o()*.2]);for(let[u,g]of ql)wr.push([u,3.25,g,.3]);wr.push([-2.4,.66,-19.4,.32]),Xf(wr,Wf);let lh=new Es({color:16734746});{let u=new Ne(new gr(.8,20).rotateX(-Math.PI/2),lh);u.scale.set(1.2,1,1),u.position.set(Wn,.04,xe),it.add(u);let g=u.clone();g.scale.set(.55,1,.55),g.position.set(pi,.04,mi),it.add(g);let y=[];for(let E=0;E<6;E++)y.push(new tn(.07,.09,1.2,6).rotateZ(Math.PI/2-.18).rotateY(E*1.05).translate(Wn,.14,xe));let v=new Ne(Ls(y),new Qn({color:2759184,emissive:4198916,roughness:1}));it.add(v)}let qa={time:{value:0},light:{value:1}},Yf=new Sn({uniforms:qa,transparent:!0,depthWrite:!1,vertexShader:`#include <common>
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
      }`});{let u=new _n(1,1),g=new lo;g.setIndex(u.index),g.setAttribute("position",u.attributes.position),g.setAttribute("uv",u.attributes.uv);let y=[],v=[];for(let A=0;A<26;A++)y.push(Wn,1.2,xe,A/26),v.push(7.6,.4,9);for(let A=0;A<18;A++)y.push(Wn+.5,ze.ridge+1.4,xe,A/18),v.push(14,6,14);for(let A=0;A<14;A++)y.push(pi+1.5,Vi.ridge+1.3,mi,A/14),v.push(12,5,12);for(let[A,D]of $l.slice(0,4))for(let N=0;N<6;N++)y.push(A,tt(A,D)+4.6,D,N/6),v.push(10,4,10);g.setAttribute("off",new Oi(new Float32Array(y),4)),g.setAttribute("rise",new Oi(new Float32Array(v),3)),g.instanceCount=y.length/4;let E=new Ne(g,Yf);E.frustumCulled=!1,E.renderOrder=4,it.add(E)}let Za={time:{value:0},k:{value:1}};{let u=new Sn({uniforms:Za,transparent:!0,depthWrite:!1,blending:hr,side:ln,vertexShader:`#include <common>
#include <logdepthbuf_pars_vertex>
varying float vL;varying vec2 vU;varying vec3 vN,vV;void main(){vU=uv;vL=position.z;vN=normalMatrix*normal;vec4 mv=modelViewMatrix*vec4(position,1.);vV=mv.xyz;gl_Position=projectionMatrix*mv;
#include <logdepthbuf_vertex>
}`,fragmentShader:`#include <logdepthbuf_pars_fragment>
uniform float time,k;varying float vL;varying vec2 vU;varying vec3 vN,vV;void main(){
#include <logdepthbuf_fragment>
float a=(1.-smoothstep(0.,1.,vL))*smoothstep(0.,.08,vL);float e=smoothstep(0.,.25,vU.x)*smoothstep(1.,.75,vU.x);a*=smoothstep(.12,.85,abs(dot(normalize(vN),normalize(-vV))))*smoothstep(.6,3.,length(vV));gl_FragColor=vec4(vec3(1.,.86,.62)*a*e*.05*k,1.);
        #include <tonemapping_fragment>
        #include <colorspace_fragment>
      }`}),g=[],y=gi.clone().negate(),v=(E,A,D,N,I,V,H)=>{if(gi.x*V+gi.z*H<=.05)return;let G=Math.min(9,(A+I*.5)/Math.max(.15,-y.y))*1.15,Q=new Pe(N,I,1,1,1,1);Q.translate(0,0,.5);let vt=Q.attributes.position;for(let _t=0;_t<vt.count;_t++){let Vt=vt.getZ(_t);vt.setXYZ(_t,vt.getX(_t),vt.getY(_t),Vt)}let pt=new Ne(Q,u),Yt=new Ue().lookAt(new O(0,0,0),y.clone().multiplyScalar(-1),new O(0,1,0));pt.quaternion.setFromRotationMatrix(Yt),pt.scale.set(1,1,G),pt.position.set(E,A,D),pt.renderOrder=2,it.add(pt),g.push(pt)};for(let E of bi)E.x<6&&E.z<-4&&E.y<6&&v(E.x-E.nx*.3,E.y,E.z-E.nz*.3,E.w*.9,E.h*.85,E.nx,E.nz);v(ze.x0+.45,4.9,xe,.7,1.2,-1,0),v(-4.4,1.9,ei.z1-.45,.6,.9,0,1),v(-1.6,1.9,ei.z1-.45,.6,.9,0,1),v(-4.4,1.9,ei.z1-.45,.01,.01,0,1)}let hh=[];for(let u=0;u<160;u++)hh.push(Wn-7+o()*14,.3+o()*4.5,xe-4+o()*8);let $a=new va(new Ke().setAttribute("position",new de(hh,3)),new Kr({color:16767392,size:.022,transparent:!0,opacity:.55,depthWrite:!1,blending:hr}));it.add($a);let qn=t.stops.filter(u=>yr[u.id]),Ja=[],qf=new Qn({color:15909198,emissive:13144090,emissiveIntensity:1.4,roughness:.3,metalness:.4});qn.forEach((u,g)=>{let[[y,v],[E,A,D]]=yr[u.id],N=E-y,I=D-v,V=Math.hypot(N,I),H=new Ne(new Ta(.16),qf),G=y+N/V*1.8,Q=v+I/V*1.8;H.position.set(G,tt(G,Q)+2.05,Q),H.userData.i=g,H.userData.y=H.position.y,it.add(H),Ja.push(H)});let Et={x:70,z:6,yaw:Math.PI/2,pitch:0,vx:0,vz:0},yn={yaw:Et.yaw,pitch:0},Zf=(u,g)=>u>ze.ix0-.1&&u<ze.ix0+fo&&g>ze.iz0&&g<ze.iz1,Ka=(u,g)=>1.62+(Zf(u,g)?.32:0)+tt(u,g);function $f(u,g){for(let E=0;E<2;E++){for(let[A,D,N,I,V]of ce){let H=N-A,G=I-D,Q=H*H+G*G||1e-6,vt=On(((u-A)*H+(g-D)*G)/Q,0,1),pt=A+H*vt,Yt=D+G*vt,_t=u-pt,Vt=g-Yt,ye=Math.hypot(_t,Vt),oe=.32+V;ye<oe&&ye>1e-6&&(u=pt+_t/ye*oe,g=Yt+Vt/ye*oe)}for(let[A,D,N]of dn){let I=u-A,V=g-D,H=Math.hypot(I,V),G=.32+N;H<G&&H>1e-6&&(u=A+I/H*G,g=D+V/H*G)}}let v=Math.hypot(u,g);return v>260&&(u*=260/v,g*=260/v),[u,g]}let Jf=(u,g,y,v)=>ce.some(([E,A,D,N,I])=>{let V=(y-u)*(N-A)-(v-g)*(D-E);if(Math.abs(V)<1e-9)return!1;let H=((E-u)*(N-A)-(A-g)*(D-E))/V,G=((E-u)*(v-g)-(A-g)*(y-u))/V;return H>0&&H<1&&G>=0&&G<=1&&I>.1}),Ae=null,be=null,_i=!0;function Tr(){if(Ae){_i&&Ae.state==="suspended"&&Ae.resume();return}if(!_i)return;try{Ae=new(window.AudioContext||window.webkitAudioContext)}catch{return}let u=Ae.sampleRate,g=Ae.createBuffer(1,u*4,u),y=g.getChannelData(0),v=0,E=0,A=0;for(let Q=0;Q<y.length;Q++){let vt=Math.random()*2-1;v=.99765*v+vt*.099,E=.963*E+vt*.2965,A=.57*A+vt*1.0527,y[Q]=(v+E+A+vt*.1848)*.2}let D=Ae.createGain();D.gain.value=.9,D.connect(Ae.destination);let N=(Q,vt,pt="bandpass")=>{let Yt=Ae.createBufferSource();Yt.buffer=g,Yt.loop=!0,Yt.playbackRate.value=.5+Math.random()*.1;let _t=Ae.createBiquadFilter();_t.type=pt,_t.frequency.value=Q,_t.Q.value=vt;let Vt=Ae.createGain();return Vt.gain.value=0,Yt.connect(_t),_t.connect(Vt),Vt.connect(D),Yt.start(),{g:Vt,f:_t}},I=N(500,.6),V=N(260,.4,"lowpass"),H=N(180,.7,"lowpass"),G=[N(420,1.4),N(950,1.6)];be={wind:I,sea:V,rumble:H,master:D,talk:G,crackT:0,harpT:2,note:0,talkT:0,larkT:3,larkOn:0,gullT:4,bleatT:5,barkT:6}}function Kf(u){let g=.02+Math.random()*.05,y=Ae.createBuffer(1,Math.ceil(Ae.sampleRate*g),Ae.sampleRate),v=y.getChannelData(0);for(let N=0;N<v.length;N++)v[N]=(Math.random()*2-1)*Math.pow(1-N/v.length,3);let E=Ae.createBufferSource();E.buffer=y;let A=Ae.createBiquadFilter();A.type="highpass",A.frequency.value=900+Math.random()*2500;let D=Ae.createGain();D.gain.value=u*(.2+Math.random()*.5),E.connect(A),A.connect(D),D.connect(be.master),E.start()}function yo(u,g,y,v,E,A,D=2,N=0){let I=Ae.currentTime,V=Ae.createOscillator(),H=Ae.createGain(),G=Ae.createBiquadFilter();if(V.type=u,V.frequency.setValueAtTime(g,I),V.frequency.exponentialRampToValueAtTime(y,I+v*.7),N){let Q=Ae.createOscillator(),vt=Ae.createGain();Q.frequency.value=7+Math.random()*2,vt.gain.value=N,Q.connect(vt),vt.connect(V.frequency),Q.start(I),Q.stop(I+v+.05)}G.type="bandpass",G.frequency.value=A||g,G.Q.value=D,H.gain.setValueAtTime(0,I),H.gain.linearRampToValueAtTime(E,I+Math.min(.03,v*.2)),H.gain.exponentialRampToValueAtTime(5e-4,I+v),V.connect(G),G.connect(H),H.connect(be.master),V.start(I),V.stop(I+v+.05)}let uh=[146.83,164.81,174.61,196,220,246.94,261.63,293.66,329.63,349.23,392],fh=[7,5,4,5,7,7,8,7,5,4,2,4,5,4,2,0,2,4,5,7,5,4,2,4];function dh(u,g){let y=Ae.sampleRate,v=Math.round(y/u),E=Math.ceil(y*2.6),A=Ae.createBuffer(1,E,y),D=A.getChannelData(0),N=new Float32Array(v);for(let Q=0;Q<v;Q++)N[Q]=Math.random()*2-1;let I=0;for(let Q=0;Q<E;Q++){let vt=(I+1)%v,pt=(N[I]+N[vt])*.4985;D[Q]=N[I],N[I]=pt,I=vt}let V=Ae.createBufferSource();V.buffer=A;let H=Ae.createGain();H.gain.value=g;let G=Ae.createBiquadFilter();G.type="lowpass",G.frequency.value=2600,V.connect(G),G.connect(H),H.connect(be.master),V.start()}function jf(u){if(!Ae||!be)return;let g=Ae.currentTime,y=fs,v=Math.hypot(Et.x-Wn,Et.z-xe),E=Math.hypot(Et.x-pi,Et.z-mi),A=Math.max(Ar?On(1.4-v/9,0,1):0,On(1-E/7,0,1)*(nc?1:.3));if(be.wind.g.gain.setTargetAtTime((1-y*.8)*(.32+.18*Math.sin(g*.23)+.1*Math.sin(g*.71)),g,.4),be.wind.f.frequency.setTargetAtTime(380+160*Math.sin(g*.17),g,.5),be.sea.g.gain.setTargetAtTime((1-y*.7)*(.25+.15*Math.sin(g*.45)),g,.5),be.rumble.g.gain.setTargetAtTime(A*.7,g,.3),be.crackT-=u,be.crackT<0&&A>.02&&(Kf(A),be.crackT=Math.random()*.22),be.talkT-=u,be.talkT<0){be.talkT=.1+Math.random()*.16;let I=Ar?.3:0;be.talk[0].g.gain.setTargetAtTime(I*(.25+Math.random()*.75),g,.05),be.talk[1].g.gain.setTargetAtTime(I*.45*Math.random(),g,.04)}let D=1-y;if(D>.3){if(be.larkT-=u,be.larkT<0&&(be.larkOn<=0&&(be.larkOn=1.5+Math.random()*3),be.larkOn-=u,yo("sine",2600+Math.random()*2600,2600+Math.random()*3200,.05+Math.random()*.06,.022*D,0,.7),be.larkT=be.larkOn>0?.05+Math.random()*.09:2.5+Math.random()*5),be.gullT-=u,be.gullT<0){let V=1+(Math.random()*3|0);for(let H=0;H<V;H++)setTimeout(()=>Ae&&yo("sawtooth",760,1250,.32,.028*D,1500,3),H*380);be.gullT=7+Math.random()*12}let I=Math.hypot(Et.x+82,Et.z-58);if(be.bleatT-=u,be.bleatT<0){let V=On(1.3-I/90,0,1)*D;V>.02&&yo("sawtooth",290+Math.random()*60,250+Math.random()*40,.7,.05*V,1e3,2.5,18),be.bleatT=4+Math.random()*9}}let N=Math.hypot(Et.x-33,Et.z-20);if(be.barkT-=u,be.barkT<0){let I=On(1.2-N/60,0,1)*(1-y*.7);if(I>.03){let V=1+(Math.random()*3|0);for(let H=0;H<V;H++)setTimeout(()=>Ae&&yo("square",420,240,.16,.045*I,700,1.5),H*260)}be.barkT=8+Math.random()*16}if(Ar&&(be.harpT-=u,be.harpT<0)){let I=fh[be.note++%fh.length],V=On(1.2-Math.hypot(Et.x+17.3,Et.z+13.6)/12,.15,1)*.5;dh(uh[I],V),be.note%4===1&&dh(uh[Math.max(0,I-4)]/2,V*.55),be.harpT=(be.note%8===0?1.1:.52)*(1+(Math.random()-.5)*.08)}}let wi=document.createElement("div");wi.className="ll-ui";let si=u=>String(u).replace(/[&<>"]/g,g=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"})[g]);wi.innerHTML='<div class="ll-panel" hidden><p class="ll-n"></p><h2 tabindex="-1"></h2><div class="ll-txt"></div><p class="ll-src"></p><div class="ll-btns"><button type="button" class="btn" data-k="prev">\u2190 '+si(n(t.ui.prev))+'</button><button type="button" class="btn solid" data-k="next">'+si(n(t.ui.next))+' \u2192</button><button type="button" class="ll-x" data-k="close" aria-label="'+si(n(t.ui.close))+'">\xD7</button></div></div><div class="ll-bar"><button type="button" class="btn solid" data-k="tour">'+si(n(t.ui.tour))+' \u2192</button><button type="button" class="btn" data-k="snd" aria-pressed="'+_i+'"></button><button type="button" class="btn" data-k="fs">'+si(n(t.ui.fs))+'</button><span class="ll-help">'+si(n(r?t.ui.helpTouch:t.ui.help))+'</span></div><canvas class="ll-plan" width="200" height="160" aria-hidden="true"></canvas><div class="ll-stick" aria-hidden="true"><i></i></div><div class="ll-fade"></div>',i.appendChild(wi);let xi=wi.querySelector(".ll-panel"),hs=wi.querySelector(".ll-stick"),ph=hs.querySelector("i"),mh=wi.querySelector(".ll-fade"),gh=wi.querySelector('[data-k="snd"]'),_h=()=>{gh.textContent=(_i?"\u266A ":"")+n(_i?t.ui.soundOff:t.ui.soundOn),gh.setAttribute("aria-pressed",_i)};_h();let ri=-1,ja=-1,Oe=null;function xh(u){ri=u;let g=qn[u];xi.hidden=!1,xi.scrollTop=0,xi.querySelector(".ll-n").textContent=n(t.ui.stop).replace("{n}",u+1).replace("{of}",qn.length),xi.querySelector("h2").textContent=n(g.t),xi.querySelector(".ll-txt").innerHTML=n(g.p).map(v=>"<p>"+si(v)+"</p>").join("");let y=xi.querySelector(".ll-src");y.innerHTML=g.src&&g.src.length?si(n(t.ui.sources))+": "+g.src.map(v=>v.url?`<a href="${si(v.url)}" target="_blank" rel="noopener">${si(n(v.t))}</a>`:si(n(v.t))).join(" \xB7 "):"",xi.querySelector('[data-k="prev"]').disabled=u===0,xi.querySelector('[data-k="next"]').textContent=(u===qn.length-1?n(t.ui.again):n(t.ui.next))+" \u2192"}let Mo=!1;function us(u,g){Et.fov=0,u=(u+qn.length)%qn.length;let[[y,v],[E,A,D]]=yr[qn[u].id],N=Math.atan2(-(E-y),-(D-v)),I=Math.atan2(A-Ka(y,v),Math.hypot(E-y,D-v)),V=N-Et.yaw;for(;V>Math.PI;)V-=2*Math.PI;for(;V<-Math.PI;)V+=2*Math.PI;let H=g||a||Jf(Et.x,Et.z,y,v)||Math.hypot(y-Et.x,v-Et.z)>90;Oe={t:0,dur:H?.9:Math.min(3.4,1+Math.hypot(y-Et.x,v-Et.z)/12),jump:H,from:{...Et},to:{x:y,z:v,yaw:Et.yaw+V,pitch:I}},g&&(Object.assign(Et,Oe.to),yn.yaw=Et.yaw,yn.pitch=Et.pitch,Oe=null,Mo=!0),xh(u),ja=-1}wi.addEventListener("click",u=>{let g=u.target.closest("button");if(!g)return;let y=g.dataset.k;y==="tour"||y==="next"?us(ri+1):y==="prev"?us(ri-1):y==="close"?(xi.hidden=!0,ja=ri,l.focus({preventScroll:!0})):y==="snd"?(_i=!_i,_h(),_i?Ae?Ae.resume():Tr():Ae&&Ae.suspend()):y==="fs"&&(document.fullscreenElement?document.exitFullscreen():i.requestFullscreen&&i.requestFullscreen().catch(()=>{}))});let Qa=wi.querySelector(".ll-plan"),Te=Qa.getContext("2d"),vh=1.85,Fs=(u,g)=>[100+u*vh,80+g*vh*1];function Qf(){Te.clearRect(0,0,200,160),Te.fillStyle="rgba(8,10,16,.62)",Te.fillRect(0,0,200,160),Te.strokeStyle="rgba(230,220,200,.75)",Te.lineWidth=2.2,Te.beginPath(),ti.forEach(([y,v],E)=>{let[A,D]=Fs(y,v);E?Te.lineTo(A,D):Te.moveTo(A,D)}),Te.closePath(),Te.stroke(),Te.fillStyle="rgba(230,220,200,.45)";for(let y of ie){if(y[2]-y[0]>40)continue;let[v,E]=Fs(y[0],y[1]),[A,D]=Fs(y[2],y[3]);Te.fillRect(v,E,A-v,D-E)}qn.forEach((y,v)=>{let[[E,A]]=yr[y.id];if(Math.abs(E)>50||Math.abs(A)>40)return;let[D,N]=Fs(E,A);Te.fillStyle=v===ri?"#fff":"#f2c14e",Te.beginPath(),Te.arc(D,N,3.2,0,7),Te.fill()});let[u,g]=Fs(On(Et.x,-52,52),On(Et.z,-42,42));Te.save(),Te.translate(u,g),Te.rotate(-Et.yaw),Te.fillStyle="#e8483f",Te.beginPath(),Te.moveTo(0,-7),Te.lineTo(5,5),Te.lineTo(0,2),Te.lineTo(-5,5),Te.closePath(),Te.fill(),Te.restore(),Te.fillStyle="rgba(230,220,200,.85)",Te.font="600 10px system-ui, sans-serif",Te.fillText(e?"G":"N",188,14),Te.beginPath(),Te.moveTo(191,18),Te.lineTo(191,30),Te.strokeStyle="rgba(230,220,200,.85)",Te.lineWidth=1.2,Te.stroke()}Qa.addEventListener("click",u=>{let g=Qa.getBoundingClientRect(),y=(u.clientX-g.left)/g.width*200,v=(u.clientY-g.top)/g.height*160,E=-1,A=14;qn.forEach((D,N)=>{let[[I,V]]=yr[D.id],[H,G]=Fs(I,V),Q=Math.hypot(H-y,G-v);Q<A&&(A=Q,E=N)}),E>=0&&us(E)});let Rn={};l.addEventListener("keydown",u=>{let g=u.key.toLowerCase();["w","a","s","d","arrowup","arrowdown","arrowleft","arrowright","q","e","shift"].includes(g)&&(Rn[g]=1,u.preventDefault(),Oe=null),g==="n"&&us(ri+1),Tr()}),l.addEventListener("keyup",u=>{Rn[u.key.toLowerCase()]=0}),l.addEventListener("blur",()=>{for(let u in Rn)Rn[u]=0});let oi=null,yh=new La,Mh=new St;l.addEventListener("pointerdown",u=>{oi={id:u.pointerId,x:u.clientX,y:u.clientY,moved:0},l.setPointerCapture(u.pointerId),l.focus({preventScroll:!0}),Tr()}),l.addEventListener("pointermove",u=>{if(!oi||oi.id!==u.pointerId)return;let g=u.clientX-oi.x,y=u.clientY-oi.y;oi.x=u.clientX,oi.y=u.clientY,oi.moved+=Math.abs(g)+Math.abs(y);let v=u.pointerType==="touch"?.0062:.0045;Oe&&(yn.yaw=Et.yaw,yn.pitch=Et.pitch,Oe=null),yn.yaw+=g*v,yn.pitch=On(yn.pitch+y*v,-1.25,1.25)}),l.addEventListener("pointerup",u=>{if(oi&&oi.moved<6){let g=l.getBoundingClientRect();Mh.set((u.clientX-g.left)/g.width*2-1,-(u.clientY-g.top)/g.height*2+1),yh.setFromCamera(Mh,nt);let y=yh.intersectObjects(Ja)[0];y&&us(y.object.userData.i)}oi=null});let Os={x:0,y:0},So=null,Sh=u=>{let g=hs.getBoundingClientRect(),y=g.left+g.width/2,v=g.top+g.height/2,E=(u.clientX-y)/(g.width/2),A=(u.clientY-v)/(g.height/2),D=Math.hypot(E,A);D>1&&(E/=D,A/=D),Os.x=E,Os.y=A,ph.style.transform=`translate(${E*34}px,${A*34}px)`};hs.addEventListener("pointerdown",u=>{So=u.pointerId,hs.setPointerCapture(So),Sh(u),Oe&&(yn.yaw=Et.yaw,yn.pitch=Et.pitch,Oe=null),u.preventDefault(),Tr()}),hs.addEventListener("pointermove",u=>{u.pointerId===So&&Sh(u)});let bh=()=>{So=null,Os.x=Os.y=0,ph.style.transform=""};hs.addEventListener("pointerup",bh),hs.addEventListener("pointercancel",bh);let Eh={value:0};{let u=`uniform float ctime;
float csH(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}
float csN(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(csH(i),csH(i+vec2(1.,0.)),f.x),mix(csH(i+vec2(0.,1.)),csH(i+vec2(1.,1.)),f.x),f.y);}
float cloudShade(vec3 v){vec3 w=(vec4(v-viewMatrix[3].xyz,0.)*viewMatrix).xyz;vec2 p=(w.xz+ctime*vec2(-6.5,4.5))/520.+vec2(3.7,1.3);
float n=csN(p)*.55+csN(p*2.07+3.1)*.3+csN(p*4.3+7.7)*.15;return smoothstep(.55,.7,n);}
`,g=_e.lights_fragment_begin.replace("getDirectionalLightInfo( directionalLight, directLight );",`getDirectionalLightInfo( directionalLight, directLight );
		directLight.color *= csh;`),y=new Set;it.traverse(v=>{for(let E of[].concat(v.material||[])){if(!E.isMeshStandardMaterial||y.has(E))continue;y.add(E);let A=E.onBeforeCompile,D=A&&A!==yi.prototype.onBeforeCompile?A.toString():"";E.onBeforeCompile=(N,I)=>{D&&A.call(E,N,I),N.uniforms.ctime=Eh,N.fragmentShader=u+N.fragmentShader.replace("#include <lights_fragment_begin>",`float cmask = cloudShade(-vViewPosition), csh = 1. - .72 * cmask;
`+g).replace("#include <aomap_fragment>",`reflectedLight.indirectDiffuse *= 1. - .3 * cmask; reflectedLight.indirectSpecular *= 1. - .3 * cmask;
#include <aomap_fragment>`)},E.customProgramCacheKey=()=>D+"|cs",E.needsUpdate=!0}})}function bo(){let u=i.clientWidth,g=i.clientHeight;h.setSize(u,g,!1),nt.aspect=u/g,nt.updateProjectionMatrix()}bo(),new ResizeObserver(bo).observe(i);let tc=!0;new IntersectionObserver(u=>{tc=u[0].isIntersecting,tc&&(ec=performance.now())}).observe(i);let ec=performance.now(),nn=0,fs=0,Ar=!1,nc=!1,Eo=0,wo=0,wh=0,ic=new O,sc=new O;function Th(u){if(requestAnimationFrame(Th),!tc||document.hidden)return;let g=Math.min(.5,(u-ec)/1e3),y=Math.min(.05,g);ec=u,nn+=y,g>.034?(Eo+=g,wo=0):g<.019&&(wo+=g,Eo=0),Eo>1.2&&d>.6&&(d=Math.max(.6,d-.15),h.setPixelRatio(d),bo(),Eo=0),wo>4&&d<f&&(d=Math.min(f,d+.1),h.setPixelRatio(d),bo(),wo=0);let v=0;if(Oe){Oe.t+=g/Oe.dur;let H=Oe.t>=1?1:(1-Math.cos(Math.PI*Oe.t))/2;Oe.jump?(mh.style.opacity=String(Math.sin(Math.min(1,Oe.t)*Math.PI)),Oe.t>=.5&&!Oe.done&&(Object.assign(Et,Oe.to),Oe.done=!0,nt.position.y=Ka(Et.x,Et.z))):["x","z","yaw","pitch"].forEach(G=>{Et[G]=Oe.from[G]+(Oe.to[G]-Oe.from[G])*H}),Oe.t>=1&&(Object.assign(Et,Oe.to),Oe=null,mh.style.opacity="0"),yn.yaw=Et.yaw,yn.pitch=Et.pitch,Et.vx=Et.vz=0}else{let H=1-Math.exp(-y*16);Et.yaw+=(yn.yaw-Et.yaw)*H,Et.pitch+=(yn.pitch-Et.pitch)*H,(Rn.arrowleft||Rn.q)&&(yn.yaw+=1.8*y),(Rn.arrowright||Rn.e)&&(yn.yaw-=1.8*y);let G=Rn.shift?2.1:1,Q=(Rn.w||Rn.arrowup?1:0)-(Rn.s||Rn.arrowdown?1:0)-Os.y,vt=(Rn.d?1:0)-(Rn.a?1:0)+Os.x,pt=Math.max(1,Math.hypot(Q,vt));Q/=pt,vt/=pt;let Yt=(-Math.sin(Et.yaw)*Q+Math.cos(Et.yaw)*vt)*3.3*G,_t=(-Math.cos(Et.yaw)*Q-Math.sin(Et.yaw)*vt)*3.3*G,Vt=1-Math.exp(-y*9);Et.vx+=(Yt-Et.vx)*Vt,Et.vz+=(_t-Et.vz)*Vt;let ye=Math.hypot(Et.vx,Et.vz);ye>.02&&([Et.x,Et.z]=$f(Et.x+Et.vx*y,Et.z+Et.vz*y),v=Math.min(1,ye/3.3)),qn.forEach((oe,at)=>{let[[Ct,kt]]=yr[oe.id];at!==ri&&at!==ja&&Math.hypot(Et.x-Ct,Et.z-kt)<1.8&&xh(at)})}wh+=y*9*v;let E=Et.hy!=null?Et.hy:Ka(Et.x,Et.z)+(a?0:Math.sin(wh)*.025*v);nt.position.set(Et.x,nt.position.y?nt.position.y+(E-nt.position.y)*Math.min(1,y*10):E,Et.z),nt.rotation.set(Et.pitch,Et.yaw,0);let A=Et.fov||(s?68:60)-(ri>=0&&(qn[ri].id==="wall"||qn[ri].id==="sands")&&!Oe?s?38:42:0);Mo&&(nt.fov=A,nt.updateProjectionMatrix(),Mo=!1),Math.abs(nt.fov-A)>.05&&(nt.fov+=(A-nt.fov)*Math.min(1,y*2.5),nt.updateProjectionMatrix());let D=me(Et.x,Et.z,-.3);Ar=nc=!1,D&&(Ar=Et.x>ze.x0&&Et.x<ze.x1&&Et.z>ze.z0&&Et.z<ze.z1,nc=Et.x>Vi.x0&&Et.x<Vi.x1&&Et.z>Vi.z0&&Et.z<Vi.z1),fs+=((D?1:0)-fs)*Math.min(1,y*2.2),h.toneMappingExposure=.62+fs*.38;let N=1-fs*.82;for(let H of Xt)H.envMapIntensity=N;oh.intensity=.15*N,qa.light.value=.35+(1-fs)*.65,Za.k.value=.25+fs*.45,ic.set(Et.x,0,Et.z);let I=76/x.shadow;sc.set(Math.round(ic.x/I)*I,0,Math.round(ic.z/I)*I),Yn.target.position.copy(sc),Yn.position.copy(sc).addScaledVector(gi,120),Yn.target.updateMatrixWorld();let V=1+Math.sin(nn*11)*.07+Math.sin(nn*23.7)*.05+(Math.random()-.5)*.09;ii.intensity=60*V,Xa.intensity=22*V,Wa.intensity=6*(1+Math.sin(nn*13)*.08),Ya.intensity=9*(1+Math.sin(nn*9.3)*.07),ii.position.x=Wn+Math.sin(nn*7)*.05,ii.position.z=xe+Math.cos(nn*9)*.05,lh.color.setRGB(1,.3+Math.sin(nn*3)*.04,.08),ch.time.value=nn,qa.time.value=nn,Kl.time.value=nn,jl.time.value=nn,th.time.value=nn,Za.time.value=nn,Eh.value=nn,Vf(nn),$a.rotation.y=Math.sin(nn*.05)*.02,$a.position.y=Math.sin(nn*.3)*.05,Ja.forEach((H,G)=>{H.rotation.y=nn*1.4+G,H.position.y=H.userData.y+Math.sin(nn*2+G)*.06,H.visible=G!==ri||!!Oe}),jf(y),(nn*10|0)%2===0&&Qf(),h.render(it,nt)}i.classList.add("ready"),nt.position.y=0,l.focus({preventScroll:!0}),_i&&Tr();let Ah={dem:X,ground:tt,goStop:(u,g)=>us(u,g),renderer:h,me:Et,view:(u,g,y,v,E,A,D)=>{xi.hidden=!0,Et.fov=D||0,Mo=!0,Oe=null,Et.x=u,Et.z=y,Et.hy=g,nt.position.y=g,Et.yaw=yn.yaw=Math.atan2(-(v-u),-(A-y)),Et.pitch=yn.pitch=Math.atan2(E-g,Math.hypot(v-u,A-y))}};return requestAnimationFrame(Th),setTimeout(()=>us(0),300),window.LLYS3D=Ah,Ah}export{ev as start};
/*! Bundled license information:

three/build/three.module.js:
  (**
   * @license
   * Copyright 2010-2023 Three.js Authors
   * SPDX-License-Identifier: MIT
   *)
*/
