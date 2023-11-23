
- 외계행성
외계행성은 태양계 밖의 행성으로, 태양이 아닌 다른 항성 주위를 공전하고 있는 행성이다. 지금까지 4,100 여개의 외계행성이 발견되었으며 모두 우리 은하 내에 존재한다. 우리 은하에만 수십억 개의 행성이 존재하는 것으로 추측되며 대부분 항성을 돌고 있다. 최초로 확인된 외계행성은 1992년 보고된 처녀자리에 있는 펄사 PSR B1257+12 주위를 공전하는 행성이다. 태양과 비슷한 별의 주의를 도는 외계행성으로서 최초로 확인된 것은 1995년에 보고된 51Pegasi 주위를 도는 행성이다. 이후 외계행성 탐색관측연구가 국제적으로 활발히 진행되어 2017년 중반까지 3,500개 이상의 외계행성이 공식 등록되었다. 이중 2,000여개는 NASA에서 2009년 발사한 케플러 우주망원경으로 발견한 행성이다. 외계행성을 찾는 대표적인 방법은 direct imaging 방법, radial velocity 방법, transit 방법, microlensing 방법, timing 방법, astrometry 방법이 있다.

-Transit 방법
행성이 모항성의 앞을 가로질러 나가게 되면 별과 행성의 상대적인 크기에 따라 별의 관측된 시각적 밝기가 조금씩 떨어지게 된다. 이러한 밝기의 변화를 보고 외계행성의 존재를 유추하는 것이 트랜짓 방법이다. 행성이 모성의 원반 앞을 지나가는 시간을 측정하여 행성에 대한 여러가지 정보를 수집할 수 있다. 식 시간을 측정하고 주연감광 효과를 포함하는 별의 대기 모델을 이용하면 행성의 반지름을 결정할 수 있다. 반지름이 결정되면 행성의 평균 밀도를 계산할 수 있게 된다.

<p align="center"><img src="https://i.imgur.com/yyDetXE.png" width="800">

- 관측
-관측 장비
광학계 : 주경 D = 1000mm, 부경 D = 250mm, F-ratio = 8.0
CCD(Sophia-2048B): 2048x2048 pixels (15 $\mu$ m), 30.7mm x 30.7mm
Field of View = 13.2 x 13.2  $arcmin^2$ 

<p align="center"><img src="https://i.imgur.com/dstSHIe.png" width="400">

<http://nysc.dothome.co.kr/>을 참고하여 관측 대상을 선정하였다. HAT-P-3b가 식현상이 주기가 짧고 밤중에 일어날 것이며, 다른 팀의 관측과 겹치지 않았기에 선정하였다.

| Distance              |         130.0 ($\pm$ 10.0)pc |
|:----------------------|:-----------------------------|
| Spectral type         | K                            |
| Magnitude V           |                        11.86 |
| Mass                  | 0.917 ($\pm$ 0.03) $M_{sun}$ |
| Effective Temperature |        5224.0 ($\pm$ 69.0) K |
| Radius                | 0.799 ($\pm$ 0.039)$R_{sun}$ |
| Ra                    |                   13:44:23.0 |
| Dec                   |                    +48:01:43 |
| Semi-Major Axis       |   0.03866 ($\pm$ 0.00041) AU |
| Orbital Period        | 2.899703 ($\pm$ 5.4e-05) day |
| inclination           |       87.07 ($\pm$ 0.55) deg |
| primary_depth(mag)    |                     0.010809 |  

-관측 정보

| 관측 일시  |          2020-02-10 |
|:-------|:--------------------|
| 적경     |        13:44:22.999 |
| 적위     |           +48:01:43 |
| 관측 시작  | 2020-02-10 23:42:00 |
| 관측 마무리 | 2020-02-11 05:59:11 |
| 노출시간   |                 60s |
| 필터     | R                   |  

- CCD Preprocessing
CCD 영상자료는 영점이동, 암전자 생성률, 양자효율의 차이 등에 따라, 관측자가 원하지 않는 신호가 포함되어 있어, 이를 보정해 주어야 원하는 천체의 신호를 정확하게 얻을 수 있다. 관측하는 기간동안 여분의 시간동안 기기적 특성을 제거하는 데 사용할 영상들을 얻어야한다. 이런 images로는 bias images, dark images, flat images 등이 있다. 

<p align="center"><img src="https://i.imgur.com/T1BDeF9.png" width="400">
 
> Master bias (38 combine)

