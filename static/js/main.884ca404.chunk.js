(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{156:function(e,t,a){e.exports=a(180)},161:function(e,t,a){},162:function(e,t,a){},163:function(e,t,a){},167:function(e,t,a){},168:function(e,t,a){},173:function(e,t,a){},175:function(e,t,a){},180:function(e,t,a){"use strict";a.r(t);var n=a(0),r=a.n(n),c=a(48),l=a.n(c),o=(a(161),a(11)),i=(a(162),a(163),a(249)),s=a(250),u=function(e){return r.a.createElement("div",{className:"header",style:{width:"100%"}},r.a.createElement("img",{className:"photo",src:"https://www.inside.unsw.edu.au/sites/default/files/inline-images/crest.jpg",alt:"1 Group 2 Group 3 Group 4"}),"1 Group 2 Group 3 Group 4",r.a.createElement(i.a,{container:!0,justifyContent:"flex-end",sx:{mx:2,width:"10%"}},r.a.createElement(s.a,{onClick:function(){e.openBadges(!0)}},"BADGES")))},m=(a(167),a(256)),d=a(247),f=a(254),h=a(255),p=a(123),E=a.n(p),b=a(253),y=a(128);function g(e,t,a,n,c){return r.a.createElement(d.a,{button:!0,component:"a",href:e,target:"_blank",rel:"noopener noreferrer",onClick:function(){c(n+1)}},r.a.createElement(f.a,null,r.a.createElement(E.a,null)),r.a.createElement(h.a,{primary:a,secondary:t}))}var v=function(e){for(var t=[],a=e.articles.length-1;a>=0;a--){var n=e.articles[a],c=n.article.url,l=Object(y.a)(new Date(n.article.date_of_publication),"yyyy-MM-dd"),o=n.article.headline;t.push(g(c,l,o,e.numArticleClicks,e.setNumArticleClicks)),t.push(r.a.createElement(b.a,null))}return r.a.createElement(m.a,{sx:{width:"20%",maxWidth:360,height:"100%",maxHeight:1,overflow:"auto",bgcolor:"background.paper"}},t)},j=(a(168),a(76));function w(e,t){var a="undefined"!==typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(!a){if(Array.isArray(e)||(a=function(e,t){if(!e)return;if("string"===typeof e)return x(e,t);var a=Object.prototype.toString.call(e).slice(8,-1);"Object"===a&&e.constructor&&(a=e.constructor.name);if("Map"===a||"Set"===a)return Array.from(e);if("Arguments"===a||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(a))return x(e,t)}(e))||t&&e&&"number"===typeof e.length){a&&(e=a);var n=0,r=function(){};return{s:r,n:function(){return n>=e.length?{done:!0}:{done:!1,value:e[n++]}},e:function(e){throw e},f:r}}throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}var c,l=!0,o=!1;return{s:function(){a=a.call(e)},n:function(){var e=a.next();return l=e.done,e},e:function(e){o=!0,c=e},f:function(){try{l||null==a.return||a.return()}finally{if(o)throw c}}}}function x(e,t){(null==t||t>e.length)&&(t=e.length);for(var a=0,n=new Array(t);a<t;a++)n[a]=e[a];return n}function O(e){var t,a=[],n=w(e);try{for(n.s();!(t=n.n()).done;){var r,c=w(t.value.locations);try{for(c.s();!(r=c.n()).done;){var l=r.value,o=l.lat,i=l.lng;a.push({coordinates:[parseFloat(i),parseFloat(o)]})}}catch(s){c.e(s)}finally{c.f()}}}catch(s){n.e(s)}finally{n.f()}return a}var S=function(e){for(var t=[],a=e.articles.length-1;a>=0;a--){var n=e.articles[a];t=t.concat(O(n.article.reports))}return r.a.createElement(j.ComposableMap,{"data-tip":"",style:{width:"80%"},projection:"geoMercator",projectionConfig:{scale:100}},r.a.createElement(j.Geographies,{geography:"https://raw.githubusercontent.com/zcreativelabs/react-simple-maps/master/topojson-maps/world-110m.json"},function(t){return t.geographies.map(function(t){return r.a.createElement(j.Geography,{key:t.rsmKey,geography:t,onMouseEnter:function(){var a,n=t.properties,r=n.NAME,c=n.POP_EST;e.setHovering("".concat(r," \u2014 ").concat((a=c)>1e9?Math.round(a/1e8)/10+"Bn":a>1e6?Math.round(a/1e5)/10+"M":Math.round(a/100)/10+"K"))},onMouseLeave:function(){e.setHovering("")},onClick:function(){var a=t.properties.NAME;e.setCountry("".concat(a))},style:{default:{fill:"#D6D6DA",outline:"none"},hover:{fill:"#F53",outline:"none"},pressed:{fill:"#E42",outline:"none"}}})})}),t.map(function(e){var t=e.coordinates;return r.a.createElement(j.Marker,{coordinates:t,style:{pointerEvents:"none"}},r.a.createElement("circle",{r:10,fill:"#F00",stroke:"#fff",strokeWidth:2}))}))},C=(a(173),a(245)),k=a(243),A=a(257),M=a(127),N=a(251),_=a(235),B=function(e){var t=Object(n.useState)(null),a=Object(o.a)(t,2),c=a[0],l=a[1],u=Object(n.useState)(null),m=Object(o.a)(u,2),d=m[0],f=m[1],h=Object(n.useState)(null),p=Object(o.a)(h,2),E=p[0],b=p[1],g=Object(n.useState)(!1),v=Object(o.a)(g,2),j=v[0],w=v[1],x=Object(M.a)({palette:{mode:"dark"}});return r.a.createElement(N.a,{theme:x},r.a.createElement("div",{className:"searchBar",style:{paddingTop:"1%",paddingBottom:"1%"}},r.a.createElement(C.a,{sx:{mx:4,width:"30%"},id:"countrySearch",label:"Country",variant:"standard",value:e.country,placeholder:"Country",onChange:function(t){var a=t.target.value;e.setCountry(a)},InputLabelProps:{shrink:!0}}),r.a.createElement(k.a,{clearable:!0,label:"Start Date",value:c,format:"dd-MM-yyyy",onChange:function(e){l(e)},renderInput:function(e){return r.a.createElement(C.a,Object.assign({sx:{width:"30%"}},e))}}),r.a.createElement(A.a,{sx:{mx:2}},"to"),r.a.createElement(k.a,{label:"End Date",value:d,onChange:function(e){f(e)},renderInput:function(e){return r.a.createElement(C.a,Object.assign({sx:{width:"30%"}},e))}}),r.a.createElement(C.a,{sx:{mx:4,width:"50%"},id:"keyTerms",label:"Key Terms (Separated by comma)",variant:"standard",value:E,onChange:function(e){var t=e.target.value;b(t)}}),r.a.createElement(i.a,{container:!0,justifyContent:"flex-end",sx:{mx:2,width:"10%"}},r.a.createElement(s.a,{disabled:j,onClick:function(){var t=function(e,t,a,n,r,c,l){if(null==n||"string"!=typeof n||""===n)return alert("Country cannot be empty."),null;null==e&&(e=new Date),null==t&&(t=Object(_.a)(new Date,20)),null!=a&&"string"==typeof n&&""!==a||(a="outbreak"),e=Object(y.a)(e,"yyyy-MM-dd"),t=Object(y.a)(t,"yyyy-MM-dd");var o="https://seng3011-bobby-tables-backend.herokuapp.com/article?end_date=".concat(e,"T00%3A00%3A00&start_date=").concat(t,"T00%3A00%3A00&key_terms=").concat(a,"&location=").concat(n,"&limit=1000&offset=0");return console.log(o),r(!0),new Promise(function(e,t){fetch(o).then(function(a){400===a.status||403===a.status?a.json().then(function(e){alert(e.error),t(e.error)}):200===a.status?a.json().then(function(t){e(t)}):t("Error: "+a.status+" response received!"),r(!1),c(l+1)}).catch(function(t){r(!1),c(l+1),console.log(t),e(null)})})}(d,c,E,e.country,w,e.setNumSearches,e.numSearches);null!=t&&t.then(function(t){null!=t&&e.setArticles(t.articles),w(!1)})}},j?"Searching":"Search"))))},T=a(54),D=(a(175),function(e){var t=Object(n.useRef)();return Object(n.useEffect)(function(){var a=function(a){a.target===t.current&&e.setShow(!1)};return window.addEventListener("click",a),function(){window.removeEventListener("click",a)}},[e]),r.a.createElement("div",{ref:t,className:"modal ".concat(e.show?"active":"")},r.a.createElement("div",{className:"modal__content"},!e.hideCloseButton&&r.a.createElement("span",{onClick:function(){return e.setShow(!1)},className:"modal__close"},"\xd7"),e.children))}),G=function(e){return r.a.createElement("div",{className:"modal__header"},e.children)},I=function(e){return r.a.createElement("div",{className:"modal__body"},e.children)},F=a(55),R=a.n(F),L={bgcolor:"background.paper",borderColor:"text.primary",m:1,border:1,width:"5rem",height:"5rem",padding:"10px"};var P=function(e){return r.a.createElement(D,{show:e.badgesOpen,setShow:e.setBadgesOpen},r.a.createElement(G,null,r.a.createElement("h2",null,"Badges")),r.a.createElement(I,null,r.a.createElement(i.a,{container:!0,spacing:2,sx:{padding:2}},function(e,t){var a=[];return e>0&&a.push(r.a.createElement(i.a,{item:!0,xs:2,sx:{padding:"10px"}},r.a.createElement(A.a,{sx:Object(T.a)({},L,{borderRadius:4})},r.a.createElement(R.a,null),r.a.createElement(b.a,null),"Searched once"))),e>=5&&a.push(r.a.createElement(i.a,{item:!0,xs:2},r.a.createElement(A.a,{sx:Object(T.a)({},L,{borderRadius:4})},r.a.createElement(R.a,null),r.a.createElement(b.a,null),"Searched 5 Times"))),e>=10&&a.push(r.a.createElement(i.a,{item:!0,xs:2},r.a.createElement(A.a,{sx:Object(T.a)({},L,{borderRadius:4})},r.a.createElement(R.a,null),r.a.createElement(b.a,null),"Searched 10 Times"))),t>0&&a.push(r.a.createElement(i.a,{item:!0,xs:2,sx:{padding:"10px"}},r.a.createElement(A.a,{sx:Object(T.a)({},L,{borderRadius:4})},r.a.createElement(R.a,null),r.a.createElement(b.a,null),"Visited one article"))),t>=5&&a.push(r.a.createElement(i.a,{item:!0,xs:2},r.a.createElement(A.a,{sx:Object(T.a)({},L,{borderRadius:4})},r.a.createElement(R.a,null),r.a.createElement(b.a,null),"Visited 5 articles"))),t>=10&&a.push(r.a.createElement(i.a,{item:!0,xs:2},r.a.createElement(A.a,{sx:Object(T.a)({},L,{borderRadius:4})},r.a.createElement(R.a,null),r.a.createElement(b.a,null),"Visited 10 articles"))),a.length<=0&&a.push(r.a.createElement(i.a,{item:!0,xs:12},"You have no badges yet.")),a}(e.numSearches,e.numArticleClicks))))},H=a(244),K=a(241),V=a(125),J=a(242);var W=function(){var e=Object(n.useState)([]),t=Object(o.a)(e,2),a=t[0],c=t[1],l=Object(n.useState)(""),i=Object(o.a)(l,2),s=i[0],m=i[1],d=Object(n.useState)(null),f=Object(o.a)(d,2),h=f[0],p=f[1],E=Object(n.useState)(!1),y=Object(o.a)(E,2),g=y[0],j=y[1],w=Object(n.useState)(0),x=Object(o.a)(w,2),O=x[0],C=x[1],k=Object(n.useState)(0),A=Object(o.a)(k,2),M=A[0],N=A[1];return r.a.createElement("div",{className:"App",style:{height:"100%",width:"100%"}},r.a.createElement(K.b,{dateAdapter:H.a},r.a.createElement("header",{style:{width:"100%"}},r.a.createElement(u,{openBadges:j})),r.a.createElement("main",{style:{height:"100%"}},r.a.createElement(P,{badgesOpen:g,setBadgesOpen:j,numSearches:O,numArticleClicks:M}),r.a.createElement(B,{setArticles:c,setCountry:p,country:h,numSearches:O,setNumSearches:C}),r.a.createElement(J.a,{direction:"row",justifyContent:"end",alignItems:"flex-start",sx:{height:"80%",flexGrow:"1",flexShrink:"1",flexBasis:"auto"}},r.a.createElement(v,{articles:a,numArticleClicks:M,setNumArticleClicks:N}),r.a.createElement(b.a,{orientation:"vertical"}),r.a.createElement(S,{articles:a,setHovering:m,setCountry:p})),r.a.createElement(V.a,null,s))))},z=function(e){e&&e instanceof Function&&a.e(3).then(a.bind(null,261)).then(function(t){var a=t.getCLS,n=t.getFID,r=t.getFCP,c=t.getLCP,l=t.getTTFB;a(e),n(e),r(e),c(e),l(e)})};l.a.render(r.a.createElement(r.a.StrictMode,null,r.a.createElement(W,null)),document.getElementById("root")),z()}},[[156,1,2]]]);
//# sourceMappingURL=main.884ca404.chunk.js.map