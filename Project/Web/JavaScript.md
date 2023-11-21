# Vanilla JS
<https://nomadcoders.co/javascript-for-beginners/lobby>

-Vanilla JS : 다른 라이브러리를 사용하지 않고 순수 JavaScript 뜻함
## WELCOME TO JAVASCRIPT
- css, js는 html을 browser에 열어서 그 안에서 실행된다.
- js 보통 끝에서 open하도록 설정
ex) < script src=" .js" >< /script >
- console Mac) chrome: cmd+option+j , safari: cmd+option+i
- JavaScript : ex) myName (camel case) MyName (pascal case)
- Python : ex) my_name (snake case)
- // : 주석처리, ; : 끝에 항상 붙임

### Data Type
- Integer(ex: 1, 2), Float(ex: 0.5, 5.5), String(ex: "ring" +로 합성), Boolean(true, false, null, undefined), variable, function, etc..
- undefined : 변수 선언은 했지만 값을 할당하지 않음
- null : 값이 없음

### 선언
- const[always] : 재선언 금지, 재할당 금지, 불변량 (default)
- let[sometimes] : 재선언 금지, 재할당 가능, 업데이트 가능, 업데이트 시 variable 명으로 바로 선언
- var[never] : 재선언 가능, 재할당 가능, 원하면 어디서든 업데이트, 대신 실수로 변수 변경 시 방지 불가 (규칙x)
- const, let은 개발자의 의도 파악 가능함

### array : [ , , , ] 하나의 변수 안에 데이터의 list를 가지는 것
```
const daysOfWeek = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"];
```
ex) 5th element value? index: 0부터 시작, console.log(daysOfWeek[4]) -> "fri"
ex) daysOfWeek.push() : array에 값 추가
ex) daysOfWeek[0] = "월요일" : array 값 변경

### object : property를 가진 데이터를 저장, {} 사용
```
const player = {
	name : tomato,
	color : red,
	food : true
};
```
- const는 let과 다르게 update는 안되지만 list의 경우 property 수정/변경시 update 가능
- console.log(player) property 부르는 방법
ex) console.log(player.name) -> tomato
ex) console.log(player["name"]) -> tomato
ex) player.color = "blue", console.log(player.color) -> blue : property 변경
ex) player.koreanName = "토마토" -> property 추가

### function : 반복해서 사용할 수 있는 code 조각이다, code를 캡슐화하여 실행 여러번 가능
```
function title(arguments){
	code
}
title(arguments);
```
- arguments : 인수 해당 function 내에서 어떤 정보를 줄 수 있는 값
ex) console.log() : object안에 선언된 함수
- return O : function 호출 값 = return 값, X : undefined
- return 하는 순간 function 종료

### conditional : 조건문
```
conditional

if (){
	true일때 ~;
}else{
	false일때 ~;
}
else if (){
	true일때 ~;  //if가 false일 때 다른 조건문
}
```
- && : and, || : or
- == : 값만을 같은지 비교 (동등연산자), === : 값 + 유형 같은지 비교 (일치연산자) (추천), !== : 같지 않음 확인
ex) 0 == false -> true, 0 === false -> false
```
const calculator = {  
	plus : function(a,b) {  
	console.log(a + "+" + b + "=" + a+b);  
	},  
	minus : function(a,b) {  
	console.log(a + "-" + b + "=" + a-b);  
	},  
	multiple : function(a,b) {  
	console.log(a + "*" + b + "=" + a*b);  
	},  
	divide : function(a,b) {  
	console.log(a + "/" + b + "=" + a/b);  
	},  
	squareRoot : function(a) {  
	console.log( a + "^" + 2 + "=" + a*a);  
	}  
}
```
- prompt() : function, 2 arguments (message, default)
-cancel = null, ok = value 사용자에게 창을 띄운다
- parseInt : convert string to number
- typeof : type 확인
- NaN : Not a Number
```
const age=parseInt(prompt("How old are you"));
```