- Bias images
셔터를 닫은 상태에서 0초 노출을 주어 얻은 값으로 원론적으로는 항상 일정한 값을 가져야 하지만, 외부온도의 변화, 망원경의 지향방향 등의 요인들에 의해 약간씩 변화한다. 따라서 이를 정확하게 보정해주기 위해서는 영점영상을 수시로 얻어야 한다. 그러나 이렇게 하는 경우 관측시간의 낭비가 심각하다. 관측의 효율성을 위해 천문용 CCD의 경우 overscan이라는 기기적인 영점 변화를 기록한 부분을 CCD 영상에 덧붙여 두고, 이를 이용하여 시간에 따른 영점의 변화를 보정할 수 있도록 되어있다. CCD로 사용한 Sophia-2048는 overscan기능이 없었으므로 사용하지 않았다. overscan은 정확도 보다는 효율을 높이기 위한 기능이다.

<p align="center"><img src="https://i.imgur.com/QCqZOwn.png" width="400">
 
> Master dark (combine)

- Dark images
모든 반도체들은 상온에서 어느정도 암전자를 발생시킨다. (dark electron) 암전자의 생성률은 온도에 따라 지수함수 꼴로 증가한다. 대부분의 천문용 CCD의 경우 액체질소(liquid nitrogen, LN2)를 사용하여 -100 $^\circ C$ 정도의 온도를 유지하고 있어, 암전자를 거의 발생시키지 않는다. 그러나 열전냉각방식으로 CCD를 냉각하는 경우 또는 특정 CCD 칩의 경우 무시할 수 없을 정도의 암전자를 발생시킨다. 그러므로 이와같은 경우에는 관측기간 동안 암전자 영상을 얻어서 이를 보정해 주어야 한다.

<p align="center"><img src="https://i.imgur.com/GpVsWJg.png" width="400">
 
> Master flat (R filter 5 combine)

- Flat images
CCD 칩의 화소 하나하나는 광증배관 하나와 같은 역할을 하며, 따라서 각화소가 빛에 반응하여 발생시키는 광전자의 수도 동일할 수 없으며, 입사광의 파장에 따른 반응도 동일하지 않다. 그러므로 빛에 반응하는 양자효율의 차이를 보정하여야한다. 그러나 각 화소의 절대적인 양자효율을 알 필요는 없기 때문에 균일한 광원을 촬영한 상대적인 양자효율의 차이를 보정한다. 천문관측에서는 바닥고르기에 사용하는 균일한 광원으로는 분포가 밤하늘의 에너지 분포와는 완벽하게 동일하지 않다. 따라서 매우 정교한 측광이 필요한 경우에는 박명하늘을 사용하지 않고, 별이 거의 없는 밤하늘을 촬영한 영상을 사용한다. 한편 돔 내에 설치된 영사막에 비친 전등 빛을 촬영하는 경우도 있으나, 망원경의 초점거리에 비해 거리가 너무 가까워 균일광원이 되지 못한다. 이런 경우 박명하늘을 촬영한 flat images를 사용하여 큰 규모의 차이를 보정해 주어야 한다. flat image를 얻는 동안에 점점 더 어두워지므로 나중에 얻는 flat image같은 경우 노출을 조금 더 주어 얻어야한다. 방위각 115 $^\circ$  고도 65 $^\circ$ 18시 33분부터 flat image를 얻었다. dark image와 flat image를 얻을 때 bias가 포함되어 있으므로 보정해주어야 원하는 이미지 전처리를 수행할수 있다. 앞서 작업해놓은 bias, dark, flat을 통해 이미지를 보정하였다. 이미지를 bias, dark, flat을 통해 보정했지만 끝난것이 아니다. 관측하는 동안 위치가 변화했기 때문에 이미지들의 위치를 이동시켜 맞게 align 해주어야한다.

<p align="center"><img src="https://i.imgur.com/CR4e8M4.png" width="400"><img src="https://i.imgur.com/UO1pla5.png" width="400">

> 상 : dark60s에서 bias 보정한 이미지
> 하 : flat R에서 bias 보정한 이미지

<p align="center"><img src="https://i.imgur.com/eYL2pOl.png" width="400"><img src="https://i.imgur.com/Ns36AfW.png" width="400">

> 상 : 전처리 전, 하 : 전처리 후

- 좌표동정 및 CAT파일 생성
하단의 왼쪽 이미지와 오른쪽 이미지처럼 별들의 x_pixel값과 y_pixel값에 차이가 있다. 이러한 차이를 줄여주기 위해서 xregistar라는 Task를 사용한다. xregi에서 일정한 영역을 지정해주면 그 영역을 기준으로 이미지 상의 별들의 위치를 서로 찾아 맞춰주게 된다. x_pixel, y_pixel을 [650:1050], [650:1050] 영역을 기준으로 위치를 이동시켜 맞춰주었다.

<p align="center"><img src="https://i.imgur.com/BctXjGN.png" width="400"><img src="https://i.imgur.com/BWcVrq1.png" width="400">

