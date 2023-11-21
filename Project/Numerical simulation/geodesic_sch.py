#%%
import numpy as np
from matplotlib import pyplot as plt
import math
from numpy.linalg import norm
from tqdm import tqdm
from time import sleep
import pandas as pd
import pickle
import pyarrow
import decimal
from decimal import *
import time
import gc

getcontext().prec = 50

AU = decimal.Decimal(str(149.6*10**9)) # m
daysec = decimal.Decimal(str(24.0 * 60 * 60))

yrsec = decimal.Decimal(str(1 * 365)) * daysec
AUyr = yrsec/AU   # AU/yr
c = decimal.Decimal(str(299792458)) # m/s
G = decimal.Decimal(str(6.67384 * 10**(-11))) # m^3 kg^-1 s^-2
M_sun = decimal.Decimal(str(1.989*10**30)) * G / c**2

r_sch = 2*G*decimal.Decimal(str(1.989*10**30))/(c**2) # m

# mass [kg], Perihelion [m], Aphelion [m], semi-major axis [m], Period [s], Eccenticity
S_mer, S_ven, S_ear, S_mar, S_jup, S_sat, S_ura, S_nep = decimal.Decimal(str(57.909227*10**9)), decimal.Decimal(str(108.209475*10**9)), decimal.Decimal(str(149.598262*10**9)), decimal.Decimal(str(227.943824*10**9)), decimal.Decimal(str(778.340821*10**9)), decimal.Decimal(str(1426.666422*10**9)), decimal.Decimal(str(2870.658186*10**9)), decimal.Decimal(str(4498.396441*10**9))
E_m, E_v, E_e, E_ma, E_j, E_s, E_u, E_n = decimal.Decimal(str(0.20563593)), decimal.Decimal(str(0.00677672)), decimal.Decimal(str(0.01671123)), decimal.Decimal(str(0.0933941)), decimal.Decimal(str(0.04838624)), decimal.Decimal(str(0.05386179)), decimal.Decimal(str(0.04725744)), decimal.Decimal(str(0.00859048))

M_mer, P_mer, A_mer, TT_m = decimal.Decimal(str(0.330104*10**24)) * G / c**2, decimal.Decimal(str((1-E_m)*S_mer)), decimal.Decimal(str((1+E_m)*S_mer)), decimal.Decimal('87.97')*daysec * c         # mercury
M_ven, P_ven, A_ven, TT_v = decimal.Decimal(str(4.86732*10**24)) * G / c**2, decimal.Decimal(str((1-E_v)*S_ven)), decimal.Decimal(str((1+E_v)*S_ven)), decimal.Decimal('224.7')*daysec * c          # venus
M_ear, P_ear, A_ear, TT_e = decimal.Decimal(str(5.97219*10**24)) * G / c**2, decimal.Decimal(str((1-E_e)*S_ear)), decimal.Decimal(str((1+E_e)*S_ear)), decimal.Decimal('365.26')*daysec * c         # earth
M_mar, P_mar, A_mar, TT_ma = decimal.Decimal(str(0.641693*10**24)) * G / c**2, decimal.Decimal(str((1-E_ma)*S_mar)), decimal.Decimal(str((1+E_ma)*S_mar)), decimal.Decimal('686.98')*daysec * c     # mars
M_jup, P_jup, A_jup, TT_j = decimal.Decimal(str(1898.13*10**24)) * G / c**2, decimal.Decimal(str((1-E_j)*S_jup)), decimal.Decimal(str((1+E_j)*S_jup)), decimal.Decimal('4332.82')*daysec * c        # jupiter
M_sat, P_sat, A_sat, TT_s = decimal.Decimal(str(568.319*10**24)) * G / c**2, decimal.Decimal(str((1-E_s)*S_sat)), decimal.Decimal(str((1+E_s)*S_sat)), decimal.Decimal('10755.7')*daysec * c        # saturn
M_ura, P_ura, A_ura, TT_u = decimal.Decimal(str(86.8103*10**24)) * G / c**2, decimal.Decimal(str((1-E_u)*S_ura)), decimal.Decimal(str((1+E_u)*S_ura)), decimal.Decimal('30587.15')*daysec * c       # uranus
M_nep, P_nep, A_nep, TT_n = decimal.Decimal(str(102.410*10**24)) * G / c**2, decimal.Decimal(str((1-E_n)*S_nep)), decimal.Decimal(str((1+E_n)*S_nep)), decimal.Decimal('60190.03')*daysec * c       # neptune

# observed
shift_mer = decimal.Decimal('42.98') # +_0.04 "/century
shift_ven = decimal.Decimal('8.6247') # +_0.005 "/century
shift_ear = decimal.Decimal('3.8387') # +_0.004 "/century
shift_mar = decimal.Decimal('1.3624') # +_0.0005 "/century

def pi():
    getcontext().prec += 2  # extra digits for intermediate steps
    three = decimal.Decimal(3)      # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s               # unary plus applies the new precision

def cos(x):
    """Return the cosine of x as measured in radians.

    The Taylor series approximation works best for a small value of x.
    For larger values, first compute x = x % (2 * pi).

    >>> print(cos(Decimal('0.5')))
    0.8775825618903727161162815826
    >>> print(cos(0.5))
    0.87758256189
    >>> print(cos(0.5+0j))
    (0.87758256189+0j)

    """
    x=x % (2*pi())
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s

def sin(x):
    """Return the sine of x as measured in radians.

    The Taylor series approximation works best for a small value of x.
    For larger values, first compute x = x % (2 * pi).

    >>> print(sin(Decimal('0.5')))
    0.4794255386042030002732879352
    >>> print(sin(0.5))
    0.479425538604
    >>> print(sin(0.5+0j))
    (0.479425538604+0j)

    """
    x=decimal.Decimal(str(x)) % (2*pi())
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s

def divide_mercury(rk_r,rk_phi,rk_t):
    r = []
    phi = []
    t = []
    
    for i in tqdm(range(len(rk_t))):
        if 85 < rk_t[i] < 95:
            r.append(rk_r[i])
            phi.append(rk_phi[i])
            t.append(rk_t[i])
    return r,phi,t