- isNaN : NaN인지 확인, return boolean
```
const age=parseInt(prompt("How old are you?"));
console.log(isNaN(age));

Number : false
text : true
```
condition은 boolean으로 판별 가능해야 한다.

## JAVASCRIPT ON THE BROWSER
### The Document Object
- console에 document(:browser에 존재하는 object) 입력하면 작성한 html 호출
- console.dir(document) 호출 -> document.title = html title
- JavaScript에서 html document 객체로 부터 title 가져올 수 있음
- JavaScript는 html에 접근하고 읽을수 있음, 수정 또한 가능
- document = web site
- document.body 호출 -> body 항목만 호출

### html에서 항목을 가져와서 js에서 변경
- document.getElementById("title") -> html에 있는 id 호출
- js 에서는 html에서 표현하는 object 보여줌
- title.innerText = "got you" -> js에서 바꾸기 가능
- console.dir("title") -> js에서 html이 표현하는 object 보여줌

### 값 호출
- getElementsByClassName() : 많은 elemet 가져올 때 사용 (array 반환)
- getElementsByTagName() : name을 할당할 수 있음 (array 반환)
- querySelector : element를 css selector방식으로 검색 -> 한 개의 element return
-class 내부에 있는 h1 가지고 올 수 있음 (id 또한 가능)
-조건 맞는 element 모두 반환 querySelectorAll (array 형태)
- querySelector("#hello");와 getElementById("hello"); 같음 -> 전자 주로 사용

### Event
- event : 어떤 행동을 하는 것 -> js가 모두 listen 할 수 있음
- eventListener : event를 listen함 -> js에게 무슨 event listen할지 알려줘야함
- .addEventListner("click") : 누군가 title을 click하는 것을 listen

```
const title = document.querySelector("div.hello:first-child h1");

function handleTitleClick(){
	title.style.color = "blue";
}
title.addEventListener("click", handleTitleClick);
```
-click하면 handleTitleClick function이 동작 -> 그래서 handleTitleClick()를 안넣음 (js가 대신 실행)
-function에서 ()이 괄호안을 추가함으로써 실행 동작가능

<https://developer.mozilla.org/ko/docs/Web/HTML/Element/Heading_Elements>
- MozillaDeveloperNetwork (MDN)에 검색 listen하고 싶은 event를 찾는 좋은 방법 (JavaScript element)
<https://developer.mozilla.org/en-US/docs/Web/API/HTMLHeadingElement>
- JavaScript관점의 html Heading Element 의미 (HTMLHeadingElement)
- html element property 검색 가능
> [!NOTE]
> EventTarget $\leftarrow$ Node $\leftarrow$ Element $\leftarrow$ HTMLElement $\leftarrow$ HTMLHeadingElement
- console.dir로 element로 출력하여 on으로 시작하는 것이 사용 가능한 event

```
const title = document.querySelector("div.hello:first-child h1");

  

console.dir(title)

  

function handleTitleClick() {

	title.style.color = "blue";

}

  

function handleMouseEnter() {

	title.innerText = "Mouse is here!";

}

  

function handleMouseLeave() {

	title.innerText = "Mouse is gone!";

}

  

title.addEventListener("click", handleTitleClick);

title.addEventListener("mouseenter", handleMouseEnter);

title.addEventListener("mouseleave", handleMouseLeave);
```

