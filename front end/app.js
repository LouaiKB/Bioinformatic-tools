const containers = document.querySelectorAll('.container');

containers.forEach(element => {
	
	element.addEventListener('mouseenter', (evt) => {
		evt.target.style.cssText = 'width: 260px; height: 160px; display: flex; align-items: center; justify-content: center;';
	});
	
	element.addEventListener('mouseleave', (evt) => {
		evt.target.style.cssText = 'width: 250px; height: 150px';
	});

});

// const myCustomDiv = document.createElement('div');

// function respondToTheClick(evt) {
// 	if(evt.target.nodeName === 'P') {
// 		console.log('A paragraph was clicked: ' + evt.target.textContent);
// 	}
// }
// for (let i = 1; i <= 200; i++) {
//     const newElement = document.createElement('p');
//     newElement.innerHTML = '<p>This is paragraph number</p><span>' + i + '</span>';

//     myCustomDiv.appendChild(newElement);
// }

// document.body.appendChild(myCustomDiv);


// myCustomDiv.addEventListener('click', respondToTheClick);


// document.querySelector('#content').addEventListener('click', function (evt) {
//     if (evt.target.nodeName === 'SPAN') {  // ← verifies target is desired element
//         console.log('A span was clicked with text ' + evt.target.textContent);
//     }
// });
// 