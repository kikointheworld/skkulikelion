const APIKEY = "cc190b9e175f52039ee68ff7a96165e9";
const IMAGE_URL = "https://image.tmdb.org/t/p/w500";
const nowplayingURL = `https://api.themoviedb.org/3/movie/now_playing?api_key=${APIKEY}&language=en-US`;
const popularURL = `https://api.themoviedb.org/3/movie/popular?api_key=${APIKEY}&language=en-US`;
const topratedURL = `https://api.themoviedb.org/3/movie/top_rated?api_key=${APIKEY}&language=en-US`;
const upcomingURL = `https://api.themoviedb.org/3/movie/upcoming?api_key=${APIKEY}&language=en-US`;

const options = {
  method: "GET",
  headers: {
    "Content-Type": "application/json; charset=utf-8",
  },
};

// 나우플레잉 부분
const now_playing = document.querySelector("#now_playing");
fetch(nowplayingURL, options)
  .then((response) => response.json())
  .then((response) => {
    response.results.forEach((element) => {
      console.log(element.title, element.backdrop_path, element.vote_average);
      let movie = document.createElement("li");
      let movieDiv = document.createElement("div");
      let backdrop = document.createElement("img");
      backdrop.setAttribute("src", IMAGE_URL + element.backdrop_path);
      let title = document.createElement("h4");
      let rate = document.createElement("span");
      title.innerHTML = element.title;
      rate.innerHTML = "★" + element.vote_average;
      movieDiv.appendChild(backdrop);
      movieDiv.appendChild(title);
      movieDiv.appendChild(rate);
      movie.appendChild(movieDiv);
      now_playing.appendChild(movie);
    });
  });

// 파퓰러 부분
const popular = document.querySelector("#popular");
fetch(popularURL, options)
  .then((response) => response.json())
  .then((response) => {
    response.results.forEach((element) => {
      console.log(element.title, element.backdrop_path, element.vote_average);
      let movie = document.createElement("li");
      let movieDiv = document.createElement("div");
      let backdrop = document.createElement("img");
      backdrop.setAttribute("src", IMAGE_URL + element.backdrop_path);
      let title = document.createElement("h4");
      let rate = document.createElement("span");
      title.innerHTML = element.title;
      rate.innerHTML = "★" + element.vote_average;
      movieDiv.appendChild(backdrop);
      movieDiv.appendChild(title);
      movieDiv.appendChild(rate);
      movie.appendChild(movieDiv);
      popular.appendChild(movie);
    });
  });

// 톱 레이티드 부분
const toprated = document.querySelector("#top_rated");
fetch(topratedURL, options)
  .then((response) => response.json())
  .then((response) => {
    response.results.forEach((element) => {
      console.log(element.title, element.backdrop_path, element.vote_average);
      let movie = document.createElement("li");
      let movieDiv = document.createElement("div");
      let backdrop = document.createElement("img");
      backdrop.setAttribute("src", IMAGE_URL + element.backdrop_path);
      let title = document.createElement("h4");
      let rate = document.createElement("span");
      title.innerHTML = element.title;
      rate.innerHTML = "★" + element.vote_average;
      movieDiv.appendChild(backdrop);
      movieDiv.appendChild(title);
      movieDiv.appendChild(rate);
      movie.appendChild(movieDiv);
      toprated.appendChild(movie);
    });
  });

// 톱 레이티드 부분
const upcoming = document.querySelector("#upcoming");
fetch(upcomingURL, options)
  .then((response) => response.json())
  .then((response) => {
    response.results.forEach((element) => {
      console.log(element.title, element.backdrop_path, element.vote_average);
      let movie = document.createElement("li");
      let movieDiv = document.createElement("div");
      let backdrop = document.createElement("img");
      backdrop.setAttribute("src", IMAGE_URL + element.backdrop_path);
      let title = document.createElement("h4");
      let rate = document.createElement("span");
      title.innerHTML = element.title;
      rate.innerHTML = "★" + element.vote_average;
      movieDiv.appendChild(backdrop);
      movieDiv.appendChild(title);
      movieDiv.appendChild(rate);
      movie.appendChild(movieDiv);
      upcoming.appendChild(movie);
    });
  });
