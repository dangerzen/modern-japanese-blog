import json
import logging
import shutil

import css_html_js_minify
import markdown
from pathlib import Path

BLOG_TITLE = 'My Minimal Blog'
BLOG_DESCRIPTION = 'Saving bytes one blog at a time.'

POSTS_INPUT_DIR = 'posts/'
POSTS_OUTPUT_DIR = 'public/blog/'

ASSETS_INPUT_DIR = 'assets/'
ASSETS_OUTPUT_DIR = 'public/blog/assets/'

HOME_PAGE_TEMPLATE = '''
<!doctype html>
<html lang="en" class="scroll-smooth">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="{description}">
    <meta name="author" content="Modern Japanese Blog">
    <meta name="theme-color" content="#F9F9F9">
    <title>{title}</title>
    <link rel="stylesheet" type="text/css" href="assets/blog.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Noto+Sans+JP:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="data:image/x-icon;base64,AAABAAEAEBAAAAAAAABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AJzn/2A+z///O8z//zfJ//80xv//nuL/L////wD///8A////AP///wD///8A////AP///wD///8A////AEnY//9F1f//QtL//z/P//87zP//Pcr///b8//8xw//7////AP///wD///8A////AP///wD///8A////AP///wBN3P//Sdn//0bV//9C0v//P8///0vQ///7/v//NMb//////wD///8A////AP///wD///8A////AP///wD///8AUN///03c//9J2f//Rtb//0PT//8/0P//PM3//zjJ//////8A////AP///wD///8A////AJ9wN/6cbjb/mWw2/1Ti//9R3///Tdz//0rZ//9G1v//Q9P//z/Q//88zf//OMr//zXH//8xw//+////AKZzN6ajcjf/oHA3/51uNv9Y5v//VOP//1Hg//9O3f//Str//0fW//9D0///QND//zzN//85yv//Ncf///X8/wSpdTf/pnM3/6NyN/+gcDf/XOn//1jm//9V4///UeD//07d//9K2v//R9f//0PT//9A0P//PM3//znK//82x///rHc3/6l1N/+mdDf/o3I3/////wBc6f//WOb//1Xj//9S4P//Tt3//0va//9H1///RNT//0DR//89zf//Ocv//7B5N/+tdzf/qnY3/6d0N/+kcjf/oHA3/51uNv+bbTb/l2s2/5RpNv+UaTb/m+r/ZEfX//9E1P//QdH//z3O//+zezf/sHk3/613N/+qdjf/p3Q3/6RyN/+hcDf/nm82/5ttNv+Yazb/lGk2/5RpNv9L2v//R9f//0TU//9B0f//tn045LN7N/+weTf/rXg3/6p2N/+ndDf/pHI3/6FxN/+ebzb/m202/5hrNv+VaTb/T97//0vb//9I1///ZNv/df///wC3fTj+tHs3/7B6N/+teDf/qnY3/6d0N/+kczf/oXE3/55vNv+bbTb/mGs2/1Ph//9P3v//TNv//////wD///8A////AP///wD///8AsXo37654N++rdjfvqHQ376VzN/+hcTf/nm82/5ttNv////8A////AP///wD///8A////AP///wD///8A////ALR8N//v5Nb/rng3/6t2N/+odTf/pXM3/6JxN/+fbzf/////AP///wD///8A////AP///wD///8A////AP///wC3fjj//////7R/Pv+ueDf/q3c3/6h1N/+lczf/onE3/////wD///8A////AP///wD///8A////AP///wD///8A////ALh+OP+1fDj/sno3/694N/+sdzf/qXU3/////wD///8A////AP///wD///8A/D8AAPAPAADwDwAA8A8AAIABAAAAAQAAAAAAAAgAAAAAEAAAAAAAAAABAACAAQAA8A8AAPAPAADwDwAA+B8AAA==" rel="icon" type="image/x-icon" />
  </head>
  <body class="antialiased">
    <!-- 暗色模式切换按钮 -->
    <button class="theme-toggle" onclick="toggleTheme()" aria-label="切换暗色模式">
      <span class="theme-icon">🌙</span>
    </button>
    
    <!-- 主容器 -->
    <div class="blog-container">
      <!-- 博客头部 -->
      <header class="blog-header">
        <h1 class="blog-title">{title}</h1>
        <p class="blog-description">{description}</p>
      </header>
      
      <!-- 文章列表 -->
      <main class="posts-grid">
        <h2 class="section-title">最新文章</h2>
        <ul class="posts-list">
          {posts}
        </ul>
      </main>
    </div>
    
    <!-- JavaScript -->
    <script>
      // 暗色模式切换
      function toggleTheme() {{
        const html = document.documentElement;
        const icon = document.querySelector('.theme-icon');
        
        if (html.classList.contains('dark')) {{
          html.classList.remove('dark');
          icon.textContent = '🌙';
          localStorage.setItem('theme', 'light');
        }} else {{
          html.classList.add('dark');
          icon.textContent = '☀️';
          localStorage.setItem('theme', 'dark');
        }}
      }}
      
      // 初始化主题
      function initTheme() {{
        const savedTheme = localStorage.getItem('theme');
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        const icon = document.querySelector('.theme-icon');
        
        if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {{
          document.documentElement.classList.add('dark');
          icon.textContent = '☀️';
        }} else {{
          icon.textContent = '🌙';
        }}
      }}
      
      // 页面加载完成后初始化
      document.addEventListener('DOMContentLoaded', initTheme);
      
      // 监听系统主题变化
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {{
        if (!localStorage.getItem('theme')) {{
          const icon = document.querySelector('.theme-icon');
          if (e.matches) {{
            document.documentElement.classList.add('dark');
            icon.textContent = '☀️';
          }} else {{
            document.documentElement.classList.remove('dark');
            icon.textContent = '🌙';
          }}
        }}
      }});
      
      // 添加平滑滚动和动画
      document.addEventListener('DOMContentLoaded', function() {{
        // 为所有卡片添加进入动画
        const cards = document.querySelectorAll('.blog-card');
        const observer = new IntersectionObserver((entries) => {{
          entries.forEach((entry) => {{
            if (entry.isIntersecting) {{
              entry.target.style.opacity = '1';
              entry.target.style.transform = 'translateY(0)';
            }}
          }});
        }}, {{ threshold: 0.1 }});
        
        cards.forEach((card, index) => {{
          card.style.opacity = '0';
          card.style.transform = 'translateY(20px)';
          card.style.transition = `opacity 0.6s ease-out ${{index * 0.1}}s, transform 0.6s ease-out ${{index * 0.1}}s`;
          observer.observe(card);
        }});
      }});
    </script>
  </body>
</html>
'''

