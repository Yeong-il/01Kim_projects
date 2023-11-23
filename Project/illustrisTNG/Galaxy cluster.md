
- 은하 형성에 대한 우주론적 자기 유체 역학 시뮬레이션인 illustrisTNG의 Data를 이용하여 z=0 은하단의 특성을 Red/Blue cluster를 기준에 따라 분류하고 물리적 특성을 비교하였다. Field 은하의 특성과 비교하여 sSFR수치와 Quenching Fraction에 따라, 즉 Star Formation이 z=0 은하단의 일반적인 모습인 Red cluster 보다 높게 나타날 수 있는 Blue cluster의 기준을 제시하였다. Blue cluster와 Red cluster의 은하단 매질 (ICM) Temperature Profile에 대하여 Fitting함으로써 cluster내 중심 온도를 계산해 특성을 비교하였다. 또한, Star Formation을 하는 은하의 cluster 안에서의 위치분포를 파악함으로써 특징을 분석하였다.

- 은하형성에 대한 연구는 우주의 균질성, 은하의 진화 방식, 다양한 구조가 구축되는 방식 등에 관한 연구이다. Blue cluster에 대한 연구는 은하단과 은하단 내 매질의 공진화를 연구하기 위해 필요하다. Blue cluster가 뜨거운 ICM (Intracluster Medium)을 수용하고 진화단계를 제한하는지 조사하는 것은 은하 형태와 진화 사이 연관성을 제시한다. 이러한 연구를 진행하기 위해서는 광범위한 Blue cluster에 대한 조사가 필요하다. 진화에 대한 연구는 time scale이 크기 때문에 관측 결과로만 진행하기에는 한계가 있기 때문에 시뮬레이션 Data (illustrisTNG)를 사용해 연구를 진행하였다. Galaxy cluster의 특성을 구성하는 은하 들의 Star Formation Rate, Mass, Quenching Fration에 따라 Red/Blue cluster의 기준을 나누고 Gas에 대한 시각화를 통해 위치에 따른 물리량 분포 차이를 연구하였다.

- Data Preprocessing : FOF subfind로 정렬된 z=0, scale factor = 1, h = 0.6774 (100km/s/Mpc) snapshot 99 data를 사용하였다. 또한, Halo Group 안의 Subhalo data는 Subflag =1 로 구분된 9,485,689개의 은하와, Halo Data는 galaxy cluster인 $10^{14}M_{\odot}$ 이상 426개를 사용하였다.

![700](https://i.imgur.com/aMiOeCA.png)

- Specific Star Formation Rate : illustrisTNG는 Halo 안 각각의 Subhalo들이 가지는 Star Formation Rate를 $M_{\odot}/yr$ 단위로 제공한다. 질량이 큰 Subhalo일수록 SFR이 커지는 경향성이 있기 때문에 Mass normalize하여 Specific Star Formation Rate를 계산하였다.

$$
SSFR = SFR_{half-mass-radius}/M_{half-mass-radius}
$$

- Quenching Fraction : Quenching이란 은하가 더 이상 Star Formation을 할 수 없는 상태를 말한다. sSFR=0인 Subhalo를 Quenching 되었다고 판단한다.

$$
Quenching-Fraction=N_{SSFR=0}/N_{total}*100
$$

Field 은하 (single halo)의 median 값과 비교하여 log sSFR값이 -9.9257 이상이고, Quenching Fraction이 98.79%보다 낮은 Halos를 Blue cluster로 분류하였고, 총 63개의 Blue cluster를 선별하였다. sSFR이 -10.25 (log scale) 이하이고, Quenching Fraction이 99% 이상인 Halos를 Red cluster로 분류하였다. 분류 결과 Red cluster가 질량이 비교적 큰 경향성을 보인다.
![700](https://i.imgur.com/jesFYO5.png)
- Temperature Profile (Cell에서의 mean Temperature 계산)

$$
T=\frac{(\gamma-1) U_{thermal}}{\mu m_H k}
$$

$\mu$ = mean moleculer weight, $m_H$ = mass of H, $k$ = boltzmann constant

$$
n(r)=n_0 [1+(\frac{r}{r_c})^2]^{-3\beta/2}, T(r)=A n(r)^{\gamma_{p}-1}
$$

$n_0,r_c,\beta,\gamma_p, A$ = fitting parameter

```math
R^2=1-\frac{SSR}{SST} (SST=\sum^{n}_{i}(y_i-\widetilde{y})^2, SSR=\sum^{n}_{i}(y_i-\widehat{y_i})^2)
```

: 모델 적합도

![700](https://i.imgur.com/ENsy4MA.png)

- Result & Discussion
![700](https://i.imgur.com/KAPXx39.png)
은하단 중심으로부터의 거리에 따라 Red/Blue cluster의 Quenching Fraction과 sSFR 값을 비교해보면 Quenching Fraction은 큰 차이가 없기는 하지만 cluster 안쪽에서 Blue cluster가 약간 낮게 나타났고, sSFR은 더 크게 나타났다. 선행 연구와 동일하게 Blue cluster 환경에서 Star Formation이 더 활발히 일어날 것으로 판단할 수 있다. ICM Temperature profile의 Fitting을 통해 Halo 내 중심온도를 계산한 값을 질량에 따라 나타냈다. 두 종류 cluster 모두 질량이 증가함에 따라서 중심온도가 증가하는 양상을 보였는데, Blue cluster의 중심 온도가 Red cluster보다 계층적으로 낮게 나타나는 것을 확인할 수 있다. 중심 온도 뿐만 아니라 모든 반경에 걸쳐서 Blue cluster의 gas 온도가 낮다는 점 또한 확인하였다.
![700](https://i.imgur.com/L4tLWhs.png)

Fitting parameter 분포 : parameter A가 Blue cluster가 Red cluster보다 작은 경향성을 보이는 데, 이는 Blue cluster의 중심온도가 Red cluster보다 낮은 것과 연관되어 해석된다. 다른 parameter 같은 경우는 Blue cluster과 Red cluster의 분포 차이가 크지 않았다.

- conclusion : 본 연구에서는 z=0 (현재) 에서의 TNG data를 통해 이미 안정화된 은하단 규모에서 Blue cluster에 대한 기준을 확립하고, ICM Temperature Profile은 Fitting을 통해 중심온도를 계산하여 Red cluster와 비교 분석하였다. 또한 Subhalo의 Quenching, Star Formation Position을 수치에 따라 나타내며 Star Formation이 일어날 수 있는 지역을 시각화하였다. 분석결과, Gas Temperature가 Blue cluster에서 더 낮은 것을 확인하였고 이것이 은하단 구성 은하의 star formation 및 quenching fraction에 영향을 주는 것으로 생각된다. 따라서 Blue cluster 환경에서 Quenching Fraction이 낮고 Star Formation이 활발할 것으로 추정된다.
