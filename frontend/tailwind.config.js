import frappeUIPreset from 'frappe-ui/src/tailwind/preset'

export default {
	presets: [frappeUIPreset],
	content: [
		'./index.html',
		'./src/**/*.{vue,js,ts,jsx,tsx}',
		'./node_modules/frappe-ui/src/**/*.{vue,js,ts,jsx,tsx}',
		'../node_modules/frappe-ui/src/**/*.{vue,js,ts,jsx,tsx}',
		'./node_modules/frappe-ui/frappe/**/*.{vue,js,ts,jsx,tsx}',
		'../node_modules/frappe-ui/frappe/**/*.{vue,js,ts,jsx,tsx}',
	],
	theme: {
		extend: {
			colors: {
				'level-primary': '#2563EB',
				'level-secondary': '#7C3AED',
				'level-teal': '#14B8A6',
				'level-orange': '#F59E0B',
				'level-dark': '#1F2937',
				'level-gray': '#6B7280',
				'level-light': '#F3F4F6',
				'level-border': '#E5E7EB',
				'level-input': '#D1D5DB',
			},
			backgroundImage: {
				'level-gradient': 'linear-gradient(135deg, #2563EB 0%, #7C3AED 100%)',
			},
			fontFamily: {
				'code': ['JetBrains Mono', 'Fira Code', 'monospace'],
			},
			strokeWidth: {
				1.5: '1.5',
			},
			screens: {
				'2xl': '1600px',
				'3xl': '1920px',
			},
			spacing: {
				'18': '4.5rem',
				'88': '22rem',
				'128': '32rem',
			},
			borderRadius: {
				'card': '12px',
				'button': '8px',
			},
		},
	},
	plugins: [],
}
