(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{16:function(e,t,n){e.exports=n(28)},21:function(e,t,n){},22:function(e,t,n){},25:function(e,t,n){},26:function(e,t,n){},28:function(e,t,n){"use strict";n.r(t);var a=n(0),r=n.n(a),c=n(3),o=n.n(c),l=(n(21),n(4)),i=n(5),s=n(7),u=n(6),d=n(8),m=(n(22),n(27),n(25),function(){return r.a.createElement("div",{className:"header"},r.a.createElement("img",{className:"photo",src:"https://www.inside.unsw.edu.au/sites/default/files/inline-images/crest.jpg",alt:"1 Group 2 Group 3 Group 4"}),"1 Group 2 Group 3 Group 4")}),h=n(1),f=(n(26),n(37)),b=n(38),y=function(e){var t=e.url,n=e.date,a=e.headline,c=e.main_text;e.reports;return r.a.createElement("div",{className:"article"},r.a.createElement("h1",null,a),r.a.createElement("h2",null,"Date of publication: ",n),r.a.createElement("h2",null,"Url: ",t),r.a.createElement("br",null),r.a.createElement("p",null,"Main text: ",c),r.a.createElement("br",null))},g=function(e){function t(e){var n;return Object(l.a)(this,t),(n=Object(s.a)(this,Object(u.a)(t).call(this,e))).state={articles:[]},n}return Object(d.a)(t,e),Object(i.a)(t,[{key:"doRender",value:function(){console.log(this.state.articles)}},{key:"render",value:function(){return this.state.articles.length>0?this.state.articles[0]:null}}]),t}(r.a.Component);new g;function p(e,t){var n="undefined"!==typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(!n){if(Array.isArray(e)||(n=function(e,t){if(!e)return;if("string"===typeof e)return v(e,t);var n=Object.prototype.toString.call(e).slice(8,-1);"Object"===n&&e.constructor&&(n=e.constructor.name);if("Map"===n||"Set"===n)return Array.from(e);if("Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))return v(e,t)}(e))||t&&e&&"number"===typeof e.length){n&&(e=n);var a=0,r=function(){};return{s:r,n:function(){return a>=e.length?{done:!0}:{done:!1,value:e[a++]}},e:function(e){throw e},f:r}}throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}var c,o=!0,l=!1;return{s:function(){n=n.call(e)},n:function(){var e=n.next();return o=e.done,e},e:function(e){l=!0,c=e},f:function(){try{o||null==n.return||n.return()}finally{if(l)throw c}}}}function v(e,t){(null==t||t>e.length)&&(t=e.length);for(var n=0,a=new Array(t);n<t;n++)a[n]=e[n];return a}var E=function(e){function t(e){var n;return Object(l.a)(this,t),(n=Object(s.a)(this,Object(u.a)(t).call(this,e))).setArticles=e.setArticles,n.changeDates=n.changeDates.bind(Object(h.a)(Object(h.a)(n))),n.changeLocation=n.changeLocation.bind(Object(h.a)(Object(h.a)(n))),n.changeKeyTerms=n.changeKeyTerms.bind(Object(h.a)(Object(h.a)(n))),n.submitForms=n.submitForms.bind(Object(h.a)(Object(h.a)(n))),n.resetScore=n.resetScore.bind(Object(h.a)(Object(h.a)(n))),n.state={startDate:null,endDate:null,location:"",key_terms:""},n}return Object(d.a)(t,e),Object(i.a)(t,[{key:"changeDates",value:function(e){this.setState({startDate:e.startDate}),this.setState({endDate:e.endDate})}},{key:"changeLocation",value:function(e){this.setState({location:e.target.value})}},{key:"changeKeyTerms",value:function(e){this.setState({key_terms:e.target.value})}},{key:"resetScore",value:function(){localStorage.setItem("userPoints",0),window.location.reload(!1)}},{key:"submitForms",value:function(){var e=this,t=this.state.location,n=this.state.key_terms;try{var a=Object(b.a)(this.state.endDate,"yyyy-MM-dd"),r=Object(b.a)(this.state.startDate,"yyyy-MM-dd")}catch(s){return void alert("Date can not be empty")}var c=[],o=[];if(""===t)alert("Location can not be empty");else if(""===n)alert("Key Terms can not be empty");else{var l=localStorage.getItem("userPoints");null===l&&(l=0),localStorage.setItem("userPoints",parseInt(l)+1),console.log("started loading"),document.getElementById("NoResults").hidden=!0,document.getElementById("LoadingIndicator").hidden=!1;var i=t.charAt(0).toUpperCase()+t.slice(1);c.push(A(a,r,n.toLowerCase(),i).then(function(e){o.push(e)})),Promise.all(c).then(function(t){var n,a=[],r=p(o[0].articles);try{for(r.s();!(n=r.n()).done;){var c=n.value;a.push(new y(c.article))}}catch(l){r.e(l)}finally{r.f()}console.log("finished loading"),document.getElementById("LoadingIndicator").hidden=!0,e.props.setArticles(a)})}}},{key:"render",value:function(){return r.a.createElement("div",{className:"searchBar"},r.a.createElement("div",{class:"container"},r.a.createElement("div",{class:"column"},r.a.createElement(f.a,{change:this.changeDates,dateformat:"yyyy-MM-dd",id:"datetimepicker",placeholder:"Enter date range: "})),r.a.createElement("div",{class:"column"},r.a.createElement("form",null,r.a.createElement("label",null,r.a.createElement("input",{onChange:this.changeLocation,placeholder:"Location",type:"text",id:"location",style:{width:"370px"}})))),r.a.createElement("div",{class:"column"},r.a.createElement("form",null,r.a.createElement("label",null,r.a.createElement("input",{onChange:this.changeKeyTerms,placeholder:"Key terms seperated by commas",type:"text",id:"keyterms",style:{width:"370px"}})))),r.a.createElement("button",{onClick:this.submitForms},"Submit"),r.a.createElement("button",{onClick:this.resetScore},"Reset Your Score")))}}]),t}(r.a.Component),j=function(e){return r.a.createElement("h1",{hidden:"true",id:"LoadingIndicator"},"Loading...")},O=function(e){return r.a.createElement("h1",{hidden:"true",id:"NoResults"},"0 results matched your search criteria")},w=function(e){function t(e){var n;return Object(l.a)(this,t),(n=Object(s.a)(this,Object(u.a)(t).call(this,e))).state={articles:[]},n}return Object(d.a)(t,e),Object(i.a)(t,[{key:"setArticles",value:function(e){this.setState({articles:e}),console.log(e.length),0==e.length&&(document.getElementById("NoResults").hidden=!1)}},{key:"render",value:function(){return r.a.createElement("div",{className:"App"},r.a.createElement(m,null),r.a.createElement(E,{setArticles:this.setArticles.bind(this)}),r.a.createElement("header",{className:"App-header"},"Your current score is: ",localStorage.getItem("userPoints"),r.a.createElement(j,null),r.a.createElement(O,null),this.state.articles))}}]),t}(r.a.Component);var k=function(){return r.a.createElement(w,null)},S=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,39)).then(function(t){var n=t.getCLS,a=t.getFID,r=t.getFCP,c=t.getLCP,o=t.getTTFB;n(e),a(e),r(e),c(e),o(e)})};o.a.render(r.a.createElement(r.a.StrictMode,null,r.a.createElement(k,null)),document.getElementById("root")),S();var A=t.default=function(e,t,n,a){return new Promise(function(r,c){fetch("https://seng3011-bobby-tables-backend.herokuapp.com/article?end_date=".concat(e,"T00%3A00%3A00&start_date=").concat(t,"T00%3A00%3A00&key_terms=").concat(n,"&location=").concat(a,"&limit=1000&offset=0")).then(function(e){400===e.status||403===e.status?e.json().then(function(e){alert(e.error),c(e.error)}):200===e.status&&e.json().then(function(e){r(e)})}).catch(function(e){return console.log(e)})})}}},[[16,1,2]]]);
//# sourceMappingURL=main.ace3af12.chunk.js.map