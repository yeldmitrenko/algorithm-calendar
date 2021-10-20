from models.insurance_type_list import InsuranceType
from models.property_list import Property
from models.benefits_list import Benefits
from models.types_insure import CorporateInsurance, LifeInsurance, PropertyInsurance
from models.corporate_list import CorporateInsurancesType
from manager.insurance_mang import InsuranceManager
from models.sort_order import SortOrder
from models.insurance import Insurance


def main():
    manager1 = InsuranceManager()
    VUSO_housing = PropertyInsurance(Property.HOUSE, 500000, 180000, InsuranceType.PROPERTY, 24, 10000, 15,
                                     ['fire', 'robbery', 'tornado', 'burglary', 'flood'])
    VUSO_people_help = LifeInsurance('Jack Jonson', 'John Snow', [Benefits.JURIDICAL_HELP], InsuranceType.LIFE, 12,
                                     1500.5, 31,
                                     ['deaths', 'trauma', 'fines'])
    VUSO_company = CorporateInsurance('IT', 250, CorporateInsurancesType.CYBER_CASES, InsuranceType.CORPORATE, 72,
                                      15000, 23, ['court', 'robbery', 'industrial accident'])
    VS_insure = Insurance(InsuranceType.LIFE, 23, 14500, 23, ['deaths'])

    manager1.add_insurances(VS_insure)
    manager1.add_insurances(VUSO_company)
    manager1.add_insurances(VUSO_housing)
    print(manager1.search_by_type(InsuranceType.LIFE))
    print(manager1.sort_by_price(SortOrder.DESC))
    print(manager1.sort_by_risk(SortOrder.ASC))


if __name__ == '__main__':
    main()