def divide_venus(rk_r,rk_phi,rk_t):
    r = []
    phi = []
    t = []
    
    for i in tqdm(range(len(rk_t))):
        if 220 < rk_t[i] < 230:
            r.append(rk_r[i])
            phi.append(rk_phi[i])
            t.append(rk_t[i])
    return r,phi,t

def divide_earth(rk_r,rk_phi,rk_t):
    r = []
    phi = []
    t = []
    
    for i in tqdm(range(len(rk_t))):
        if 360 < rk_t[i] < 370:
            r.append(rk_r[i])
            phi.append(rk_phi[i])
            t.append(rk_t[i])
    return r,phi,t

def divide_mars(rk_r,rk_phi,rk_t):
    r = []
    phi = []
    t = []
    
    for i in tqdm(range(len(rk_t))):
        if 680 < rk_t[i] < 690:
            r.append(rk_r[i])
            phi.append(rk_phi[i])
            t.append(rk_t[i])
    return r,phi,t

#%%

def vel_cor(M,m,r,a):
    G = decimal.Decimal('1')
    #c = decimal.Decimal('1')
    # M: mass of sun, m: mass of planet, r: distance from the sun, a: semi major axis
    v = np.sqrt(G*(M)*((2/r)-(1/a)))
    return v

def red_mass(M1,M2):
    reduce = (M1*M2)/(M1+M2)
    return reduce

def eccentricity(r_Aphelion,r_Perihelion):
    e = (r_Aphelion-r_Perihelion)/(r_Aphelion+r_Perihelion)
    return e

def ang_mom(M1,M2,r,a):
    # angular momentum conservation law
    v = vel_cor(M1,M2,r,a)
    # mm = red_mass(M1,M2)
    L = M2*r*v
    return L

def find_perihelion(r,phi):
    for k in tqdm(range(1,len(r)-1)):
        if r[k-1]>r[k]<r[k+1]:
            return k, r[k], phi[k]
    
def tri(r,phi):
    x = []
    y = []
    
    for j in tqdm(range(len(r))):
        x.append(r[j]*cos(phi[j]))
        y.append(r[j]*sin(phi[j]))
    return x, y

def convergence(U_h,U_05h,U_025h,i):
    return np.abs(U_h[i]-U_05h[2*i])/np.abs(U_05h[2*i]-U_025h[4*i])

# sun
xs, ys = 0, 0
xvs, yvs = 0, 0

# mercury
xm, ym = decimal.Decimal(str(P_mer)), decimal.Decimal('0')
xvm, yvm = decimal.Decimal('0'), decimal.Decimal(str(vel_cor(M_sun,M_mer,P_mer,S_mer)))
ang_mer = yvm*xm

# venus
xv, yv = decimal.Decimal(str(P_ven)), decimal.Decimal('0')
xvv, yvv = decimal.Decimal('0'), decimal.Decimal(str(vel_cor(M_sun,M_ven,P_ven,S_ven)))
ang_ven = yvv*xv

# earth
xe, ye = decimal.Decimal(str(P_ear)), decimal.Decimal('0')
xve, yve = decimal.Decimal('0'), decimal.Decimal(str(vel_cor(M_sun,M_ear,P_ear,S_ear)))
ang_ear = yve*xe

# mars
xma, yma = decimal.Decimal(P_mar), decimal.Decimal('0')
xvma, yvma = decimal.Decimal('0'), decimal.Decimal(vel_cor(M_sun,M_mar,P_mar,S_mar))
ang_mar = yvma*xma

# jupiter
xj, yj = decimal.Decimal(P_jup), decimal.Decimal('0')
xvj, yvj = decimal.Decimal('0'), decimal.Decimal(vel_cor(M_sun,M_jup,P_jup,S_jup))
ang_jup = decimal.Decimal(ang_mom(M_sun,M_jup,P_jup,S_jup)) / decimal.Decimal(str(1898.13*10**24))

# saturn
xsa, yas = decimal.Decimal(P_sat), decimal.Decimal('0')
xvsa, yvsa = decimal.Decimal('0'), decimal.Decimal(vel_cor(M_sun,M_sat,P_sat,S_sat))
ang_sat = decimal.Decimal(ang_mom(M_sun,M_sat,P_sat,S_sat)) / decimal.Decimal(str(568.319*10**24))

# uranus
xu, yu = decimal.Decimal(P_ura), decimal.Decimal('0')
xvu, yvu = decimal.Decimal('0'), decimal.Decimal(vel_cor(M_sun,M_ura,P_ura,S_ura))
ang_ura = decimal.Decimal(ang_mom(M_sun,M_ura,P_ura,S_ura)) / decimal.Decimal(str(86.8103*10**24))

# neptune
xn, yn = decimal.Decimal(P_nep), decimal.Decimal('0')
xvn, yvn = decimal.Decimal('0'), decimal.Decimal(vel_cor(M_sun,M_nep,P_nep,S_nep))
ang_nep = decimal.Decimal(ang_mom(M_sun,M_nep,P_nep,S_nep)) / decimal.Decimal(str(102.410*10**24))

#%%
def geodesic(r,dr,phi,t,tau,l,e):
    #e = decimal.Decimal(((1-2*M_sun/r)*(1+l*l/r/r))).sqrt()
    dtau = e/(1-2*M_sun/r)
    dphi = l/(r*r)
    ddr = -M_sun/r/r+l*l/r/r/r-3*M_sun*l*l/r/r/r/r
    #dr = (2*((e*e-1)/2-(-M_sun/r+l*l/(2*r*r)-M_sun*l*l/(r*r*r)))).sqrt()
    return dr, ddr, dphi, dtau

def newtonian(r,dr,phi,t,tau,l,e):
    dtau = e/(1-2*M_sun/r)
    dphi = l/(r*r)
    ddr = l*l/r/r/r-M_sun/r/r
    return dr, ddr, dphi, dtau

