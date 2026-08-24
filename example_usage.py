from client import OmnichannelEcommerceGrowthMAndAIntegratorClient

def main():
    client = OmnichannelEcommerceGrowthMAndAIntegratorClient()
    res = client.model_brand_growth_mna('Smart Kitchen Appliances D2C', 8200000.0, 21.0)
    print('M&A Model: ' + res['mna_model_id'] + ' for ' + res['target_brand'])
    print('Post-Acquisition EBITDA: $' + str(res['post_acquisition_run_rate_ebitda_usd']) + ' (Synergies: +$' + str(res['shared_3pl_logistics_synergy_usd']) + ')')
    print('Retail Expansion Score: ' + str(res['walmart_target_retail_expansion_score']) + '/100 | Multiple Lift: +' + str(res['valuation_multiple_expansion_pct']) + '%')

if __name__ == '__main__':
    main()
