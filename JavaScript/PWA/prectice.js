var request = window.indexedDB.open("my-database", 4);

request.onsuccess = function(event) {
  var db = event.target.result;
  var exchangeTransaction = db.transaction("exchange_rates");
  var exchangeStore = exchangeTransaction.objectStore("exchange_rates");
  var exchangeIndex = exchangeStore.index("from_idx");
  var exchangeCursor = exchangeIndex.openCursor("CAD");
  exchangeCursor.onsuccess = function(event) {
    var cursor = event.target.result;
    if (!cursor) {
      return;
    }
    var rate = cursor.value;
    console.log(rate.exchange_from + " to " + rate.exchange_to + ": "+ rate.rate);
    cursor.continue();
  };
};