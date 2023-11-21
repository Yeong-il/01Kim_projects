
- CNN이란 (Convolutional Neural Networks : 합성곱 신경망) : 이미지 분야에서 강점을 가진 합성곱 연산을 이용한 딥러닝 모델

-데이터의 형상을 유지하기 때문에 픽셀 사이의 연관성, 채널 상의 연관성을 고려할 수 있음
-파라미터를 공유하기 때문에 fully-connected layer에 비해 학습해야할 파라미터 개수가 적음
-다양한 크기의 입력을 쉽게 처리할 수 있음. pooling을 사용하면 이미지 크기를 줄일 수 있음.

![700](https://i.imgur.com/lWK61qD.png)

Convolution : y축 기준 좌우 반전이 된 함수 g를 $\tau$ 만큼 이동한 후, 또 다른 함수 f와 곱하여 구간에 대해 적분

$(f*g)(t)=\int^{\infty}_{-\infty}f(\tau)g(t-\tau)d\tau(f*g)(i,j)=\sum^{h-1}_{x=0}\sum^{w-1}_{y=0}f(x,y)g(i-x,j-y)$

![500](https://i.imgur.com/ZQSpVbE.png)

![500](https://i.imgur.com/h5q6VjO.png)