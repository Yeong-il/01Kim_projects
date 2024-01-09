# ReactJS
## The Basics Of ReactJS

```
<!DOCTYPE html>

<html>

	<body>

		<div id="root"></div>

	</body>

	<script src="https://unpkg.com/react@17.0.2/umd/react.production.min.js"></script> //리액트 import

	<script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script> //리액트-DOM import

	<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script> //babel import 변환 시 사용

	<script type="text/babel"> //babel 적용

		const root = document.getElementById("root");

		const Title = () => (

			<h3

				id="title" onMouseEnter={() => console.log("mouse enter")}>

				Hello I'm title

			</h3>

		);

		const Button = () => (

		<button

			style={{

				backgroundColor: "tomato",

			}}

				onClick={() => console.log("I'm clicked")}>	

				Click Me

			</button>

		);

		/*

		const h3 = React.createElement("h3",{

			id: "title",

			onMouseEnter: () => console.log("mouse enter"),

		}, "Hello I'm title");

		*/

		/*

		const btn = React.createElement("button", {

			onClick: () => console.log("I'm clicked"),

			style: {

				backgroundColor: "tomato",

			},

		}, "Click me");

		*/

		const Container = () => (

			<div>

				<Title />

				<Button />

			</div>

		);

		//const container = React.createElement("div", null, [Title, Button]);

		ReactDOM.render(<Container />, root);

	</script>

</html>
```
- react import -> createElement function react object 접근 가능
- ReactJS - interactive하게 하는 library, element생성
- React-dom - library or package. react element들 html body에 배치하도록 해줌
- ReactDOM.render() - react element들을 html로 만들어 배치
- ReactJS는 업데이트 해야하는 html 업데이트 가능

- JSX - JavaScript 확장
- html과 비슷 property를 html tag 속성처럼 작성
- JSX는 브라우저가 이해할 수 있도록 babel로 이해하도록 바꿔주는 작업 필요
- arrow function () => () : function return과 같음 [component]첫글자 대문자!

- React.use.State() : react기능 쓸수 있게 해줌
- counter : 현재의 값 state
- setCounter : 이벤트 발생시 변화를 주는 부분 counter로 다시 저장
- ReactJS는 매번 자동으로 리랜더링 (실제로 바뀌는 값만)
- state 세팅 - (1) setState(state + 1), (2) setState(state => state + 1)

- props: function으로 부터 전달받는 속성값
- props: 객체 => 구조분해 할당 사용하면 매우 유용
- props에 function도 보낼수 있음
- 불필요한 re-render는 React.memo()로 관리 가능 (parent의 state변경하면 child의 component도 re-render발생)
- React.memo(): component rendering하고 결과를 Memoizing 다음 rendering에서 props같으면 Momoizing내용 재사용
- PropTypes 모듈: React parameter 잘못 넘길 시 확인할 수 없는 문제점 줄이기 위해 사용

## REACT_JS BEGINNERS - create react app
- node js 사용자 버전 설치 -> terminal에서 node-v로 설치됬는 지 확인
- terminal npx create-react-app 입력
- npm i prop-types : prop설치

```
import Button from "./Button";

import styles from "./App.module.css";

import { useState, useEffect } from "react";

function App() {

	const [counter, setValue] = useState(0);

	const [keyword, setKeyword] = useState("");

	const onClick = () => setValue((prev) => prev + 1);

	const onChange = (event) => setKeyword(event.target.value);

	useEffect(() => {

		console.log("i run only once.");

	}, []);

	useEffect(() => {

		console.log("I run when 'keyword' changes.");

	}, [keyword]);

	useEffect(() => {

		console.log("I run when 'counter' changes.");

	}, [counter]);

	useEffect(() => {

		console.log("I run when keyword & counter change");

	}, [keyword, counter]);

	return (

	<div>

	<input

		value={keyword}

		onChange={onChange}

		type="text"

		placeholder="Search here..."

	/>

	<h1>{counter}</h1>

	<button onClick={onClick}>click me</button>

	</div>

);

}

export default App;
```
- react사용 : 최소 단위의 랜더링을 위해 사용함
- useState() : 변수와 변수를 제어하는 함수로 변하는값을 구성, 제어,리랜더링
- props : tag property를 함수의 argument처럼 component에 값을 전달
- useEffect() : 코드 실행시점을 관리, dependency 없으면 1회 실행, 있을 경우 해당 값이 변할 때 실행
- parent component에서 rerendering 발생 시 모든 child가 rerendering
- propType 설치하고 props 타입 지정가능 isRequired로 지정가능

- effect에서 함수 반환 : effect를 위한 clean-up 매커니즘
- effect는 rendering이 실행되는 때마다 실행됨
