function(doc) {
    for (i in doc.language) {
        emit(doc.language[i], doc._id);
    }
}
