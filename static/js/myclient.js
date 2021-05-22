var saveIt = () => {
	let code = document.getElementById('codeid').value;
	fetch('/save', {
		method: 'POST',
		headers: { 'Content-Type': 'application/text' },
		body: code
	})
		.then((response) => response.json())
		.then((res) => console.log(res))
		.catch((err) => console.log(err));
};
