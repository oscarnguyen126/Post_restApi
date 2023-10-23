function post(url, data, onSuccess, onFail) {
  $.ajax({
    type: "POST",
    url,
    contentType: "application/json",
    data: JSON.stringify(data),
    success: onSuccess,
    onFail,
  });
}

function get(url, onSuccess, onFail) {
  $.ajax({
    type: "GET",
    url,
    contentType: "application/json",
    success: onSuccess,
    onFail,
  });
}
