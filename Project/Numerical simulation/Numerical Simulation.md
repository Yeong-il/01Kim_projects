Due to recent developments in computer technology and the importance of computer calculations, the use of numerical simulation methods in research gains more and more importance. Numerical simulation is a computational technique used to model and analyze complex real-world or theoretical systems and phenomena. It involves solving mathematical models through numerical methods, typically on a computer, to understand and predict the behavior of systems. Numerical simulation can address situations where observations are challenging or when it's difficult to precisely obtain solutions to theoretical equations. In the future, numerical simulations are likely to see increasing use in many areas of astrophysics. 

## Numerical Simulation steps 
### Numerical Method - Runge-Kutta Method 

The Runge-Kutta method is finding solutions to ordinary differential equations (ODEs). It's a widely used family of methods that provide an accurate and efficient way to approximate the solutions of ODEs, particularly for initial value problems. The most commonly used member of this family is the fourth-order Runge-Kutta method, often referred to a RK4.

![500](https://i.imgur.com/EeiI4XS.png)
> Runge-Kutta 4th order method

$$
\begin{flalign*}
&y' = f(x,t) = \frac{dy}{dt} ,y_{n} = f(x_{n},t_{n})\\
&\\
&K_{1} = \Delta t f(x_{n},t_{n})\\
&K_{2} = \Delta t f(x_{n}+\frac{1}{2}K_{1},t_{n}+\frac{\Delta t}{2})\\
&K_{3} = \Delta t f(x_{n}+\frac{1}{2}K_{2},t_{n}+\frac{\Delta t}{2})\\
&K_{4} = \Delta t f(x_{n}+K_{3},t_{n}+\Delta t)\\\\
&y_{n+1} = y_{n}+\frac{1}{6}K_{1}+\frac{1}{3}K_{2}+\frac{1}{3}K_{3}+\frac{1}{6}K_{4} 
\end{flalign*}
$$

### Deviation

$$
\begin{flalign*}
&f(x+\Delta x,t+\Delta t) = f(x,t)+\Delta x \frac{\partial f}{\partial x}+\Delta t \frac{\partial f}{\partial t}+\frac{1}{2}(\Delta x^2\frac{\partial ^2f}{\partial x^2}+2\Delta x \Delta t \frac{\partial^2f}{\partial x \partial t}+\Delta t^2 \frac{\partial^2f}{\partial t^2}+\cdots)\\
&\\
&K_{1}=\Delta t f(x_{n},t_{n})&&
\end{flalign*}
$$

$$
\begin{flalign*}
K_{2}& = \Delta t f(x_{n}+\frac{1}{2}K_{1},t_{n}+\frac{1}{2}\Delta t)\\
& = \Delta t f(x_{n},t_{n})+\frac{1}{2}\Delta t K_{1}f_{x}(x_{n},t_{n})+ \frac{1}{2}(\Delta t)^2f_{t}(x_{n},t_{n})+\frac{1}{2}\Delta t(\frac{1}{4}K_{1}^2\frac{\partial^2f}{\partial x^2}+2\frac{1}{4}\Delta t K_{1}\frac{\partial^2f}{\partial x \partial t}+\frac{1}{4}\Delta t^2 \frac{\partial^2 f}{\partial t^2})+\cdots\\
& = \Delta t f(x_{n},t_{n})+\frac{1}{2}(\Delta t)^2f(x_{n},t_{n})f_{x}(x_{n},t_{n})+\frac{1}{2}(\Delta t)^2f_{t}(x_{n},t_{n})+\frac{\Delta t^3}{8}(f^2(x_{n},t_{n})\frac{\partial^2f}{\partial x^2}+2f(x_{n},t_{n})\frac{\partial^2f}{\partial x \partial t}+\frac{\partial^2 f}{\partial t^2})\\
&+\vartheta (\Delta t^4)&&
\end{flalign*}
$$

$$
\begin{flalign*}
K_{3}& = \Delta tf(x_{n}+\frac{1}{2}K_{2},t_{n}+\frac{1}{2}\Delta t)\\
& = \Delta t f(x_{n},t_{n})+\frac{1}{2}\Delta t K_{2}f_{x}(x_{n},t_{n})+\Delta t(\frac{1}{2}\Delta t)f_{t}(x_{n},t_{n})+\frac{1}{2}\Delta t(\frac{1}{4}K_{2}^2\frac{\partial^2f}{\partial x^2}+2\frac{1}{4}\Delta t K_{2}\frac{\partial^2f}{\partial x \partial t}+\frac{1}{4}\Delta t^2 \frac{\partial^2 f}{\partial t^2})+\cdots\\
& = \Delta tf(x_{n},t_{n})+\frac{1}{4}(\Delta t)^2f(x_{n},t_{n})f_{x}(x_{n},t_{n})+\frac{1}{2}(\Delta t)^3(f(x_n,t_n)f_{x}^2(x_{n},t_{n})+f_{t}(x_{n},t_{n})f_{x}(x_{n},t_{n}))\\
&+\frac{1}{2}(\Delta t)^2f_{t}(x_{n},t_{n})+\frac{\Delta t^3}{8}(f^2(x_{n},t_{n})\frac{\partial^2f}{\partial x^2}+2f(x_{n},t_{n})\frac{\partial^2f}{\partial x \partial t}+\frac{\partial^2 f}{\partial t^2})+\vartheta (\Delta t^4)
&&
\end{flalign*}
$$

$$
\begin{flalign*}
K_{4}& = \Delta t f(x_{n}+K_{3},t_{n}+\Delta t)\\
& = \Delta t f(x_{n},t_{n})+\Delta tK_{3}f_{x}(x_{n},t_{n})+(\Delta t)^2f_{t}(x_{n},t_{n})+\frac{1}{2}\Delta t^3(f^2(x_{n},t_{n})\frac{\partial^2f}{\partial x^2}+2f(x_{n},t_{n})\frac{\partial^2f}{\partial x \partial t}+\frac{\partial^2 f}{\partial t^2})+\cdots+\vartheta(\Delta t^4)\\
& = \Delta tf(x_{n},t_{n})+\frac{1}{2}(\Delta t)^2f(x_{n},t_{n})f_{x}(x_{n},t_{n})+\frac{1}{2}(\Delta t)^3(f(x_n,t_n)f_{x}^2(x_{n},t_{n})+f_{t}(x_{n},t_{n})f_{x}(x_{n},t_{n}))+(\Delta t)^2f_{x}(x_{n},t_{n})\\
&+\frac{1}{2}(\Delta t)^3(f^2(x_{n},t_{n})\frac{\partial^2f}{\partial x^2}+2f(x_{n},t_{n})\frac{\partial^2f}{\partial x \partial t}+\frac{\partial^2 f}{\partial t^2})+\vartheta(\Delta t^4)&&
\end{flalign*}
$$

$$
\begin{flalign*}
y_{n+1}& = \gamma_{1}K_{1}+\gamma_{2}K_{2}+\gamma_{3}K_{3}+\gamma_{4}K_{4}\\
& = (\gamma_{1}+\gamma_{2}+\gamma_{3}+\gamma_{4})\Delta tf(x_{n},t_{n})+(\gamma_{2}+\gamma_{3}+2\gamma_{4})\frac{\Delta t^2}{2}(f(x_{n},t_{n})f_{t}(x_{n},t_{n})+f_{t}(x_{n},t_{n}))+\Delta t^3[(\frac{\gamma_{2}}{8}+\frac{\gamma_{3}}{8}+\frac{\gamma_{4}}{2})\\
&(f^2(x_{n},t_{n})\frac{\partial^2f}{\partial x^2}+2f(x_{n},t_{n})\frac{\partial^2f}{\partial x \partial t}+\frac{\partial^2 f}{\partial t^2})+\vartheta (\Delta t^4)+(\frac{\gamma_{3}}{4}+\frac{\gamma_{4}}{2})(f(x_{n},t_{n})f_{x}^2(x_{n},t_{n})+f_{t}(x_{n},t_{n})f_{x}(x_{n},t_{n}))]+\vartheta(\Delta t^4)
&&
\end{flalign*}
$$

$$
\begin{flalign*}
y_{n+1}& = y_{n}+y\prime\Delta t+y\prime\prime\frac{\Delta t^2}{2!}+y\prime\prime\prime\frac{\Delta t^3}{3!}+\cdots\\
& = y_{n}+f(x_{n},t_{n})\Delta t+(f_{x}(x_{n},t_{n})f(x_{n},t_{n})+f_{t}(x_{n},t_{n}))\frac{\Delta t^2}{2!}+(f_{x}(x_{n},t_{n})^2f(x_{n},t_{n})+f_{x}(x_{n},t_{n})f_{t}(x_{n},t_{n})\\
& = +f_{xx}(x_{n},t_{n})f^2(x_{n},t_{n})+2f(x_{n},t_{n})f_{xt}(x_{n},t_{n})+f_{tt}(x_{n},t_{n}))\frac{\Delta t^3}{3!}+\cdots
&&
\end{flalign*}
$$

$$
\gamma_{1}=\gamma_{4}=\frac{1}{6},\gamma_{2}=\gamma_{3}=\frac{2}{6}\\
$$

### High order Runge-Kutta Method

The Runge-Kutta-Fehlberg (RKF) method is a numerical integration technique for solving ordinary differential equations (ODEs). It is an adaptive method that adjusts the step size during integration to control the accuracy of the solution. The RKF method is based on the classic Runge-Kutta method, but it also uses an embedded method (like the fourth-order method) to estimate the error and adaptively adjust the step size.

- RKF 5th order method

$$
\begin{flalign*}
&y' = f(x,t) = \frac{dy}{dt} ,y_{n} = f(x_{n},t_{n})\\
&K_{1} = \Delta t f(x_{n},t_{n})\\
&K_{2} = \Delta t f(x_{n}+\frac{1}{4}K_{1}, t_{n}+\frac{1}{4}\Delta t)\\
&K_{3} = \Delta t f(x_{n}+\frac{3}{32}K_{1}+\frac{9}{32}K_{2}, t_{n}+\frac{3}{8}\Delta t)\\
&K_{4} = \Delta t f(x_{n}+\frac{1932}{2197}K_{1}-\frac{7200}{2197}K_{2}+\frac{7296}{2197}K_{3},t_{n}+\frac{12}{13}\Delta t)\\
&K_{5} = \Delta t f(x_{n}+\frac{439}{216}K_{1}-8K_{2}+\frac{3680}{513}K_{3}-\frac{845}{4104}K_{4},t_{n}+\Delta t)\\
&K_{6} = \Delta t f(x_{n}-\frac{8}{27}K_{1}+2K_{2}-\frac{3544}{2565}K_{3}+\frac{1859}{4104}K_{4}-\frac{11}{40}K_{5},t_{n}+\frac{1}{2}\Delta t)\\\\
&y_{n+1} = y_{n}+\frac{16}{135}K_{1}+\frac{6656}{12825}K_{3}+\frac{28561}{56430}K_{4}-\frac{9}{50}K_{5}+\frac{2}{55}K_{6}&&
\end{flalign*}
$$


- RKF 6th order method

$$
\begin{flalign*}
&y' = f(x,t) = \frac{dy}{dt} ,y_{n} = f(x_{n},t_{n})\\
&K_{1} = \Delta t f(x_{n},t_{n})\\
&K_{2} = \Delta t f(x_{n}+\frac{1}{6}K_{1},t_{n}+\frac{1}{6}\Delta t)\\
&K_{3} = \Delta t f(x_{n}+\frac{4}{75}K_{1}+\frac{16}{75}K_{2},t_{n}+\frac{4}{15}\Delta t)\\
&K_{4} = \Delta t f(x_{n}+\frac{5}{6}K_{1}-\frac{8}{3}K_{2}+\frac{5}{2}K_{3},t_{n}+\frac{2}{3}\Delta t)\\
&K_{5} = \Delta t f(x_{n}-\frac{8}{5}K_{1}+\frac{144}{25}K_{2}-4K_{3}+\frac{16}{25}K_{4},t_{n}+\frac{4}{5}\Delta t)\\
&K_{6} = \Delta t f(x_{n}+\frac{361}{320}K_{1}-\frac{18}{5}K_{2}+\frac{407}{128}K_{3}-\frac{11}{80}K_{4}+\frac{55}{128}K_{5},t_{n}+\Delta t)\\
&K_{7} = \Delta t f(x_{n}-\frac{11}{640}K_{1}+\frac{11}{256}K_{3}-\frac{11}{160}K_{4}+\frac{11}{256}K_{5},t_{n})\\
&K_{8} = \Delta t f(x_{n}+\frac{93}{640}K_{1}-\frac{18}{5}K_{2}+\frac{803}{256}K_{3}-\frac{11}{160}K_{4}+\frac{99}{256}K_{5}+K_{7},t_{n}+\Delta t)\\
&y_{n+1} = y_{n}+\frac{7}{1408}K_{1}+\frac{1125}{2816}K_{3}+\frac{9}{32}K_{4}+\frac{125}{768}K_{5}+\frac{5}{66}K_{7}+\frac{5}{66}K_{8}&&
\end{flalign*}
$$


- RKF 7th order method

$$
\begin{flalign*}
&y' = f(x,t) = \frac{dy}{dt} ,y_{n} = f(x_{n},t_{n})\\\\
&K_{1} = \Delta t f(x_{n},t_{n})\\
&K_{2} = \Delta t f(x_{n}+\frac{2}{33}K_{1},t_{n}+\frac{2}{33}\Delta t)\\
&K_{3} = \Delta t f(x_{n}+\frac{4}{33}K_{2},t_{n}+\frac{4}{33}\Delta t)\\
&K_{4} = \Delta t f(x_{n}+\frac{1}{22}K_{1}+\frac{3}{22}K_{3},t_{n}+\frac{2}{11}\Delta t)\\
&K_{5} = \Delta t f(x_{n}+\frac{43}{64}K_{1}-\frac{165}{64}K_{3}+\frac{77}{32}K_{4},t_{n}+\frac{1}{2}\Delta t)\\
&K_{6} = \Delta t f(x_{n}-\frac{2383}{486}K_{1}+\frac{1067}{54}K_{3}-\frac{26312}{1701}K_{4}+\frac{2176}{1701}K_{5},t_{n}+\frac{2}{3}\Delta t)\\
&K_{7} = \Delta t f(x_{n}+\frac{10077}{4802}K_{1}-\frac{5643}{686}K_{3}+\frac{116259}{16807}K_{4}-\frac{6240}{16807}K_{5}+\frac{1053}{2401}K_{6},t_{n}+\frac{6}{7}\Delta t)\\
&K_{8} = \Delta t f(x_{n}-\frac{733}{176}K_{1}+\frac{141}{8}K_{3}-\frac{335763}{23296}K_{4}+\frac{216}{77}K_{5}-\frac{4617}{2816}K_{6}+\frac{7203}{9152}K_{7},t_{n}+\Delta t)\\
&K_{9} = \Delta t f(x_{n}+\frac{15}{352}K_{1}-\frac{5445}{46592}K_{4}+\frac{18}{77}K_{5}-\frac{1215}{5632}K_{6}+\frac{1029}{18304}K_{7},t_{n})\\
&K_{10} = \Delta t f(x_{n}-\frac{1833}{352}K_{1}+\frac{141}{8}K_{3}-\frac{51237}{3584}K_{4}+\frac{18}{7}K_{5}-\frac{729}{512}K_{6}+\frac{1029}{1408}K_{7}+K_{9},t_{n}+\Delta t)\\\\
&y_{n+1} = y_{n}+\frac{11}{864}K_{1}+\frac{1771561}{6289920}K_{4}+\frac{32}{105}K_{5}+\frac{243}{2560}K_{6}+\frac{16807}{74880}K_{7}+\frac{11}{270}K_{9}+\frac{11}{270}K_{10}&&
\end{flalign*}
$$


- RKF 8th order method

$$
\begin{flalign*}
&y' = f(x,t) = \frac{dy}{dt} ,y_{n} = f(x_{n},t_{n})\\\\
&K_{1} = \Delta t f(x_{n},t_{n})\\
&K_{2} = \Delta t f(x_{n}+\frac{2}{27}K_{1},t_{n}+\frac{2}{27}\Delta t)\\
&K_{3} = \Delta t f(x_{n}+\frac{1}{36}K_{1}+\frac{1}{12}K_{2},t_{n}+\frac{1}{9}\Delta t)\\
&K_{4} = \Delta t f(x_{n}+\frac{1}{24}K_{1}+\frac{1}{8}K_{3},t_{n}+\frac{1}{6}\Delta t)\\
&K_{5} = \Delta t f(x_{n}+\frac{20}{48}K_{1}-\frac{75}{48}K_{3}+\frac{75}{48}K_{4},t_{n}+\frac{5}{12}\Delta t)\\
&K_{6} = \Delta t f(x_{n}+\frac{1}{20}K_{1}+\frac{1}{4}K_{4}+\frac{1}{5}K_{5},t_{n}+\frac{1}{2}\Delta t)\\
&K_{7} = \Delta t f(x_{n}-\frac{25}{108}K_{1}+\frac{125}{108}K_{4}-\frac{260}{108}K_{5}+\frac{250}{108}K_{6},t_{n}\frac{5}{6}\Delta t)\\
&K_{8} = \Delta t f(x_{n}+\frac{31}{300}K_{1}+\frac{61}{225}K_{5}-\frac{2}{9}K_{6}+\frac{13}{900}K_{7},t_{n}+\frac{1}{6}\Delta t)\\
&K_{9} = \Delta t f(x_{n}+2K_{1}-\frac{53}{6}K_{4}+\frac{704}{45}K_{5}-\frac{107}{9}K_{6}+\frac{67}{90}K_{7}+3K_{8},t_{n}+\frac{2}{3}\Delta t)\\
&K_{10} = \Delta t f(x_{n}-\frac{91}{108}K_{1}+\frac{23}{108}K_{4}-\frac{976}{135}K_{5}+\frac{311}{54}K_{6}-\frac{19}{60}K_{7}+\frac{17}{6}K_{8}-\frac{1}{12}K_{9},t_{n}+\frac{1}{3}\Delta t)\\
&K_{11} = \Delta t f(x_{n}+\frac{2383}{4100}K_{1}-\frac{341}{164}K_{4}+\frac{4496}{1025}K_{5}-\frac{301}{82}K_{6}+\frac{2133}{4100}K_{7}+\frac{45}{82}K_{8}+\frac{45}{164}K_{9}+\frac{18}{41}K_{10},t_{n}+\Delta t)\\
&K_{12} = \Delta t f(x_{n}+\frac{3}{205}K_{1}-\frac{6}{41}K_{6}-\frac{3}{205}K_{7}-\frac{3}{41}K_{8}+\frac{3}{41}K_{9}+\frac{6}{41}K_{10},t_{n})\\
&K_{13} = \Delta t f(x_{n}-\frac{1777}{4100}K_{1}-\frac{341}{164}K_{4}+\frac{4496}{1025}K_{5}-\frac{289}{82}K_{6}+\frac{2193}{4100}K_{7}+\frac{51}{82}K_{8}+\frac{33}{164}K_{9}+\frac{12}{41}K_{10}+K_{12},t_{n}+\Delta t)\\
&y_{n+1} = y_{n}+\frac{34}{105}K_{6}+\frac{9}{35}K_{7}+\frac{9}{35}K_{8}+\frac{9}{280}K_{9}+\frac{9}{280}K_{10}+\frac{41}{840}K_{12}+\frac{41}{840}K_{13}&&
\end{flalign*}
$$

### Problem Formulation

$$
\begin{flalign*}
&<Schwarzschild\;geodesic>\\\\
&ds^2=-(1-\frac{2M}{r})dt^2+(1-\frac{2M}{r})^{-1}dr^2+r^2d\theta^2+r\sin^2{\theta}d\phi^2\\\\
&<conserved\;quantity>\\\\
&(1-\frac{2M}{r})\frac{dt}{d\tau}=\widetilde{E},\;\;\;r^2\frac{d\phi}{d\tau}=\widetilde{L}\\\\
&(\frac{dr}{d\tau})^2=\widetilde{E}^2-(1-\frac{2M}{r})(1+\frac{\widetilde{L}^2}{r^2})\\\\
&\frac{d^2r}{d\tau^2}=-\frac{M}{r^2}+\frac{\widetilde{L}^2}{r^3}-\frac{3M\widetilde{L}^2}{r^4}\\\\
&(\frac{dr}{d\phi})^2=\frac{(dr/d\tau)^2}{(d\phi/d\tau)^2}=\frac{\widetilde{E}^2-(1-\frac{2M}{r})(1+\frac{\widetilde{L}^2}{r^2})}{\widetilde{L}^2/r^4} &&
\end{flalign*}
$$

The Schwarzschild metric describes the spacetime geometry around a spherically symmetric non-rotating mass, such as a black hole. Geodesics in this metric represent the paths that particles or light rays follow when influenced solely by gravity. Constructing an algorithm to compute geodesics in the Schwarzschild metric is a complex task.

### Deviation

$$
\begin{flalign*}
&x^{\mu}=(t,r,\theta,\phi)=(x^0,x^1,x^2,x^3)\\
&ds^2 = -(1-\frac{2M}{r})dt^2+(1-\frac{2M}{r})^{-1} dr^2+r^2\Omega^2(d\Omega^2=d\theta^2+\sin^2{\theta}d{\phi}^2)\\
&ds^2_{Minkowski}=-dt^2+dr^2+r^2d\Omega^2\\
&ds^2=-e^{2\alpha(r)}dt^2+e^{2\beta(r)}dr^2+e^{2\gamma(r)}r^2d\Omega^2\\\\
&\overline{r}=e^{\gamma(r)}r\\
&d\overline{r}=e^{\gamma}rdr+e^{\gamma}rd\gamma=(1+r\frac{d\gamma}{dr})e^{\gamma}dr\\
&ds^2=-e^{2\alpha(r)}dt^2+(1+r\frac{d\gamma}{dr})^{-2}\;e^{2\beta(\gamma)-2\gamma(r)}d\overline{r}^2+\overline{r}^2d\Omega^2\\
&ds^2=-e^{2\alpha(r)}dt^2+e^{2\beta(r)}dr^2+r^2d\Omega^2(\overline{r}\rightarrow r)\\\\
&<Static \& Spherically-Symmetric>\\
&g_{00}=-e^{2\alpha(r)},g_{11}=e^{2\beta(r)},g_{22}=r^2,g_{33}=r^2\sin^2{\theta}\\
&g^{00}=-\frac{1}{e^{2\alpha(r)}},g^{11}=\frac{1}{e^{2\beta(r)}},g^{22}=\frac{1}{r^2},g^{33}=\frac{1}{r^2\sin^2{\theta}}\\
&g_{\mu\nu},g^{\mu\nu}=0(\mu\neq\nu),\Gamma^{\alpha}_{\mu\nu}=\Gamma^{\alpha}_{\nu\mu}\\
&\Gamma^{\mu}_{\nu\sigma}=\frac{1}{2}g^{\mu\lambda}(g_{\lambda\nu,\sigma}+g_{\lambda\sigma,\nu}-g_{\nu\sigma,\lambda})(\Gamma^{\beta}_{\nu\sigma,\rho}=\frac{\partial}{\partial x^{\rho}}\Gamma^{\beta}_{\nu\sigma})&&
\end{flalign*}
$$


$$
\begin{flalign*}
&\Gamma^{0}_{00}=\frac{1}{2}g^{00}(g_{00,0}+g_{00,0}-g_{00,0})=0\\
&\Gamma^{0}_{0i}=\frac{1}{2}g^{00}(g_{0i,0}+g_{00,i}-g_{0i,0})=\frac{1}{2}g^{00}g_{00,i}=\frac{1}{2}g^{00}\partial _{r}(-e^{2\alpha(r)})=\partial_{r}\alpha\\
&\Gamma^{0}_{ij}=\frac{1}{2}g^{00}(g_{0i,j}+g_{0j,i}-g_{ij,0})=0
&&
\end{flalign*}
$$


$$
\begin{flalign*}
&\Gamma^{1}_{00}=\frac{1}{2}g^{11}(g_{10,0}+g_{10,0}-g_{00,1})=-\frac{1}{2}g^{11}\partial_r(-e^{2\alpha(r)})=\frac{(\partial_r\alpha) e^{2\alpha(r)}}{e^{2\beta(r)}}=e^{2(\alpha-\beta)}(\partial_r \alpha)\\
&\Gamma^{1}_{0i}=\frac{1}{2}g^{11}(g_{10,i}+g_{1i,0}-g_{0i,1})=0\\
&\Gamma^{1}_{ij}=\frac{1}{2}g^{11}(g_{1i,j}+g_{1j,i}-g_{ij,1})=0\\
&\Gamma^{1}_{11}=\frac{1}{2}g^{11}(g_{11,1}+g_{11,1}-g_{11,1})=\frac{1}{2}g^{11}\partial_r g_{11}=\frac{1}{2e^{2\beta}}2\partial_{r}\beta e^{2\beta}=\partial_r\beta\\
&\Gamma^{1}_{22}=\frac{1}{2}g^{11}(g_{12,2}+g_{12,2}-g_{22,1})=\frac{1}{2}g^{11}\partial_r(-g_{22})=\frac{1}{2e^{2\beta}}\partial_r(-r^2)=-\frac{r}{e^{2\beta}}=-re^{-2\beta}\\
&\Gamma^{1}_{33}=\frac{1}{2}g^{11}(g_{13,3}+g_{13,3}-g_{33,1})=\frac{1}{2}g^{11}\partial_r(-g_{33})=\frac{1}{2e^{2\beta}}\partial_r(-r^2\sin^{\theta})=-\frac{r\sin^2{\theta}}{e^{2\beta}}=-re^{-2\beta}\sin^2{\theta}
&&
\end{flalign*}
$$


$$
\begin{flalign*}
&\Gamma^{2}_{00}=\frac{1}{2}g^{22}(g_{20,0}+g_{20,0}-g_{00,2)}=0\\
&\Gamma^{2}_{0i}=\frac{1}{2}g^{22}(g_{20,i}+g_{2i,0}-g_{0i,2})=0\\
&\Gamma^{2}_{ij}=\frac{1}{2}g^{22}(g_{2i,i}+g_{2i,i}-g_{ii,2})=-\frac{1}{2}g^{22}\partial_{2}g_{33}=-\frac{1}{2r^2}\partial_{\theta}(r^{2}\sin^2{\theta})=-\sin{\theta}\cos{\theta}\\
&\Gamma^{2}_{12}=\frac{1}{2}g^{22}(g_{21,2}+g_{22,1}-g_{12,2}=\frac{1}{2}g^{22}\partial_{r}(g_{22})=\frac{1}{2r^2}\partial_{r}(r^2)=\frac{1}{r}\\
&\Gamma^{2}_{13}=\frac{1}{2}g^{22}(g_{21,3}+g_{23,1}-g_{13,2})=0\\
&\Gamma^{2}_{23}=\frac{1}{2}g^{22}(g_{22,3}+g_{23,2}-g_{23,2})=0
&&
\end{flalign*}
$$


$$
\begin{flalign*}
&\Gamma^{3}_{00}=\frac{1}{2}g^{33}(g_{30,0}+g_{30,0}-g_{00,3})\\
&\Gamma^{3}_{0i}=\frac{1}{2}g^{33}(g_{30,i}+g_{3i,0}-g_{0i,3})=0\\
&\Gamma^{3}_{ii}=\frac{1}{2}g^{33}(g_{3i,i}+g_{3i,i}-g_{ii,3})=0\\
&\Gamma^{3}_{ij}=\frac{1}{2}g^{33}(g_{3i,j}+g_{3j,i}-g_{ij,3})=\frac{1}{2}g^{33}(g_{3j,i}+g_{3i,j})\\
&\Gamma^{3}_{13}=\frac{1}{2}g^{33}(g_{31,3}+g_{33,1}-g_{13,3})=\frac{1}{2}g^{33}\partial_{r}(g_{33})=\frac{1}{2r^2\sin^2{\theta}}\partial_{r}(r^2\sin^2{\theta})=\frac{1}{r}\\
&\Gamma^{3}_{23}=\frac{1}{2}g^{33}(g_{32,3}+g_{33,2}-g_{23,3})=\frac{1}{2}g^{33}\partial_{\theta}(g_{33})=\frac{1}{2r^2\sin^2{\theta}}\partial_{\theta}(r^2\sin^2{\theta})=\frac{\cos{\theta}}{\sin{\theta}}
&&
\end{flalign*}
$$


$$
\begin{flalign*}
&\Gamma^{0}_{01}=\Gamma^{t}_{tr}=\partial_{r}\alpha,\;\; \Gamma^{2}_{33}=\Gamma^{\theta}_{\phi\phi}=-\sin{\theta}\cos{\theta}\\
&\Gamma^{1}_{00}=\Gamma^{r}_{tt}=e^{2(\alpha-\beta)}(\partial_{r}\alpha),\;\; \Gamma^{2}_{12}=\Gamma^{\theta}_{r\theta}=\frac{1}{r}\\
&\Gamma^{1}_{11}=\Gamma^{r}_{rr}=\partial_{r}\beta,\;\;\Gamma^{3}_{13}=\Gamma^{\phi}_{r\phi}=\frac{1}{r}\\
&\Gamma^{1}_{22}=\Gamma^{r}_{\theta\theta}=-re^{-2\beta},\;\;\Gamma^{3}_{23}=\Gamma^{\phi}_{\theta\phi}=\frac{\cos{\theta}}{\sin{\theta}}\\
&\Gamma^{1}_{33}=\Gamma^{r}_{\phi\phi}=-re^{-2\beta}\sin^2{\theta}\\
&&
\end{flalign*}
$$


- Ricci tensor

$$
\begin{flalign*}
&R_{\mu\nu}=r^{\beta}_{\mu\nu\beta}=\Gamma^{\beta}_{\mu\beta,\nu}-\Gamma^{\beta}_{\mu\nu,\beta}+\Gamma^{\alpha}_{\mu\beta}\Gamma^{\beta}_{\alpha\mu}-\Gamma^{\alpha}_{\mu\nu}\Gamma^{\beta}_{\alpha\beta}\;\;\;\;\;R_{\mu\nu}=0\;(\mu\neq\nu)\\
&R_{00}=e^{2(\alpha-\beta)}[\partial^{2}_{r}\alpha+(\partial_{r}\alpha)^2-(\partial_r\alpha)(\partial_{r}\beta)+\frac{2}{r}(\partial_r\alpha)]\\
&R_{11}=-\partial^{2}_{r}\alpha-(\partial_{r}\alpha)^{2}+(\partial_{r}^{\beta})(\partial_{r}\alpha)+\frac{2}{r}(\partial_{r}\beta)\\
&R_{22}=e^{-2\beta}[r(\partial\beta)-r(\partial_r\alpha)-1]+1\\
&R_{33}=\sin^2{\theta}[e^{-2\beta}(r(\partial_r\beta)-r(\partial_r\alpha)-1)+1]\\
&=\sin^2{\theta}R_{22}\\
&&
\end{flalign*}
$$


- Ricci Scalar

$$
\begin{flalign*}
&R=R^{\mu}_{\mu}=g^{00}R_{00}+g^{11}R_{11}+g^{22}R_{22}+g^{33}R_{33}\\
&=-2e^{-2\beta}(\partial_{r}^{2}\alpha+(\partial_r\alpha)^2-(\partial_r\alpha)(\partial_r\beta)+\frac{2}{r}(\partial_{r}\alpha)-\frac{2}{r}(\partial_{r}\beta)+\frac{1}{r^2}(1-e^{2\beta}))\\
&&
\end{flalign*}
$$

- Ricci tesor = 0

$$
\begin{flalign*}
&0=e^{2(\beta-\alpha)}R_{00}+R_{11}=\frac{2}{r}(\partial_r\alpha+\partial_r\beta)\rightarrow\alpha=-\beta+c(c:constant)\\
&time coordinate t\rightarrow e^{-c}t-\alpha=\beta\\
&R_{22}=0\\
&=e^{2\alpha}[2r(\partial_r\alpha)+1]-1\\
&e^{2\alpha}(2r(\partial_r\alpha)+1)=1\rightarrow \partial_{r}(re^{2\alpha})=1\\
&e^{2\alpha}=1-\frac{R_{s}}{r}\leftarrow \partial_r(re^{2\alpha}=1\leftrightarrow=re^{2\alpha}=C+r\\
&ds^2=-(1-\frac{2M}{r})dt^2+(1-\frac{2M}{r})^{-1}dr^2+r^2d\Omega^2 \sim Schwarzschild metric
&&
\end{flalign*}
$$


- Schwarzschild geodesic

$$
\begin{flalign*}
&ds^2=-(1-\frac{2M}{r}dt^2+(1-\frac{2M}{r})^{-1}dr^2+r^2d\theta^2+r\sin^2{\theta}d\phi^2\\\\
&<conserved quantity>\\
&(1-\frac{2M}{r})\frac{dt}{d\tau}=\widetilde{E},r^2\frac{d\phi}{d\tau}=\widetilde{L}\\
&\frac{d^2x^{\mu}}{d\lambda^2}+\Gamma^{\mu}_{\alpha\beta}\frac{dx^{\alpha}}{d\lambda}\frac{dx^\beta}{d\lambda}=0\\
&\frac{d^2t}{d\tau^2}=\frac{-2M}{r(r-2M)}(\frac{dr}{d\tau})(\frac{dt}{d\tau})\\
&\frac{d^2r}{d\tau^2}=(r-2M)[-\frac{M}{r^3}(\frac{dt}{d\tau})^2+\frac{M}{r(r-2M)^2}(\frac{dr}{d\tau})^2+(\frac{d\phi}{d\tau})^2]\\
&\frac{d^2\phi}{d\tau^2}=\frac{-2}{r}(\frac{dr}{d\tau})(\frac{d\phi}{d\tau})\\\\
&(\frac{dr}{d\tau})^2=\widetilde{E}^2-(1-\frac{2M}{r})(1+\frac{\widetilde{L}^2}{r^2})\\
&\frac{d^2r}{d\tau^2}=-\frac{M}{r^2}+\frac{\widetilde{L}^2}{r^3}-\frac{3M\widetilde{L}^2}{r^4}\\
&(\frac{dr}{d\phi})^2=\frac{(dr/d\tau)^2}{(d\phi/d\tau)^2}=\frac{\widetilde{E}^2-(1-\frac{2M}{r})(1+\frac{\widetilde{L}^2}{r^2})}{\widetilde{L}^2/r^4}\\
&u=1/r,du=-(1/r^2)dr\\
&(\frac{du}{d\phi})^2=\frac{\widetilde{E}^2-1}{\widetilde{L}^2}+\frac{2Mu}{\widetilde{L}^2}-u^2+2Mu^3\\
&\frac{du^2}{d\phi}=\frac{M}{\widetilde{L}^2}-u+3Mu^2\\
&\int^{\phi+\delta\phi}_{0}d\phi=\int^{u_1}_{u_{2}}\frac{\pm 1}{\sqrt{\frac{\widetilde{E}^2-1}{\widetilde{L}^2}+\frac{2Mu}{\widetilde{L}^2}-u^2+2Mu^3}}du \sim exact solution\\
&&
\end{flalign*}
$$


- Approximated analytic solution

$$
\begin{flalign*}
&(\frac{du}{d\phi})^2=\frac{\widetilde{E}^2-1}{\widetilde{L}^2}+\frac{2M}{\widetilde{L}^2}u-u^2+2Mu^3\\
&u=\frac{M}{\widetilde{L}^2}+w, du=dw\\
&(\frac{dw}{d\phi})^2=\frac{\widetilde{E}^2-1}{\widetilde{L}^2}+\frac{2M}{\widetilde{L}^2}(\frac{M}{\widetilde{L}^2}+w)-(\frac{M}{\widetilde{L}^2}+w)^2+2M(\frac{M}{\widetilde{L}^2}+w)^3\\
&=-k^2(w-\frac{3M^3}{k^2\widetilde{L}^4}+\frac{\widetilde{E}^2-1}{\widetilde{L}^2}+\frac{M^2}{\widetilde{L}^4}+\frac{2M^4}{\widetilde{L}^6}+(\frac{3M^3}{k\widetilde{L}^4})^2 \sim [k^2=(1-\frac{6M^2}{\widetilde{L}^2}),w_0=\frac{3M^3}{k^2\widetilde{L}^4}]\\
&w=w_0Acos{k(\phi+\phi_0)}\\
&\delta\phi=\frac{2\pi}{k}-2\pi=2\pi[(1-\frac{6M^2}{\widetilde{L}^2})^{-1/2}-1]\\
&\phi_{prec}=\pi(\frac{6M^2}{\widetilde{L}^2})\sim [42.98"/century]
&&
\end{flalign*}
$$

### Numerical Calculation Code Verification test

A "convergence test" is a technique used in various scientific and mathematical disciplines, including physics, to assess the accuracy and reliability of numerical methods or computational simulations. It is typically used to determine if a numerical solution is approaching a meaningful result, especially when an exact analytical solution is not readily available. The primary purpose of a convergence test is to ensure that the numerical approximation is sufficiently accurate.

$$
\begin{flalign*}
&u_{h}(x,t) = u_{sol}(x,t)+hE_{1}+h^2E_{2}+h^3E_{3}+h^4E_{4}+\vartheta (h^5)\\
&u_{h/2}(x,t) = u_{sol}(x,t)+(\frac{h}{2})E_{1}+(\frac{h}{2})^2E_{2}+(\frac{h}{2})^3E_{3}+(\frac{h}{2})^4E_{4}+\vartheta (h^5)\\
&u_{h/4}(x,t) = u_{sol}(x,t)+(\frac{h}{4})E_{1}+(\frac{h}{4})^2E_{2}+(\frac{h}{4})^3E_{3}+(\frac{h}{4})^4E_{4}+\vartheta (h^5)\\\\
&u_{h}(x,t)-u_{h/2}(x,t) = (\frac{1}{2}h)E_{1}+(\frac{3}{4}h^2)E_{2}+(\frac{7}{8}h^3)E_{3}+(\frac{15}{16}h^4)E_{4}+\vartheta (h^5)\\
&u_{h/2}(x,t)-u_{h/4}(x,t) = (\frac{1}{4}h)E_{1}+(\frac{3}{16}h^2)E_{2}+(\frac{7}{64}h^3)E_{3}+(\frac{15}{256}h^4)E_{4}+\vartheta (h^5)\\\\
&\frac{u_{h}(x,t)-u_{h/2}(x,t)}{u_{h/2}(x,t)-u_{h/4}(x,t)} \approx \frac{(\frac{15}{16}h^4)E_{4}+\vartheta (h^5)}{(\frac{15}{256}h^4)E_{4}+\vartheta (h^5)} \approx 2^4\\
\end{flalign*}
$$

$order = N)$

$$
\begin{flalign*}
&\frac{u_{h}(x,t)-u_{h/2}(x,t)}{u_{h/2}(x,t)-u_{h/4}(x,t)} \approx 2^N&&
\end{flalign*}
$$

![500](https://i.imgur.com/nofGkrc.png)
![500](https://i.imgur.com/gFBIFyb.png)

> Mercury convergence test

### Additional Steps To Solve Problems

Due to the nature of simulation, the execution results are discontinuous even if the grid size is very small, so interpolation or extrapolation is necessary to estimate continuous results. 

- Interpolation
Interpolation is the process of estimating values within the range of known data points. When you have data at specific points and want to estimate the values between those points, interpolation methods are used. This technique is commonly used in various fields, such as mathematics, physics, astrophysics and scientific field.

- Extrapolation
Extrapolation, on the other hand, is the process of estimating values outside the range of known data points. It involves extending a known data trend or pattern to predict values beyond the observed data. Extrapolation is used when you want to make predictions of phenomenon beyond the available data range.
The biggest feature of both methods is estimated through relationships without knowing the general formula.

- Lagrange Polynomial function
The Lagrange polynomial, is a method in numerical analysis for interpolating a set of data points with a polynomial. 
1. $x$ is the variable for which we want to interpolate a corresponding $y$-value.
2. $x_{i}$ and $y_{i}$ are the known data points.
3. The sum runs from $i$=0 to $n$, inclusive, covering all the data points.
4. The product term in the sum does not incorporate the term when j equals i, thus ensuring that the polynomial accurately passes through the associated point $(x_{i},y_{i})$.
The Lagrange polynomial offers a method for creating a polynomial that intersects a given set of points. The Lagrange interpolating polynomial, denoted as P(x), with degrees $\leq$(n-1), is designed to pass through the n points 

$$
(x_1, y_1 = f(x_1)), (x_2, y_2 = f(x_2)), ..., (x_n, y_n = f(x_n))
$$

. It is expressed as:

$$
\begin{flalign*}
&P(x)=\sum_{j=1}^{n}P_j(x)\\
&P_j(x)=y_{j}\prod_{k=1; k\neq j}^{n}\frac{x-x_k}{x_j-x_k}.\\
&P(x)	=	y_1+\frac{(x-x_1)(x-x_3)\cdots(x-x_n)}{(x_2-x_1)(x_2-x_3)\cdots(x_2-x_n)}y_2+\cdots+\frac{(x-x_1)(x-x_2)\cdots(x-x_{n-1})}{(x_n-x_1)(x_n-x_2)\cdots(x_n-x_{n-1})}y_n
\end{flalign*}
$$

The Lagrange polynomial provides an exact interpolation for the given data points, meaning that it passes exactly through the provided points.

- Cubic Spline function
A cubic spline function is a piecewise-defined polynomial function that is used for interpolation or smoothing. It is a commonly used method in numerical analysis and computer graphics to approximate a curve or set of data points with a smooth and continuous curve. $f(x)=a+bx+cx^{2}+dx^{3}$

1. The curve passes the original data value $x_{i}$ at each point.
2. Two curves must meet at each point. In other words, the function values of the two curves at each point $x_{i}$ must be the same.
3. Make the smoothness of the two curves the same at each point. In other words, the differential values of the two curves at each point $x_{i}$ are the same.
4. Let’s make the two curves meet ‘more’ smoothly. In other words, the second derivative values of the two curves at each point $x_{i}$ are equal.

![500](https://i.imgur.com/zpwR08a.png)

![500](https://i.imgur.com/XYrKWS7.png)

![500](https://i.imgur.com/8MtbHTL.png)

![500](https://i.imgur.com/LdwiAEN.png)
> interpolation, extrapolation

### Results and Analysis
![500](https://i.imgur.com/AWD3wPR.png)

![500](https://i.imgur.com/Ck7wiEd.png)

![500](https://i.imgur.com/ce8AJjy.png)

![500](https://i.imgur.com/rBK563c.png)

| Precession [arcsec/century] | Observed | Aanalytic approximated sol | Numerical geodesic sol [RK4] | Error [Analytic &amp; RK4] |
|:----------------------------|:---------|:---------------------------|:-----------------------------|:---------------------------|
| Mercury                     |  42.9799 |                    42.9900 |                      43.0025 |                   0.0291 % |
| Venus                       |   8.2647 |                     8.6265 |                       8.6983 |                   0.8323 % |
| Earth                       |   3.8387 |                     3.8395 |                       3.8222 |                   0.0173 % |
| Mars                        |   1.3624 |                     1.3549 |                       1.3549 |                   0.2738 % |  

| Period [day] | Observed | Analytic approximated sol | Numerical geodesic sol [RK4] | Error [Observed &amp; RK4] |
|:-------------|:---------|:--------------------------|:-----------------------------|:---------------------------|
| Mercury      |    87.97 |                   87.9594 |                      87.9594 |                   0.0120 % |
| Venus        |    224.7 |                  224.6771 |                     224.6771 |                   0.0102 % |
| Earth        |   365.26 |                  365.2167 |                     365.2167 |                   0.0119 % |
| Mars         |   686.94 |                  686.9143 |                     686.9143 |                   0.0037 % |  

As a result of the numerical simulation, the precession [''/century] had an error of less than 1 % compared to the analytic solution, and the period had an error of approximately 0.1 % compared to the observed value. This is the result of improved accuracy through a combination of numerical simulation and interpolation, and when comparing observed values and periods, it can be concluded that general relativity has a significant impact on the solar system.
