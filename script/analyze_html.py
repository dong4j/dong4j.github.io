from bs4 import BeautifulSoup

# 示例HTML代码
def tuijiandeboke():
    html_content = '''
    <div class="site-card-group">
    <div class="site-card 生活">
        <span class="site-card-tag">生活</span
        ><a
        class="img"
        target="_blank"
        title="张洪Heo"
        href="https://blog.zhheo.com/"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/jpa69F22590681718335705067.png!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="张洪Heo"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/jpa69F22590681718335705067.png!cover_siteshot"
        />
        <div class="img-alt is-center">张洪Heo</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="张洪Heo"
        href="https://blog.zhheo.com/"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/8DSTSS20990281646044689944.PNG!cover_mini"
            data-fancybox="images"
            data-caption="张洪Heo"
            class="fancybox"
            data-srcset="https://p.zhheo.com/8DSTSS20990281646044689944.PNG!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/8DSTSS20990281646044689944.PNG!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="张洪Heo"
                data-ll-status="loaded"
                src="https://p.zhheo.com/8DSTSS20990281646044689944.PNG!cover_mini"
            /></a>
            <div class="img-alt is-center">张洪Heo</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">张洪Heo</span
            ><span class="desc" title="产品设计师，独立开发者，设计与科技分享"
            >产品设计师，独立开发者，设计与科技分享</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag">技术</span
        ><a
        class="img"
        target="_blank"
        title="小冰"
        href="https://zfe.space/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/Ct7CRc21290481618973112604.jpg!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="小冰"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/Ct7CRc21290481618973112604.jpg!cover_siteshot"
        />
        <div class="img-alt is-center">小冰</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="小冰"
        href="https://zfe.space/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/20200904222157.png!cover_mini"
            data-fancybox="images"
            data-caption="小冰"
            class="fancybox"
            data-srcset="https://p.zhheo.com/20200904222157.png!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/20200904222157.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="小冰"
                data-ll-status="loaded"
                src="https://p.zhheo.com/20200904222157.png!cover_mini"
            /></a>
            <div class="img-alt is-center">小冰</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">小冰</span
            ><span class="desc" title="冰糖红茶组织发起人，Butterfly魔改专家"
            >冰糖红茶组织发起人，Butterfly魔改专家</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag">技术</span
        ><a
        class="img"
        target="_blank"
        title="Akilar"
        href="https://akilar.top/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/2023409e2dee361faf95c9e405125e2d4358070001.png!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="Akilar"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/2023409e2dee361faf95c9e405125e2d4358070001.png!cover_siteshot"
        />
        <div class="img-alt is-center">Akilar</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="Akilar"
        href="https://akilar.top/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/qU1OfH24290881661329002842.jpg!cover_mini"
            data-fancybox="images"
            data-caption="Akilar"
            class="fancybox"
            data-srcset="https://p.zhheo.com/qU1OfH24290881661329002842.jpg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/qU1OfH24290881661329002842.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Akilar"
                data-ll-status="loaded"
                src="https://p.zhheo.com/qU1OfH24290881661329002842.jpg!cover_mini"
            /></a>
            <div class="img-alt is-center">Akilar</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">Akilar</span
            ><span class="desc" title="前端开发工程师，Butterfly魔改专家"
            >前端开发工程师，Butterfly魔改专家</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag vip">技术<i class="light"></i></span
        ><a
        class="img"
        target="_blank"
        title="小康"
        href="https://www.antmoe.com/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/1J90dO25190481618973271553.jpg!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="小康"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/1J90dO25190481618973271553.jpg!cover_siteshot"
        />
        <div class="img-alt is-center">小康</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="小康"
        href="https://www.antmoe.com/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/bfe443d24cdc68c552a1aebb493e547f7c1cfa06.jpg!cover_mini"
            data-fancybox="images"
            data-caption="小康"
            class="fancybox"
            data-srcset="https://p.zhheo.com/bfe443d24cdc68c552a1aebb493e547f7c1cfa06.jpg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/bfe443d24cdc68c552a1aebb493e547f7c1cfa06.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="小康"
                data-ll-status="loaded"
                src="https://p.zhheo.com/bfe443d24cdc68c552a1aebb493e547f7c1cfa06.jpg!cover_mini"
            /></a>
            <div class="img-alt is-center">小康</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">小康</span
            ><span class="desc" title="全栈开发工程师，Butterfly魔改专家"
            >全栈开发工程师，Butterfly魔改专家</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag vip">技术<i class="light"></i></span
        ><a
        class="img"
        target="_blank"
        title="Adil"
        href="https://blog.adil.com.cn/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/SB32Uw23090581653027870462.jpg!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="Adil"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/SB32Uw23090581653027870462.jpg!cover_siteshot"
        />
        <div class="img-alt is-center">Adil</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="Adil"
        href="https://blog.adil.com.cn/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/KKKL6z23990381615774419596.jpg!cover_mini"
            data-fancybox="images"
            data-caption="Adil"
            class="fancybox"
            data-srcset="https://p.zhheo.com/KKKL6z23990381615774419596.jpg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/KKKL6z23990381615774419596.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Adil"
                data-ll-status="loaded"
                src="https://p.zhheo.com/KKKL6z23990381615774419596.jpg!cover_mini"
            /></a>
            <div class="img-alt is-center">Adil</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">Adil</span
            ><span
            class="desc"
            title="BW/HANA顾问，BI工程师，数据分析师，数据科学家。"
            >BW/HANA顾问，BI工程师，数据分析师，数据科学家。</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag">技术</span
        ><a
        class="img"
        target="_blank"
        title="林木木"
        href="https://immmmm.com/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/TKr7Qq25390481618972613803.JPG!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="林木木"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/TKr7Qq25390481618972613803.JPG!cover_siteshot"
        />
        <div class="img-alt is-center">林木木</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="林木木"
        href="https://immmmm.com/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/4Fvg5z20590281612593905877.jpeg!cover_mini"
            data-fancybox="images"
            data-caption="林木木"
            class="fancybox"
            data-srcset="https://p.zhheo.com/4Fvg5z20590281612593905877.jpeg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/4Fvg5z20590281612593905877.jpeg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="林木木"
                data-ll-status="loaded"
                src="https://p.zhheo.com/4Fvg5z20590281612593905877.jpeg!cover_mini"
            /></a>
            <div class="img-alt is-center">林木木</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">林木木</span
            ><span class="desc" title="全栈开发工程师，生活化语言的技术博客"
            >全栈开发工程师，生活化语言的技术博客</span
            >
        </div></a
        >
    </div>
    <div class="site-card 生活">
        <span class="site-card-tag">生活</span
        ><a
        class="img"
        target="_blank"
        title="风记星辰"
        href="https://www.thyuu.com/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/x48cF423191281640339671599.jpg!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="风记星辰"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/x48cF423191281640339671599.jpg!cover_siteshot"
        />
        <div class="img-alt is-center">风记星辰</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="风记星辰"
        href="https://www.thyuu.com/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/kU9QfW25891281640339638550.jpg!cover_mini"
            data-fancybox="images"
            data-caption="风记星辰"
            class="fancybox"
            data-srcset="https://p.zhheo.com/kU9QfW25891281640339638550.jpg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/kU9QfW25891281640339638550.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="风记星辰"
                data-ll-status="loaded"
                src="https://p.zhheo.com/kU9QfW25891281640339638550.jpg!cover_mini"
            /></a>
            <div class="img-alt is-center">风记星辰</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">风记星辰</span
            ><span class="desc" title="设计师，有着优秀设计与交互的记录生活的博客"
            >设计师，有着优秀设计与交互的记录生活的博客</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag">技术</span
        ><a
        class="img"
        target="_blank"
        title="iMaeGoo"
        href="https://www.imaegoo.com/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/lORqCr21590581653027615808.jpg!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="iMaeGoo"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/lORqCr21590581653027615808.jpg!cover_siteshot"
        />
        <div class="img-alt is-center">iMaeGoo</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="iMaeGoo"
        href="https://www.imaegoo.com/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/eaaa072fdff28c0088dbda9246d48e94296be053.jpeg!cover_mini"
            data-fancybox="images"
            data-caption="iMaeGoo"
            class="fancybox"
            data-srcset="https://p.zhheo.com/eaaa072fdff28c0088dbda9246d48e94296be053.jpeg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/eaaa072fdff28c0088dbda9246d48e94296be053.jpeg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="iMaeGoo"
                data-ll-status="loaded"
                src="https://p.zhheo.com/eaaa072fdff28c0088dbda9246d48e94296be053.jpeg!cover_mini"
            /></a>
            <div class="img-alt is-center">iMaeGoo</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">iMaeGoo</span
            ><span class="desc" title="开发工程师，Twikoo评论作者"
            >开发工程师，Twikoo评论作者</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag vip">技术<i class="light"></i></span
        ><a
        class="img"
        target="_blank"
        title="LinkinStar"
        href="https://www.linkinstars.com/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/pKaVPB25790581653027657765.jpg!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="LinkinStar"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/pKaVPB25790581653027657765.jpg!cover_siteshot"
        />
        <div class="img-alt is-center">LinkinStar</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="LinkinStar"
        href="https://www.linkinstars.com/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/HKNZPB25290381646386132784.jpg!cover_mini"
            data-fancybox="images"
            data-caption="LinkinStar"
            class="fancybox"
            data-srcset="https://p.zhheo.com/HKNZPB25290381646386132784.jpg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/HKNZPB25290381646386132784.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="LinkinStar"
                data-ll-status="loaded"
                src="https://p.zhheo.com/HKNZPB25290381646386132784.jpg!cover_mini"
            /></a>
            <div class="img-alt is-center">LinkinStar</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">LinkinStar</span
            ><span class="desc" title="全栈开发工程师，高质量后端技术博客"
            >全栈开发工程师，高质量后端技术博客</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag">技术</span
        ><a
        class="img"
        target="_blank"
        title="Eurkon"
        href="https://blog.eurkon.com/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/DfKvcq22390581653027743671.jpg!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="Eurkon"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/DfKvcq22390581653027743671.jpg!cover_siteshot"
        />
        <div class="img-alt is-center">Eurkon</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="Eurkon"
        href="https://blog.eurkon.com/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/XimyzZ24690381617172546542.jpg!cover_mini"
            data-fancybox="images"
            data-caption="Eurkon"
            class="fancybox"
            data-srcset="https://p.zhheo.com/XimyzZ24690381617172546542.jpg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/XimyzZ24690381617172546542.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Eurkon"
                data-ll-status="loaded"
                src="https://p.zhheo.com/XimyzZ24690381617172546542.jpg!cover_mini"
            /></a>
            <div class="img-alt is-center">Eurkon</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">Eurkon</span
            ><span
            class="desc"
            title="前端工程师，专注分享echart开发博客，Butterfly魔改专家"
            >前端工程师，专注分享echart开发博客，Butterfly魔改专家</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag">技术</span
        ><a
        class="img"
        target="_blank"
        title="贰猹"
        href="https://noionion.top/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/jWcZPm20390581653027963038.jpg!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="贰猹"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/jWcZPm20390581653027963038.jpg!cover_siteshot"
        />
        <div class="img-alt is-center">贰猹</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="贰猹"
        href="https://noionion.top/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/HOBVt121690181611239776283.jpg!cover_mini"
            data-fancybox="images"
            data-caption="贰猹"
            class="fancybox"
            data-srcset="https://p.zhheo.com/HOBVt121690181611239776283.jpg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/HOBVt121690181611239776283.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="贰猹"
                data-ll-status="loaded"
                src="https://p.zhheo.com/HOBVt121690181611239776283.jpg!cover_mini"
            /></a>
            <div class="img-alt is-center">贰猹</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">贰猹</span
            ><span class="desc" title="前端工程师，Butterfly魔改专家"
            >前端工程师，Butterfly魔改专家</span
            >
        </div></a
        >
    </div>
    <div class="site-card 生活">
        <span class="site-card-tag vip">生活<i class="light"></i></span
        ><a
        class="img"
        target="_blank"
        title="思宁小椭圆"
        href="https://snhere.com/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/50QOrq20690581653031506635.jpg!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="思宁小椭圆"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/50QOrq20690581653031506635.jpg!cover_siteshot"
        />
        <div class="img-alt is-center">思宁小椭圆</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="思宁小椭圆"
        href="https://snhere.com/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/UTc20Z21090481619315110835.png!cover_mini"
            data-fancybox="images"
            data-caption="思宁小椭圆"
            class="fancybox"
            data-srcset="https://p.zhheo.com/UTc20Z21090481619315110835.png!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/UTc20Z21090481619315110835.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="思宁小椭圆"
                data-ll-status="loaded"
                src="https://p.zhheo.com/UTc20Z21090481619315110835.png!cover_mini"
            /></a>
            <div class="img-alt is-center">思宁小椭圆</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">思宁小椭圆</span
            ><span class="desc" title="设计师，记录生活的博客"
            >设计师，记录生活的博客</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag">技术</span
        ><a
        class="img"
        target="_blank"
        title="Tianli"
        href="https://tianli-blog.club/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/3lt2id24590781657704885285.jpeg!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="Tianli"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/3lt2id24590781657704885285.jpeg!cover_siteshot"
        />
        <div class="img-alt is-center">Tianli</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="Tianli"
        href="https://tianli-blog.club/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/XWoXiJ21390681623031453657.jpg!cover_mini"
            data-fancybox="images"
            data-caption="Tianli"
            class="fancybox"
            data-srcset="https://p.zhheo.com/XWoXiJ21390681623031453657.jpg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/XWoXiJ21390681623031453657.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Tianli"
                data-ll-status="loaded"
                src="https://p.zhheo.com/XWoXiJ21390681623031453657.jpg!cover_mini"
            /></a>
            <div class="img-alt is-center">Tianli</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">Tianli</span
            ><span
            class="desc"
            title="全栈开发工程师，TianliCDN公益项目发起人，大量后端技术干货"
            >全栈开发工程师，TianliCDN公益项目发起人，大量后端技术干货</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag">技术</span
        ><a
        class="img"
        target="_blank"
        title="Black Flies"
        href="https://www.yyyzyyyz.cn/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/UNgmTB20090581653028140854.jpg!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="Black Flies"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/UNgmTB20090581653028140854.jpg!cover_siteshot"
        />
        <div class="img-alt is-center">Black Flies</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="Black Flies"
        href="https://www.yyyzyyyz.cn/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/30KJu924491281638520724858.jpg!cover_mini"
            data-fancybox="images"
            data-caption="Black Flies"
            class="fancybox"
            data-srcset="https://p.zhheo.com/30KJu924491281638520724858.jpg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/30KJu924491281638520724858.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Black Flies"
                data-ll-status="loaded"
                src="https://p.zhheo.com/30KJu924491281638520724858.jpg!cover_mini"
            /></a>
            <div class="img-alt is-center">Black Flies</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">Black Flies</span
            ><span
            class="desc"
            title="全栈开发工程师，友链朋友圈项目开发者，技术入门分享博客"
            >全栈开发工程师，友链朋友圈项目开发者，技术入门分享博客</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag">技术</span
        ><a
        class="img"
        target="_blank"
        title="DORAKIKA"
        href="https://blog.dorakika.cn/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/xYfKY120390681654186803887.jpg!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="DORAKIKA"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/xYfKY120390681654186803887.jpg!cover_siteshot"
        />
        <div class="img-alt is-center">DORAKIKA</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="DORAKIKA"
        href="https://blog.dorakika.cn/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/mqaizf23990681654186719414.jpeg!cover_mini"
            data-fancybox="images"
            data-caption="DORAKIKA"
            class="fancybox"
            data-srcset="https://p.zhheo.com/mqaizf23990681654186719414.jpeg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/mqaizf23990681654186719414.jpeg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="DORAKIKA"
                data-ll-status="loaded"
                src="https://p.zhheo.com/mqaizf23990681654186719414.jpeg!cover_mini"
            /></a>
            <div class="img-alt is-center">DORAKIKA</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">DORAKIKA</span
            ><span class="desc" title="前端开发工程师，Butterfly魔改专家"
            >前端开发工程师，Butterfly魔改专家</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag vip">技术<i class="light"></i></span
        ><a
        class="img"
        target="_blank"
        title="Leonus"
        href="https://blog.leonus.cn/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/8fM9lC24490881660197764084.jpg!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="Leonus"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/8fM9lC24490881660197764084.jpg!cover_siteshot"
        />
        <div class="img-alt is-center">Leonus</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="Leonus"
        href="https://blog.leonus.cn/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/SfsTYH22691081664849306675.jpg!cover_mini"
            data-fancybox="images"
            data-caption="Leonus"
            class="fancybox"
            data-srcset="https://p.zhheo.com/SfsTYH22691081664849306675.jpg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/SfsTYH22691081664849306675.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Leonus"
                data-ll-status="loaded"
                src="https://p.zhheo.com/SfsTYH22691081664849306675.jpg!cover_mini"
            /></a>
            <div class="img-alt is-center">Leonus</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">Leonus</span
            ><span class="desc" title="前端开发工程师，Butterfly魔改专家"
            >前端开发工程师，Butterfly魔改专家</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag vip">技术<i class="light"></i></span
        ><a
        class="img"
        target="_blank"
        title="轻笑Chuckle"
        href="https://www.qcqx.cn/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/JlKuqq24590881660808625008.jpg!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="轻笑Chuckle"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/JlKuqq24590881660808625008.jpg!cover_siteshot"
        />
        <div class="img-alt is-center">轻笑Chuckle</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="轻笑Chuckle"
        href="https://www.qcqx.cn/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/0lEniY21190481681450391342.jpg!cover_mini"
            data-fancybox="images"
            data-caption="轻笑Chuckle"
            class="fancybox"
            data-srcset="https://p.zhheo.com/0lEniY21190481681450391342.jpg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/0lEniY21190481681450391342.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="轻笑Chuckle"
                data-ll-status="loaded"
                src="https://p.zhheo.com/0lEniY21190481681450391342.jpg!cover_mini"
            /></a>
            <div class="img-alt is-center">轻笑Chuckle</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">轻笑Chuckle</span
            ><span class="desc" title="前端开发工程师，Butterfly魔改专家"
            >前端开发工程师，Butterfly魔改专家</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag">技术</span
        ><a
        class="img"
        target="_blank"
        title="异次元de机智君"
        href="https://www.anzifan.com/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/GiBjJw23090881661239410602.jpg!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="异次元de机智君"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/GiBjJw23090881661239410602.jpg!cover_siteshot"
        />
        <div class="img-alt is-center">异次元de机智君</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="异次元de机智君"
        href="https://www.anzifan.com/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/yTZ1wq21990881660979779481.jpg!cover_mini"
            data-fancybox="images"
            data-caption="异次元de机智君"
            class="fancybox"
            data-srcset="https://p.zhheo.com/yTZ1wq21990881660979779481.jpg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/yTZ1wq21990881660979779481.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="异次元de机智君"
                data-ll-status="loaded"
                src="https://p.zhheo.com/yTZ1wq21990881660979779481.jpg!cover_mini"
            /></a>
            <div class="img-alt is-center">异次元de机智君</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">异次元de机智君</span
            ><span class="desc" title="前端开发工程师，优质Notion主题开发者"
            >前端开发工程师，优质Notion主题开发者</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag vip">技术<i class="light"></i></span
        ><a
        class="img"
        target="_blank"
        title="One"
        href="https://blog.closex.org"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/fJCEWd21890981662286758308.webp!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="One"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/fJCEWd21890981662286758308.webp!cover_siteshot"
        />
        <div class="img-alt is-center">One</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="One"
        href="https://blog.closex.org"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/uUxNRn24890981662286728042.png!cover_mini"
            data-fancybox="images"
            data-caption="One"
            class="fancybox"
            data-srcset="https://p.zhheo.com/uUxNRn24890981662286728042.png!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/uUxNRn24890981662286728042.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="One"
                data-ll-status="loaded"
                src="https://p.zhheo.com/uUxNRn24890981662286728042.png!cover_mini"
            /></a>
            <div class="img-alt is-center">One</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">One</span
            ><span class="desc" title="深度技术专家💎 英文原创🚀"
            >深度技术专家💎 英文原创🚀</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag vip">技术<i class="light"></i></span
        ><a
        class="img"
        target="_blank"
        title="安知鱼"
        href="https://blog.anheyu.com/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/2022d8aaa85e003815b7274b4d135adf1b9f283510.png!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="安知鱼"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/2022d8aaa85e003815b7274b4d135adf1b9f283510.png!cover_siteshot"
        />
        <div class="img-alt is-center">安知鱼</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="安知鱼"
        href="https://blog.anheyu.com/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/2agSs823390981662276333884.jpg!cover_mini"
            data-fancybox="images"
            data-caption="安知鱼"
            class="fancybox"
            data-srcset="https://p.zhheo.com/2agSs823390981662276333884.jpg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/2agSs823390981662276333884.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="安知鱼"
                data-ll-status="loaded"
                src="https://p.zhheo.com/2agSs823390981662276333884.jpg!cover_mini"
            /></a>
            <div class="img-alt is-center">安知鱼</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">安知鱼</span
            ><span class="desc" title="前端开发工程师，Butterfly魔改专家"
            >前端开发工程师，Butterfly魔改专家</span
            >
        </div></a
        >
    </div>
    <div class="site-card 生活">
        <span class="site-card-tag vip">生活<i class="light"></i></span
        ><a
        class="img"
        target="_blank"
        title="杜老师说"
        href="https://dusays.com/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/20232a3d7480ce441103fcef77a51e44c702013002.png!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="杜老师说"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/20232a3d7480ce441103fcef77a51e44c702013002.png!cover_siteshot"
        />
        <div class="img-alt is-center">杜老师说</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="杜老师说"
        href="https://dusays.com/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/2022343daeb6a541ee3f755638d49641045f215912.png!cover_mini"
            data-fancybox="images"
            data-caption="杜老师说"
            class="fancybox"
            data-srcset="https://p.zhheo.com/2022343daeb6a541ee3f755638d49641045f215912.png!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/2022343daeb6a541ee3f755638d49641045f215912.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="杜老师说"
                data-ll-status="loaded"
                src="https://p.zhheo.com/2022343daeb6a541ee3f755638d49641045f215912.png!cover_mini"
            /></a>
            <div class="img-alt is-center">杜老师说</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">杜老师说</span
            ><span
            class="desc"
            title="高级网络工程师，网站技术运营总监，系统运维、架构设计以及优化专家"
            >高级网络工程师，网站技术运营总监，系统运维、架构设计以及优化专家</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag">技术</span
        ><a
        class="img"
        target="_blank"
        title="山岳库博"
        href="https://kmar.top/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/q4Qq0P23490481681393714064.png!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="山岳库博"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/q4Qq0P23490481681393714064.png!cover_siteshot"
        />
        <div class="img-alt is-center">山岳库博</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="山岳库博"
        href="https://kmar.top/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/9LChx723790481649211637357.jpg!cover_mini"
            data-fancybox="images"
            data-caption="山岳库博"
            class="fancybox"
            data-srcset="https://p.zhheo.com/9LChx723790481649211637357.jpg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/9LChx723790481649211637357.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="山岳库博"
                data-ll-status="loaded"
                src="https://p.zhheo.com/9LChx723790481649211637357.jpg!cover_mini"
            /></a>
            <div class="img-alt is-center">山岳库博</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">山岳库博</span
            ><span class="desc" title="开发学习启发性二刺螈"
            >开发学习启发性二刺螈</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag">技术</span
        ><a
        class="img"
        target="_blank"
        title="三钻"
        href="https://tridiamond.tech"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/pObrdp23590881691978615238.png!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="三钻"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/pObrdp23590881691978615238.png!cover_siteshot"
        />
        <div class="img-alt is-center">三钻</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="三钻"
        href="https://tridiamond.tech"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/cuToQP20490881691978584862.png!cover_mini"
            data-fancybox="images"
            data-caption="三钻"
            class="fancybox"
            data-srcset="https://p.zhheo.com/cuToQP20490881691978584862.png!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/cuToQP20490881691978584862.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="三钻"
                data-ll-status="loaded"
                src="https://p.zhheo.com/cuToQP20490881691978584862.png!cover_mini"
            /></a>
            <div class="img-alt is-center">三钻</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">三钻</span
            ><span
            class="desc"
            title="Think like an artist, develop like an artisan."
            >Think like an artist, develop like an artisan.</span
            >
        </div></a
        >
    </div>
    <div class="site-card 生活">
        <span class="site-card-tag">生活</span
        ><a
        class="img"
        target="_blank"
        title="南方嘉木"
        href="https://blog.cancin.cn/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/HoVkwY23790781720160317515.png!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="南方嘉木"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/HoVkwY23790781720160317515.png!cover_siteshot"
        />
        <div class="img-alt is-center">南方嘉木</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="南方嘉木"
        href="https://blog.cancin.cn/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/2023ba5d41f53e024640a50f083bc35ffc9a271801.png!cover_mini"
            data-fancybox="images"
            data-caption="南方嘉木"
            class="fancybox"
            data-srcset="https://p.zhheo.com/2023ba5d41f53e024640a50f083bc35ffc9a271801.png!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/2023ba5d41f53e024640a50f083bc35ffc9a271801.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="南方嘉木"
                data-ll-status="loaded"
                src="https://p.zhheo.com/2023ba5d41f53e024640a50f083bc35ffc9a271801.png!cover_mini"
            /></a>
            <div class="img-alt is-center">南方嘉木</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">南方嘉木</span
            ><span class="desc" title="不畏将来，不念过往。"
            >不畏将来，不念过往。</span
            >
        </div></a
        >
    </div>
    <div class="site-card 生活">
        <span class="site-card-tag">生活</span
        ><a
        class="img"
        target="_blank"
        title="星辰日记"
        href="https://blog.xsot.cn/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/DUnmWW24990981727260789475.png!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="星辰日记"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/DUnmWW24990981727260789475.png!cover_siteshot"
        />
        <div class="img-alt is-center">星辰日记</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="星辰日记"
        href="https://blog.xsot.cn/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/4fN2mk21290981727260752974.png!cover_mini"
            data-fancybox="images"
            data-caption="星辰日记"
            class="fancybox"
            data-srcset="https://p.zhheo.com/4fN2mk21290981727260752974.png!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/4fN2mk21290981727260752974.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="星辰日记"
                data-ll-status="loaded"
                src="https://p.zhheo.com/4fN2mk21290981727260752974.png!cover_mini"
            /></a>
            <div class="img-alt is-center">星辰日记</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">星辰日记</span
            ><span class="desc" title="我已很久不再成为我自己"
            >我已很久不再成为我自己</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag vip">技术<i class="light"></i></span
        ><a
        class="img"
        target="_blank"
        title="小智の空间站"
        href="https://blog.cuixinyu.com/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/Kbr2GR21190581684724951703.jpg!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="小智の空间站"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/Kbr2GR21190581684724951703.jpg!cover_siteshot"
        />
        <div class="img-alt is-center">小智の空间站</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="小智の空间站"
        href="https://blog.cuixinyu.com/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/Lw31mF20490681686542824945.jpg!cover_mini"
            data-fancybox="images"
            data-caption="小智の空间站"
            class="fancybox"
            data-srcset="https://p.zhheo.com/Lw31mF20490681686542824945.jpg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/Lw31mF20490681686542824945.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="小智の空间站"
                data-ll-status="loaded"
                src="https://p.zhheo.com/Lw31mF20490681686542824945.jpg!cover_mini"
            /></a>
            <div class="img-alt is-center">小智の空间站</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">小智の空间站</span
            ><span class="desc" title="记录学习踩坑">记录学习踩坑</span>
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag vip">技术<i class="light"></i></span
        ><a
        class="img"
        target="_blank"
        title="御网尚书"
        href="https://www.hack-gov.com.cn/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/xNsxEx21390481682175493528.png!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="御网尚书"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/xNsxEx21390481682175493528.png!cover_siteshot"
        />
        <div class="img-alt is-center">御网尚书</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="御网尚书"
        href="https://www.hack-gov.com.cn/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/J63Ohw23490481682175454831.jpg!cover_mini"
            data-fancybox="images"
            data-caption="御网尚书"
            class="fancybox"
            data-srcset="https://p.zhheo.com/J63Ohw23490481682175454831.jpg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/J63Ohw23490481682175454831.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="御网尚书"
                data-ll-status="loaded"
                src="https://p.zhheo.com/J63Ohw23490481682175454831.jpg!cover_mini"
            /></a>
            <div class="img-alt is-center">御网尚书</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">御网尚书</span
            ><span
            class="desc"
            title="这有关于计算机网络安全、信息安全、心理学相关的知识，还有利用安全技术打击网络犯罪的内容分享和解读。"
            >这有关于计算机网络安全、信息安全、心理学相关的知识，还有利用安全技术打击网络犯罪的内容分享和解读。</span
            >
        </div></a
        >
    </div>
    <div class="site-card 生活">
        <span class="site-card-tag vip">生活<i class="light"></i></span
        ><a
        class="img"
        target="_blank"
        title="陈束"
        href="https://pellucid.art/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/qXIpd024290881692182442018.png!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="陈束"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/qXIpd024290881692182442018.png!cover_siteshot"
        />
        <div class="img-alt is-center">陈束</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="陈束"
        href="https://pellucid.art/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/a6XgCR25790881692182397968.png!cover_mini"
            data-fancybox="images"
            data-caption="陈束"
            class="fancybox"
            data-srcset="https://p.zhheo.com/a6XgCR25790881692182397968.png!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/a6XgCR25790881692182397968.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="陈束"
                data-ll-status="loaded"
                src="https://p.zhheo.com/a6XgCR25790881692182397968.png!cover_mini"
            /></a>
            <div class="img-alt is-center">陈束</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">陈束</span
            ><span class="desc" title="欲买桂花同载酒，终不似，少年游。"
            >欲买桂花同载酒，终不似，少年游。</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag vip">技术<i class="light"></i></span
        ><a
        class="img"
        target="_blank"
        title="六月是只猫"
        href="https://www.lyszm.com/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/HTbEDz25990381709622359388.webp!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="六月是只猫"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/HTbEDz25990381709622359388.webp!cover_siteshot"
        />
        <div class="img-alt is-center">六月是只猫</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="六月是只猫"
        href="https://www.lyszm.com/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/WLwD6L21691281703383276323.png!cover_mini"
            data-fancybox="images"
            data-caption="六月是只猫"
            class="fancybox"
            data-srcset="https://p.zhheo.com/WLwD6L21691281703383276323.png!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/WLwD6L21691281703383276323.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="六月是只猫"
                data-ll-status="loaded"
                src="https://p.zhheo.com/WLwD6L21691281703383276323.png!cover_mini"
            /></a>
            <div class="img-alt is-center">六月是只猫</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">六月是只猫</span
            ><span class="desc" title="生活，一半家长里短，一半山川湖海…"
            >生活，一半家长里短，一半山川湖海…</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag vip">技术<i class="light"></i></span
        ><a
        class="img"
        target="_blank"
        title="伍十七"
        href="https://blog.everfu.cn/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/bjJkPm22790481712469567696.png!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="伍十七"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/bjJkPm22790481712469567696.png!cover_siteshot"
        />
        <div class="img-alt is-center">伍十七</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="伍十七"
        href="https://blog.everfu.cn/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/ux0kIi22991081728380609610.png!cover_mini"
            data-fancybox="images"
            data-caption="伍十七"
            class="fancybox"
            data-srcset="https://p.zhheo.com/ux0kIi22991081728380609610.png!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/ux0kIi22991081728380609610.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="伍十七"
                data-ll-status="loaded"
                src="https://p.zhheo.com/ux0kIi22991081728380609610.png!cover_mini"
            /></a>
            <div class="img-alt is-center">伍十七</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">伍十七</span
            ><span
            class="desc"
            title="我是一名正在上大一的前端爱好者，专注于构建优秀的应用程序。"
            >我是一名正在上大一的前端爱好者，专注于构建优秀的应用程序。</span
            >
        </div></a
        >
    </div>
    <div class="site-card 生活">
        <span class="site-card-tag vip">生活<i class="light"></i></span
        ><a
        class="img"
        target="_blank"
        title="ImQi1"
        href="https://imqi1.com/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/cL1Sfy21690481682067736817.png!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="ImQi1"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/cL1Sfy21690481682067736817.png!cover_siteshot"
        />
        <div class="img-alt is-center">ImQi1</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="ImQi1"
        href="https://imqi1.com/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/AlHts524090481711968040077.png!cover_mini"
            data-fancybox="images"
            data-caption="ImQi1"
            class="fancybox"
            data-srcset="https://p.zhheo.com/AlHts524090481711968040077.png!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/AlHts524090481711968040077.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="ImQi1"
                data-ll-status="loaded"
                src="https://p.zhheo.com/AlHts524090481711968040077.png!cover_mini"
            /></a>
            <div class="img-alt is-center">ImQi1</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">ImQi1</span
            ><span class="desc" title="综合个人博客，主要分享技术"
            >综合个人博客，主要分享技术</span
            >
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag vip">技术<i class="light"></i></span
        ><a
        class="img"
        target="_blank"
        title="刘洪亮"
        href="https://lhliang.com/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/QNLIze24490781688438564717.jpg!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="刘洪亮"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/QNLIze24490781688438564717.jpg!cover_siteshot"
        />
        <div class="img-alt is-center">刘洪亮</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="刘洪亮"
        href="https://lhliang.com/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/yBL3GR23190581683172711460.jpg!cover_mini"
            data-fancybox="images"
            data-caption="刘洪亮"
            class="fancybox"
            data-srcset="https://p.zhheo.com/yBL3GR23190581683172711460.jpg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/yBL3GR23190581683172711460.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="刘洪亮"
                data-ll-status="loaded"
                src="https://p.zhheo.com/yBL3GR23190581683172711460.jpg!cover_mini"
            /></a>
            <div class="img-alt is-center">刘洪亮</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">刘洪亮</span
            ><span class="desc" title="不忘初心，方得始终">不忘初心，方得始终</span>
        </div></a
        >
    </div>
    <div class="site-card 技术">
        <span class="site-card-tag vip">技术<i class="light"></i></span
        ><a
        class="img"
        target="_blank"
        title="小N同学"
        href="https://www.imcharon.com/"
        rel="external nofollow"
        ><img
            class="flink-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/shfjy022990681655435429493.jpg!cover_siteshot"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="小N同学"
            style="pointer-events: none"
            data-ll-status="loaded"
            src="https://p.zhheo.com/shfjy022990681655435429493.jpg!cover_siteshot"
        />
        <div class="img-alt is-center">小N同学</div></a
        ><a
        class="info cf-friends-link"
        target="_blank"
        title="小N同学"
        href="https://www.imcharon.com/"
        rel="external nofollow"
        ><div class="site-card-avatar">
            <a
            href="https://p.zhheo.com/buYgVO22990681624844309044.jpg!cover_mini"
            data-fancybox="images"
            data-caption="小N同学"
            class="fancybox"
            data-srcset="https://p.zhheo.com/buYgVO22990681624844309044.jpg!cover_mini 1600w"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/buYgVO22990681624844309044.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="小N同学"
                data-ll-status="loaded"
                src="https://p.zhheo.com/buYgVO22990681624844309044.jpg!cover_mini"
            /></a>
            <div class="img-alt is-center">小N同学</div>
        </div>
        <div class="site-card-text">
            <span class="title cf-friends-name">小N同学</span
            ><span class="desc" title="运维工程师，大量技术干货文章"
            >运维工程师，大量技术干货文章</span
            >
        </div></a
        >
    </div>
    </div>

    '''

    # 解析HTML
    soup = BeautifulSoup(html_content, 'lxml')
    # 找到所有.site-card元素
    site_cards = soup.find_all('div', class_='site-card')


    # 遍历每个.site-card元素
    for card in site_cards:
        # 提取信息
        tag = card.find('span', class_='site-card-tag').text
        name = card.find('span', class_='title cf-friends-name').text
        link = card.find('a', class_='info cf-friends-link')['href']
        avatar = card.find('img', class_='flink-avatar cf-friends-avatar entered loaded')['src']
        descr = card.find('span', class_='desc').text
        siteshot = card.find('img', class_='flink-avatar entered loaded')['src']
        color = 'speed'  # 这个值是固定的，直接赋值

        # 输出结果
        result = f'''
        - name: {name}
        link: {link}
        avatar: {avatar}
        descr: {descr}
        siteshot: {siteshot}
        tag: {tag}
        color: {color}
        recommend:
        '''

        print(result)


