a =0
print('''Attraverso questo programma potrai trovare la soluzione di sistemi a 2 o 3 incognite:
dovrai inserire solamente i coefficienti, la struttura dell\'equazione sarà x+y=termine noto''')
while a == 0:
	print()
	n=input('innanzitutto scegli numero di incognite e di equazioni:  ')
	if n == '2':
		print()
		print('PRIMA EQUAZIONE')
		x1=input('inserisci il coefficiente della x: ')
		y1=input('inserisci il coefficiente della y: ')
		t1=input('inserisci il coefficiente del termine noto: ')

		if int(y1)<0:
			print('la 1 equazione è:',x1,'x',y1,'y =',t1)
		else:
			print('la 1 equazione è:',x1,'x','+',y1,'y =',t1)	

		print()
		print('SECONDA EQUAZIONE')
		x2=input('inserisci il coefficiente della x: ')
		y2=input('inserisci il coefficiente della y: ')
		t2=input('inserisci il coefficiente del termine noto: ')

		if int(y2)<0:
			print('la 2 equazione è:',x2,'x',y2,'y =',t2)
		else:
			print('la 2 equazione è:',x2,'x','+',y2,'y =',t2)

		r_coeff1=[int(x1),int(x2)]
		r_coeff2=[int(y1),int(y2)]
		r_t_noto=[(int(t1)),int(t2)]

		def DETERMINANTE(colonna1, colonna2):
			risultato=(int(colonna1[0])*int(colonna2[1]))-(int(colonna1[1])*int(colonna2[0]))
			return risultato

		D= DETERMINANTE(r_coeff1, r_coeff2)
		Dx= DETERMINANTE(r_t_noto, r_coeff2)
		Dy= DETERMINANTE(r_coeff1, r_t_noto)

		print('x =', Dx/D)
		print('y =', Dy/D)
		a = 1

	elif n == '3':
		print()
		print('PRIMA EQUAZIONE')
		x1=input('inserisci il coefficiente della x: ')
		y1=input('inserisci il coefficiente della y: ')
		z1=input('inserisci il coefficiente della z: ')
		t1=input('inserisci il coefficiente del termine noto: ')

		if int(y1)<0:
			if int(z1)<0:
				print('la 1° equazione è:',x1,'x',y1,'y',z1,'z =',t1)
			else:
				print('la 1° equazione è:',x1,'x',y1,'y', '+',z1,'z =',t1)
		else:
			if int(z1)<0:
				print('la 1° equazione è:',x1,'x','+',y1,'y',z1,'z =',t1)
			else:
				print('la 1° equazione è:',x1,'x','+',y1,'y +',z1,'z =',t1)

		print()
		print('SECONDA EQUAZIONE')
		x2=input('inserisci il coefficiente della x: ')
		y2=input('inserisci il coefficiente della y: ')
		z2=input('inserisci il coefficiente della z: ')
		t2=input('inserisci il coefficiente del termine noto: ')

		if int(y2)<0:
			if int(z2)<0:
				print('la 2° equazione è:',x2,'x',y2,'y',z2,'z =',t2)
			else:
				print('la 2° equazione è:',x2,'x',y2,'y','+',z2,'z =',t2)
		else:
			if int(z2)<0:
				print('la 2° equazione è:',x2,'x','+',y2,'y',z2,'z =',t2)
			else:
				print('la 2° equazione è:',x2,'x','+',y2,'y +',z2,'z =',t2)

		print()
		print('TERZA EQUAZIONE')
		x3=input('inserisci il coefficiente della x: ')
		y3=input('inserisci il coefficiente della y: ')
		z3=input('inserisci il coefficiente della z: ')
		t3=input('inserisci il coefficiente del termine noto: ')

		if int(y3)<0:
			if int(z3)<0:
				print('la 3° equazione è:',x3,'x',y3,'y',z3,'z =',t3)
			else:
				print('la 3° equazione è:',x3,'x',y3,'y','+',z3,'z','=',t3)
		else:
			if int(z3)<0:
				print('la 3° equazione è:',x3,'x','+',y3,'y',z3,'z =',t3)
			else:
				print('la 3° equazione è:',x3,'x','+',y3,'y +',z3,'z =',t3)

		r_coeff1=[int(x1),int(x2),int(x3)]
		r_coeff2=[int(y1),int(y2),int(y3)]
		r_coeff3=[int(z1),int(z2),int(z3)]
		r_t_noto=[(int(t1)),int(t2),int(t3)]

		def DETERMINANTE(colonna1, colonna2, colonna3):
			Diag_max1=(colonna1[0])*(colonna2[1])*(colonna3[2])
			Diag_max2=(colonna1[2])*(colonna2[0])*(colonna3[1])
			Diag_max3=(colonna1[1])*(colonna2[2])*(colonna3[0])
			Diag_min1=(colonna1[2])*(colonna2[1])*(colonna3[0])
			Diag_min2=(colonna1[0])*(colonna2[2])*(colonna3[1])
			Diag_min3=(colonna1[1])*(colonna2[0])*(colonna3[2])
			Diag_max= (Diag_max3)+(Diag_max1)+(Diag_max2)
			Diag_min= (Diag_min3)+(Diag_min1)+(Diag_min2)
	
			risultato=(Diag_max)-(Diag_min)
			return risultato

		D= DETERMINANTE(r_coeff1, r_coeff2, r_coeff3)
		Dx= DETERMINANTE(r_t_noto, r_coeff2, r_coeff3)
		Dy= DETERMINANTE(r_coeff1, r_t_noto, r_coeff3)
		Dz= DETERMINANTE(r_coeff1, r_coeff2, r_t_noto)

		print('x =', Dx/D)
		print('y =', Dy/D)
		print('z =', Dz/D)
		a = 1

	else:
		print('numero inserito non corretto: RIPROVA')
		a = 0