const updateBruce = update.bind(bruce);

updateBruce(1904, "actor");
// bruce는 이제 { name: "Bruce", birthYear: 1904, occupation: "actor"}
updateBruce(madeline, 1274, "king"); 
// bruce는 이제 { name: "Bruce", birthYear: 1274, occupation: "king"}
// madeline은 변하지 않는다.