module.exports = {
	// mode: "jit",
	content: [
		"./templates/*.html",
		"./templates/*/*.html",
		"./*/templates/*.html",
		"./*/templates/*/*.html",
		"./*/templates/*/*/*.html",
	],
	theme: {
        colors: {
            transparent: 'transparent',
			current: 'currentColor',
			'white': "#fff",
			'black': "#1f1f1f",

			'neutral-5': '#F3F3F4',
			'neutral-10': '#E9E9EA',
			'neutral-20': '#D1D2D4',
			'neutral-30': '#E9ECEF',
			'neutral-40': '#A4A5A8',
			'neutral-50': '#CED4DA',
			'neutral-60': '#76777D',
			'neutral-70': '#606168',
			'neutral-75': '#686E74',
			'neutral-80': '#494A51',
			'neutral-90': '#32343C',
			'neutral-100': '#1B1D26 ',
			'neutral-black': '#000 ',
			'bronze':' #AC6D2F',
			'prata': '#C0C0C0',
			'ouro': '#DBB000',
			'estrategia': '#F40000',
			'controle': '#E5813E',
			'manutencao': '#D7B85B',
			'aquisicao': '#FF560E',
			'mercado': '#F79900',
			'descarte': '#B59E74',


            'primary-red': '#D40203',
            'primary-red-o': '#D4020333',
						'primary-red-o-2':' rgba(212, 2, 3, 0.1)',

            'primary-green': '#42CC82',
            'primary-green-o': '#42CC821A',

						'primary-blue': '#6AC9CE',
        },

        spacing: {
			'0': '0',
			'1': '1px',
			'2': '0.125rem',
			'4': '0.25rem',
			'8': '0.5rem',
			'10': '.625rem',
			'12': '0.75rem',
			'14': '0.875rem',
			'16': '1rem',
			'20': '1.25rem',
			'24': '1.5rem',
			'32': '2rem',
			'40': '2.5rem',
			'48': '3rem',
			'56': '3.5rem',
			'64': '4rem',
			'72': '4.5rem',
			'80': '5rem',
			'96': '6rem',
			'120': '7.5rem',
			'160': '10rem',
		},

        fontFamily: {
			sans: ['Inter', 'sans-serif'],
		},

        lineHeight: {
			'100': '100%',
			'140': '140%',
			'150': '150%',
		},

        screens: {
			'min2xl': { 'min': '1441px' },
			// => @media (max-width: 1535px) { ... }

			'2xl': { 'max': '1441px' },
			// => @media (max-width: 1535px) { ... }

			'xl': { 'max': '1367px' },
			// => @media (max-width: 1279px) { ... }

			'lg': { 'max': '1281px' },
			// => @media (max-width: 1023px) { ... }

			'md2': { 'max': '1180px' },
			// => @media (max-width: 767px) { ... }

			'md': { 'max': '767px' },
			// => @media (max-width: 767px) { ... }

			'sm': { 'max': '639px' },
			// => @media (max-width: 639px) { ... }
		},

        extend: {
			letterSpacing: {
				'tight': '-0.02em'
			},

			fontSize: {
				'2xl': ['1.5rem', {
					lineHeight: '150%',
				}],
				'xl': ['1.125rem', {
					lineHeight: '150%',
				}],
				'base': ['1rem', {
					lineHeight: '150%',
				}],
				'sm': ['0.875rem', {
					lineHeight: '150%',
				}],
				'xs': ['.75rem', {
					lineHeight: '150%',
					letterSpacing: '0.03em',
				}],
				'xs-space': ['.75rem', {
					lineHeight: '150%',
					letterSpacing: '0.1em',
				}],
			},

			boxShadow: {
				'xs': '0px 1px 2px #CED4DA',
				'sm': '0px 8px 16px rgba(206, 212, 218, 0.3)',
				'md': '0px 4px 11px rgba(0, 0, 0, 0.04)',
				'lg': '0px 9px 16px rgba(0, 0, 0, 0.08);',
			}
		},
    },
	variants: {},
	plugins: [],

};

// https://tailwindcss.com/