function filter_list(l) {

    // je cherche a créer un nouveau tableau avec seulement les entiers

    const filter = l.filter(item => typeof(item) === 'number');
    return filter;

  }

filter_list([1,2,'a','b'])