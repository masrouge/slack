from slacker import Slacker
slack = Slacker('xoxp-2329760138-30261499940-196507534403-7f9d79796327788391cf4771f71ba514')

response = slack.usergroups.users.update(usergroup='S5S05J2NM',users='U50FR5U8K,	U13MJE4TV,	U3P99UFSL,	U3PA5CB27,	U0J57JGBD,	U14EQ9S1K,	U1QJW5TQF,	U3M3BJG3H,	U0WUJ443Z,	U2JHHJ8BT,	U5ANYT154,	U15R5M5TP,	U0YMJUG4A,	U4QP012B1,	U0PSESVTJ,	U13N5P010,	U146KARPU,	U0KL0DHBR,	U1BVB4W1X,	U2B8ZD8TH,	U2D6K5UD9,	U2L5QAQQL,	U4E5NK152,	U4Q9KASSZ,	U0W7NK17F,	U0N5TJA77,	U2FTVRKE2,	U4T165RQR,	U11N10D0S,	U4TJU5FNH,	U3KQ8EUSV,	U0LQS0XRU,	U10LAKGN5,	U145UCZ1A,	U3CSSF9UZ,	U3RSZ6Q9E,	U0F9MNQ73,	U0X0J067R,	U0HLS53N1,	U0LHN0Z2S,	U3KP21RCY,	U41DG0U05,	U11Q1EXNG,	U1AUZRPSL,	U1BUNKVG9,	U4C2UPGLD,	U146HUKJ5,	U143ZDCJ2,	U0HLBGPN3,	U0RGAS8JV,	U3AL4CS1K,	U146DSTQU,	U0EMERLE9,	U146XPBG8,	U1D83QK26,	U1XB8Q5GF,	U3T1BH55K,	U3L0PP933,	U35R0EHB4,	U57E189M2,	U0FCYE8BV,	U0TG08LET,	U1465E9GW,	U1EQUNW58,	U0Q3AMYV8,	U10P5E02U,	U176VP92T,	U4321Q4P2,	U570GSUSW,	U144H2J1M,	U0Y77D9DK,	U0WS57XDE,	U1UMQN53J,	U14BLSF0T,	U10N08X3L,	U0L6NFMK8,	U0WTUR0MU,	U0KUNJHK7,	U0YDHSW3C,	U1AE73AJH,	U0FKMDUMD,	U0LQYSMC3,	U2AK4QYP6,	U2T63T2F5,	U141G1WCR,	U0Q2XTYQ5,	U2JH9Q23E,	U2TNEJ2JZ,	U3353FL31,	U0F689L4A,	U0X6ERLHJ,	U0V9SCJMQ,	U0Y7MCVE2,	U11V1TLR5,	U146DMRED,	U1QN7B2MV,	U261W96N4,	U0Q16LRSL,	U0UREU62C,	U0KLECD1S,	U1F3Q86E4,	U37LZD70R,	U4B03KTC5,	U10KVQ6QL,	U146FV8F4,	U1NJ43P3J,	U1643KBPW,	U13P8AF98,	U1GD7D4BH,	U0Y05QNE7,	U11PH8S1J,	U11M2F0TH,	U0MCJ5XFA,	U2JM26L9F,	U36HJ3F0F,	U56A859Q8,	U0FD48DV5,	U176Y5J5N,	U13NVMADN,	U14763W1E,	U11UX0UQH,	U3Y8P8010,	U0FT77EP5,	U1XD8799S,	U1CU5NTV2,	U0FTUG3RB,	U0W69QF9Q,	U2E4PEHAB,	U3PF6LQSH,	U5083LWHG,	U57R53JHL,	U15DJ7Q02,	U0Q0T9CF3,	U14E22VGF,	U1R4H3DBQ,	U5DK8JG76,	U28879VML,	U0Q3N3Y14,	U2B8LQBM2,	U3NGE4LE4,	U0TG3AG2U,	U0KDK3A84,	U1XG4MR2T,	U1WT54M5Z,	U23LCNUTV,	U1459FLKH,	U0FBB2R4Z,	U0Q16BNRE,	U10KZHNPQ,	U10KWCNKV,	U1T5Z0TU5,	U13MMA5E2,	U3G9VJLAF,	U0Q2EBKKM,	U1LKLA66L,	U3A2E1UD7,	U10BVTZ52,	U146GQEFK,	U14RW53PS,	U41ESQYKW,	U186L6283,	U1GLW328Z,	U0PSEUCPJ,	U0Y5YUZEC,	U15L3KYBZ,	U3FN0SFCP,	U0QAEEF8U,	U2T6R5KDJ,	U0R72EGRF,	U15EYHEG3,	U1NLP8TED,	U2Z6YNUF6,	U338FAVLY,	U0YQ44QBE,	U0JEADY3D,	U0CEJMDJ4,	U12H2N2RX,	U1ECPV2E5,	U2CGT4R98,	U14702XST,	U3AQ51KUP,	U4CHVHV27,	U15BLJK0W,	U38BUPFJ6,	U3Q1G3G8Y,	U0YN2EPSS,	U0NK3JCHK,	U0QQF8LTX,	U39UW4XUY,	U54B8J13Q,	U1EECELEA,	U1QNE1E8M,	U30RDFKRQ,	U4DF5MXQR,	U145KCX62,	U0KEN3KB4,	U0Y1U5SCE,	U0Y1R6KEE,	U0TDFRT8X,	U15KA2Q84,	U2T4VTJ03,	U4E642PE0,	U0W7PEPTN,	U0JS76EBS,	U15A9EQBS,	U0Z3HPN1L,	U4WU6021Y,	U0FCV4BN1,	U0KEBSQ06,	U15LAKUNR,	U3EFX3YSF,	U13N5P6MQ,	U22EHEKEZ,	U2B1FGNVB,	U10BFDML6,	U0JC311S6,	U0WT8BAHK,	U2TTK7S64,	U0FB5HFBP,	U0NDHS8JF')