# %%
def rk4(r,dr,phi,t,tau,l,tauf,h,TT):

    N = int((tauf-tau)/h)
        
    r0 = [r]
    dr0 = [dr]
    phi0 = [phi]
    t0 = [t]
    tau0 = [tau]
    e = decimal.Decimal(((1-2*M_sun/r)*(1+l*l/r/r))).sqrt()
        
    for i in tqdm(range(1,N+1)):
        tau = tau + h * i
        
        k1 = geodesic(r,dr,phi,t,tau,l,e)
        k2 = geodesic(r+h*k1[0]/2,dr+h*k1[1]/2,phi+h*k1[2]/2,t+h*k1[3]/2,tau+h/2,l,e)
        k3 = geodesic(r+h*k2[0]/2,dr+h*k2[1]/2,phi+h*k2[2]/2,t+h*k2[3]/2,tau+h/2,l,e)
        k4 = geodesic(r+h*k3[0],dr+h*k3[1],phi+h*k3[2],t+h*k3[3],tau+h,l,e)
    
        r = r + decimal.Decimal(str((k1[0]/6+k2[0]/3+k3[0]/3+k4[0]/6)*h))
        dr = dr + decimal.Decimal(str((k1[1]/6+k2[1]/3+k3[1]/3+k4[1]/6)*h))
        phi = phi + decimal.Decimal(str((k1[2]/6+k2[2]/3+k3[2]/3+k4[2]/6)*h))
        t = t + decimal.Decimal(str((k1[3]/6+k2[3]/3+k3[3]/3+k4[3]/6)*h))
            
        r0.append(r)
        dr0.append(dr)
        phi0.append(phi)
        t0.append(t/(c*decimal.Decimal('86400')))
        tau0.append(tau/(c*decimal.Decimal('86400')))
    
    return r0, dr0, phi0, t0, tau0
"""
def rk4_NT(r,dr,phi,t,tau,l,tauf,h):
    N = int((tauf-tau)/h)
        
    r0 = [r]
    dr0 = [dr]
    phi0 = [phi]
    t0 = [t]
    tau0 = [tau]
    e = decimal.Decimal(((1-2*M_sun/r)*(1+l*l/r/r))).sqrt()
    #print(e)
    
    for i in tqdm(range(1,N+1)):
        tau = tau + h * i
        
        k1 = newtonian(r,dr,phi,t,tau,l,e)
        k2 = newtonian(r+h*k1[0]/2,dr+h*k1[1]/2,phi+h*k1[2]/2,t+h*k1[3]/2,tau+h/2,l,e)
        k3 = newtonian(r+h*k2[0]/2,dr+h*k2[1]/2,phi+h*k2[2]/2,t+h*k2[3]/2,tau+h/2,l,e)
        k4 = newtonian(r+h*k3[0],dr+h*k3[1],phi+h*k3[2],t+h*k3[3],tau+h,l,e)
    
        r = r + (k1[0]/6+k2[0]/3+k3[0]/3+k4[0]/6)*h
        dr = dr + (k1[1]/6+k2[1]/3+k3[1]/3+k4[1]/6)*h
        phi = phi + (k1[2]/6+k2[2]/3+k3[2]/3+k4[2]/6)*h
        t = t + (k1[3]/6+k2[3]/3+k3[3]/3+k4[3]/6)*h
        
        r0.append(r)
        dr0.append(dr)
        phi0.append(phi)
        t0.append(t/(c*decimal.Decimal('86400')))
        tau0.append(tau/(c*decimal.Decimal('86400')))
    
    return r0, dr0, phi0, t0, tau0
"""
#%%
def rk5(r,dr,phi,t,tau,l,tauf,h):
    N = int((tauf-tau)/h)
        
    r0 = [r]
    dr0 = [dr]
    phi0 = [phi]
    t0 = [t]
    tau0 = [tau]
    e = decimal.Decimal(((1-2*M_sun/r)*(1+l*l/r/r))).sqrt()
    #print(e)
    
    for i in tqdm(range(1,N+1)):
        tau = tau + h * i
        
        k1 = geodesic(r,dr,phi,t,tau,l,e)
        k2 = geodesic(r+h*k1[0]/4,dr+h*k1[1]/4,phi+h*k1[2]/4,t+h*k1[3]/4,tau+h/4,l,e)
        k3 = geodesic(r+h*k1[0]*3/32+h*k2[0]*9/32,dr+h*k1[1]*3/32+h*k2[1]*9/32,phi+h*k1[2]*3/32+h*k2[2]*9/32,t+h*k1[3]*3/32+h*k2[3]*9/32,tau+h*3/8,l,e)
        k4 = geodesic(r+h*k1[0]*1932/2197-h*k2[0]*7200/2197+h*k3[0]*7296/2197,dr+h*k1[1]*1932/2197-h*k2[1]*7200/2197+h*k3[1]*7296/2197,phi+h*k1[2]*1932/2197-h*k2[2]*7200/2197+h*k3[2]*7296/2197,t+h*k1[3]*1932/2197-h*k2[3]*7200/2197+h*k3[3]*7296/2197,tau+h*12/13,l,e)
        k5 = geodesic(r+h*k1[0]*439/216-h*k2[0]*8+h*k3[0]*3680/513-h*k4[0]*845/4104,dr+h*k1[1]*439/216-h*k2[1]*8+h*k3[1]*3680/513-h*k4[1]*845/4104,phi+h*k1[2]*439/216-h*k2[2]*8+h*k3[2]*3680/513-h*k4[2]*845/4104,t+h*k1[3]*439/216-h*k2[3]*8+h*k3[3]*3680/513-h*k4[3]*845/4104,tau+h,l,e)
        k6 = geodesic(r-h*k1[0]*8/27+h*k2[0]*2-h*k3[0]*3544/2565+h*k4[0]*1859/4104-h*k5[0]*11/40,dr-h*k1[1]*8/27+h*k2[1]*2-h*k3[1]*3544/2565+h*k4[1]*1859/4104-h*k5[1]*11/40,phi-h*k1[2]*8/27+h*k2[2]*2-h*k3[2]*3544/2565+h*k4[2]*1859/4104-h*k5[2]*11/40,t-h*k1[3]*8/27+h*k2[3]*2-h*k3[3]*3544/2565+h*k4[3]*1859/4104-h*k5[3]*11/40,tau+h/2,l,e)

        r = r + decimal.Decimal(str(h*k1[0]*16/135+h*k3[0]*6656/12825+h*k4[0]*28561/56430-h*k5[0]*9/50+h*k6[0]*2/55))
        dr = dr + decimal.Decimal(str(h*k1[1]*16/135+h*k3[1]*6656/12825+h*k4[1]*28561/56430-h*k5[1]*9/50+h*k6[1]*2/55))
        phi = phi + decimal.Decimal(str(h*k1[2]*16/135+h*k3[2]*6656/12825+h*k4[2]*28561/56430-h*k5[2]*9/50+h*k6[2]*2/55))
        t = t + decimal.Decimal(str(h*k1[3]*16/135+h*k3[3]*6656/12825+h*k4[3]*28561/56430-h*k5[3]*9/50+h*k6[3]*2/55))
        """
        k2 = geodesic(r+h*k1[0]/4,dr+h*k1[1]/4,phi+h*k1[2]/4,t+h*k1[3]/4,tau+h/4,l,e)
        k3 = geodesic(r+h*k1[0]/8+h*k2[0]/8,dr+h*k1[1]/8+h*k2[1]/8,phi+h*k1[2]/8+h*k2[2]/8,t+h*k1[3]/8+h*k2[3]/8,tau+h/4,l,e)
        k4 = geodesic(r-h*k2[0]/2+h*k3[0],dr-h*k2[1]/2+h*k3[1],phi-h*k2[2]/2+h*k3[2],t-h*k2[3]/2+h*k3[3],tau+h/2,l,e)
        k5 = geodesic(r+h*k1[0]*3/16+h*k4[0]*9/16,dr+h*k1[1]*3/16+h*k4[1]*9/16,phi+h*k1[2]*3/16+h*k4[2]*9/16,t+h*k1[3]*3/16+h*k4[3]*9/16,tau+h*3/4,l,e)
        k6 = geodesic(r-h*3*k1[0]/7+h*k2[0]*2/7+h*k3[0]*12/7-h*k4[0]*12/7+h*k5[0]*8/7,dr-h*3*k1[1]/7+h*k2[1]*2/7+h*k3[1]*12/7-h*k4[1]*12/7+h*k5[1]*8/7,phi-h*3*k1[2]/7+h*k2[2]*2/7+h*k3[2]*12/7-h*k4[2]*12/7+h*k5[2]*8/7,t-h*3*k1[3]/7+h*k2[3]*2/7+h*k3[3]*12/7-h*k4[3]*12/7+h*k5[3]*8/7,tau+h,l,e)
        
        r = r + decimal.Decimal(str((7*k1[0]+32*k3[0]+12*k4[0]+32*k5[0]+7*k6[0])*h/90))
        dr = dr + decimal.Decimal(str((7*k1[1]+32*k3[1]+12*k4[1]+32*k5[1]+7*k6[1])*h/90))
        phi = phi + decimal.Decimal(str((7*k1[2]+32*k3[2]+12*k4[2]+32*k5[2]+7*k6[2])*h/90))
        t = t + decimal.Decimal(str((7*k1[3]+32*k3[3]+12*k4[3]+32*k5[3]+7*k6[3])*h/90))
        """
        r0.append(r)
        dr0.append(dr)
        phi0.append(phi)
        t0.append(t/(c*decimal.Decimal('86400')))
        tau0.append(tau/(c*decimal.Decimal('86400')))
    
    return r0, dr0, phi0, t0, tau0