POST_PAGE_TEMPLATE = '''
<!doctype html>
<html lang="en" class="scroll-smooth">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="{description}">
    <meta name="author" content="Modern Japanese Blog">
    <meta name="theme-color" content="#F9F9F9">
    <title>{title} - {blog_title}</title>
    <link rel="stylesheet" type="text/css" href="../assets/blog.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Noto+Sans+JP:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="data:image/x-icon;base64,AAABAAEAEBAAAAAAAABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAD///8A////AP///wD///8A////AJzn/2A+z///O8z//zfJ//80xv//nuL/L////wD///8A////AP///wD///8A////AP///wD///8A////AEnY//9F1f//QtL//z/P//87zP//Pcr///b8//8xw//7////AP///wD///8A////AP///wD///8A////AP///wBN3P//Sdn//0bV//9C0v//P8///0vQ///7/v//NMb//////wD///8A////AP///wD///8A////AP///wD///8AUN///03c//9J2f//Rtb//0PT//8/0P//PM3//zjJ//////8A////AP///wD///8A////AJ9wN/6cbjb/mWw2/1Ti//9R3///Tdz//0rZ//9G1v//Q9P//z/Q//88zf//OMr//zXH//8xw//+////AKZzN6ajcjf/oHA3/51uNv9Y5v//VOP//1Hg//9O3f//Str//0fW//9D0///QND//zzN//85yv//Ncf///X8/wSpdTf/pnM3/6NyN/+gcDf/XOn//1jm//9V4///UeD//07d//9K2v//R9f//0PT//9A0P//PM3//znK//82x///rHc3/6l1N/+mdDf/o3I3/////wBc6f//WOb//1Xj//9S4P//Tt3//0va//9H1///RNT//0DR//89zf//Ocv//7B5N/+tdzf/qnY3/6d0N/+kcjf/oHA3/51uNv+bbTb/l2s2/5RpNv+UaTb/m+r/ZEfX//9E1P//QdH//z3O//+zezf/sHk3/613N/+qdjf/p3Q3/6RyN/+hcDf/nm82/5ttNv+Yazb/lGk2/5RpNv9L2v//R9f//0TU//9B0f//tn045LN7N/+weTf/rXg3/6p2N/+ndDf/pHI3/6FxN/+ebzb/m202/5hrNv+VaTb/T97//0vb//9I1///ZNv/df///wC3fTj+tHs3/7B6N/+teDf/qnY3/6d0N/+kczf/oXE3/55vNv+bbTb/mGs2/1Ph//9P3v//TNv//////wD///8A////AP///wD///8AsXo37654N++rdjfvqHQ376VzN/+hcTf/nm82/5ttNv////8A////AP///wD///8A////AP///wD///8A////ALR8N//v5Nb/rng3/6t2N/+odTf/pXM3/6JxN/+fbzf/////AP///wD///8A////AP///wD///8A////AP///wC3fjj//////7R/Pv+ueDf/q3c3/6h1N/+lczf/onE3/////wD///8A////AP///wD///8A////AP///wD///8A////ALh+OP+1fDj/sno3/694N/+sdzf/qXU3/////wD///8A////AP///wD///8A/D8AAPAPAADwDwAA8A8AAIABAAAAAQAAAAAAAAgAAAAAEAAAAAAAAAABAACAAQAA8A8AAPAPAADwDwAA+B8AAA==" rel="icon" type="image/x-icon" />
  </head>
  <body class="antialiased">
    <!-- 暗色模式切换按钮 -->
    <button class="theme-toggle" onclick="toggleTheme()" aria-label="切换暗色模式">
      <span class="theme-icon">🌙</span>
    </button>
    
    <!-- 主容器 -->
    <div class="blog-container">
      <!-- 返回首页链接 -->
      <nav class="navigation">
        <a href="../" class="home-link">
          <span>返回首页</span>
        </a>
      </nav>
      
      <!-- 文章内容 -->
      <article class="post-article">
        <!-- 文章头部 -->
        <header class="post-header">
          <h1 class="post-title">{title}</h1>
          <div class="post-meta">
            <time class="post-date" datetime="{date}">{date}</time>
            <span class="post-reading-time">• 预计阅读时间 3 分钟</span>
          </div>
        </header>
        
        <!-- 文章内容 -->
        <div class="post-content prose">
          {content}
        </div>
        
        <!-- 文章底部 -->
        <footer class="post-footer">
          <div class="post-navigation">
            <a href="../" class="back-to-posts">← 查看更多文章</a>
          </div>
        </footer>
      </article>
    </div>
    
    <!-- JavaScript -->
    <script>
      // 暗色模式切换
      function toggleTheme() {{
        const html = document.documentElement;
        const icon = document.querySelector('.theme-icon');
        
        if (html.classList.contains('dark')) {{
          html.classList.remove('dark');
          icon.textContent = '🌙';
          localStorage.setItem('theme', 'light');
        }} else {{
          html.classList.add('dark');
          icon.textContent = '☀️';
          localStorage.setItem('theme', 'dark');
        }}
      }}
      
      // 初始化主题
      function initTheme() {{
        const savedTheme = localStorage.getItem('theme');
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        const icon = document.querySelector('.theme-icon');
        
        if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {{
          document.documentElement.classList.add('dark');
          icon.textContent = '☀️';
        }} else {{
          icon.textContent = '🌙';
        }}
      }}
      
      // 页面加载完成后初始化
      document.addEventListener('DOMContentLoaded', initTheme);
      
      // 监听系统主题变化
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {{
        if (!localStorage.getItem('theme')) {{
          const icon = document.querySelector('.theme-icon');
          if (e.matches) {{
            document.documentElement.classList.add('dark');
            icon.textContent = '☀️';
          }} else {{
            document.documentElement.classList.remove('dark');
            icon.textContent = '🌙';
          }}
        }}
      }});
      
      // 文章内容增强
      document.addEventListener('DOMContentLoaded', function() {{
        // 为代码块添加复制按钮
        const codeBlocks = document.querySelectorAll('pre code');
        codeBlocks.forEach(function(codeBlock) {{
          const button = document.createElement('button');
          button.className = 'copy-button';
          button.textContent = '复制';
          button.onclick = function() {{
            navigator.clipboard.writeText(codeBlock.textContent);
            button.textContent = '已复制!';
            setTimeout(() => {{
              button.textContent = '复制';
            }}, 2000);
          }};
          codeBlock.parentNode.style.position = 'relative';
          codeBlock.parentNode.appendChild(button);
        }});
        
        // 添加阅读进度条
        const progressBar = document.createElement('div');
        progressBar.className = 'reading-progress';
        document.body.appendChild(progressBar);
        
        function updateProgress() {{
          const windowHeight = window.innerHeight;
          const documentHeight = document.documentElement.scrollHeight - windowHeight;
          const scrolled = (window.scrollY / documentHeight) * 100;
          progressBar.style.width = scrolled + '%';
        }}
        
        window.addEventListener('scroll', updateProgress);
        updateProgress();
      }});
    </script>
    
    <style>
      /* 文章页面特定样式 */
      .navigation {{
        margin-bottom: var(--space-golden-md);
      }}
      
      .post-article {{
        background: var(--yuki-snow);
        border-radius: var(--radius-2xl);
        padding: var(--space-golden-lg);
        box-shadow: var(--shadow-washi);
        border: 1px solid var(--color-border);
      }}
      
      .post-header {{
        margin-bottom: var(--space-golden-md);
        text-align: center;
        border-bottom: 1px solid var(--color-border);
        padding-bottom: var(--space-6);
      }}
      
      .post-title {{
        font-size: var(--text-4xl);
        font-weight: 800;
        margin-bottom: var(--space-4);
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.05em;
        line-height: var(--leading-tight);
      }}
      
      .post-meta {{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: var(--space-2);
        font-size: var(--text-sm);
        color: var(--color-text-muted);
        margin-bottom: var(--space-4);
      }}
      
      .post-date {{
        font-weight: 500;
      }}
      
      .post-reading-time {{
        opacity: 0.8;
      }}
      
      .post-content {{
        line-height: var(--leading-relaxed);
        font-size: var(--text-lg);
        max-width: none;
      }}
      
      .post-footer {{
        margin-top: var(--space-golden-lg);
        padding-top: var(--space-6);
        border-top: 1px solid var(--color-border);
        text-align: center;
      }}
      
      .back-to-posts {{
        display: inline-flex;
        align-items: center;
        gap: var(--space-2);
        padding: var(--space-3) var(--space-6);
        background: var(--color-bg-secondary);
        border-radius: var(--radius-lg);
        font-weight: 500;
        transition: all var(--duration-normal) var(--easing-ease-out);
        border: 1px solid var(--color-border);
      }}
      
      .back-to-posts:hover {{
        background: var(--color-accent);
        color: white;
        transform: translateY(-2px);
        box-shadow: var(--shadow-floating);
      }}
      
      .copy-button {{
        position: absolute;
        top: var(--space-2);
        right: var(--space-2);
        padding: var(--space-1) var(--space-2);
        background: var(--color-bg-primary);
        border: 1px solid var(--color-border);
        border-radius: var(--radius-base);
        font-size: var(--text-xs);
        cursor: pointer;
        transition: all var(--duration-fast) var(--easing-ease-out);
      }}
      
      .copy-button:hover {{
        background: var(--color-accent);
        color: white;
      }}
      
      .reading-progress {{
        position: fixed;
        top: 0;
        left: 0;
        height: 3px;
        background: var(--gradient-primary);
        z-index: var(--z-fixed);
        transition: width 0.3s ease;
      }}
      
      @media (max-width: 768px) {{
        .post-article {{
          padding: var(--space-6);
        }}
        
        .post-title {{
          font-size: var(--text-2xl);
        }}
        
        .post-meta {{
          flex-direction: column;
          gap: var(--space-1);
        }}
      }}
    </style>
  </body>
</html>
'''