#Long list
#U50FR5U8K,	U13MJE4TV,	U3P99UFSL,	U3PA5CB27,	U0J57JGBD,	U14EQ9S1K,	U1QJW5TQF,	U3M3BJG3H,	U0WUJ443Z,	U2JHHJ8BT,	U5ANYT154,	U15R5M5TP,	U0YMJUG4A,	U4QP012B1,	U0PSESVTJ,	U13N5P010,	U146KARPU,	U0KL0DHBR,	U1BVB4W1X,	U2B8ZD8TH,	U2D6K5UD9,	U2L5QAQQL,	U4E5NK152,	U4Q9KASSZ,	U0W7NK17F,	U0N5TJA77,	U2FTVRKE2,	U4T165RQR,	U11N10D0S,	U4TJU5FNH,	U3KQ8EUSV,	U0LQS0XRU,	U10LAKGN5,	U145UCZ1A,	U3CSSF9UZ,	U3RSZ6Q9E,	U0F9MNQ73,	U0X0J067R,	U0HLS53N1,	U0LHN0Z2S,	U3KP21RCY,	U41DG0U05,	U11Q1EXNG,	U1AUZRPSL,	U1BUNKVG9,	U4C2UPGLD,	U146HUKJ5,	U143ZDCJ2,	U0HLBGPN3,	U0RGAS8JV,	U3AL4CS1K,	U146DSTQU,	U0EMERLE9,	U146XPBG8,	U1D83QK26,	U1XB8Q5GF,	U3T1BH55K,	U3L0PP933,	U35R0EHB4,	U57E189M2,	U0FCYE8BV,	U0TG08LET,	U1465E9GW,	U1EQUNW58,	U0Q3AMYV8,	U10P5E02U,	U176VP92T,	U4321Q4P2,	U570GSUSW,	U144H2J1M,	U0Y77D9DK,	U0WS57XDE,	U1UMQN53J,	U14BLSF0T,	U10N08X3L,	U0L6NFMK8,	U0WTUR0MU,	U0KUNJHK7,	U0YDHSW3C,	U1AE73AJH,	U0FKMDUMD,	U0LQYSMC3,	U2AK4QYP6,	U2T63T2F5,	U141G1WCR,	U0Q2XTYQ5,	U2JH9Q23E,	U2TNEJ2JZ,	U3353FL31,	U0F689L4A,	U0X6ERLHJ,	U0V9SCJMQ,	U0Y7MCVE2,	U11V1TLR5,	U146DMRED,	U1QN7B2MV,	U261W96N4,	U0Q16LRSL,	U0UREU62C,	U0KLECD1S,	U1F3Q86E4,	U37LZD70R,	U4B03KTC5,	U10KVQ6QL,	U146FV8F4,	U1NJ43P3J,	U1643KBPW,	U13P8AF98,	U1GD7D4BH,	U0Y05QNE7,	U11PH8S1J,	U11M2F0TH,	U0MCJ5XFA,	U2JM26L9F,	U36HJ3F0F,	U56A859Q8,	U0FD48DV5,	U176Y5J5N,	U13NVMADN,	U14763W1E,	U11UX0UQH,	U3Y8P8010,	U0FT77EP5,	U1XD8799S,	U1CU5NTV2,	U0FTUG3RB,	U0W69QF9Q,	U2E4PEHAB,	U3PF6LQSH,	U5083LWHG,	U57R53JHL,	U15DJ7Q02,	U0Q0T9CF3,	U14E22VGF,	U1R4H3DBQ,	U5DK8JG76,	U28879VML,	U0Q3N3Y14,	U2B8LQBM2,	U3NGE4LE4,	U0TG3AG2U,	U0KDK3A84,	U1XG4MR2T,	U1WT54M5Z,	U23LCNUTV,	U1459FLKH,	U0FBB2R4Z,	U0Q16BNRE,	U10KZHNPQ,	U10KWCNKV,	U1T5Z0TU5,	U13MMA5E2,	U3G9VJLAF,	U0Q2EBKKM,	U1LKLA66L,	U3A2E1UD7,	U10BVTZ52,	U146GQEFK,	U14RW53PS,	U41ESQYKW,	U186L6283,	U1GLW328Z,	U0PSEUCPJ,	U0Y5YUZEC,	U15L3KYBZ,	U3FN0SFCP,	U0QAEEF8U,	U2T6R5KDJ,	U0R72EGRF,	U15EYHEG3,	U1NLP8TED,	U2Z6YNUF6,	U338FAVLY,	U0YQ44QBE,	U0JEADY3D,	U0CEJMDJ4,	U12H2N2RX,	U1ECPV2E5,	U2CGT4R98,	U14702XST,	U3AQ51KUP,	U4CHVHV27,	U15BLJK0W,	U38BUPFJ6,	U3Q1G3G8Y,	U0YN2EPSS,	U0NK3JCHK,	U0QQF8LTX,	U39UW4XUY,	U54B8J13Q,	U1EECELEA,	U1QNE1E8M,	U30RDFKRQ,	U4DF5MXQR,	U145KCX62,	U0KEN3KB4,	U0Y1U5SCE,	U0Y1R6KEE,	U0TDFRT8X,	U15KA2Q84,	U2T4VTJ03,	U4E642PE0,	U0W7PEPTN,	U0JS76EBS,	U15A9EQBS,	U0Z3HPN1L,	U4WU6021Y,	U0FCV4BN1,	U0KEBSQ06,	U15LAKUNR,	U3EFX3YSF,	U13N5P6MQ,	U22EHEKEZ,	U2B1FGNVB,	U10BFDML6,	U0JC311S6,	U0WT8BAHK,	U2TTK7S64,	U0FB5HFBP,	U0NDHS8JF
# Short List
#U0J57JGBD,	U0W7PEPTN,	U0X0J067R,	U10KVQ6QL,	U0X6ERLHJ,	U0JC311S6
#ax_all
#Add here list of users to be included

response = slack.usergroups.users.list(usergroup='S5S05J2NM')
#ax_all

users = response.body['users']
for user in users:
    print(user)
    print