#%%
def rk6(r,dr,phi,t,tau,l,tauf,h):
    N = int((tauf-tau)/h)
        
    r0 = [r]
    dr0 = [dr]
    phi0 = [phi]
    t0 = [t]
    tau0 = [tau]
    e = decimal.Decimal(((1-2*M_sun/r)*(1+l*l/r/r))).sqrt()
    #print(e)
    
    for i in tqdm(range(1,N+1)):
        tau = tau + h * i
        
        k1 = geodesic(r,dr,phi,t,tau,l,e)
        k2 = geodesic(r+h*k1[0]/6,dr+h*k1[1]/6,phi+h*k1[2]/6,t+h*k1[3]/6,tau+h/6,l,e)
        k3 = geodesic(r+h*k1[0]*4/75+h*k2[0]*16/75,dr+h*k1[1]*4/75+h*k2[1]*16/75,phi+h*k1[2]*4/75+h*k2[2]*16/75,t+h*k1[3]*4/75+h*k2[3]*16/75,tau+h*4/15,l,e)
        k4 = geodesic(r+h*k1[0]*5/6-h*k2[0]*8/3+h*k3[0]*5/2,dr+h*k1[1]*5/6-h*k2[1]*8/3+h*k3[1]*5/2,phi+h*k1[2]*5/6-h*k2[2]*8/3+h*k3[2]*5/2,t+h*k1[3]*5/6-h*k2[3]*8/3+h*k3[3]*5/2,tau+h*2/3,l,e)
        k5 = geodesic(r-h*k1[0]*8/5+h*k2[0]*144/25-h*k3[0]*4+h*k4[0]*16/25,dr-h*k1[1]*8/5+h*k2[1]*144/25-h*k3[1]*4+h*k4[1]*16/25,phi-h*k1[2]*8/5+h*k2[2]*144/25-h*k3[2]*4+h*k4[2]*16/25,t-h*k1[3]*8/5+h*k2[3]*144/25-h*k3[3]*4+h*k4[3]*16/25,tau+h*4/5,l,e)
        k6 = geodesic(r+h*k1[0]*361/320-h*k2[0]*18/5+h*k3[0]*407/128-h*k4[0]*11/80+h*k5[0]*55/128,dr+h*k1[1]*361/320-h*k2[1]*18/5+h*k3[1]*407/128-h*k4[1]*11/80+h*k5[1]*55/128,phi+h*k1[2]*361/320-h*k2[2]*18/5+h*k3[2]*407/128-h*k4[2]*11/80+h*k5[2]*55/128,t+h*k1[3]*361/320-h*k2[3]*18/5+h*k3[3]*407/128-h*k4[3]*11/80+h*k5[3]*55/128,tau+h,l,e)
        k7 = geodesic(r-h*k1[0]*11/640+h*k3[0]*11/256-h*k4[0]*11/160+h*k5[0]*11/256,dr-h*k1[1]*11/640+h*k3[1]*11/256-h*k4[1]*11/160+h*k5[1]*11/256,phi-h*k1[2]*11/640+h*k3[2]*11/256-h*k4[2]*11/160+h*k5[2]*11/256,t-h*k1[3]*11/640+h*k3[3]*11/256-h*k4[3]*11/160+h*k5[3]*11/256,tau,l,e)
        k8 = geodesic(r+h*k1[0]*93/640-h*k2[0]*18/5+h*k3[0]*803/256-h*k4[0]*11/160+h*k5[0]*99/256+h*k7[0],dr+h*k1[1]*93/640-h*k2[1]*18/5+h*k3[1]*803/256-h*k4[1]*11/160+h*k5[1]*99/256+h*k7[1],phi+h*k1[2]*93/640-h*k2[2]*18/5+h*k3[2]*803/256-h*k4[2]*11/160+h*k5[2]*99/256+h*k7[2],t+h*k1[3]*93/640-h*k2[3]*18/5+h*k3[3]*803/256-h*k4[3]*11/160+h*k5[3]*99/256+h*k7[3],tau+h,l,e)

        r = r + decimal.Decimal(str(h*k1[0]*7/1408+h*k3[0]*1125/2816+h*k4[0]*9/32+h*k5[0]*125/768+h*k7[0]*5/66+h*k8[0]*5/66))
        dr = dr + decimal.Decimal(str(h*k1[1]*7/1408+h*k3[1]*1125/2816+h*k4[1]*9/32+h*k5[1]*125/768+h*k7[1]*5/66+h*k8[1]*5/66))
        phi = phi + decimal.Decimal(str(h*k1[2]*7/1408+h*k3[2]*1125/2816+h*k4[2]*9/32+h*k5[2]*125/768+h*k7[2]*5/66+h*k8[2]*5/66))
        t = t + decimal.Decimal(str(h*k1[3]*7/1408+h*k3[3]*1125/2816+h*k4[3]*9/32+h*k5[3]*125/768+h*k7[3]*5/66+h*k8[3]*5/66))
        """
        k2 = geodesic(r+h*k1[0]/3,dr+h*k1[1]/3,phi+h*k1[2]/3,t+h*k1[3]/3,tau+h/3,l,e)
        k3 = geodesic(r+h*k2[0]*2/3,dr+h*k2[1]*2/3,phi+h*k2[2]*2/3,t+h*k2[3]*2/3,tau+h*2/3,l,e)
        k4 = geodesic(r+h*k1[0]/12+h*k2[0]/3-h*k3[0]/12,dr+h*k1[1]/12+h*k2[1]/3-h*k3[1]/12,phi+h*k1[2]/12+h*k2[2]/3-h*k3[2]/12,t+h*k1[3]/12+h*k2[3]/3-h*k3[3]/12,tau+h/3,l,e)
        k5 = geodesic(r-h*k1[0]/16+h*k2[0]*9/8-h*k3[0]*3/16-h*k4[0]*3/8,dr-h*k1[1]/16+h*k2[1]*9/8-h*k3[1]*3/16-h*k4[1]*3/8,phi-h*k1[2]/16+h*k2[2]*9/8-h*k3[2]*3/16-h*k4[2]*3/8,t-h*k1[3]/16+h*k2[3]*9/8-h*k3[3]*3/16-h*k4[3]*3/8,tau+h/2,l,e)
        k6 = geodesic(r+h*k2[0]*9/8-h*k3[0]*3/8-h*k4[0]*3/4+h*k5[0]/2,dr+h*k2[1]*9/8-h*k3[1]*3/8-h*k4[1]*3/4+h*k5[1]/2,phi+h*k2[2]*9/8-h*k3[2]*3/8-h*k4[2]*3/4+h*k5[2]/2,t+h*k2[3]*9/8-h*k3[3]*3/8-h*k4[3]*3/4+h*k5[3]/2,tau+h/2,l,e)
        k7 = geodesic(r+h*k1[0]*9/44-h*k2[0]*9/11+h*k3[0]*63/44+h*k4[0]*18/11-h*k6[0]*16/11,dr+h*k1[1]*9/44-h*k2[1]*9/11+h*k3[1]*63/44+h*k4[1]*18/11-h*k6[1]*16/11,phi+h*k1[2]*9/44-h*k2[2]*9/11+h*k3[2]*63/44+h*k4[2]*18/11-h*k6[2]*16/11,t+h*k1[3]*9/44-h*k2[3]*9/11+h*k3[3]*63/44+h*k4[3]*18/11-h*k6[3]*16/11,tau+h,l,e)
        
        r = r + decimal.Decimal(str(h*k1[0]*11/120+h*k3[0]*27/40+h*k4[0]*27/40-h*k5[0]*4/15-h*k6[0]*4/15+h*k7[0]*11/120))
        dr = dr + decimal.Decimal(str(h*k1[1]*11/120+h*k3[1]*27/40+h*k4[1]*27/40-h*k5[1]*4/15-h*k6[1]*4/15+h*k7[1]*11/120))
        phi = phi + decimal.Decimal(str(h*k1[2]*11/120+h*k3[2]*27/40+h*k4[2]*27/40-h*k5[2]*4/15-h*k6[2]*4/15+h*k7[2]*11/120))
        t = t + decimal.Decimal(str(h*k1[3]*11/120+h*k3[3]*27/40+h*k4[3]*27/40-h*k5[3]*4/15-h*k6[3]*4/15+h*k7[3]*11/120))
        """
        r0.append(r)
        dr0.append(dr)
        phi0.append(phi)
        t0.append(t/(c*decimal.Decimal('86400')))
        tau0.append(tau/(c*decimal.Decimal('86400')))
    
    return r0, dr0, phi0, t0, tau0

