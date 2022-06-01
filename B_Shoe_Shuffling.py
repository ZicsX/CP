for s in[*open(0)][2::2]:
 *r,=range(1,len(a:=s.split()+[0]));i=j=0;p=a[0]
 for x in a:
  if x!=p:
   if j-i<2:r=-1,;break
   r[i:j]=r[i+1:j]+[r[i]];i=j;p=x
  j+=1
 print(*r)