def parse_blog_post_file(file: Path) -> json:
    values = {'file': file.name, 'date': file.name[0:10], 'content': ''}
    is_content = False
    with file.open() as f:
        for i, line in enumerate(f):
            if i == 0:
                if line != '---\n':
                    logging.error(f'Missing "---" on first line in {file}')
            elif line == '---\n':
                is_content = True
            elif is_content:
                values['content'] += line
            elif ': ' in line:
                tokens = line.split(': ')
                values[tokens[0]] = tokens[1].rstrip('\n')
            else:
                logging.error(f'This syntax is not supported yet: {line}')
    values['content'] = markdown.markdown(values['content'])
    if 'slug' not in values:
        values['slug'] = file.name.lower().rstrip('.md').replace(' ', '-')
    return values


def generate_post(values: json):
    post_dir = Path(f'{POSTS_OUTPUT_DIR}/{values["slug"]}')
    post_dir.mkdir(parents=True, exist_ok=True)
    page_html = POST_PAGE_TEMPLATE.format(
        blog_title=BLOG_TITLE,
        title=values['title'],
        description=BLOG_DESCRIPTION,
        date=values['date'],
        content=values['content'])
    (post_dir / Path('index.htm')).write_text(page_html)


def generate_site():
    shutil.rmtree(POSTS_OUTPUT_DIR, ignore_errors=True)
    Path(POSTS_OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    posts_html = ''
    post_files = list(Path(POSTS_INPUT_DIR).glob('*.md'))
    post_files.reverse()  # Put more recent posts at the top
    for file in post_files:
        values = parse_blog_post_file(file)
        generate_post(values)
        slug = values['slug']
        title = values.get('title', 'Untitled')
        date = values.get('date', '')
        description = values.get('description', '')
        
        # 创建文章摘要（取content的前150个字符）
        content_text = values.get('content', '')
        # 移除HTML标签来获取纯文本
        import re
        plain_text = re.sub(r'<[^>]+>', '', content_text)
        excerpt = plain_text[:150] + '...' if len(plain_text) > 150 else plain_text
        
        # 生成卡片式文章项
        posts_html += f'''
        <li>
          <article class="blog-card">
            <header class="card-header">
              <h3 class="post-title">
                <a href="{slug}">{title}</a>
              </h3>
              <div class="post-meta">
                <time class="post-date" datetime="{date}">{date}</time>
                <span class="reading-time">• 3 分钟阅读</span>
              </div>
            </header>
            
            <div class="card-content">
              <p class="post-excerpt">{excerpt}</p>
              <a href="{slug}" class="read-more">
                <span>阅读更多</span>
              </a>
            </div>
          </article>
        </li>'''
    
    home_page = HOME_PAGE_TEMPLATE.format(title=BLOG_TITLE, description=BLOG_DESCRIPTION, posts=posts_html)
    Path(f'{POSTS_OUTPUT_DIR}/index.htm').write_text(home_page)
    shutil.copytree(ASSETS_INPUT_DIR, ASSETS_OUTPUT_DIR)

    # 只压缩CSS文件，保持HTML可读性
    css_files = list(Path(ASSETS_OUTPUT_DIR).glob('*.css'))
    for css_file in css_files:
        if not css_file.name.endswith('.min.css'):
            css_html_js_minify.minify.process_multiple_files(str(css_file))


def main():
    generate_site()


if __name__ == '__main__':
    main()
