/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./generate_static_blog.py", "./public/**/*.{html,htm}"],
  darkMode: 'class', // 支持手动切换暗色模式
  theme: {
    extend: {
      // 现代日式色彩系统
      colors: {
        // 主色调
        'sumi': {
          50: '#F7F7F7',
          100: '#E8E8E8',
          200: '#D1D1D1',
          300: '#B8B8B8',
          400: '#8B8B8B',
          500: '#666666',
          600: '#4A4A4A',
          700: '#2A2A2A',
          800: '#1A1A1A',
          900: '#0F0F0F',
        },
        'washi': {
          50: '#FDFDFD',
          100: '#FAFAFA',
          200: '#F9F9F9',
          300: '#F5F5F5',
          400: '#F0F0F0',
          500: '#E8E8E8',
        },
        'shuiro': {
          50: '#FEF2F2',
          100: '#FEE2E2',
          200: '#FECACA',
          300: '#FCA5A5',
          400: '#F87171',
          500: '#E74C3C',
          600: '#DC2626',
          700: '#B91C1C',
          800: '#991B1B',
          900: '#7F1D1D',
        },
        'seiji': {
          50: '#F0FDF4',
          100: '#DCFCE7',
          200: '#BBF7D0',
          300: '#86EFAC',
          400: '#4ADE80',
          500: '#27AE60',
          600: '#16A34A',
          700: '#15803D',
          800: '#166534',
          900: '#14532D',
        }
      },
      
      // 字体系统
      fontFamily: {
        'primary': ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        'japanese': ['Noto Sans JP', 'sans-serif'],
        'mono': ['JetBrains Mono', 'Fira Code', 'monospace'],
      },
      
      // 字体大小 - 基于1.25倍比例
      fontSize: {
        'xs': ['0.75rem', { lineHeight: '1.25' }],
        'sm': ['0.875rem', { lineHeight: '1.4' }],
        'base': ['1rem', { lineHeight: '1.5' }],
        'lg': ['1.125rem', { lineHeight: '1.5' }],
        'xl': ['1.25rem', { lineHeight: '1.5' }],
        '2xl': ['1.5rem', { lineHeight: '1.4' }],
        '3xl': ['1.875rem', { lineHeight: '1.3' }],
        '4xl': ['2.25rem', { lineHeight: '1.2' }],
        '5xl': ['3rem', { lineHeight: '1.1' }],
      },
      
      // 黄金比例间距
      spacing: {
        '18': '4.5rem',
        '22': '5.5rem',
        'golden-sm': '1.618rem',
        'golden-md': '2.618rem',
        'golden-lg': '4.236rem',
      },
      
      // 最大宽度
      maxWidth: {
        'content': '42rem',
        'sidebar': '16rem',
        'container': '1200px',
      },
      
      // 圆角
      borderRadius: {
        'none': '0',
        'sm': '0.125rem',
        'base': '0.25rem',
        'md': '0.375rem',
        'lg': '0.5rem',
        'xl': '0.75rem',
        '2xl': '1rem',
        '3xl': '1.5rem',
      },
      
      // 阴影系统
      boxShadow: {
        'washi': '0 2px 8px 0 rgba(42, 42, 42, 0.08)',
        'floating': '0 8px 32px 0 rgba(42, 42, 42, 0.12)',
        'card': '0 4px 16px 0 rgba(42, 42, 42, 0.08)',
        'card-hover': '0 8px 32px 0 rgba(42, 42, 42, 0.16)',
      },
      
      // 动画时长
      transitionDuration: {
        'fast': '150ms',
        'normal': '300ms',
        'slow': '500ms',
      },
      
      // 动画曲线
      transitionTimingFunction: {
        'ease-out-quart': 'cubic-bezier(0.25, 1, 0.5, 1)',
        'ease-in-quart': 'cubic-bezier(0.5, 0, 0.75, 0)',
        'ease-in-out-quart': 'cubic-bezier(0.76, 0, 0.24, 1)',
      },
      
      // 自定义动画
      animation: {
        'fade-in': 'fadeIn 0.6s ease-out',
        'slide-up': 'slideUp 0.4s ease-out',
        'slide-down': 'slideDown 0.4s ease-out',
        'scale-in': 'scaleIn 0.3s ease-out',
        'float': 'float 3s ease-in-out infinite',
      },
      
      // 关键帧
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        slideDown: {
          '0%': { transform: 'translateY(-20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        scaleIn: {
          '0%': { transform: 'scale(0.95)', opacity: '0' },
          '100%': { transform: 'scale(1)', opacity: '1' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-10px)' },
        },
      },
      
      // 渐变
      backgroundImage: {
        'gradient-japanese': 'linear-gradient(135deg, #E74C3C 0%, #27AE60 100%)',
        'gradient-spring': 'linear-gradient(135deg, #FFB7C5 0%, #E8F4FD 100%)',
        'gradient-summer': 'linear-gradient(135deg, #B8E6B8 0%, #87CEEB 100%)',
        'gradient-autumn': 'linear-gradient(135deg, #DEB887 0%, #CD853F 100%)',
        'gradient-winter': 'linear-gradient(135deg, #F0F8FF 0%, #E6E6FA 100%)',
      },
    },
  },
  plugins: [
    // 添加自定义组件类
    function({ addComponents, theme }) {
      addComponents({
        '.btn-primary': {
          backgroundColor: theme('colors.shuiro.500'),
          color: theme('colors.white'),
          padding: `${theme('spacing.3')} ${theme('spacing.6')}`,
          borderRadius: theme('borderRadius.md'),
          fontWeight: theme('fontWeight.medium'),
          transition: `all ${theme('transitionDuration.normal')} ${theme('transitionTimingFunction.ease-out-quart')}`,
          '&:hover': {
            backgroundColor: theme('colors.shuiro.600'),
            transform: 'translateY(-1px)',
            boxShadow: theme('boxShadow.card-hover'),
          },
        },
        '.card': {
          backgroundColor: theme('colors.white'),
          borderRadius: theme('borderRadius.xl'),
          padding: theme('spacing.6'),
          boxShadow: theme('boxShadow.washi'),
          transition: `all ${theme('transitionDuration.normal')} ${theme('transitionTimingFunction.ease-out-quart')}`,
          '&:hover': {
            transform: 'translateY(-2px)',
            boxShadow: theme('boxShadow.floating'),
          },
        },
        '.text-gradient': {
          background: theme('backgroundImage.gradient-japanese'),
          '-webkit-background-clip': 'text',
          '-webkit-text-fill-color': 'transparent',
          'background-clip': 'text',
        },
      })
    },
    // 添加工具类
    function({ addUtilities }) {
      addUtilities({
        '.text-balance': {
          'text-wrap': 'balance',
        },
        '.writing-vertical': {
          'writing-mode': 'vertical-rl',
          'text-orientation': 'mixed',
        },
        '.backdrop-blur-washi': {
          'backdrop-filter': 'blur(8px) saturate(1.8)',
          '-webkit-backdrop-filter': 'blur(8px) saturate(1.8)',
        },
      })
    },
  ],
}