```
function handleWindowResize() {

	document.body.style.backgroundColor = "tomato";

}

function handleWindowCopy() {

	alert("copier!");

}

function handleWindowOffline() {

	alert("SOS no WIFI");

}

function handleWindowOnline() {

	alert("ALL GOOD");

}

window.addEventListener("resize", handleWindowResize); // 크기 조정

window.addEventListener("copy", handleWindowCopy); // 복사 붙여넣기

window.addEventListener("offline", handleWindowOffline); // wifi 연결 off

window.addEventListener("online", handleWindowOnline); // wifi 연결 on
```
### CSS
```
function handleTitleClick() {

	const currentColor = h1.style.color;

	let newColor;

	if(currentColor === "blue") {

		newColor = "tomato";

	} else {

		newColor = "blue";

	}

h1.style.color = newColor;

}

h1.addEventListener("click", handleTitleClick);

1) click event 발생 및 함수 실행  
2) currentColor 변수 선언 후 h1.style.color 값 복사 (getter)  
3) newColor 변수 선언  
4) currentColor 현재 값 확인  
5) 조건에 따라 newColor에 "tomato" or "blue" 값 대입  
6) 마지막으로 h1.style.color에 newColor값 대입 (setter)
```
- current color : getter 최근 color값 복사 const로 선언
- newColor : setter 변수에 대입된 색상을 h1.style.color에 최종적으로 할당 let으로 선언
- css 파일에 style 작업하는 것이 좋음, js는 animation
- class이름을 그냥 string으로 적으면 에러 발생 위험 변수를 생성하여 할당이 좋음
- toggle function : class name이 존재하는지 확인 -> 존재) class name 제거, 존재x) class name 추가 const도 필요없이 string으로 해도 무방
## LOGIN

```
const logininForm = document.querySelector("#login-form");

const loginButton = document.querySelector("#login-form input");

function onLoginSubmit(event) {

	event.preventDefault(); // 브라우저가 기본 동작을 실행하지 못하게 막음

	console.log(event);

}

logininForm.addEventListener("submit", onLoginSubmit);
//submit 이벤트가 발생한다면 onLoginSubmit 함수를 실행시킨다흔 의미이다
//JS는 onLoginSubmit함수 호출시 인자 담아서 호출 event object를 담은 정보들
```
- form을 submit시 브라우저는 기본적으로 페이지를 새로고침 하도록 되어있음
- preventDefault함수는 eventListner 함수의 첫번째 argument는 지금 막 벌어진 event 정보 갖고 있음

```
// js file

const loginForm = document.querySelector("#login-form");

const loginInput = document.querySelector("#login-form input");

const greeting = document.querySelector("#greeting");


const HIDDEN_CLASSNAME = "hidden";

const USERNAME_KEY = "username";


function onLoginSubmit(event) {

	event.preventDefault();

	loginForm.classList.add(HIDDEN_CLASSNAME);

	const username = loginInput.value;

	localStorage.setItem(USERNAME_KEY,username);

	paintGreetings(username);

}

function paintGreetings(username){

	greeting.innerText = `Hello ${username}`;

	greeting.classList.remove(HIDDEN_CLASSNAME);

}

const savedUsername = localStorage.getItem(USERNAME_KEY);

if(savedUsername === null){

	loginForm.classList.remove(HIDDEN_CLASSNAME);

	loginForm.addEventListener("submit",onLoginSubmit);

} else {

	paintGreetings(savedUsername);

}
```

```
// html file

<!DOCTYPE html>

<html lang="en">

	<head>

		<meta charset="UTF-8">

		<meta http-equiv="X-UA-Compatible" content="IE=edge" />

		<meta name="viewport" content="width=device-width, initial-scale=1.0">

		<link rel="stylesheet" href="style.css">

		<title>Momentum App</title>

	</head>

	<body>

		<form class="hidden" id="login-form">

			<input

				required

				maxlength="15"

				type="text"

				placeholder="What is your name?"

			/>

			<input type="submit" value="Log in" />

		</form>

		<h1 id="greeting" class="hidden"></h1>

		<script src="app.js"></script>

	</body>

</html>
```
- step 1 : 화면 새로고침 방지
-loginForm.classList.add(HIDDEN_CLASSNAME);
- step 2 : form 다시 숨김
-const username = loginInput.value
- step 3 : value를 username이라는 key로 저장
-localStorage.setItem(USERNAME_KEY,username)
- step 4 : username값을 key와 함께 local storage에 저장
-paintGreetings(username)
- step 5 : 비어있는 h1 요소안에 `Hello username` 텍스트 추가
-const savedUsername = localStorage.getItem(USERNAME_KEY)
- step 6 : app 시작되면 local storage에서 savedusername얻는데 username key를 통해 찾음
- step 7 : 처음에는 key랑 value가 null이므로
-if (savedUsername === null) {  
	loginForm.classList.remove(HIDDEN_CLASSNAME);  
	// form에 hidden을 지워주고  
	loginForm.addEventListener("submit", onLoginSubmit);  
	// form이 submit될때만 onLoginSubmit함수를 실행 시키도록 한다  
	} else {  
		paintGreetings(savedUsername);  
		// 유저정보가 localstoreage에서 나오고 있다  
		// paintGreeting은 only localstoarage에서만 값을 불러온다  
}
## CLOCK

