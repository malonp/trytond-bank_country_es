##############################################################################
#
#    GNU Condo: The Free Management Condominium System
#    Copyright (C) 2016- M. Alonso <port02.server@gmail.com>
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from trytond.modules.bank_country import banknumber, configuration


def check_code(number):
    '''
    Check Spanish Bank code.
    '''

    def get_control(digitos):
        resultado = 11 - sum(int(d) * 2**i for i, d in enumerate(digitos)) % 11
        return resultado if resultado < 10 else 11 - resultado

    # python lib stdnum check if the bban part of number has the correct structure

    value = '00' + number[0:8]
    d1 = get_control(value)
    if d1 != int(number[8]):
        return False

    value = number[10:20]
    d2 = get_control(value)
    if d2 != int(number[9]):
        return False

    return True


banknumber.check_code_es = check_code
configuration.BANK_COUNTRIES.append('ES')
