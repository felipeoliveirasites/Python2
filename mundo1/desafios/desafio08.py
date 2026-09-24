m = float(input('Digite em metros: '))
dm = m*10
cm = m*100
mm = m*1000
km = m/1000
hm = m/100
dam = m/10

print('{}m tem {:.0f}dm , {:.0f}cm e tem {:.0f}mm\n {:.0f}km, {:.0f}hm e {:.0f}dam'.format(m,dm,cm,mm,km,hm,dam))