```
const clock = document.querySelector("h2#clock");

function getClock() {

	const date = new Date();

	const hours = String(date.getHours()).padStart(2,"0");

	const minutes = String(date.getMinutes()).padStart(2,"0");

	const seconds = String(date.getSeconds()).padStart(2,"0");

	clock.innerText = `${hours}:${minutes}:${seconds}`;

}

getClock();

setInterval(getClock, 1000);
```
- setInterval(sayHello, 5000); 는 매초, 매분마다 반복되는 일을 해야할때 실행하는 함수. 
-첫번째 인수에는 함수이름을 적도 두번째인수는 시간을 적어야함. 1초는 1000임 (ms 단위)
- setTimeout(sayHello,1000);는 함수를 바로 실행하고 싶지않을때 사용하는 함수,
-예시와같은 setTimeout은 1초 뒤에 sayHello를 실행시킨다는 의미임.
- getHours().padStart(2,"0") 는 getHours로 시간을 받아오고 1시일 경우 01이 아닌 1로 나타난다. 그래서 01로 나오게 하기위해 사용하는 함수임. 
- padStart(2,"0") 2는 두글자가 되지않으면 0을 앞에 추가한다 라는 의미임. 뒤에 추가하고싶으면 padEnd를 사용하면됨.
## QUOTES AND BACKGROUND

```
const quotes = [

	{

	quote: 'I never dreamed about success, I worked for it',

	author: 'Estee Lauder'

	},

	{

	quote: 'Do not try to be original, just try to be good.',

	author: 'Paul Rand'

	},

	{

	quote: 'Do not be afraid to give up the good to go for the great',

	author: 'John D. Rockefeller'

	},

	{

	quote: 'If you cannot fly then run. If you cannot run, then walk. And if you cannot walk, then crawl, but whatever you do, you have to keep moving forward.',

	author: 'Martin Luther King Jr.'

	},

	{

	quote: 'Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.',

	author: 'Thomas Edison'

	},

	{

	quote: 'The fastest way to change yourself is to hang out with people who are already the way you want to be',

	author: 'REid Hoffman'

	},

	{

	quote: 'Money is like gasoline during a road trip. You do not want to run out of gas on your trip, but you are not doing a tour of gas stations',

	author: 'Tim O Reilly'

	},

	{

	quote: 'Some people dream of success, while other people get up every morning and make it happen',

	author: 'Wayne Huizenga'

	},

	{

	quote: 'The only thing worse than starting something and falling.. is not starting something',

	author: 'SEth Godin'

	},

	{

	quote: 'If you really want to do something, you will find a way. If you do not, you will find an excuse.',

	author: 'Jim Rohn'

	},

	];

const quote = document.querySelector("#quote span:first-child");

const author = document.querySelector("#quote span:last-child");

const todaysQuote = quotes[Math.floor(Math.random() * quotes.length)];

quote.innerText = todaysQuote.quote;

author.innerText = todaysQuote.author;
```

```
const images =["0.jpeg","1.jpeg","2.jpeg"];

const chosenImage = images[Math.floor(Math.random() * images.length)];

const bgImage = document.createElement("img");

bgImage.src = `img/${chosenImage}`;

document.body.appendChild(bgImage);
```
## TO DO LIST



## WEATHER