#%%
def rk7(r,dr,phi,t,tau,l,tauf,h):
    N = int((tauf-tau)/h)
        
    r0 = [r]
    dr0 = [dr]
    phi0 = [phi]
    t0 = [t]
    tau0 = [tau]
    e = decimal.Decimal(((1-2*M_sun/r)*(1+l*l/r/r))).sqrt()
    #print(e)
    
    for i in tqdm(range(1,N+1)):
        tau = tau + h * i
        k1 = geodesic(r,dr,phi,t,tau,l,e)
        k2 = geodesic(r+h*k1[0]*2/33,dr+h*k1[1]*2/33,phi+h*k1[2]*2/33,t+h*k1[3]*2/33,tau+h*2/33,l,e)
        k3 = geodesic(r+h*k2[0]*4/33,dr+h*k2[1]*4/33,phi+h*k2[2]*4/33,t+h*k2[3]*4/33,tau+h*4/33,l,e)
        k4 = geodesic(r+h*k1[0]/22+h*k3[0]*3/22,dr+h*k1[1]/22+h*k3[1]*3/22,phi+h*k1[2]/22+h*k3[2]*3/22,t+h*k1[3]/22+h*k3[3]*3/22,tau+h*2/11,l,e)
        k5 = geodesic(r+h*k1[0]*43/64-h*k3[0]*165/64+h*k4[0]*77/32,dr+h*k1[1]*43/64-h*k3[1]*165/64+h*k4[1]*77/32,phi+h*k1[2]*43/64-h*k3[2]*165/64+h*k4[2]*77/32,t+h*k1[3]*43/64-h*k3[3]*165/64+h*k4[3]*77/32,tau+h/2,l,e)
        k6 = geodesic(r-h*k1[0]*2383/486+h*k3[0]*1067/54-h*k4[0]*26312/1701+h*k5[0]*2176/1701,dr-h*k1[1]*2383/486+h*k3[1]*1067/54-h*k4[1]*26312/1701+h*k5[1]*2176/1701,phi-h*k1[2]*2383/486+h*k3[2]*1067/54-h*k4[2]*26312/1701+h*k5[2]*2176/1701,t-h*k1[3]*2383/486+h*k3[3]*1067/54-h*k4[3]*26312/1701+h*k5[3]*2176/1701,tau+h*2/3,l,e)
        k7 = geodesic(r+h*k1[0]*10077/4802-h*k3[0]*5643/686+h*k4[0]*116259/16807-h*k5[0]*6240/16807+h*k6[0]*1053/2401,dr+h*k1[1]*10077/4802-h*k3[1]*5643/686+h*k4[1]*116259/16807-h*k5[1]*6240/16807+h*k6[1]*1053/2401,phi+h*k1[2]*10077/4802-h*k3[2]*5643/686+h*k4[2]*116259/16807-h*k5[2]*6240/16807+h*k6[2]*1053/2401,t+h*k1[3]*10077/4802-h*k3[3]*5643/686+h*k4[3]*116259/16807-h*k5[3]*6240/16807+h*k6[3]*1053/2401,tau+h*6/7,l,e)
        k8 = geodesic(r-h*k1[0]*733/176+h*k3[0]*141/8-h*k4[0]*335763/23296+h*k5[0]*216/77-h*k6[0]*4617/2816+h*k7[0]*7203/9152,dr-h*k1[1]*733/176+h*k3[1]*141/8-h*k4[1]*335763/23296+h*k5[1]*216/77-h*k6[1]*4617/2816+h*k7[1]*7203/9152,phi-h*k1[2]*733/176+h*k3[2]*141/8-h*k4[2]*335763/23296+h*k5[2]*216/77-h*k6[2]*4617/2816+h*k7[2]*7203/9152,t-h*k1[3]*733/176+h*k3[3]*141/8-h*k4[3]*335763/23296+h*k5[3]*216/77-h*k6[3]*4617/2816+h*k7[3]*7203/9152,tau+h,l,e)
        k9 = geodesic(r+h*k1[0]*15/352-h*k4[0]*5445/46592+h*k5[0]*18/77-h*k6[0]*1215/5632+h*k7[0]*1029/18304,dr+h*k1[1]*15/352-h*k4[1]*5445/46592+h*k5[1]*18/77-h*k6[1]*1215/5632+h*k7[1]*1029/18304,phi+h*k1[2]*15/352-h*k4[2]*5445/46592+h*k5[2]*18/77-h*k6[2]*1215/5632+h*k7[2]*1029/18304,t+h*k1[3]*15/352-h*k4[3]*5445/46592+h*k5[3]*18/77-h*k6[3]*1215/5632+h*k7[3]*1029/18304,tau,l,e)
        k10 = geodesic(r-h*k1[0]*1833/352+h*k3[0]*141/8-h*k4[0]*51237/3584+h*k5[0]*18/7-h*k6[0]*729/512+h*k7[0]*1029/1408+h*k9[0],dr-h*k1[1]*1833/352+h*k3[1]*141/8-h*k4[1]*51237/3584+h*k5[1]*18/7-h*k6[1]*729/512+h*k7[1]*1029/1408+h*k9[1],phi-h*k1[2]*1833/352+h*k3[2]*141/8-h*k4[2]*51237/3584+h*k5[2]*18/7-h*k6[2]*729/512+h*k7[2]*1029/1408+h*k9[2],t-h*k1[3]*1833/352+h*k3[3]*141/8-h*k4[3]*51237/3584+h*k5[3]*18/7-h*k6[3]*729/512+h*k7[3]*1029/1408+h*k9[3],tau+h,l,e)
        
        r = r + decimal.Decimal(str(h*k1[0]*11/864+h*k4[0]*1771561/6289920+h*k5[0]*32/105+h*243*k6[0]/2560+h*16807*k7[0]/74880+h*11*k9[0]/270+h*11*k10[0]/270))
        dr = dr + decimal.Decimal(str(h*k1[1]*11/864+h*k4[1]*1771561/6289920+h*k5[1]*32/105+h*243*k6[1]/2560+h*16807*k7[1]/74880+h*11*k9[1]/270+h*11*k10[1]/270))
        phi = phi + decimal.Decimal(str(h*k1[2]*11/864+h*k4[2]*1771561/6289920+h*k5[2]*32/105+h*243*k6[2]/2560+h*16807*k7[2]/74880+h*11*k9[2]/270+h*11*k10[2]/270))
        t = t + decimal.Decimal(str(h*k1[3]*11/864+h*k4[3]*1771561/6289920+h*k5[3]*32/105+h*243*k6[3]/2560+h*16807*k7[3]/74880+h*11*k9[3]/270+h*11*k10[3]/270))
        
        r0.append(r)
        dr0.append(dr)
        phi0.append(phi)
        t0.append(t/(c*decimal.Decimal('86400')))
        tau0.append(tau/(c*decimal.Decimal('86400')))
    
    return r0, dr0, phi0, t0, tau0

