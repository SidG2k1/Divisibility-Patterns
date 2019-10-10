#include "builtin.hpp"
#include "functions.hpp"

/**
Contains functions used in extended essay code
*/

namespace __functions__ {

str *const_0;


str *__name__;



__ss_int sigma(__ss_int num) {
    /**
    returns the number or factors for a positive integer n
    */
    __ss_int __0, __1, divisor, nfactors;

    nfactors = 0;

    FAST_FOR(divisor,1,(num+1),1,0,1)
        if ((__mods(num, divisor)==0)) {
            nfactors = (nfactors+1);
        }
    END_FOR

    return nfactors;
}

void *filewrite(str *filename, str *inp) {
    /**
    Writes 'filename' with 'inp'
    */
    file *fil;

    fil = open(filename, const_0);
    fil->write(inp);
    fil->close();
    return NULL;
}

void __init() {
    const_0 = new str("w+");

    __name__ = new str("functions");

}

} // module namespace

