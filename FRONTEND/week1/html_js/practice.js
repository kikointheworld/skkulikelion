// document.getElementById("lion").style.color = "red";
// document.getElementById("tiger").style.color = "red";
// document.getElementById("bear").style.color = "blue";

// 해당 태그 이름을 가진 노드 전부 가져옴
const animal = document.getElementsByTagName("li");

animal[0].style.color = "red";

// document.querySelector("CSS선택자"); => 첫번째 애새끼만 반환
// document.querySelectorAll("CSS선택자"); =>

// DOM 조작, innerHTML, classList classList.add("클래스 명") / classList.remove("클래스 명") // classList.toggle("클래스 명")
// 토글은 클래스명 존재하면 클래스 추가 없으면 삭제
// animals.innerHTML = "<li class='animal'>Cat</li>" => r고양이 추가