#%%
def rk8(r,dr,phi,t,tau,l,tauf,h):
    N = int((tauf-tau)/h)
        
    r0 = [r]
    dr0 = [dr]
    phi0 = [phi]
    t0 = [t]
    tau0 = [tau]
    e = decimal.Decimal(((1-2*M_sun/r)*(1+l*l/r/r))).sqrt()
    #print(e)
    
    for i in tqdm(range(1,N+1)):
        tau = tau + h * i
        k1 = geodesic(r,dr,phi,t,tau,l,e)
        k2 = geodesic(r+h*k1[0]*2/27,dr+h*k1[1]*2/27,phi+h*k1[2]*2/27,t+h*k1[3]*2/27,tau+h*2/27,l,e)
        k3 = geodesic(r+h*k1[0]/36+h*k2[0]/12,dr+h*k1[1]/36+h*k2[1]/12,phi+h*k1[2]/36+h*k2[2]/12,t+h*k1[3]/36+h*k2[3]/12,tau+h/9,l,e)
        k4 = geodesic(r+h*k1[0]/24+h*k3[0]/8,dr+h*k1[1]/24+h*k3[1]/8,phi+h*k1[2]/24+h*k3[2]/8,t+h*k1[3]/24+h*k3[3]/8,tau+h/6,l,e)
        k5 = geodesic(r+h*k1[0]*20/48-h*k3[0]*75/48+h*k4[0]*75/48,dr+h*k1[1]*20/48-h*k3[1]*75/48+h*k4[1]*75/48,phi+h*k1[2]*20/48-h*k3[2]*75/48+h*k4[2]*75/48,t+h*k1[3]*20/48-h*k3[3]*75/48+h*k4[3]*75/48,tau+h*5/12,l,e)
        k6 = geodesic(r+h*k1[0]/20+h*k4[0]/4+h*k5[0]/5,dr+h*k1[1]/20+h*k4[1]/4+h*k5[1]/5,phi+h*k1[2]/20+h*k4[2]/4+h*k5[2]/5,t+h*k1[3]/20+h*k4[3]/4+h*k5[3]/5,tau+h/2,l,e)
        k7 = geodesic(r-h*k1[0]*25/108+h*k4[0]*125/108-h*k5[0]*260/108+h*k6[0]*250/108,dr-h*k1[1]*25/108+h*k4[1]*125/108-h*k5[1]*260/108+h*k6[1]*250/108,phi-h*k1[2]*25/108+h*k4[2]*125/108-h*k5[2]*260/108+h*k6[2]*250/108,t-h*k1[3]*25/108+h*k4[3]*125/108-h*k5[3]*260/108+h*k6[3]*250/108,tau+h*5/6,l,e)
        k8 = geodesic(r+h*k1[0]*31/300+h*k5[0]*61/225-h*k6[0]*2/9+h*k7[0]*13/900,dr+h*k1[1]*31/300+h*k5[1]*61/225-h*k6[1]*2/9+h*k7[1]*13/900,phi+h*k1[2]*31/300+h*k5[2]*61/225-h*k6[2]*2/9+h*k7[2]*13/900,t+h*k1[3]*31/300+h*k5[3]*61/225-h*k6[3]*2/9+h*k7[3]*13/900,tau+h/6,l,e)
        k9 = geodesic(r+h*k1[0]*2-h*k4[0]*53/6+h*k5[0]*704/45-h*k6[0]*107/9+h*k7[0]*67/90+h*k8[0]*3,dr+h*k1[1]*2-h*k4[1]*53/6+h*k5[1]*704/45-h*k6[1]*107/9+h*k7[1]*67/90+h*k8[1]*3,phi+h*k1[2]*2-h*k4[2]*53/6+h*k5[2]*704/45-h*k6[2]*107/9+h*k7[2]*67/90+h*k8[2]*3,t+h*k1[3]*2-h*k4[3]*53/6+h*k5[3]*704/45-h*k6[3]*107/9+h*k7[3]*67/90+h*k8[3]*3,tau+h*2/3,l,e)
        k10 = geodesic(r-h*k1[0]*91/108+h*k4[0]*23/108-h*k5[0]*976/135+h*k6[0]*311/54-h*k7[0]*19/60+h*k8[0]*17/6-h*k9[0]/12,dr-h*k1[1]*91/108+h*k4[1]*23/108-h*k5[1]*976/135+h*k6[1]*311/54-h*k7[1]*19/60+h*k8[1]*17/6-h*k9[1]/12,phi-h*k1[2]*91/108+h*k4[2]*23/108-h*k5[2]*976/135+h*k6[2]*311/54-h*k7[2]*19/60+h*k8[2]*17/6-h*k9[2]/12,t-h*k1[3]*91/108+h*k4[3]*23/108-h*k5[3]*976/135+h*k6[3]*311/54-h*k7[3]*19/60+h*k8[3]*17/6-h*k9[3]/12,tau+h/3,l,e)
        k11 = geodesic(r+h*k1[0]*2383/4100-h*k4[0]*341/164+h*k5[0]*4496/1025-h*k6[0]*301/82+h*k7[0]*2133/4100+h*k8[0]*45/82+h*k9[0]*45/164+h*k10[0]*18/41,dr+h*k1[1]*2383/4100-h*k4[1]*341/164+h*k5[1]*4496/1025-h*k6[1]*301/82+h*k7[1]*2133/4100+h*k8[1]*45/82+h*k9[1]*45/164+h*k10[1]*18/41,phi+h*k1[2]*2383/4100-h*k4[2]*341/164+h*k5[2]*4496/1025-h*k6[2]*301/82+h*k7[2]*2133/4100+h*k8[2]*45/82+h*k9[2]*45/164+h*k10[2]*18/41,t+h*k1[3]*2383/4100-h*k4[3]*341/164+h*k5[3]*4496/1025-h*k6[3]*301/82+h*k7[3]*2133/4100+h*k8[3]*45/82+h*k9[3]*45/164+h*k10[3]*18/41,tau+h,l,e)
        k12 = geodesic(r+h*k1[0]*3/205-h*k6[0]*6/41-h*k7[0]*3/205-h*k8[0]*3/41+h*k9[0]*3/41+h*k10[0]*6/41,dr+h*k1[1]*3/205-h*k6[1]*6/41-h*k7[1]*3/205-h*k8[1]*3/41+h*k9[1]*3/41+h*k10[1]*6/41,phi+h*k1[2]*3/205-h*k6[2]*6/41-h*k7[2]*3/205-h*k8[2]*3/41+h*k9[2]*3/41+h*k10[2]*6/41,t+h*k1[3]*3/205-h*k6[3]*6/41-h*k7[3]*3/205-h*k8[3]*3/41+h*k9[3]*3/41+h*k10[3]*6/41,tau,l,e)
        k13 = geodesic(r-h*k1[0]*1777/4100-h*k4[0]*341/164+h*k5[0]*4496/1025-h*k6[0]*289/82+h*k7[0]*2193/4100+h*k8[0]*51/82+h*k9[0]*33/164+h*k10[0]*12/41+h*k12[0],dr-h*k1[1]*1777/4100-h*k4[1]*341/164+h*k5[1]*4496/1025-h*k6[1]*289/82+h*k7[1]*2193/4100+h*k8[1]*51/82+h*k9[1]*33/164+h*k10[1]*12/41+h*k12[1],phi-h*k1[2]*1777/4100-h*k4[2]*341/164+h*k5[2]*4496/1025-h*k6[2]*289/82+h*k7[2]*2193/4100+h*k8[2]*51/82+h*k9[2]*33/164+h*k10[2]*12/41+h*k12[2],t-h*k1[3]*1777/4100-h*k4[3]*341/164+h*k5[3]*4496/1025-h*k6[3]*289/82+h*k7[3]*2193/4100+h*k8[3]*51/82+h*k9[3]*33/164+h*k10[3]*12/41+h*k12[3],tau+h,l,e)
        
        r = r + decimal.Decimal(str((34*k6[0]/105+9*k7[0]/35+9*k8[0]/35+9*k9[0]/280+9*k10[0]/280+41*k12[0]/840+41*k13[0]/840)*h))
        dr = dr + decimal.Decimal(str((34*k6[1]/105+9*k7[1]/35+9*k8[1]/35+9*k9[1]/280+9*k10[1]/280+41*k12[1]/840+41*k13[1]/840)*h))
        phi = phi + decimal.Decimal(str((34*k6[2]/105+9*k7[2]/35+9*k8[2]/35+9*k9[2]/280+9*k10[2]/280+41*k12[2]/840+41*k13[2]/840)*h))
        t = t + decimal.Decimal(str((34*k6[3]/105+9*k7[3]/35+9*k8[3]/35+9*k9[3]/280+9*k10[3]/280+41*k12[3]/840+41*k13[3]/840)*h))
        
        r0.append(r)
        dr0.append(dr)
        phi0.append(phi)
        t0.append(t/(c*decimal.Decimal('86400')))
        tau0.append(tau/(c*decimal.Decimal('86400')))
    
    return r0, dr0, phi0, t0, tau0