def jishu():
    html_content = '''
    <div class="flink-list">
        <div class="flink-list-item 生活">
            <span class="site-card-tag vip">生活<i class="light"></i></span
            ><a
            class="cf-friends-link"
            href="https://www.pptwiki.com/"
            rel="external nofollow"
            title="PPT百科"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/msbg5a21491081730170214492.webp!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="PPT百科"
                data-ll-status="loaded"
                src="https://p.zhheo.com/msbg5a21491081730170214492.webp!cover_mini"
            />
            <div class="img-alt is-center">PPT百科</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">PPT百科</span
                ><span
                class="flink-item-desc"
                title="PPT百科网站为用户提供各类免费的PPT模板下载服务，包含PPT背景图,PPT素材,PPT背景,PPT可见,PPT定制免费PPT模板下载等。致力于提高职场人士制作PPT效率。免费下载的PPT模板类型涵盖工作汇报、营销策划、老师教学课件、商业计划书、医学医疗、竞聘述职等类型幻灯片"
                >PPT百科网站为用户提供各类免费的PPT模板下载服务，包含PPT背景图,PPT素材,PPT背景,PPT可见,PPT定制免费PPT模板下载等。致力于提高职场人士制作PPT效率。免费下载的PPT模板类型涵盖工作汇报、营销策划、老师教学课件、商业计划书、医学医疗、竞聘述职等类型幻灯片</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item 发电">
            <span class="site-card-tag vip">发电<i class="light"></i></span
            ><a
            class="cf-friends-link"
            href="https://blog.ciraos.top/"
            rel="external nofollow"
            title="葱苓"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/M81kOO22290681654830382223.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="葱苓"
                data-ll-status="loaded"
                src="https://p.zhheo.com/M81kOO22290681654830382223.jpg!cover_mini"
            />
            <div class="img-alt is-center">葱苓</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">葱苓</span
                ><span class="flink-item-desc" title="DARE &amp; DO"
                >DARE &amp; DO</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item 发电">
            <span class="site-card-tag">发电</span
            ><a
            class="cf-friends-link"
            href="https://blog.sakura.vin/"
            rel="external nofollow"
            title="樱花小镇"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/a19JmO21590981663034175438.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="樱花小镇"
                data-ll-status="loaded"
                src="https://p.zhheo.com/a19JmO21590981663034175438.png!cover_mini"
            />
            <div class="img-alt is-center">樱花小镇</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">樱花小镇</span
                ><span class="flink-item-desc" title="小园新种红樱树，闲绕花枝便当游。"
                >小园新种红樱树，闲绕花枝便当游。</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item 发电">
            <span class="site-card-tag">发电</span
            ><a
            class="cf-friends-link"
            href="https://www.furlary.com"
            rel="external nofollow"
            title="Furry·云迹工作室"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/vB6ElO25790781688867337717.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Furry·云迹工作室"
                data-ll-status="loaded"
                src="https://p.zhheo.com/vB6ElO25790781688867337717.jpg!cover_mini"
            />
            <div class="img-alt is-center">Furry·云迹工作室</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Furry·云迹工作室</span
                ><span class="flink-item-desc" title="FurLibrary社区论坛"
                >FurLibrary社区论坛</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item 发电">
            <span class="site-card-tag">发电</span
            ><a
            class="cf-friends-link"
            href="https://blog.moyuql.top/"
            rel="external nofollow"
            title="MoyuqL"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/pNCzbg25390581714701953709.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="MoyuqL"
                data-ll-status="loaded"
                src="https://p.zhheo.com/pNCzbg25390581714701953709.png!cover_mini"
            />
            <div class="img-alt is-center">MoyuqL</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">MoyuqL</span
                ><span class="flink-item-desc" title="MoyuqL与你同在~"
                >MoyuqL与你同在~</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item 发电">
            <span class="site-card-tag">发电</span
            ><a
            class="cf-friends-link"
            href="https://blog.haiskyblog.top/"
            rel="external nofollow"
            title="Haisky"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/DFB9If23890481681696478453.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Haisky"
                data-ll-status="loaded"
                src="https://p.zhheo.com/DFB9If23890481681696478453.jpg!cover_mini"
            />
            <div class="img-alt is-center">Haisky</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Haisky</span
                ><span
                class="flink-item-desc"
                title="这有关于开发、技术相关的问题和看法，还有对于动漫的一些杂评。"
                >这有关于开发、技术相关的问题和看法，还有对于动漫的一些杂评。</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item 发电">
            <span class="site-card-tag">发电</span
            ><a
            class="cf-friends-link"
            href="https://tangmv.cn/"
            rel="external nofollow"
            title="汤木的幻想乡"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/WVMxAO20590281709005505509.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="汤木的幻想乡"
                data-ll-status="loaded"
                src="https://p.zhheo.com/WVMxAO20590281709005505509.png!cover_mini"
            />
            <div class="img-alt is-center">汤木的幻想乡</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">汤木的幻想乡</span
                ><span class="flink-item-desc" title="扣首问路，码梦为生。"
                >扣首问路，码梦为生。</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.ccknbc.cc/"
            rel="external nofollow"
            title="CC康纳百川"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/22377a1f636487acccc99b7e603c11c973f49f58.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="CC康纳百川"
                data-ll-status="loaded"
                src="https://p.zhheo.com/22377a1f636487acccc99b7e603c11c973f49f58.png!cover_mini"
            />
            <div class="img-alt is-center">CC康纳百川</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">CC康纳百川</span
                ><span class="flink-item-desc" title="一个无趣的人">一个无趣的人</span>
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.2broear.com/"
            rel="external nofollow"
            title="2broear"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/BvXh9L24090481618971460104.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="2broear"
                data-ll-status="loaded"
                src="https://p.zhheo.com/BvXh9L24090481618971460104.png!cover_mini"
            />
            <div class="img-alt is-center">2broear</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">2broear</span
                ><span
                class="flink-item-desc"
                title="记录生活，分享生活，兴趣指引方向，会玩才会学"
                >记录生活，分享生活，兴趣指引方向，会玩才会学</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.vian.top/"
            rel="external nofollow"
            title="vian"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/ok2bDj23890481648808738532.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="vian"
                data-ll-status="loaded"
                src="https://p.zhheo.com/ok2bDj23890481648808738532.jpg!cover_mini"
            />
            <div class="img-alt is-center">vian</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">vian</span
                ><span class="flink-item-desc" title="想要的都拥有 得不到的都释怀"
                >想要的都拥有 得不到的都释怀</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item HA">
            <span class="site-card-tag">HA</span
            ><a
            class="cf-friends-link"
            href="https://blog.linsnow.cn/"
            rel="external nofollow"
            title="L1nSn0w"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/VE2SdE21990681654261399825.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="L1nSn0w"
                data-ll-status="loaded"
                src="https://p.zhheo.com/VE2SdE21990681654261399825.jpg!cover_mini"
            />
            <div class="img-alt is-center">L1nSn0w</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">L1nSn0w</span
                ><span class="flink-item-desc" title="我很菜，你忍一下"
                >我很菜，你忍一下</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://huangzz.xyz/"
            rel="external nofollow"
            title="No.9537"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/WXVoWj23290481650863852414.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="No.9537"
                data-ll-status="loaded"
                src="https://p.zhheo.com/WXVoWj23290481650863852414.jpg!cover_mini"
            />
            <div class="img-alt is-center">No.9537</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">No.9537</span
                ><span
                class="flink-item-desc"
                title="Yep, another mini daily blog here."
                >Yep, another mini daily blog here.</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item HA">
            <span class="site-card-tag">HA</span
            ><a
            class="cf-friends-link"
            href="https://www.rz.sb/"
            rel="external nofollow"
            title="若志随笔"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/mC1sqW21190781625814671716.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="若志随笔"
                data-ll-status="loaded"
                src="https://p.zhheo.com/mC1sqW21190781625814671716.jpg!cover_mini"
            />
            <div class="img-alt is-center">若志随笔</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">若志随笔</span
                ><span class="flink-item-desc" title="记点想记的东西，做点想做的事情"
                >记点想记的东西，做点想做的事情</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://eallion.com/"
            rel="external nofollow"
            title="大大的小蜗牛"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/cACotY25990681624260179168.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="大大的小蜗牛"
                data-ll-status="loaded"
                src="https://p.zhheo.com/cACotY25990681624260179168.jpg!cover_mini"
            />
            <div class="img-alt is-center">大大的小蜗牛</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">大大的小蜗牛</span
                ><span class="flink-item-desc" title="机会总是垂青于有准备的人！"
                >机会总是垂青于有准备的人！</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.hin.cool/"
            rel="external nofollow"
            title="W4J1e"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/R7X8vA22790681624844247504.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="W4J1e"
                data-ll-status="loaded"
                src="https://p.zhheo.com/R7X8vA22790681624844247504.jpg!cover_mini"
            />
            <div class="img-alt is-center">W4J1e</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">W4J1e</span
                ><span class="flink-item-desc" title="偏爱不务正业">偏爱不务正业</span>
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://nikoblog.top/"
            rel="external nofollow"
            title="Niko"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/EPqrlB23590181643178575328.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Niko"
                data-ll-status="loaded"
                src="https://p.zhheo.com/EPqrlB23590181643178575328.jpg!cover_mini"
            />
            <div class="img-alt is-center">Niko</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Niko</span
                ><span class="flink-item-desc" title="一个不务正业的小学生"
                >一个不务正业的小学生</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://snow.js.org/"
            rel="external nofollow"
            title="小林书架"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/PfPpi424990781657508689165.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="小林书架"
                data-ll-status="loaded"
                src="https://p.zhheo.com/PfPpi424990781657508689165.jpg!cover_mini"
            />
            <div class="img-alt is-center">小林书架</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">小林书架</span
                ><span class="flink-item-desc" title="Creator &amp; OIer"
                >Creator &amp; OIer</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://easyf12.top/"
            rel="external nofollow"
            title="一蓑烟雨"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/m45U5l21890781657986918059.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="一蓑烟雨"
                data-ll-status="loaded"
                src="https://p.zhheo.com/m45U5l21890781657986918059.jpg!cover_mini"
            />
            <div class="img-alt is-center">一蓑烟雨</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">一蓑烟雨</span
                ><span
                class="flink-item-desc"
                title="竹杖芒鞋轻胜马，谁怕？一蓑烟雨任平生。"
                >竹杖芒鞋轻胜马，谁怕？一蓑烟雨任平生。</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.heart-of-engine.top/"
            rel="external nofollow"
            title="Heart-of-engine"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/uARRaH24290181611238902309.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Heart-of-engine"
                data-ll-status="loaded"
                src="https://p.zhheo.com/uARRaH24290181611238902309.jpg!cover_mini"
            />
            <div class="img-alt is-center">Heart-of-engine</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Heart-of-engine</span
                ><span
                class="flink-item-desc"
                title="专注于数学与编程的完美结合,分享生活,分享知识"
                >专注于数学与编程的完美结合,分享生活,分享知识</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://yujie.pro/"
            rel="external nofollow"
            title="夜灭"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/n2GOxQ21390781658916193439.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="夜灭"
                data-ll-status="loaded"
                src="https://p.zhheo.com/n2GOxQ21390781658916193439.jpg!cover_mini"
            />
            <div class="img-alt is-center">夜灭</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">夜灭</span
                ><span
                class="flink-item-desc"
                title="夜灭的小窝，谈天说地热爱二次元且会写bug"
                >夜灭的小窝，谈天说地热爱二次元且会写bug</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item HA">
            <span class="site-card-tag">HA</span
            ><a
            class="cf-friends-link"
            href="http://www.lg3000.top/"
            rel="external nofollow"
            title="立更情报"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/rbzCNf21590781627611075921.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="立更情报"
                data-ll-status="loaded"
                src="https://p.zhheo.com/rbzCNf21590781627611075921.jpg!cover_mini"
            />
            <div class="img-alt is-center">立更情报</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">立更情报</span
                ><span class="flink-item-desc" title="学会享受没用的愉悦"
                >学会享受没用的愉悦</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.imcao.cn/"
            rel="external nofollow"
            title="ImCaO"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/zHHCd024190281645408061931.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="ImCaO"
                data-ll-status="loaded"
                src="https://p.zhheo.com/zHHCd024190281645408061931.jpg!cover_mini"
            />
            <div class="img-alt is-center">ImCaO</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">ImCaO</span
                ><span class="flink-item-desc" title="花有重开日，人无再少年。"
                >花有重开日，人无再少年。</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.joyer.top/"
            rel="external nofollow"
            title="Joyer"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/hJtlu222490481650863664546.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Joyer"
                data-ll-status="loaded"
                src="https://p.zhheo.com/hJtlu222490481650863664546.jpg!cover_mini"
            />
            <div class="img-alt is-center">Joyer</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Joyer</span
                ><span class="flink-item-desc" title="一只会唱Lahee~的龙"
                >一只会唱Lahee~的龙</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://imbhj.com/"
            rel="external nofollow"
            title="Ordis"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/0DSUf223090381614569730788.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Ordis"
                data-ll-status="loaded"
                src="https://p.zhheo.com/0DSUf223090381614569730788.png!cover_mini"
            />
            <div class="img-alt is-center">Ordis</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Ordis</span
                ><span class="flink-item-desc" title="OrdisBlog">OrdisBlog</span>
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://0skyu.cn/"
            rel="external nofollow"
            title="零域"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/grq5YF23390681624259613396.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="零域"
                data-ll-status="loaded"
                src="https://p.zhheo.com/grq5YF23390681624259613396.jpg!cover_mini"
            />
            <div class="img-alt is-center">零域</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">零域</span
                ><span class="flink-item-desc" title="Pin Young的笔记小屋"
                >Pin Young的笔记小屋</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="http://www.cq.qcwy.org.cn"
            rel="external nofollow"
            title="长情"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/9d51b1822d7fd0a96b6137ce650206d9612c7427.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="长情"
                data-ll-status="loaded"
                src="https://p.zhheo.com/9d51b1822d7fd0a96b6137ce650206d9612c7427.jpg!cover_mini"
            />
            <div class="img-alt is-center">长情</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">长情</span
                ><span class="flink-item-desc" title="你相信什么，你就看到什么"
                >你相信什么，你就看到什么</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.sunguoqi.com/"
            rel="external nofollow"
            title="小孙同学"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/mF789723990881630316499898.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="小孙同学"
                data-ll-status="loaded"
                src="https://p.zhheo.com/mF789723990881630316499898.jpg!cover_mini"
            />
            <div class="img-alt is-center">小孙同学</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">小孙同学</span
                ><span class="flink-item-desc" title="热爱可抵漫长岁月！"
                >热爱可抵漫长岁月！</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.linkkk.top/"
            rel="external nofollow"
            title="linkkk"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/7yPEzH23690781658303016410.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="linkkk"
                data-ll-status="loaded"
                src="https://p.zhheo.com/7yPEzH23690781658303016410.jpg!cover_mini"
            />
            <div class="img-alt is-center">linkkk</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">linkkk</span
                ><span class="flink-item-desc" title="一个摸鱼初中生的博客"
                >一个摸鱼初中生的博客</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item HA">
            <span class="site-card-tag">HA</span
            ><a
            class="cf-friends-link"
            href="https://myblog.wallleap.cn/"
            rel="external nofollow"
            title="wallleap"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/0YmKuM24890381647241308636.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="wallleap"
                data-ll-status="loaded"
                src="https://p.zhheo.com/0YmKuM24890381647241308636.jpg!cover_mini"
            />
            <div class="img-alt is-center">wallleap</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">wallleap</span
                ><span class="flink-item-desc" title="Luwang’s Blog"
                >Luwang’s Blog</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.wmza.cn/"
            rel="external nofollow"
            title="Wlog"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/62m40A20890981662276368925.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Wlog"
                data-ll-status="loaded"
                src="https://p.zhheo.com/62m40A20890981662276368925.jpg!cover_mini"
            />
            <div class="img-alt is-center">Wlog</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Wlog</span
                ><span class="flink-item-desc" title="一个普通人">一个普通人</span>
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://kkfw.vercel.app/"
            rel="external nofollow"
            title="Seeker"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/0b2ba60e4b45bdcb4f832c6b8e68c4692e4f3148.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Seeker"
                data-ll-status="loaded"
                src="https://p.zhheo.com/0b2ba60e4b45bdcb4f832c6b8e68c4692e4f3148.jpg!cover_mini"
            />
            <div class="img-alt is-center">Seeker</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Seeker</span
                ><span class="flink-item-desc" title="九死南荒吾不恨，兹游奇绝冠平生"
                >九死南荒吾不恨，兹游奇绝冠平生</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://wrans.top"
            rel="external nofollow"
            title="Wayne"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/2023f1de4958f6bd8c04b1a1d965a96f9a96074401.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Wayne"
                data-ll-status="loaded"
                src="https://p.zhheo.com/2023f1de4958f6bd8c04b1a1d965a96f9a96074401.png!cover_mini"
            />
            <div class="img-alt is-center">Wayne</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Wayne</span
                ><span class="flink-item-desc" title="以梦为马，不负韶华"
                >以梦为马，不负韶华</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://foolishfox.cn/"
            rel="external nofollow"
            title="FF"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/Yc6OnM20290581621328642805.jpeg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="FF"
                data-ll-status="loaded"
                src="https://p.zhheo.com/Yc6OnM20290581621328642805.jpeg!cover_mini"
            />
            <div class="img-alt is-center">FF</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">FF</span
                ><span class="flink-item-desc" title="foolish fox">foolish fox</span>
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.happyking.top/"
            rel="external nofollow"
            title="欢乐小王"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/uxhmQQ23490481649727934824.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="欢乐小王"
                data-ll-status="loaded"
                src="https://p.zhheo.com/uxhmQQ23490481649727934824.jpg!cover_mini"
            />
            <div class="img-alt is-center">欢乐小王</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">欢乐小王</span
                ><span class="flink-item-desc" title="聚散无常,别来无恙"
                >聚散无常,别来无恙</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://siax.cn/"
            rel="external nofollow"
            title="Sianx"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/etu0Gb20290981632480242474.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Sianx"
                data-ll-status="loaded"
                src="https://p.zhheo.com/etu0Gb20290981632480242474.jpg!cover_mini"
            />
            <div class="img-alt is-center">Sianx</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Sianx</span
                ><span class="flink-item-desc" title="总之岁月漫长, 然而值得等待。"
                >总之岁月漫长, 然而值得等待。</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.nbplus.eu.org/"
            rel="external nofollow"
            title="晴雀堂"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/202363ece52dc1370b657dcb54986ebe576d071002.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="晴雀堂"
                data-ll-status="loaded"
                src="https://p.zhheo.com/202363ece52dc1370b657dcb54986ebe576d071002.png!cover_mini"
            />
            <div class="img-alt is-center">晴雀堂</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">晴雀堂</span
                ><span class="flink-item-desc" title="一位普通的学牲在记录自己的生活"
                >一位普通的学牲在记录自己的生活</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.blatr.cn/"
            rel="external nofollow"
            title="青灯暮雨"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/w9wZSK25890881661238598833.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="青灯暮雨"
                data-ll-status="loaded"
                src="https://p.zhheo.com/w9wZSK25890881661238598833.jpg!cover_mini"
            />
            <div class="img-alt is-center">青灯暮雨</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">青灯暮雨</span
                ><span class="flink-item-desc" title="再渺小的星光，也有属于它的光芒"
                >再渺小的星光，也有属于它的光芒</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://penghh.fun/"
            rel="external nofollow"
            title="效率工具指南"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/eJmyW824490881661623784172.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="效率工具指南"
                data-ll-status="loaded"
                src="https://p.zhheo.com/eJmyW824490881661623784172.jpg!cover_mini"
            />
            <div class="img-alt is-center">效率工具指南</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">效率工具指南</span
                ><span class="flink-item-desc" title="分享推荐效率工具及用法介绍"
                >分享推荐效率工具及用法介绍</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://shiyu.dev/"
            rel="external nofollow"
            title="云烟成雨"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/ypskpS24090981662344080020.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="云烟成雨"
                data-ll-status="loaded"
                src="https://p.zhheo.com/ypskpS24090981662344080020.jpg!cover_mini"
            />
            <div class="img-alt is-center">云烟成雨</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">云烟成雨</span
                ><span class="flink-item-desc" title="越走越漫长的林经"
                >越走越漫长的林经</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://cworld0.com/"
            rel="external nofollow"
            title="CWorld"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/yDZFbo20490981662344164941.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="CWorld"
                data-ll-status="loaded"
                src="https://p.zhheo.com/yDZFbo20490981662344164941.jpg!cover_mini"
            />
            <div class="img-alt is-center">CWorld</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">CWorld</span
                ><span class="flink-item-desc" title="求知若愚，虚怀若谷"
                >求知若愚，虚怀若谷</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.xukaiyyds.cn/"
            rel="external nofollow"
            title="XK"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/WXYSxm22790981663811727723.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="XK"
                data-ll-status="loaded"
                src="https://p.zhheo.com/WXYSxm22790981663811727723.jpg!cover_mini"
            />
            <div class="img-alt is-center">XK</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">XK</span
                ><span class="flink-item-desc" title="一个干净整洁的个人博客"
                >一个干净整洁的个人博客</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.zerolacqua.top/"
            rel="external nofollow"
            title="丘卡饮品店"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/qZmuNO23990981664504559569.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="丘卡饮品店"
                data-ll-status="loaded"
                src="https://p.zhheo.com/qZmuNO23990981664504559569.jpg!cover_mini"
            />
            <div class="img-alt is-center">丘卡饮品店</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">丘卡饮品店</span
                ><span class="flink-item-desc" title="要来点喝的吗？"
                >要来点喝的吗？</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://study.hycbook.com/"
            rel="external nofollow"
            title="兼一书虫"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/qoSs4Q20891081665390728276.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="兼一书虫"
                data-ll-status="loaded"
                src="https://p.zhheo.com/qoSs4Q20891081665390728276.jpg!cover_mini"
            />
            <div class="img-alt is-center">兼一书虫</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">兼一书虫</span
                ><span
                class="flink-item-desc"
                title="知足且上进，温柔而坚定，生活中的温暖总会与你不期而遇。"
                >知足且上进，温柔而坚定，生活中的温暖总会与你不期而遇。</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://ichika.cc/"
            rel="external nofollow"
            title="ichika"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/L5vJoz22291081666059922606.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="ichika"
                data-ll-status="loaded"
                src="https://p.zhheo.com/L5vJoz22291081666059922606.jpg!cover_mini"
            />
            <div class="img-alt is-center">ichika</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">ichika</span
                ><span class="flink-item-desc" title="Hello,gamer!">Hello,gamer!</span>
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://mrxiaohu.cn/"
            rel="external nofollow"
            title="隔壁小胡"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/2022e7980c2f63419ea91879c84f70e579c5211610.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="隔壁小胡"
                data-ll-status="loaded"
                src="https://p.zhheo.com/2022e7980c2f63419ea91879c84f70e579c5211610.png!cover_mini"
            />
            <div class="img-alt is-center">隔壁小胡</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">隔壁小胡</span
                ><span
                class="flink-item-desc"
                title="回首往事时，不因虚度年华而悔恨，也不因碌碌无为而羞愧。"
                >回首往事时，不因虚度年华而悔恨，也不因碌碌无为而羞愧。</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://202271.xyz/"
            rel="external nofollow"
            title="醉里"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/2022287aa967141f619ea07b3ca1187aec2d054612.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="醉里"
                data-ll-status="loaded"
                src="https://p.zhheo.com/2022287aa967141f619ea07b3ca1187aec2d054612.png!cover_mini"
            />
            <div class="img-alt is-center">醉里</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">醉里</span
                ><span class="flink-item-desc" title="小豪的个人博客"
                >小豪的个人博客</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.xlenco.top/"
            rel="external nofollow"
            title="Xlenco"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/wS5wkq24190881661843441425.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Xlenco"
                data-ll-status="loaded"
                src="https://p.zhheo.com/wS5wkq24190881661843441425.jpg!cover_mini"
            />
            <div class="img-alt is-center">Xlenco</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Xlenco</span
                ><span
                class="flink-item-desc"
                title="最好的地方是没去过的地方，最好的时光，是回不来的时光。"
                >最好的地方是没去过的地方，最好的时光，是回不来的时光。</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item HA">
            <span class="site-card-tag">HA</span
            ><a
            class="cf-friends-link"
            href="https://www.leadwhite.net/"
            rel="external nofollow"
            title="leadwhite"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/JeNJaf22690781625133146612.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="leadwhite"
                data-ll-status="loaded"
                src="https://p.zhheo.com/JeNJaf22690781625133146612.jpg!cover_mini"
            />
            <div class="img-alt is-center">leadwhite</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">leadwhite</span
                ><span class="flink-item-desc" title="交互设计师，记录思考与生活"
                >交互设计师，记录思考与生活</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item HA">
            <span class="site-card-tag">HA</span
            ><a
            class="cf-friends-link"
            href="https://blog.skywt.cn/"
            rel="external nofollow"
            title="SkyWT"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/202214d97f4f77d725652876ded69f75365b274412.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="SkyWT"
                data-ll-status="loaded"
                src="https://p.zhheo.com/202214d97f4f77d725652876ded69f75365b274412.png!cover_mini"
            />
            <div class="img-alt is-center">SkyWT</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">SkyWT</span
                ><span class="flink-item-desc" title="我们的征途是星辰大海 ✨"
                >我们的征途是星辰大海 ✨</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.ganxb2.com/"
            rel="external nofollow"
            title="廿壴"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/2022abe384c951bcb1fe72b0bda07a71dd39281512.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="廿壴"
                data-ll-status="loaded"
                src="https://p.zhheo.com/2022abe384c951bcb1fe72b0bda07a71dd39281512.png!cover_mini"
            />
            <div class="img-alt is-center">廿壴</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">廿壴</span
                ><span
                class="flink-item-desc"
                title="探讨WEB技术.交流日常生活.感悟短暂人生.分享简单快乐"
                >探讨WEB技术.交流日常生活.感悟短暂人生.分享简单快乐</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.anjhon.top/"
            rel="external nofollow"
            title="Anjhon"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/202363f828e2d170f0c52acef8c9c5785659031001.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Anjhon"
                data-ll-status="loaded"
                src="https://p.zhheo.com/202363f828e2d170f0c52acef8c9c5785659031001.png!cover_mini"
            />
            <div class="img-alt is-center">Anjhon</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Anjhon</span
                ><span class="flink-item-desc" title="但知行好事，莫要问前程"
                >但知行好事，莫要问前程</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://678777.xyz/"
            rel="external nofollow"
            title="SLOVER"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/20234e938f5338ed524a9069557c5fff0fc9072401.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="SLOVER"
                data-ll-status="loaded"
                src="https://p.zhheo.com/20234e938f5338ed524a9069557c5fff0fc9072401.png!cover_mini"
            />
            <div class="img-alt is-center">SLOVER</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">SLOVER</span
                ><span class="flink-item-desc" title="诱导已亮，前方净空，祝君武运昌隆"
                >诱导已亮，前方净空，祝君武运昌隆</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://meuicat.com/"
            rel="external nofollow"
            title="爱吃肉的猫"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/Mg0wHM21790581685326817147.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="爱吃肉的猫"
                data-ll-status="loaded"
                src="https://p.zhheo.com/Mg0wHM21790581685326817147.jpg!cover_mini"
            />
            <div class="img-alt is-center">爱吃肉的猫</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">爱吃肉的猫</span
                ><span class="flink-item-desc" title="有肉有猫有生活"
                >有肉有猫有生活</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.neily.top/"
            rel="external nofollow"
            title="Neil"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/2023564599998cd95faee1c4f0b9a4863b6c125701.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Neil"
                data-ll-status="loaded"
                src="https://p.zhheo.com/2023564599998cd95faee1c4f0b9a4863b6c125701.png!cover_mini"
            />
            <div class="img-alt is-center">Neil</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Neil</span
                ><span class="flink-item-desc" title="咕咕咕！">咕咕咕！</span>
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://xiangming.site/"
            rel="external nofollow"
            title="湘铭呀！"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/20237c353298f88a40fefeb5f5322cbc411e313901.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="湘铭呀！"
                data-ll-status="loaded"
                src="https://p.zhheo.com/20237c353298f88a40fefeb5f5322cbc411e313901.png!cover_mini"
            />
            <div class="img-alt is-center">湘铭呀！</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">湘铭呀！</span
                ><span class="flink-item-desc" title="湘铭的秘密基地啊！"
                >湘铭的秘密基地啊！</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://flzzz.com/"
            rel="external nofollow"
            title="将心向明月"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/2023c96f7a6d008a792ab861094b468605a0010802.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="将心向明月"
                data-ll-status="loaded"
                src="https://p.zhheo.com/2023c96f7a6d008a792ab861094b468605a0010802.png!cover_mini"
            />
            <div class="img-alt is-center">将心向明月</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">将心向明月</span
                ><span class="flink-item-desc" title="专注收录有意思的软件和网站"
                >专注收录有意思的软件和网站</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://baili.tax/"
            rel="external nofollow"
            title="Baili"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/202344d8d8e22899ea9fa110ae31df94ae71102902.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Baili"
                data-ll-status="loaded"
                src="https://p.zhheo.com/202344d8d8e22899ea9fa110ae31df94ae71102902.png!cover_mini"
            />
            <div class="img-alt is-center">Baili</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Baili</span
                ><span class="flink-item-desc" title="一位只想找富婆而不想努力的人"
                >一位只想找富婆而不想努力的人</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.yt-blog.top/"
            rel="external nofollow"
            title="动荡の初二少年"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/2023280d829ddc8edc1721772d751ba3ba93102102.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="动荡の初二少年"
                data-ll-status="loaded"
                src="https://p.zhheo.com/2023280d829ddc8edc1721772d751ba3ba93102102.png!cover_mini"
            />
            <div class="img-alt is-center">动荡の初二少年</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">动荡の初二少年</span
                ><span class="flink-item-desc" title="一个少年的博客"
                >一个少年的博客</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.gan1ser.top/"
            rel="external nofollow"
            title="GanSer"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/Mr9oi622590481680840805606.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="GanSer"
                data-ll-status="loaded"
                src="https://p.zhheo.com/Mr9oi622590481680840805606.jpg!cover_mini"
            />
            <div class="img-alt is-center">GanSer</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">GanSer</span
                ><span class="flink-item-desc" title="紫箫吟断，素笺恨切"
                >紫箫吟断，素笺恨切</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://nur512.cn/"
            rel="external nofollow"
            title="努热木网"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/20239e8e9f55f27ef676e631fdaca9543f32115501.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="努热木网"
                data-ll-status="loaded"
                src="https://p.zhheo.com/20239e8e9f55f27ef676e631fdaca9543f32115501.png!cover_mini"
            />
            <div class="img-alt is-center">努热木网</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">努热木网</span
                ><span
                class="flink-item-desc"
                title="分享网站源码，资源，软件，技术，知识等"
                >分享网站源码，资源，软件，技术，知识等</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item HA">
            <span class="site-card-tag">HA</span
            ><a
            class="cf-friends-link"
            href="https://llx.life/"
            rel="external nofollow"
            title="陆陆侠"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/20237eda7de7070cee21d2d60540dade1359232702.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="陆陆侠"
                data-ll-status="loaded"
                src="https://p.zhheo.com/20237eda7de7070cee21d2d60540dade1359232702.png!cover_mini"
            />
            <div class="img-alt is-center">陆陆侠</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">陆陆侠</span
                ><span class="flink-item-desc" title="安安，这里是陆陆侠的生活~"
                >安安，这里是陆陆侠的生活~</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://zhuiguang.ren/"
            rel="external nofollow"
            title="追光人"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/2023c5f1e7bb515ffa1ef863c06de0fdae0c241102.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="追光人"
                data-ll-status="loaded"
                src="https://p.zhheo.com/2023c5f1e7bb515ffa1ef863c06de0fdae0c241102.png!cover_mini"
            />
            <div class="img-alt is-center">追光人</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">追光人</span
                ><span class="flink-item-desc" title="追寻生活的炽热"
                >追寻生活的炽热</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://ssnur.com"
            rel="external nofollow"
            title="Peace"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/NYiEik20591281701839945538.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Peace"
                data-ll-status="loaded"
                src="https://p.zhheo.com/NYiEik20591281701839945538.png!cover_mini"
            />
            <div class="img-alt is-center">Peace</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Peace</span
                ><span class="flink-item-desc" title="藏匿在大海中的小屋"
                >藏匿在大海中的小屋</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.dhkk.cn/"
            rel="external nofollow"
            title="大海看看"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/RrXFVq25490381678864854235.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="大海看看"
                data-ll-status="loaded"
                src="https://p.zhheo.com/RrXFVq25490381678864854235.jpg!cover_mini"
            />
            <div class="img-alt is-center">大海看看</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">大海看看</span
                ><span
                class="flink-item-desc"
                title="记录生活留住美好时刻 ，分享个人学习笔记"
                >记录生活留住美好时刻 ，分享个人学习笔记</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://mnchen.cn/"
            rel="external nofollow"
            title="墨尘"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/0kp90g21590981694413395245.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="墨尘"
                data-ll-status="loaded"
                src="https://p.zhheo.com/0kp90g21590981694413395245.png!cover_mini"
            />
            <div class="img-alt is-center">墨尘</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">墨尘</span
                ><span class="flink-item-desc" title="虽多尘色染，犹见墨痕浓"
                >虽多尘色染，犹见墨痕浓</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.dongjunke.cn/"
            rel="external nofollow"
            title="小饿"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/2CxXGi24890381679812668094.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="小饿"
                data-ll-status="loaded"
                src="https://p.zhheo.com/2CxXGi24890381679812668094.jpg!cover_mini"
            />
            <div class="img-alt is-center">小饿</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">小饿</span
                ><span
                class="flink-item-desc"
                title="80 后互联网老司机，专注于科技互联网、社交媒体运营领域。"
                >80 后互联网老司机，专注于科技互联网、社交媒体运营领域。</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.mcaoyuan.com/"
            rel="external nofollow"
            title="马草原"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/PJi12I24690481681728406865.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="马草原"
                data-ll-status="loaded"
                src="https://p.zhheo.com/PJi12I24690481681728406865.jpg!cover_mini"
            />
            <div class="img-alt is-center">马草原</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">马草原</span
                ><span
                class="flink-item-desc"
                title="If you want to tame a person , will risk tears."
                >If you want to tame a person , will risk tears.</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://holyghostf.github.io/"
            rel="external nofollow"
            title="繁華如夢"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/LLrjyT20090481682176740802.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="繁華如夢"
                data-ll-status="loaded"
                src="https://p.zhheo.com/LLrjyT20090481682176740802.jpg!cover_mini"
            />
            <div class="img-alt is-center">繁華如夢</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">繁華如夢</span
                ><span
                class="flink-item-desc"
                title="苍茫大地一剑尽挽破，何处繁华笙歌落。"
                >苍茫大地一剑尽挽破，何处繁华笙歌落。</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.licic.net/"
            rel="external nofollow"
            title="李程ic"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/FejsPp22790581684724787626.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="李程ic"
                data-ll-status="loaded"
                src="https://p.zhheo.com/FejsPp22790581684724787626.jpg!cover_mini"
            />
            <div class="img-alt is-center">李程ic</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">李程ic</span
                ><span class="flink-item-desc" title="中华人民共和国万岁！"
                >中华人民共和国万岁！</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.mocn.top/"
            rel="external nofollow"
            title="莫莫逗狗ฅ^≧ω≦^ฅ"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/qZJ2Jf20290581684128422240.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="莫莫逗狗ฅ^≧ω≦^ฅ"
                data-ll-status="loaded"
                src="https://p.zhheo.com/qZJ2Jf20290581684128422240.jpg!cover_mini"
            />
            <div class="img-alt is-center">莫莫逗狗ฅ^≧ω≦^ฅ</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">莫莫逗狗ฅ^≧ω≦^ฅ</span
                ><span class="flink-item-desc" title="莫莫逗狗ฅ^≧ω≦^ฅ"
                >莫莫逗狗ฅ^≧ω≦^ฅ</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://srj953588756.github.io/"
            rel="external nofollow"
            title="平头哥"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/bcv8G424190581685327021018.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="平头哥"
                data-ll-status="loaded"
                src="https://p.zhheo.com/bcv8G424190581685327021018.jpg!cover_mini"
            />
            <div class="img-alt is-center">平头哥</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">平头哥</span
                ><span class="flink-item-desc" title="分享感动人心的故事和产品"
                >分享感动人心的故事和产品</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.saop.cc/"
            rel="external nofollow"
            title="Asuna"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/XNt7Xu23590681686723635050.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Asuna"
                data-ll-status="loaded"
                src="https://p.zhheo.com/XNt7Xu23590681686723635050.jpg!cover_mini"
            />
            <div class="img-alt is-center">Asuna</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Asuna</span
                ><span
                class="flink-item-desc"
                title="これは、ゲームであっても遊びではない。"
                >これは、ゲームであっても遊びではない。</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://dashbing.github.io/"
            rel="external nofollow"
            title="DashBing"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/1I1KWr20990781688867889682.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="DashBing"
                data-ll-status="loaded"
                src="https://p.zhheo.com/1I1KWr20990781688867889682.jpg!cover_mini"
            />
            <div class="img-alt is-center">DashBing</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">DashBing</span
                ><span class="flink-item-desc" title="⌈搏海之明辉，何来彼岸？⌋"
                >⌈搏海之明辉，何来彼岸？⌋</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://awa.ink/"
            rel="external nofollow"
            title="低潮鲸鸣"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/0JvQ5C21990781689066919642.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="低潮鲸鸣"
                data-ll-status="loaded"
                src="https://p.zhheo.com/0JvQ5C21990781689066919642.jpg!cover_mini"
            />
            <div class="img-alt is-center">低潮鲸鸣</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">低潮鲸鸣</span
                ><span class="flink-item-desc" title="色即是null,null即是色."
                >色即是null,null即是色.</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.siena.zone/"
            rel="external nofollow"
            title="小鹿"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/3qNoYC25490781689067014773.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="小鹿"
                data-ll-status="loaded"
                src="https://p.zhheo.com/3qNoYC25490781689067014773.jpg!cover_mini"
            />
            <div class="img-alt is-center">小鹿</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">小鹿</span
                ><span class="flink-item-desc" title="跳吧，在无比宏大的星系！"
                >跳吧，在无比宏大的星系！</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.365sites.top/"
            rel="external nofollow"
            title="Winner365"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/grlqPv20690981695890586980.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Winner365"
                data-ll-status="loaded"
                src="https://p.zhheo.com/grlqPv20690981695890586980.png!cover_mini"
            />
            <div class="img-alt is-center">Winner365</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Winner365</span
                ><span
                class="flink-item-desc"
                title="所谓浮躁，也就是时时刻刻，希望以最短的时间，博取最多的存在感优越感和自我认同"
                >所谓浮躁，也就是时时刻刻，希望以最短的时间，博取最多的存在感优越感和自我认同</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://zelihole.github.io/blog2023.html"
            rel="external nofollow"
            title="沐泽"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/7Jthki23290781689738032046.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="沐泽"
                data-ll-status="loaded"
                src="https://p.zhheo.com/7Jthki23290781689738032046.jpg!cover_mini"
            />
            <div class="img-alt is-center">沐泽</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">沐泽</span
                ><span class="flink-item-desc" title="佳肴弗食，与我何干？"
                >佳肴弗食，与我何干？</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://wsbblog.cn/"
            rel="external nofollow"
            title="wsb"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/20233a932c1688b351b402e78c093e9f9526161801.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="wsb"
                data-ll-status="loaded"
                src="https://p.zhheo.com/20233a932c1688b351b402e78c093e9f9526161801.png!cover_mini"
            />
            <div class="img-alt is-center">wsb</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">wsb</span
                ><span class="flink-item-desc" title="己所不欲，勿施于人"
                >己所不欲，勿施于人</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://ffbf.top/"
            rel="external nofollow"
            title="福福不服"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/ellLhi24190781690363421584.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="福福不服"
                data-ll-status="loaded"
                src="https://p.zhheo.com/ellLhi24190781690363421584.png!cover_mini"
            />
            <div class="img-alt is-center">福福不服</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">福福不服</span
                ><span class="flink-item-desc" title="服就是不服">服就是不服</span>
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.bao-feng.top/"
            rel="external nofollow"
            title="baofeng"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/8ay6jy23090881690965690887.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="baofeng"
                data-ll-status="loaded"
                src="https://p.zhheo.com/8ay6jy23090881690965690887.png!cover_mini"
            />
            <div class="img-alt is-center">baofeng</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">baofeng</span
                ><span class="flink-item-desc" title="年年有风，风吹年年，慢慢即漫漫"
                >年年有风，风吹年年，慢慢即漫漫</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.xiowo.net/"
            rel="external nofollow"
            title="Mo"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/xA5ZrN24890881690965828457.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Mo"
                data-ll-status="loaded"
                src="https://p.zhheo.com/xA5ZrN24890881690965828457.png!cover_mini"
            />
            <div class="img-alt is-center">Mo</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Mo</span
                ><span class="flink-item-desc" title="万年鸽王，哈哈OvO"
                >万年鸽王，哈哈OvO</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="http://liuyuyang.net/"
            rel="external nofollow"
            title="YuYang"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/pzDZ5D23290881691137832042.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="YuYang"
                data-ll-status="loaded"
                src="https://p.zhheo.com/pzDZ5D23290881691137832042.png!cover_mini"
            />
            <div class="img-alt is-center">YuYang</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">YuYang</span
                ><span class="flink-item-desc" title="记录一个架构师的崛起"
                >记录一个架构师的崛起</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.sinzmise.top/"
            rel="external nofollow"
            title="汐塔魔法屋"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/3hPvx121591281733121315493.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="汐塔魔法屋"
                data-ll-status="loaded"
                src="https://p.zhheo.com/3hPvx121591281733121315493.png!cover_mini"
            />
            <div class="img-alt is-center">汐塔魔法屋</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">汐塔魔法屋</span
                ><span
                class="flink-item-desc"
                title="种下一颗有故事的种子，让它带着魔法和奇迹生根发芽"
                >种下一颗有故事的种子，让它带着魔法和奇迹生根发芽</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://demochen.com/"
            rel="external nofollow"
            title="特立独行的异类"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/mFrzyr25090881691634050409.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="特立独行的异类"
                data-ll-status="loaded"
                src="https://p.zhheo.com/mFrzyr25090881691634050409.png!cover_mini"
            />
            <div class="img-alt is-center">特立独行的异类</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">特立独行的异类</span
                ><span
                class="flink-item-desc"
                title="引入变量，跳出死循环，从不确定性中获益"
                >引入变量，跳出死循环，从不确定性中获益</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.bytecho.net/"
            rel="external nofollow"
            title="字节星球"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/ipS5Eg25990881691634299882.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="字节星球"
                data-ll-status="loaded"
                src="https://p.zhheo.com/ipS5Eg25990881691634299882.png!cover_mini"
            />
            <div class="img-alt is-center">字节星球</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">字节星球</span
                ><span class="flink-item-desc" title="汇聚字节的星球！"
                >汇聚字节的星球！</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.dalechu.cn/"
            rel="external nofollow"
            title="Dale"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/InPTvW24290881691978322698.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Dale"
                data-ll-status="loaded"
                src="https://p.zhheo.com/InPTvW24290881691978322698.png!cover_mini"
            />
            <div class="img-alt is-center">Dale</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Dale</span
                ><span
                class="flink-item-desc"
                title="Wir Werden Wissen ! Wir Werden Wissen !"
                >Wir Werden Wissen ! Wir Werden Wissen !</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.marice.top/"
            rel="external nofollow"
            title="TheIce"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/LmODg421990881692669379107.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="TheIce"
                data-ll-status="loaded"
                src="https://p.zhheo.com/LmODg421990881692669379107.png!cover_mini"
            />
            <div class="img-alt is-center">TheIce</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">TheIce</span
                ><span class="flink-item-desc" title="水穷云起处">水穷云起处</span>
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://cdt3211.top/"
            rel="external nofollow"
            title="Abner"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/Tbi8xn20990881692669429473.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Abner"
                data-ll-status="loaded"
                src="https://p.zhheo.com/Tbi8xn20990881692669429473.png!cover_mini"
            />
            <div class="img-alt is-center">Abner</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Abner</span
                ><span class="flink-item-desc" title="追求进步的小白"
                >追求进步的小白</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.lowion.cn/"
            rel="external nofollow"
            title="WilliamSun"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/kTVjys21990981693535779703.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="WilliamSun"
                data-ll-status="loaded"
                src="https://p.zhheo.com/kTVjys21990981693535779703.png!cover_mini"
            />
            <div class="img-alt is-center">WilliamSun</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">WilliamSun</span
                ><span class="flink-item-desc" title="Code&amp;&amp;Life"
                >Code&amp;&amp;Life</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.andypang.cc/"
            rel="external nofollow"
            title="偷闲小站"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/HzNOyw24090981695003820774.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="偷闲小站"
                data-ll-status="loaded"
                src="https://p.zhheo.com/HzNOyw24090981695003820774.jpg!cover_mini"
            />
            <div class="img-alt is-center">偷闲小站</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">偷闲小站</span
                ><span class="flink-item-desc" title="跨越山海，终见曙光"
                >跨越山海，终见曙光</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.fufu.ink/"
            rel="external nofollow"
            title="空想笔记"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/7bjc5z22290981695349642799.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="空想笔记"
                data-ll-status="loaded"
                src="https://p.zhheo.com/7bjc5z22290981695349642799.png!cover_mini"
            />
            <div class="img-alt is-center">空想笔记</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">空想笔记</span
                ><span
                class="flink-item-desc"
                title="この世界に偶然なんてない、あるのは必然だけ"
                >この世界に偶然なんてない、あるのは必然だけ</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.loveak.top/"
            rel="external nofollow"
            title="Plasmon222"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/U6HQW222491081697001684795.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Plasmon222"
                data-ll-status="loaded"
                src="https://p.zhheo.com/U6HQW222491081697001684795.png!cover_mini"
            />
            <div class="img-alt is-center">Plasmon222</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Plasmon222</span
                ><span class="flink-item-desc" title="✨行则将至，做则必成✨"
                >✨行则将至，做则必成✨</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.timelogs.cn/"
            rel="external nofollow"
            title="时光日志"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/ZPcEbo22391081697771723019.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="时光日志"
                data-ll-status="loaded"
                src="https://p.zhheo.com/ZPcEbo22391081697771723019.png!cover_mini"
            />
            <div class="img-alt is-center">时光日志</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">时光日志</span
                ><span class="flink-item-desc" title="纪念流失的岁月"
                >纪念流失的岁月</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.jikui.cn/"
            rel="external nofollow"
            title="揽星"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/F1wbi923991281735537839149.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="揽星"
                data-ll-status="loaded"
                src="https://p.zhheo.com/F1wbi923991281735537839149.png!cover_mini"
            />
            <div class="img-alt is-center">揽星</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">揽星</span
                ><span class="flink-item-desc" title="不积跬步,无以至千里"
                >不积跬步,无以至千里</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.chyt.top/"
            rel="external nofollow"
            title="CHYT"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/8jKMPr24091181700558560766.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="CHYT"
                data-ll-status="loaded"
                src="https://p.zhheo.com/8jKMPr24091181700558560766.png!cover_mini"
            />
            <div class="img-alt is-center">CHYT</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">CHYT</span
                ><span class="flink-item-desc" title="生活万物，唯爱小婷"
                >生活万物，唯爱小婷</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://o0.work/"
            rel="external nofollow"
            title="iYuan"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/0X71HS23890281645691738958.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="iYuan"
                data-ll-status="loaded"
                src="https://p.zhheo.com/0X71HS23890281645691738958.jpg!cover_mini"
            />
            <div class="img-alt is-center">iYuan</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">iYuan</span
                ><span class="flink-item-desc" title="不患人之不己知，患不知人也"
                >不患人之不己知，患不知人也</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.harriswong.top/"
            rel="external nofollow"
            title="Harris"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/MqLwk620390381616982063498.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Harris"
                data-ll-status="loaded"
                src="https://p.zhheo.com/MqLwk620390381616982063498.jpg!cover_mini"
            />
            <div class="img-alt is-center">Harris</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Harris</span
                ><span class="flink-item-desc" title="时不我待，只争朝夕"
                >时不我待，只争朝夕</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item HA">
            <span class="site-card-tag">HA</span
            ><a
            class="cf-friends-link"
            href="https://ishya.top/"
            rel="external nofollow"
            title="Uki"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/20226705a9a9b5a1189c226bfaeb6d5cff97072611.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Uki"
                data-ll-status="loaded"
                src="https://p.zhheo.com/20226705a9a9b5a1189c226bfaeb6d5cff97072611.png!cover_mini"
            />
            <div class="img-alt is-center">Uki</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Uki</span
                ><span class="flink-item-desc" title="散落在世界一角的故事"
                >散落在世界一角的故事</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="http://blog.yizhixiaozhu.top"
            rel="external nofollow"
            title="猪猪"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/xB75sX20491181701057664322.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="猪猪"
                data-ll-status="loaded"
                src="https://p.zhheo.com/xB75sX20491181701057664322.png!cover_mini"
            />
            <div class="img-alt is-center">猪猪</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">猪猪</span
                ><span class="flink-item-desc" title="一个简单的博客"
                >一个简单的博客</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://baiwumm.com/"
            rel="external nofollow"
            title="白雾茫茫丶"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/SHhnKF25891181701323518175.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="白雾茫茫丶"
                data-ll-status="loaded"
                src="https://p.zhheo.com/SHhnKF25891181701323518175.png!cover_mini"
            />
            <div class="img-alt is-center">白雾茫茫丶</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">白雾茫茫丶</span
                ><span class="flink-item-desc" title="身后没有灯火，身前白雾茫茫丶"
                >身后没有灯火，身前白雾茫茫丶</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://wxjxw.cn/"
            rel="external nofollow"
            title="微笑"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/s4wjP622791281701672807523.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="微笑"
                data-ll-status="loaded"
                src="https://p.zhheo.com/s4wjP622791281701672807523.png!cover_mini"
            />
            <div class="img-alt is-center">微笑</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">微笑</span
                ><span class="flink-item-desc" title="知天易，易天难。"
                >知天易，易天难。</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.imyjs.cn/"
            rel="external nofollow"
            title="编程那点事儿"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/gov25N25391281701672953343.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="编程那点事儿"
                data-ll-status="loaded"
                src="https://p.zhheo.com/gov25N25391281701672953343.png!cover_mini"
            />
            <div class="img-alt is-center">编程那点事儿</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">编程那点事儿</span
                ><span class="flink-item-desc" title="告别在空想中挥霍着生活"
                >告别在空想中挥霍着生活</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.insidentally.com/"
            rel="external nofollow"
            title="无妄当自持"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/1X0Ho224391281701673003697.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="无妄当自持"
                data-ll-status="loaded"
                src="https://p.zhheo.com/1X0Ho224391281701673003697.png!cover_mini"
            />
            <div class="img-alt is-center">无妄当自持</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">无妄当自持</span
                ><span class="flink-item-desc" title="学习、实践、分享"
                >学习、实践、分享</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://fanrongbin.com/"
            rel="external nofollow"
            title="Rongbin"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/tPPTu223491281702093414928.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Rongbin"
                data-ll-status="loaded"
                src="https://p.zhheo.com/tPPTu223491281702093414928.png!cover_mini"
            />
            <div class="img-alt is-center">Rongbin</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Rongbin</span
                ><span class="flink-item-desc" title="Thoughts and ideas"
                >Thoughts and ideas</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://m.senlinm.cn/"
            rel="external nofollow"
            title="小林笔记"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/drupWw24691281702869706820.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="小林笔记"
                data-ll-status="loaded"
                src="https://p.zhheo.com/drupWw24691281702869706820.png!cover_mini"
            />
            <div class="img-alt is-center">小林笔记</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">小林笔记</span
                ><span class="flink-item-desc" title="轻生活，秒上签"
                >轻生活，秒上签</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.nsxsb.com/"
            rel="external nofollow"
            title="小权"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/rDXy3H21791281703383457428.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="小权"
                data-ll-status="loaded"
                src="https://p.zhheo.com/rDXy3H21791281703383457428.png!cover_mini"
            />
            <div class="img-alt is-center">小权</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">小权</span
                ><span
                class="flink-item-desc"
                title="一个无聊的人创了一个无聊的网站日记"
                >一个无聊的人创了一个无聊的网站日记</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.shang.ac.cn/"
            rel="external nofollow"
            title="青猫"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/J0tsvL20691281703383506509.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="青猫"
                data-ll-status="loaded"
                src="https://p.zhheo.com/J0tsvL20691281703383506509.png!cover_mini"
            />
            <div class="img-alt is-center">青猫</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">青猫</span
                ><span class="flink-item-desc" title="我的满腔热情好像耗尽了"
                >我的满腔热情好像耗尽了</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://naokuo.top/"
            rel="external nofollow"
            title="Naokuo"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/CmMdUu22391281703730683479.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Naokuo"
                data-ll-status="loaded"
                src="https://p.zhheo.com/CmMdUu22391281703730683479.png!cover_mini"
            />
            <div class="img-alt is-center">Naokuo</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Naokuo</span
                ><span class="flink-item-desc" title="Naokuo 的 博客"
                >Naokuo 的 博客</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.xxfer.cn/"
            rel="external nofollow"
            title="小李同学 Coding"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/86S5hR21390181705035373439.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="小李同学 Coding"
                data-ll-status="loaded"
                src="https://p.zhheo.com/86S5hR21390181705035373439.png!cover_mini"
            />
            <div class="img-alt is-center">小李同学 Coding</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">小李同学 Coding</span
                ><span class="flink-item-desc" title="一支努力变强的小彩笔"
                >一支努力变强的小彩笔</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.zhilu.cyou/"
            rel="external nofollow"
            title="纸鹿本鹿"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/dO09Pw24690281706858266166.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="纸鹿本鹿"
                data-ll-status="loaded"
                src="https://p.zhheo.com/dO09Pw24690281706858266166.png!cover_mini"
            />
            <div class="img-alt is-center">纸鹿本鹿</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">纸鹿本鹿</span
                ><span class="flink-item-desc" title="纸鹿至麓不知路，支炉制露不止漉"
                >纸鹿至麓不知路，支炉制露不止漉</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://angine.tech/"
            rel="external nofollow"
            title="安擎Angine"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/jbhHGz24990281706858629804.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="安擎Angine"
                data-ll-status="loaded"
                src="https://p.zhheo.com/jbhHGz24990281706858629804.png!cover_mini"
            />
            <div class="img-alt is-center">安擎Angine</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">安擎Angine</span
                ><span class="flink-item-desc" title="By the power of language"
                >By the power of language</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://smileguide.github.io/"
            rel="external nofollow"
            title="群青流星"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/B5Nm9z25390281707657893875.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="群青流星"
                data-ll-status="loaded"
                src="https://p.zhheo.com/B5Nm9z25390281707657893875.png!cover_mini"
            />
            <div class="img-alt is-center">群青流星</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">群青流星</span
                ><span
                class="flink-item-desc"
                title="我喜欢听花开的声音，更想自由地深情地呼吸"
                >我喜欢听花开的声音，更想自由地深情地呼吸</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://lhasa.icu/"
            rel="external nofollow"
            title="游钓四方"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/yNyhHF25190281708067811974.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="游钓四方"
                data-ll-status="loaded"
                src="https://p.zhheo.com/yNyhHF25190281708067811974.png!cover_mini"
            />
            <div class="img-alt is-center">游钓四方</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">游钓四方</span
                ><span
                class="flink-item-desc"
                title="长途骑行小学生、振出并继、提琴古典乐爱好者"
                >长途骑行小学生、振出并继、提琴古典乐爱好者</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://luckqf.cn/"
            rel="external nofollow"
            title="清风"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/hkBKtx21690281708746076222.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="清风"
                data-ll-status="loaded"
                src="https://p.zhheo.com/hkBKtx21690281708746076222.png!cover_mini"
            />
            <div class="img-alt is-center">清风</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">清风</span
                ><span class="flink-item-desc" title="万般皆苦 唯有自渡"
                >万般皆苦 唯有自渡</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.june-pj.cn/"
            rel="external nofollow"
            title="June"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/MQxeBE25390381710125153276.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="June"
                data-ll-status="loaded"
                src="https://p.zhheo.com/MQxeBE25390381710125153276.png!cover_mini"
            />
            <div class="img-alt is-center">June</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">June</span
                ><span class="flink-item-desc" title="遇事不决，可问春风"
                >遇事不决，可问春风</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.outshine.cn/"
            rel="external nofollow"
            title="outshine学霸笔记"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/MyHePV21790381710726917932.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="outshine学霸笔记"
                data-ll-status="loaded"
                src="https://p.zhheo.com/MyHePV21790381710726917932.png!cover_mini"
            />
            <div class="img-alt is-center">outshine学霸笔记</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">outshine学霸笔记</span
                ><span class="flink-item-desc" title="小学、初中、高中学习资料分享。"
                >小学、初中、高中学习资料分享。</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://bluehe.cn/"
            rel="external nofollow"
            title="云心怀鹤"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/WexZmZ20090381711419660083.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="云心怀鹤"
                data-ll-status="loaded"
                src="https://p.zhheo.com/WexZmZ20090381711419660083.png!cover_mini"
            />
            <div class="img-alt is-center">云心怀鹤</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">云心怀鹤</span
                ><span class="flink-item-desc" title="风光摄影者，文艺叙述人"
                >风光摄影者，文艺叙述人</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://mozixi.com/"
            rel="external nofollow"
            title="陌子夕生活录"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/LeDZCU22190381711419801912.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="陌子夕生活录"
                data-ll-status="loaded"
                src="https://p.zhheo.com/LeDZCU22190381711419801912.png!cover_mini"
            />
            <div class="img-alt is-center">陌子夕生活录</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">陌子夕生活录</span
                ><span class="flink-item-desc" title="夕阳无别事，等风也等你…"
                >夕阳无别事，等风也等你…</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.morick66.com/"
            rel="external nofollow"
            title="Morick莫里克"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/2XjsAG23390481711968213376.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Morick莫里克"
                data-ll-status="loaded"
                src="https://p.zhheo.com/2XjsAG23390481711968213376.png!cover_mini"
            />
            <div class="img-alt is-center">Morick莫里克</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Morick莫里克</span
                ><span class="flink-item-desc" title="假装自己是个外星人"
                >假装自己是个外星人</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://yang000.cn/"
            rel="external nofollow"
            title="飞漫冬山"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/LB3WMU21990481713233179908.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="飞漫冬山"
                data-ll-status="loaded"
                src="https://p.zhheo.com/LB3WMU21990481713233179908.png!cover_mini"
            />
            <div class="img-alt is-center">飞漫冬山</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">飞漫冬山</span
                ><span class="flink-item-desc" title="片刻春风得意，未知景物朦胧"
                >片刻春风得意，未知景物朦胧</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://lennychen.top/"
            rel="external nofollow"
            title="Lenny"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/IFPjiw24290481713233382649.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Lenny"
                data-ll-status="loaded"
                src="https://p.zhheo.com/IFPjiw24290481713233382649.png!cover_mini"
            />
            <div class="img-alt is-center">Lenny</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Lenny</span
                ><span class="flink-item-desc" title="天地不仁，以万物为刍狗"
                >天地不仁，以万物为刍狗</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.likesrt.com/"
            rel="external nofollow"
            title="云深处"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/SpXeTU20790581714701787989.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="云深处"
                data-ll-status="loaded"
                src="https://p.zhheo.com/SpXeTU20790581714701787989.png!cover_mini"
            />
            <div class="img-alt is-center">云深处</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">云深处</span
                ><span class="flink-item-desc" title="只在此山中，云深不知处"
                >只在此山中，云深不知处</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://pampo.cn/"
            rel="external nofollow"
            title="Pampo"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/Smb9yO22190581714701921865.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Pampo"
                data-ll-status="loaded"
                src="https://p.zhheo.com/Smb9yO22190581714701921865.png!cover_mini"
            />
            <div class="img-alt is-center">Pampo</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Pampo</span
                ><span class="flink-item-desc" title="我希望，我们都能够变得更勇敢"
                >我希望，我们都能够变得更勇敢</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.xiamo.cc/"
            rel="external nofollow"
            title="夏末笔记"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/CX4fpL24290581715332722100.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="夏末笔记"
                data-ll-status="loaded"
                src="https://p.zhheo.com/CX4fpL24290581715332722100.png!cover_mini"
            />
            <div class="img-alt is-center">夏末笔记</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">夏末笔记</span
                ><span
                class="flink-item-desc"
                title="这里是夏末的个人博客，记录生活与工作中的一些琐事，分享WordPress美化及建站经验，偶尔也会分享一些实用的手机和电脑软件～"
                >这里是夏末的个人博客，记录生活与工作中的一些琐事，分享WordPress美化及建站经验，偶尔也会分享一些实用的手机和电脑软件～</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.iczrx.cn/"
            rel="external nofollow"
            title="晚夜"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/pDDpwo23990581715738199944.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="晚夜"
                data-ll-status="loaded"
                src="https://p.zhheo.com/pDDpwo23990581715738199944.png!cover_mini"
            />
            <div class="img-alt is-center">晚夜</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">晚夜</span
                ><span class="flink-item-desc" title="做好量变的准备，促进事物的质变"
                >做好量变的准备，促进事物的质变</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.verynb.me/"
            rel="external nofollow"
            title="晴雀堂"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/fosug221690581715738236906.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="晴雀堂"
                data-ll-status="loaded"
                src="https://p.zhheo.com/fosug221690581715738236906.png!cover_mini"
            />
            <div class="img-alt is-center">晴雀堂</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">晴雀堂</span
                ><span class="flink-item-desc" title="一位普通的学牲在记录自己的生活"
                >一位普通的学牲在记录自己的生活</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.wsq127.top/"
            rel="external nofollow"
            title="辞琼"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/Dy7ohm21990581716175039900.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="辞琼"
                data-ll-status="loaded"
                src="https://p.zhheo.com/Dy7ohm21990581716175039900.png!cover_mini"
            />
            <div class="img-alt is-center">辞琼</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">辞琼</span
                ><span class="flink-item-desc" title="突破了瓶颈，发现还有瓶盖qwq"
                >突破了瓶颈，发现还有瓶盖qwq</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.lxink.cn/"
            rel="external nofollow"
            title="凉心"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/Sitnmc24090581716528640507.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="凉心"
                data-ll-status="loaded"
                src="https://p.zhheo.com/Sitnmc24090581716528640507.png!cover_mini"
            />
            <div class="img-alt is-center">凉心</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">凉心</span
                ><span class="flink-item-desc" title="我的故事只讲给你听"
                >我的故事只讲给你听</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.liuzhen932.top/"
            rel="external nofollow"
            title="liuzhen932"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/lYmdId23790681717381057271.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="liuzhen932"
                data-ll-status="loaded"
                src="https://p.zhheo.com/lYmdId23790681717381057271.png!cover_mini"
            />
            <div class="img-alt is-center">liuzhen932</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">liuzhen932</span
                ><span class="flink-item-desc" title="只要愿意去做，人无所不通"
                >只要愿意去做，人无所不通</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.chawfoo.com/"
            rel="external nofollow"
            title="CHACAT"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/AFnQju23490681717381114379.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="CHACAT"
                data-ll-status="loaded"
                src="https://p.zhheo.com/AFnQju23490681717381114379.png!cover_mini"
            />
            <div class="img-alt is-center">CHACAT</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">CHACAT</span
                ><span class="flink-item-desc" title="阅读、思考、写作"
                >阅读、思考、写作</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://yjvc.cn/"
            rel="external nofollow"
            title="刘郎阁"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/Qy2Zlq23290681717747292716.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="刘郎阁"
                data-ll-status="loaded"
                src="https://p.zhheo.com/Qy2Zlq23290681717747292716.png!cover_mini"
            />
            <div class="img-alt is-center">刘郎阁</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">刘郎阁</span
                ><span class="flink-item-desc" title="一个积极向上的生活探索者！"
                >一个积极向上的生活探索者！</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.bsgun.cn/"
            rel="external nofollow"
            title="梦爱吃鱼"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/9Tg9h620490681718168044766.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="梦爱吃鱼"
                data-ll-status="loaded"
                src="https://p.zhheo.com/9Tg9h620490681718168044766.png!cover_mini"
            />
            <div class="img-alt is-center">梦爱吃鱼</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">梦爱吃鱼</span
                ><span class="flink-item-desc" title="但愿日子清静抬头遇见的满是柔情"
                >但愿日子清静抬头遇见的满是柔情</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.maoyiwei.com/"
            rel="external nofollow"
            title="Yves"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/oLL6hp20290681718783882942.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Yves"
                data-ll-status="loaded"
                src="https://p.zhheo.com/oLL6hp20290681718783882942.png!cover_mini"
            />
            <div class="img-alt is-center">Yves</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Yves</span
                ><span class="flink-item-desc" title="Welcome!">Welcome!</span>
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.shimmerl.top/"
            rel="external nofollow"
            title="haohang"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/BSYs8a23190681719546631222.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="haohang"
                data-ll-status="loaded"
                src="https://p.zhheo.com/BSYs8a23190681719546631222.png!cover_mini"
            />
            <div class="img-alt is-center">haohang</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">haohang</span
                ><span
                class="flink-item-desc"
                title="承诺不值钱, 做个言而有信的人太难了。"
                >承诺不值钱, 做个言而有信的人太难了。</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://moreality.net/"
            rel="external nofollow"
            title="ShootZone"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/2022bd9a73886bca784dbdf987bae92bce4f230311.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="ShootZone"
                data-ll-status="loaded"
                src="https://p.zhheo.com/2022bd9a73886bca784dbdf987bae92bce4f230311.png!cover_mini"
            />
            <div class="img-alt is-center">ShootZone</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">ShootZone</span
                ><span class="flink-item-desc" title="https://blog.roccoshi.top"
                >https://blog.roccoshi.top</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://kevinknow.cn/"
            rel="external nofollow"
            title="上帝的笑"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/P2uVbJ23190781658916331562.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="上帝的笑"
                data-ll-status="loaded"
                src="https://p.zhheo.com/P2uVbJ23190781658916331562.jpg!cover_mini"
            />
            <div class="img-alt is-center">上帝的笑</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">上帝的笑</span
                ><span class="flink-item-desc" title="深自缄默,如云漂泊"
                >深自缄默,如云漂泊</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.nalex.top/"
            rel="external nofollow"
            title="Rootlex"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/2022e0e0c669a806e588b49569e829a4985d262711.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Rootlex"
                data-ll-status="loaded"
                src="https://p.zhheo.com/2022e0e0c669a806e588b49569e829a4985d262711.png!cover_mini"
            />
            <div class="img-alt is-center">Rootlex</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Rootlex</span
                ><span class="flink-item-desc" title="寒蝉黎明之时，便是重生之日"
                >寒蝉黎明之时，便是重生之日</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://rjjr.cn/"
            rel="external nofollow"
            title="萬事屋"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/7KXfsy21690781719811336889.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="萬事屋"
                data-ll-status="loaded"
                src="https://p.zhheo.com/7KXfsy21690781719811336889.png!cover_mini"
            />
            <div class="img-alt is-center">萬事屋</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">萬事屋</span
                ><span class="flink-item-desc" title="每天写下自己的喜好"
                >每天写下自己的喜好</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.laobinghu.top/"
            rel="external nofollow"
            title="烧瑚烙饼乱刨笔记"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/RYPvgf23590781720580675821.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="烧瑚烙饼乱刨笔记"
                data-ll-status="loaded"
                src="https://p.zhheo.com/RYPvgf23590781720580675821.png!cover_mini"
            />
            <div class="img-alt is-center">烧瑚烙饼乱刨笔记</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">烧瑚烙饼乱刨笔记</span
                ><span
                class="flink-item-desc"
                title="一个2024届新高一的闲(发)言(疯)碎(日)语(常)"
                >一个2024届新高一的闲(发)言(疯)碎(日)语(常)</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.henrywhu.cn/"
            rel="external nofollow"
            title="HenryMoreau"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/mEktUE25690781721011136647.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="HenryMoreau"
                data-ll-status="loaded"
                src="https://p.zhheo.com/mEktUE25690781721011136647.png!cover_mini"
            />
            <div class="img-alt is-center">HenryMoreau</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">HenryMoreau</span
                ><span class="flink-item-desc" title="Student / Designer / Dreamchaser"
                >Student / Designer / Dreamchaser</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://xisoul.cn"
            rel="external nofollow"
            title="XiSoul"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/lf6T8421690781721101576592.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="XiSoul"
                data-ll-status="loaded"
                src="https://p.zhheo.com/lf6T8421690781721101576592.png!cover_mini"
            />
            <div class="img-alt is-center">XiSoul</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">XiSoul</span
                ><span class="flink-item-desc" title="啥都玩，可以来看看"
                >啥都玩，可以来看看</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://t-t.live/"
            rel="external nofollow"
            title="团团生活志"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/YpEwhd24990581652955109284.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="团团生活志"
                data-ll-status="loaded"
                src="https://p.zhheo.com/YpEwhd24990581652955109284.jpg!cover_mini"
            />
            <div class="img-alt is-center">团团生活志</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">团团生活志</span
                ><span class="flink-item-desc" title="爱生活 爱分享"
                >爱生活 爱分享</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://hexo.dreamerhe.cn/"
            rel="external nofollow"
            title="梦想之都"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/pTycv921790781721615537404.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="梦想之都"
                data-ll-status="loaded"
                src="https://p.zhheo.com/pTycv921790781721615537404.png!cover_mini"
            />
            <div class="img-alt is-center">梦想之都</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">梦想之都</span
                ><span class="flink-item-desc" title="朝着梦想前进">朝着梦想前进</span>
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.wniui.com/"
            rel="external nofollow"
            title="小小星子"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/B0BbQj20490781721963824721.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="小小星子"
                data-ll-status="loaded"
                src="https://p.zhheo.com/B0BbQj20490781721963824721.png!cover_mini"
            />
            <div class="img-alt is-center">小小星子</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">小小星子</span
                ><span class="flink-item-desc" title="分享生活与经历，记录我的碎碎念念"
                >分享生活与经历，记录我的碎碎念念</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://kfdzcoffee.cn/"
            rel="external nofollow"
            title="咖啡豆子coffee"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/vKdDBn25590781722220435296.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="咖啡豆子coffee"
                data-ll-status="loaded"
                src="https://p.zhheo.com/vKdDBn25590781722220435296.png!cover_mini"
            />
            <div class="img-alt is-center">咖啡豆子coffee</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">咖啡豆子coffee</span
                ><span class="flink-item-desc" title="所有奇迹的始发点"
                >所有奇迹的始发点</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://invictusme.cn/"
            rel="external nofollow"
            title="Invictusme"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/GErZPZ24490781722220544022.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Invictusme"
                data-ll-status="loaded"
                src="https://p.zhheo.com/GErZPZ24490781722220544022.png!cover_mini"
            />
            <div class="img-alt is-center">Invictusme</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Invictusme</span
                ><span class="flink-item-desc" title="Invictusme">Invictusme</span>
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.xalaok.top/"
            rel="external nofollow"
            title="Naive Koala🐨"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/MHJi5421690881722566116481.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Naive Koala🐨"
                data-ll-status="loaded"
                src="https://p.zhheo.com/MHJi5421690881722566116481.png!cover_mini"
            />
            <div class="img-alt is-center">Naive Koala🐨</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Naive Koala🐨</span
                ><span class="flink-item-desc" title="像考拉一样无忧😉"
                >像考拉一样无忧😉</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://cyrus19.cc/"
            rel="external nofollow"
            title="CC的数字花园"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/6o40nG22190881723195641711.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="CC的数字花园"
                data-ll-status="loaded"
                src="https://p.zhheo.com/6o40nG22190881723195641711.png!cover_mini"
            />
            <div class="img-alt is-center">CC的数字花园</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">CC的数字花园</span
                ><span class="flink-item-desc" title="睡不着吗？">睡不着吗？</span>
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://isming.me/"
            rel="external nofollow"
            title="码农明明桑"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/YPNIux25390881723442513210.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="码农明明桑"
                data-ll-status="loaded"
                src="https://p.zhheo.com/YPNIux25390881723442513210.png!cover_mini"
            />
            <div class="img-alt is-center">码农明明桑</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">码农明明桑</span
                ><span class="flink-item-desc" title="一个码农的日常记录"
                >一个码农的日常记录</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://luoca.cn/"
            rel="external nofollow"
            title="洛卡日记"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/Xpj9Po20690881724842686616.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="洛卡日记"
                data-ll-status="loaded"
                src="https://p.zhheo.com/Xpj9Po20690881724842686616.png!cover_mini"
            />
            <div class="img-alt is-center">洛卡日记</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">洛卡日记</span
                ><span class="flink-item-desc" title="个人阅读笔记与日常生活留存地"
                >个人阅读笔记与日常生活留存地</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://sikan.moe/"
            rel="external nofollow"
            title="akas"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/vhHezE22690981725243086682.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="akas"
                data-ll-status="loaded"
                src="https://p.zhheo.com/vhHezE22690981725243086682.png!cover_mini"
            />
            <div class="img-alt is-center">akas</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">akas</span
                ><span class="flink-item-desc" title="架空世界-厄尔科斯"
                >架空世界-厄尔科斯</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://wang618.cn/"
            rel="external nofollow"
            title="旺东自留地"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/y84ECg24890981725260088278.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="旺东自留地"
                data-ll-status="loaded"
                src="https://p.zhheo.com/y84ECg24890981725260088278.png!cover_mini"
            />
            <div class="img-alt is-center">旺东自留地</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">旺东自留地</span
                ><span class="flink-item-desc" title="爱分享、爱生活、爱音乐、爱摸鱼"
                >爱分享、爱生活、爱音乐、爱摸鱼</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://cola.xiaoayu.ren/"
            rel="external nofollow"
            title="可乐君"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/KfcSxb20790981725503827138.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="可乐君"
                data-ll-status="loaded"
                src="https://p.zhheo.com/KfcSxb20790981725503827138.png!cover_mini"
            />
            <div class="img-alt is-center">可乐君</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">可乐君</span
                ><span class="flink-item-desc" title="可乐君的小站">可乐君的小站</span>
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://haobin.org/"
            rel="external nofollow"
            title="WALLSTREE小白"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/7pe0xA21290981726636692750.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="WALLSTREE小白"
                data-ll-status="loaded"
                src="https://p.zhheo.com/7pe0xA21290981726636692750.png!cover_mini"
            />
            <div class="img-alt is-center">WALLSTREE小白</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">WALLSTREE小白</span
                ><span
                class="flink-item-desc"
                title="一个懂点金融的奶爸，分享美股、分享我和投资的故事"
                >一个懂点金融的奶爸，分享美股、分享我和投资的故事</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item HA">
            <span class="site-card-tag">HA</span
            ><a
            class="cf-friends-link"
            href="https://blog.gjcloak.top/"
            rel="external nofollow"
            title="公爵书房"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/jhb2Eu23290681655691452046.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="公爵书房"
                data-ll-status="loaded"
                src="https://p.zhheo.com/jhb2Eu23290681655691452046.jpg!cover_mini"
            />
            <div class="img-alt is-center">公爵书房</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">公爵书房</span
                ><span class="flink-item-desc" title="以指键之轻，承载知识之重"
                >以指键之轻，承载知识之重</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.lucksss.com/"
            rel="external nofollow"
            title="小林"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/njPAVE22490981693535844496.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="小林"
                data-ll-status="loaded"
                src="https://p.zhheo.com/njPAVE22490981693535844496.png!cover_mini"
            />
            <div class="img-alt is-center">小林</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">小林</span
                ><span
                class="flink-item-desc"
                title="我们总是在相同的路上 却看到了不同的风景"
                >我们总是在相同的路上 却看到了不同的风景</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://beiqiu.top/"
            rel="external nofollow"
            title="北秋"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/2xHja223091281703383350940.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="北秋"
                data-ll-status="loaded"
                src="https://p.zhheo.com/2xHja223091281703383350940.png!cover_mini"
            />
            <div class="img-alt is-center">北秋</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">北秋</span
                ><span class="flink-item-desc" title="慢慢来，会很快"
                >慢慢来，会很快</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.huochairener-blog.cn/"
            rel="external nofollow"
            title="火柴人儿"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/6Qo8X125690981727063096831.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="火柴人儿"
                data-ll-status="loaded"
                src="https://p.zhheo.com/6Qo8X125690981727063096831.png!cover_mini"
            />
            <div class="img-alt is-center">火柴人儿</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">火柴人儿</span
                ><span class="flink-item-desc" title="仰望星空的打工人"
                >仰望星空的打工人</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.lkurococ.top/"
            rel="external nofollow"
            title="Kurococ Liu"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/1wEdlF20090981727260860266.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Kurococ Liu"
                data-ll-status="loaded"
                src="https://p.zhheo.com/1wEdlF20090981727260860266.png!cover_mini"
            />
            <div class="img-alt is-center">Kurococ Liu</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Kurococ Liu</span
                ><span class="flink-item-desc" title="被子外面很危险！"
                >被子外面很危险！</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.feiyaoblog.com/"
            rel="external nofollow"
            title="飞遥"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/VAgOrX20191081728380461936.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="飞遥"
                data-ll-status="loaded"
                src="https://p.zhheo.com/VAgOrX20191081728380461936.png!cover_mini"
            />
            <div class="img-alt is-center">飞遥</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">飞遥</span
                ><span
                class="flink-item-desc"
                title="飞遥博客，一个翱翔于技术天际的分享平台"
                >飞遥博客，一个翱翔于技术天际的分享平台</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.evan.xin/"
            rel="external nofollow"
            title="Evan"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/8vlpyN25991081728883019592.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Evan"
                data-ll-status="loaded"
                src="https://p.zhheo.com/8vlpyN25991081728883019592.png!cover_mini"
            />
            <div class="img-alt is-center">Evan</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Evan</span
                ><span class="flink-item-desc" title="Practitioners of ‘Keep It Real’"
                >Practitioners of ‘Keep It Real’</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.el9.cn/"
            rel="external nofollow"
            title="老卢"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/GTIIyK24791081729669247435.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="老卢"
                data-ll-status="loaded"
                src="https://p.zhheo.com/GTIIyK24791081729669247435.png!cover_mini"
            />
            <div class="img-alt is-center">老卢</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">老卢</span
                ><span class="flink-item-desc" title="利她，有价值，不打扰"
                >利她，有价值，不打扰</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://liuyuyang.net/"
            rel="external nofollow"
            title="宇阳"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/CiJv4E25391181730945213911.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="宇阳"
                data-ll-status="loaded"
                src="https://p.zhheo.com/CiJv4E25391181730945213911.png!cover_mini"
            />
            <div class="img-alt is-center">宇阳</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">宇阳</span
                ><span class="flink-item-desc" title="记录所学知识，缩短和大神的差距！"
                >记录所学知识，缩短和大神的差距！</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.1zxbc.cn/"
            rel="external nofollow"
            title="一只小白菜"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/TJZ9sR20191181731319021764.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="一只小白菜"
                data-ll-status="loaded"
                src="https://p.zhheo.com/TJZ9sR20191181731319021764.png!cover_mini"
            />
            <div class="img-alt is-center">一只小白菜</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">一只小白菜</span
                ><span class="flink-item-desc" title="抱怨身处黑暗，不如提灯前行"
                >抱怨身处黑暗，不如提灯前行</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://jaychen.cn/"
            rel="external nofollow"
            title="JayChen"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/Z1xJKS22891181731910048348.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="JayChen"
                data-ll-status="loaded"
                src="https://p.zhheo.com/Z1xJKS22891181731910048348.png!cover_mini"
            />
            <div class="img-alt is-center">JayChen</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">JayChen</span
                ><span class="flink-item-desc" title="一个90后、一个爱折腾的人"
                >一个90后、一个爱折腾的人</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.xiaode.tech/"
            rel="external nofollow"
            title="Allen"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/bcYtxE23691181731910116812.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Allen"
                data-ll-status="loaded"
                src="https://p.zhheo.com/bcYtxE23691181731910116812.png!cover_mini"
            />
            <div class="img-alt is-center">Allen</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Allen</span
                ><span class="flink-item-desc" title="还有很多故事，想在这里讲给你听。"
                >还有很多故事，想在这里讲给你听。</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://asain.icu/"
            rel="external nofollow"
            title="千江月"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/xK3ILS22391081697771783947.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="千江月"
                data-ll-status="loaded"
                src="https://p.zhheo.com/xK3ILS22391081697771783947.png!cover_mini"
            />
            <div class="img-alt is-center">千江月</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">千江月</span
                ><span class="flink-item-desc" title="记录医生诊疗日志、传承中医文化"
                >记录医生诊疗日志、传承中医文化</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.yiyou.bj.cn/"
            rel="external nofollow"
            title="益友"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/bdTSqs21591181732166655062.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="益友"
                data-ll-status="loaded"
                src="https://p.zhheo.com/bdTSqs21591181732166655062.png!cover_mini"
            />
            <div class="img-alt is-center">益友</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">益友</span
                ><span
                class="flink-item-desc"
                title="美好的日常生活值得我们去记录，希望我们的生活每天都能充满着乐趣跟开心事。"
                >美好的日常生活值得我们去记录，希望我们的生活每天都能充满着乐趣跟开心事。</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://skylan.cc/"
            rel="external nofollow"
            title="清梦云熙"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/k3DdB225791181732166697932.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="清梦云熙"
                data-ll-status="loaded"
                src="https://p.zhheo.com/k3DdB225791181732166697932.png!cover_mini"
            />
            <div class="img-alt is-center">清梦云熙</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">清梦云熙</span
                ><span class="flink-item-desc" title="相逢何必曾相识"
                >相逢何必曾相识</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://idealclover.top/"
            rel="external nofollow"
            title="idealclover"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/Sy6WOG24291181732166742644.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="idealclover"
                data-ll-status="loaded"
                src="https://p.zhheo.com/Sy6WOG24291181732166742644.png!cover_mini"
            />
            <div class="img-alt is-center">idealclover</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">idealclover</span
                ><span class="flink-item-desc" title="翠翠的个人博客"
                >翠翠的个人博客</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://jingxin18.cn/"
            rel="external nofollow"
            title="二猫"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/CtRvsD24291181732505142894.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="二猫"
                data-ll-status="loaded"
                src="https://p.zhheo.com/CtRvsD24291181732505142894.png!cover_mini"
            />
            <div class="img-alt is-center">二猫</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">二猫</span
                ><span class="flink-item-desc" title="一个简单的Blog站点"
                >一个简单的Blog站点</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://www.puresky.top/"
            rel="external nofollow"
            title="轻雅阁"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/zfkPZg24191281733121161892.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="轻雅阁"
                data-ll-status="loaded"
                src="https://p.zhheo.com/zfkPZg24191281733121161892.png!cover_mini"
            />
            <div class="img-alt is-center">轻雅阁</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">轻雅阁</span
                ><span class="flink-item-desc" title="新时代教师的日常"
                >新时代教师的日常</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://07111.cn/"
            rel="external nofollow"
            title="森尧记"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/8mXL9V22091281733713340144.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="森尧记"
                data-ll-status="loaded"
                src="https://p.zhheo.com/8mXL9V22091281733713340144.png!cover_mini"
            />
            <div class="img-alt is-center">森尧记</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">森尧记</span
                ><span class="flink-item-desc" title="记录生活，交流技术"
                >记录生活，交流技术</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://lin-blog.xyz/"
            rel="external nofollow"
            title="Lin-Blog"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/kCHnAX23491281733713474165.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="Lin-Blog"
                data-ll-status="loaded"
                src="https://p.zhheo.com/kCHnAX23491281733713474165.png!cover_mini"
            />
            <div class="img-alt is-center">Lin-Blog</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">Lin-Blog</span
                ><span class="flink-item-desc" title="把玫瑰藏住，直到遇见她"
                >把玫瑰藏住，直到遇见她</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://mxine.link/"
            rel="external nofollow"
            title="沐潇MXine"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/8stsq225191281734919911122.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="沐潇MXine"
                data-ll-status="loaded"
                src="https://p.zhheo.com/8stsq225191281734919911122.png!cover_mini"
            />
            <div class="img-alt is-center">沐潇MXine</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">沐潇MXine</span
                ><span class="flink-item-desc" title="世界因我而更加闪亮"
                >世界因我而更加闪亮</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://mcyogurt.cn/"
            rel="external nofollow"
            title="酸奶云"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/kZju1720491281734920224913.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="酸奶云"
                data-ll-status="loaded"
                src="https://p.zhheo.com/kZju1720491281734920224913.png!cover_mini"
            />
            <div class="img-alt is-center">酸奶云</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">酸奶云</span
                ><span class="flink-item-desc" title="关于MCの另一个空间站"
                >关于MCの另一个空间站</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://sangxuesheng.com/"
            rel="external nofollow"
            title="听闻 All in the game"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/fYL7iT20190681686542581680.jpg!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="听闻 All in the game"
                data-ll-status="loaded"
                src="https://p.zhheo.com/fYL7iT20190681686542581680.jpg!cover_mini"
            />
            <div class="img-alt is-center">听闻 All in the game</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">听闻 All in the game</span
                ><span class="flink-item-desc" title="一个爱折腾的boy。"
                >一个爱折腾的boy。</span
                >
            </div></a
            >
        </div>
        <div class="flink-list-item">
            <a
            class="cf-friends-link"
            href="https://blog.gfjzz.cn/"
            rel="external nofollow"
            title="君主阁"
            target="_blank"
            ><img
                class="flink-avatar cf-friends-avatar entered loaded"
                data-lazy-src="https://p.zhheo.com/nN32fN25191281735538151884.png!cover_mini"
                onerror="this.onerror=null;this.src='/img/b_av.webp'"
                alt="君主阁"
                data-ll-status="loaded"
                src="https://p.zhheo.com/nN32fN25191281735538151884.png!cover_mini"
            />
            <div class="img-alt is-center">君主阁</div>
            <div class="flink-item-info">
                <span class="flink-item-name cf-friends-name">君主阁</span
                ><span class="flink-item-desc" title="分享技术与生活"
                >分享技术与生活</span
                >
            </div></a
            >
        </div>
    </div>
    '''

    # 解析HTML
    soup = BeautifulSoup(html_content, 'lxml')
    # 找到所有 .flink-list 元素
    site_cards = soup.find_all('div', class_='flink-list-item')


    """
    <div class="flink-list-item 生活">
        <span class="site-card-tag vip">生活<i class="light"></i></span
        ><a
        class="cf-friends-link"
        href="https://www.pptwiki.com/"
        rel="external nofollow"
        title="PPT百科"
        target="_blank"
        ><img
            class="flink-avatar cf-friends-avatar entered loaded"
            data-lazy-src="https://p.zhheo.com/msbg5a21491081730170214492.webp!cover_mini"
            onerror="this.onerror=null;this.src='/img/b_av.webp'"
            alt="PPT百科"
            data-ll-status="loaded"
            src="https://p.zhheo.com/msbg5a21491081730170214492.webp!cover_mini"
        />
        <div class="img-alt is-center">PPT百科</div>
        <div class="flink-item-info">
            <span class="flink-item-name cf-friends-name">PPT百科</span
            ><span
            class="flink-item-desc"
            title="PPT百科网站为用户提供各类免费的PPT模板下载服务，包含PPT背景图,PPT素材,PPT背景,PPT可见,PPT定制免费PPT模板下载等。致力于提高职场人士制作PPT效率。免费下载的PPT模板类型涵盖工作汇报、营销策划、老师教学课件、商业计划书、医学医疗、竞聘述职等类型幻灯片"
            >PPT百科网站为用户提供各类免费的PPT模板下载服务，包含PPT背景图,PPT素材,PPT背景,PPT可见,PPT定制免费PPT模板下载等。致力于提高职场人士制作PPT效率。免费下载的PPT模板类型涵盖工作汇报、营销策划、老师教学课件、商业计划书、医学医疗、竞聘述职等类型幻灯片</span
            >
        </div></a
        >
    </div>
    """

    # 遍历每个.flink-list 元素
    for card in site_cards:
        # 提取信息
        # 提取tag信息，如果找不到则返回空字符串
        tag_span = card.find('span', class_='site-card-tag')
        tag = tag_span.text if tag_span else ''
        link = card.find('a', class_='cf-friends-link')['href']
        name = card.find('a', class_='cf-friends-link')['title']
        avatar = card.find('img', class_='flink-avatar cf-friends-avatar entered loaded')['src']
        descr = card.find('span', class_='flink-item-desc').text
        color = 'speed'  # 这个值是固定的，直接赋值

        # 输出结果
        result = f'''
    - name: {name}
      link: {link}
      avatar: {avatar}
      descr: {descr}
      tag: {tag}
      color: {color}
      recommend:
      '''
        
        print(result)


def main():
    # tuijiandeboke()
    jishu()
    
if __name__ == "__main__":
    main()

