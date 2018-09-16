(function() {
  const searchBtn = document.getElementById("search-btn");
  const searchText = document.getElementById("search-text");
  const closeBtn = document.getElementById("close-btn");
  const form = document.getElementById("form");
  const textUnderLine = document.getElementById("text-under-line");

  closeBtn.innerHTML = '<i class="fa fa-search" aria-hidden="true"></i>';

  function getPropertyValue(elem, property) {
  //ブラウザが示す要素の厳密なサイズを取得
  const computedStyle =
  elem.currentStyle || document.defaultView.getComputedStyle(elem, ""); //currentStyleはIE,getComputedStyleはそれ以外
  const propertyValue = computedStyle.getPropertyValue(property);
  return propertyValue;
  }

  closeBtn.addEventListener(
  "click",
  e => {
  e.preventDefault();
  form.classList.toggle("is-open");
  if (form.classList.contains("is-open")) {
  closeBtn.innerHTML = '<i class="fa fa-times" aria-hidden="true"></i>';
  searchText.style.width = "auto";//#search-textのブラウザが示す小数点を含む幅を取得するためにwidthをautoにする
  //searchText.style.width = searchText.offsetWidth + 'px';
  const searchTextWidth = getPropertyValue(searchText, "width");//#search-textのブラウザが示す小数点を含む幅を取得する
  const searchBtnWidth = getPropertyValue(searchBtn, "width");//#search-btnのブラウザが示す小数点を含む幅を取得する
  //console.log(parseFloat(searchTextWidth) + parseFloat(searchBtnWidth));
  form.style.width =
  parseFloat(searchTextWidth) + parseFloat(searchBtnWidth) + "px";//#search-textの幅+#search-btnの幅を#formの幅にしてtransitionが効くようにする。width:auto;では効かないためこのようなことをしている。
  textUnderLine.style.width = searchTextWidth;//#text-under-lineの幅を#search-textの幅にする
  //leftとrightで左右ぴったりに配置
  textUnderLine.style.left = searchText.getBoundingClientRect().left - searchBtn.getBoundingClientRect().left + "px"; //#search-btnの座標から数えた#search-textの相対座標※追記:rightのみでも良かった
  textUnderLine.style.right = 0 + "px";
  form.style.right = 0; //#formの右端を×アイコンの右端に揃える
  searchText.focus();//自動でフォーカスする
  } else {
  closeBtn.innerHTML = '<i class="fa fa-search" aria-hidden="true"></i>';
  searchText.style.width = ""; //position:absolute;で配置しているため、閉じる直前に指定しないとぴったりと収まっていないため、吸収場所がボタン領域内ではなく画面外となってしまう。
  textUnderLine.style.width = "";
  textUnderLine.style.left = "";//追記:書かなくても動作した
  textUnderLine.style.right = "";//追記:書かなくても動作した
  form.style.width = "";
  form.style.right = "";
  searchText.blur();//フォーカスを解除する
  }
  },
  false
  );
})();