이제 python으로 그래프를 얻기 전에 catalogue 파일을 만들어야한다. catalogue파일에는 number, flux_aper, fluxerr_aper, mag_aper, magerr_aper, background, ximage, yimage을 포함하기 위해서 def.param에서 설정해주었다. 그리고 dex.sex에서 seeing_fwhm 5, thresh 5로 설정했다. thresh를 5로 설정한 이유는 어두운 등급의 별을 catalogue파일에 포함되지 않기 위해 했고 aperture photometry를 통해 seeing fwhm은  얻은 결과 값을 바탕으로 했다. 

<p align="center"><img src="https://i.imgur.com/I52BkE5.png" width="400"><img src="https://i.imgur.com/K5vLTki.png" width="400">

<p align="center"><img src="https://i.imgur.com/P2oAyCW.png" width="800">

imexam을 통해 얻은 왼쪽 이미지 하단의 값들중 마지막 값이 FWHM을 의미한다. aperture photometry에서 aperture radius ~ FWHM이다. 파이썬 코드를 사용하여 모든 fits 파일의 cat파일을 만들수 있다. 

<p align="center"><img src="https://i.imgur.com/7XA7l3V.png" width="400">

cat파일에 담긴 정보를 통해 fits 이미지에 담긴 별들의 번호를 매겨야 한다. 28개의 별의 정보가 담겨있는데 번호를 0번부터 28번까지 밝은 순으로 번호를 매겨 우리의 타겟 별이 몇번인가 알아보기 위해 다음과 같은 코드로 진행하게 된다. 

<p align="center"><img src="https://i.imgur.com/3NTkXkW.png" width="400"><img src="https://i.imgur.com/bhcHcwC.png" width="400">

우리가 타겟으로하는 별은 중앙에 위치한 2번별임을 알수 있다. index값으로 번호를 매겼기 때문에 0번부터 시작한다. 별이 굉장히 많기 때문에 비교성을 고르기에 어려움이 있다. 그래서 10개의 별만 표시하게 코드를 이용한다. 

<p align="center"><img src="https://i.imgur.com/yJJJzkg.png" width="400"><img src="https://i.imgur.com/eVVLxHq.png" width="400">

<p align="center"><img src="https://i.imgur.com/d98TJai.png" width="400"><img src="https://i.imgur.com/mjK5aC2.png" width="400">
 
2번은 타겟별이고 3번을 비교성으로 설정했다. 3번 별은 2번별과 등급이 비슷하고 등급 오차또한 0에 가까운 작은 값을 가지고 있기 때문에 비교성에 적합하다. 비교성을 3번으로 설정했을 때 얻을 수 있는 그래프는 다음과 같다. x축 값은 JD-HELIO로 JD와의 차이점은 JD는 지구를 중심으로한 율리우스일이지만, JD-HELIO는 태양을 중심으로 하기 때문에 태양과 지구까지의 광속거리만큼 대략 493초만큼 차이나는 율리우스 일이다. y축 값은 비교성과 목적성의 등급 차로 대기효과를 보정하였다. $(m_{1}-m_{2}=-2.5log\frac{l_1}{l_2})$

<p align="center"><img src="https://i.imgur.com/N2bNLzb.png" width="400"><img src="https://i.imgur.com/SQwVTFA.png" width="400">

- 회색대기
회색대기(항성 대기의 불투명도는 파장에 따라 변화하지만, 그것을 무시하고 평균적인 흡수로 대치하여 만든 대기 모델)와 에딩턴 근사를 가정하면 반지름 r에 따르는 빛의 세기 I(r)을 이와 같이 얻을 수 있다.

```math
I(r)=I(0)(\frac{2}{5}+\frac{3}{5}\sqrt{1-\frac{r^2}{R^2_*}})
```

<p align="center"><img src="https://i.imgur.com/d3W5pQv.png" width="400">

$R_*$는 별의 반지름이다. I(r)을 통해 별원반의 총 플럭스는 다음과 같이 구할 수 있다.


```math
F_{disk}=\int^{R_*}_{0}I(r)d\ohm=\int^{R_*}_{0}I(r)\frac{2\pi r}{d^2}dr=\frac{4\pi R^2_*}{5d^2}I(0)
```


d는 별과 지구까지의 거리를 의미한다. $\lambda$ 함수를 사용하면 식을 각도를 포함한 강도로 다시 쓸수 있다.


```math
F_{tr}(x,R_*,R_p)=\int^{R_*}_{0}I(r)\frac{r}{d^2}2\pi-\lambda(r,x,R_p,R_*)dr
```


```math
=\frac{I(0)}{d^2}\int^{R_*}_{0}(\frac{2}{5}+\frac{3}{5}\sqrt{1-\frac{r^2}{R^2_*}})2\pi-\lambda(r,x,R_p,R_*)rdr
```


