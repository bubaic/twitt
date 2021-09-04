function getCookie(name) {
	let cookieValue = null;
	if (document.cookie && document.cookie !== "") {
		const cookies = document.cookie.split(";");
		for (let i = 0; i < cookies.length; i++) {
			const cookie = cookies[i].trim();
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === name + "=") {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

function newResponse(res, headerFn, bodyFn) {
	function cloneHeaders() {
		var headers = new Headers();
		for (var kv of res.headers.entries()) {
			headers.append(kv[0], kv[1]);
		}
		return headers;
	}

	function cloneBody() {}

	var headers = headerFn ? headerFn(cloneHeaders()) : res.headers,
		body = bodyFn ? bodyFn(cloneBody()) : "";

	return new Promise(function(resolve) {
		return res.blob().then(function(blob) {
			resolve(
				new Response(blob, {
					status: res.status,
					statusText: res.statusText,
					headers: headers,
					body: body,
				})
			);
		});
	});
}

function bodyFn(res) {
	return newResponse(res, (body) => {
		return body;
	});
}

function resFn(res) {
	const csrftoken = getCookie("csrftoken");

	return newResponse(res, function(headers) {
		headers.set("HTTP_SET_REQUESTED_HEADER", "XMLHttpRequest");
		headers.set("X-Requested-With", "XMLHttpRequest");
		headers.set("X-CSRFToken", csrftoken);
		return headers;
	});
}

async function lookup(method, url, body) {
	console.log("payloads-->\n\nmethod:", method, "\nurl:", url, "\nbody:", body);
	// 	const csrftoken = getCookie("csrftoken");
	let bodyData = body;
	if (bodyData) {
		bodyData = JSON.stringify(bodyData);
	}

	const response = await fetch(`http://localhost:8000/api/${url}`, {
		headers: {
			"Content-Type": "application/json",
		},
		method: method,
		body: bodyData,
	});

	const data = await response.json();

	if (!response.ok) {
		const errObj = JSON.stringify({
			code: response.status || "",
			message: response.statusText || "Unable to fetch",
		});
		throw new Error(errObj);
	}

	return data;
}

export { getCookie, lookup };