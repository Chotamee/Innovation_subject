import math

al1=0
al2=0
al3=4.2
al4=4.2
al5=4.2
al6=-6.1
al7=-6.1
al8=-6.1

mu1=0.03
mu2=0.41
mu3=0.04
mu4=0.04
mu5=0.04
mu6=0.06
mu7=0.06
mu8=0.18

m1=6.8
m2=6.8
m3=7.2
m4=7.2
m5=7.2
m6=2.3
m7=2.3
m8=2.3

F1=3.4
F2=0
F3=9.2
F4=8.0
F5=6.9
F6=0
F7=1.4
F8=0

L1=27
L2=27
L3=69
L4=69
L5=69
L6=110
L7=110
L8=110

v01=0
v02=24
v03=11
v04=11
v05=11
v06=9
v07=9
v08=25

g=9.81


a1=F1/m1-g*(math.sin(math.radians(al1))+mu1*math.cos(math.radians(al1)))
a2=F2/m2-g*(math.sin(math.radians(al2))+mu2*math.cos(math.radians(al2)))
a3=F3/m3-g*(math.sin(math.radians(al3))+mu3*math.cos(math.radians(al3)))
a4=F4/m4-g*(math.sin(math.radians(al4))+mu4*math.cos(math.radians(al4)))
a5=F5/m5-g*(math.sin(math.radians(al5))+mu5*math.cos(math.radians(al5)))
a6=F6/m6-g*(math.sin(math.radians(al6))+mu6*math.cos(math.radians(al6)))
a7=F7/m7-g*(math.sin(math.radians(al7))+mu7*math.cos(math.radians(al7)))
a8=F8/m8-g*(math.sin(math.radians(al8))+mu8*math.cos(math.radians(al8)))


v1=(v01**2+2*a1*L1)**0.5
v2=(v02**2+2*a2*L2)**0.5
v3=(v03**2+2*a3*L3)**0.5
v4=(v04**2+2*a4*L4)**0.5
v5=(v05**2+2*a5*L5)**0.5
v6=(v06**2+2*a6*L6)**0.5
v7=(v07**2+2*a7*L7)**0.5
v8=(v08**2+2*a8*L8)**0.5


t1=(v1-v01)/a1
t2=(v2-v02)/a2
t3=(v3-v03)/a3
t4=(v4-v04)/a4
t5=(v5-v05)/a5
t6=(v6-v06)/a6
t7=(v7-v07)/a7
t8=(v8-v08)/a8


print("1. a =", a1, "м/с^2, v =", v1, "м/с, t =", t1, "с")
print("2. a =", a2, "м/с^2, v =", v2, "м/с, t =", t2, "с")
print("3. a =", a3, "м/с^2, v =", v3, "м/с, t =", t3, "с")
print("4. a =", a4, "м/с^2, v =", v4, "м/с, t =", t4, "с")
print("5. a =", a5, "м/с^2, v =", v5, "м/с, t =", t5, "с")
print("6. a =", a6, "м/с^2, v =", v6, "м/с, t =", t6, "с")
print("7. a =", a7, "м/с^2, v =", v7, "м/с, t =", t7, "с")
print("8. a =", a8, "м/с^2, v =", v8, "м/с, t =", t8, "с")