```math
=F_{disk}\frac{5}{4\pi R^2_*}\int^{R_*}_{0}(\frac{2}{5}+\frac{3}{5}\sqrt{1-\frac{r^2}{R^2_*}})2\pi-\lambda(r,x,R_p,R_*)rdr
```


이를 통해 그래프를 얻었다. b'는 궤도 경사와 관련된 값으로 클수록 궤도 경사가 크고 작을 수록 궤도경사가 작다.

<p align="center"><img src="https://i.imgur.com/i3ukQv4.png" width="400">

- Conclusion
외계행성은 태양계 이외에 행성계를 가진 천체로 의의가 있다. 항상 관심을 가질 수 밖에 없는 제 2의 지구같이 생명체의 존재 가능성을 확인하게 한다. 생명체가 존재할 수 있는 가능성이 있는 또는 거주 가능한 조건을 만족하는 영역을 골디락스 존이라고 부른다. 골디락스 존은 생명이 태어나서 자리기에 적절한 온도가 형성되는 띠이다. 보통 적적한 온도는 인간을 기준으로 판단하며 물의 끓는 점과 어는 점인 섭씨 100 $^\circ C$ ~ 0 $^\circ C$ 사이이다. 뜨겁고 밝은 별일 수록 띠는 별로부터 먼곳에 위치하고 있지만 폭은 넓다. 반대로 차갑고 어두운 별일 수록 별로 부터 가까운 곳에 있고, 그 폭은 좁다. 생명체가 존재할 수 있는 지역을 중심별의 질량과 중심별의 거리에 따라 그린 그래프 상에 관측대상인 HAT-P-3 행성게의 위치를 표시할 수 있었다. HAT-P-3은 태양 질량의 약 0.9배 이고 분광형이 K형이며 행성인 HAT-P-3b와의 거리는 약 0.04AU이다. 생명가능 지대라 표시된 영역에는 위치하지 않음을 확인할 수 있었다.

<p align="center"><img src="https://i.imgur.com/KP0nngw.png" width="400"><img src="https://i.imgur.com/G8R98F3.png" width="400">

> 별의 밝기에 따라 거주가능 영역의 크기는 큰 차이를 보인다. 왼쪽 가장 큰 것이 A형 주계열성인 시리우스의 것으로 중심별로부터 5AU(목성 정도 거리)에서 알맞은 온도가 형성되며 그 폭도 매우 넓다. 두 번째는 알파 센타우리에서 밝은 쪽(태양보다 약간 더 밝다)인 A, 세 번째는 태양 밝기 절반 정도인 B의 거주가능영역이다. 제일 오른쪽이 적색왜성 프록시마로, 육안으로 보기 힘들 정도로 작고 그 폭도 좁음을 알 수 있다.

중심별의 온도는 행성의 온도, 수명, 자외선, 행성의 생성률 등 생명체가 살 수 있을 조건에 복합적인 영향을 주어 매우 밝은 별도, 매우 어두운 별도 그 근처에는 생명체가 살기 힘들다. 실제로는 태양보다 약간 밝거나 비슷한 정도의 온도를 가진 별(분광형으로는 차가운 K형 ~ 뜨거운 F형 정도)의 별에서 생명체가 존재할 가능성이 가장 높다고 예상된다. 케플러 계획이나 세계 여러 외계행성 프로젝트의 관심도 이들 분광형 항성에 맞춰져 있다.

현재는 이러한 항성의 표면온도와 안정적인 자외선 양 적외선 양, 가시광선의 양과 행성의 대기 분포와 안정적인 오존층의 형성 등을 종합해 본 결과 분광형 K1의 한부분인 5100K부터 분광형 F7의 한부분인 6250K까지가 안정권이다. 즉 5100K ~ 6250K의 표면온도를 가진 항성이 안정적인 생명체를 품을 수 있으며 여기를 벗어나면 불안정요소가 증가하게 된다. 또한 이정도의 표면온도를 가진 항성의 질량은 태양의 0.855~1.08배인데 태양의 50%~130% 양의 열을 뿜기 때문에 항성과의 거리가 어느정도 되어 조석고정을 걱정할 필요가 없으면, 수명도 75억년에서 170억년이나 되어 안정적이며, 항성의 밀도도 적당하기 때문에 플레어의 위험성도 없다.

외계행성계는 우리 태양계 이외에 생명체가 존재할 수 있는 지역 중 하나이다. 이러한 발견은 2009년 케플러우주망원경이 발사된 이후 더욱 박차를 가하고 있다. 앞으로도 더 많은 외계행성에 대한 연구가 진행될 것이고, 다양한 학문에 영향을 끼쳐 과학의 발전을 가져올 것이다.