# %%
r,dr,phi,t,tau,l,tauf = xv,decimal.Decimal('0'),decimal.Decimal('0'),decimal.Decimal('0'),decimal.Decimal('0'),ang_ven,decimal.Decimal('240')*daysec * c
y = -3.5
h = decimal.Decimal(str(10**y))*daysec
#%%
rk4_r,rk4_dr,rk4_phi,rk4_t,rk4_tau = rk4(r,dr,phi,t,tau,l,tauf,decimal.Decimal(str(h))*decimal.Decimal(str(c)),TT_v/daysec/c)
rk4_r_div,rk4_phi_div,rk4_t_div = divide_venus(rk4_r,rk4_phi,rk4_t)

dict = {'r':rk4_r,'phi':rk4_phi,'t':rk4_t}
df = pd.DataFrame(dict)
df.to_parquet('GR_RK4_venus_10^'+str(y)+'_div.parquet', compression='gzip')

# %%
r,dr,phi,t,tau,l,tauf = xe,decimal.Decimal('0'),decimal.Decimal('0'),decimal.Decimal('0'),decimal.Decimal('0'),ang_ear,decimal.Decimal('380')*daysec * c

#%%
rk4_r,rk4_dr,rk4_phi,rk4_t,rk4_tau = rk4(r,dr,phi,t,tau,l,tauf,decimal.Decimal(str(h))*decimal.Decimal(str(c)),TT_e/daysec/c)
rk4_r_div,rk4_phi_div,rk4_t_div = divide_earth(rk4_r,rk4_phi,rk4_t)

dict = {'r':rk4_r,'phi':rk4_phi,'t':rk4_t}
df = pd.DataFrame(dict)
df.to_parquet('GR_RK4_earth_10^'+str(y)+'_div.parquet', compression='gzip')

# %%
r,dr,phi,t,tau,l,tauf = xma,decimal.Decimal('0'),decimal.Decimal('0'),decimal.Decimal('0'),decimal.Decimal('0'),ang_mar,decimal.Decimal('700')*daysec * c

#%%
rk4_r,rk4_dr,rk4_phi,rk4_t,rk4_tau = rk4(r,dr,phi,t,tau,l,tauf,decimal.Decimal(str(h))*decimal.Decimal(str(c)),TT_ma/daysec/c)
rk4_r_div,rk4_phi_div,rk4_t_div = divide_mars(rk4_r,rk4_phi,rk4_t)

dict = {'r':rk4_r,'phi':rk4_phi,'t':rk4_t}
df = pd.DataFrame(dict)
df.to_parquet('GR_RK4_mars_10^'+str(y)+'_div.parquet', compression='gzip')