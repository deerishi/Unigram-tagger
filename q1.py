import sys
tagnos=[0.0,0.0,0.0]
taglist=['O','_RARE_','I-GENE']
def main():
	f2=open('unigram.txt','r')
	for line in f2:
		p=line.split()
		
		c1=float(p[0])
		i=0
		#print p[2]
		while(i<3):	
			if(p[2]==taglist[i]):
				tagnos[i]=tagnos[i]+c1
			i=i+1
	pi_prob=[]
	#print 'tag count is=',tagnos
	f=open('gene.test','r')
	f3=open('gene_test.p1.out','w')
	for line2 in f:
		p=line2.split()
		for w in p:	
			line=w
			break
		if(line2=='\n'):
			f3.write(line2)
		else:
			for v in taglist:
				e=emission(line,v)
				pi_prob.append(e)
			max_prob=max(pi_prob)
			if(max_prob==0):
				x=line+' '+taglist[1]+'\n'
				f3.write(x)
				del pi_prob[:]	
			else:
				index_v=pi_prob.index(max_prob)
				x=line+' '+taglist[index_v]+'\n'	
				f3.write(x)
				del pi_prob[:]
	f.close()
	f3.close()	
				
				
					
def emission(w,v):
	f5=open('unigram.txt','r+')
	c1=0
	#print 'w=%s v=%s'%(w,v)
	for line in f5:
		p=line.split()
		#if(w=="heart"):
			#print 'in heart'
		if(p[3]==w and p[2]==v):
			c1=float(p[0])
			#print '\tfound seq in emi c1=%f'%(c1)
			break
	i=taglist.index(v)
	f5.close()
	if(c1==0):
		return 0.0
	else:
		x=float(c1)/tagnos[i]		
		return x
	
if __name__=='__main__':
	main()		
		
		
	
