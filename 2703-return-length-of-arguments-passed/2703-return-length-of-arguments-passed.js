/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    let result=[...args]
    return result.length
    
};

/**
 * argumentsLength(1, 2, 3); // 3
 */