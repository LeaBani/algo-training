function countSheeps(arrayOfSheep) {
    // TODO May the force be with you
    
    const countTrue = arrayOfSheep.filter(elem => elem == true).length;
    console.log(countTrue)
  }

countSheeps([true,  true,  true,  false,
    true,  true,  true,  true ,
    true,  false, true,  false,
    true,  false, false, true ,
    true,  true,  true,  true ,
    false, false, true,  true ])