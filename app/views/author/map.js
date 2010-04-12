function(doc) {
    for (i in doc.author) {
        emit(doc.author[i], doc._id);
    }
}
