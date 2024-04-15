package com.llgululu.app.util;

import com.alibaba.fastjson.JSON;
import org.springframework.util.StringUtils;

/**
 * author: zyy
 * Date: 2024/3/12/012 21:06
 * Desc:
 */
public class Test {

    public static ResultDto dyParseUrl(String redirectUrl) throws Exception {

        redirectUrl = CommonUtils.getLocation(redirectUrl);
        ResultDto dyDto = new ResultDto();

        if (!StringUtils.isEmpty(redirectUrl)) {
            /**
             * 1、用 ItemId 拿视频的详细信息，包括无水印视频url
             */
            String itemId = CommonUtils.matchNo(redirectUrl);

            StringBuilder sb = new StringBuilder();
            sb.append(CommonUtils.DOU_YIN_BASE_URL).append(itemId);

            String videoResult = CommonUtils.httpGet(sb.toString());
            System.out.println(videoResult);

//            DYResult dyResult = JSON.parseObject(videoResult, DYResult.class);
//
//            /**
//             * 2、无水印视频 url
//             */
//            String videoUrl = dyResult.getItem_list().get(0)
//                    .getVideo().getPlay_addr().getUrl_list().get(0)
//                    .replace("playwm", "play");
//            String videoRedirectUrl = CommonUtils.getLocation(videoUrl);
//
//            dyDto.setVideoUrl(videoRedirectUrl);
//            /**
//             * 3、音频 url
//             */
//            String musicUrl = dyResult.getItem_list().get(0).getMusic().getPlay_url().getUri();
//            dyDto.setMusicUrl(musicUrl);
//            /**
//             * 4、封面
//             */
//            String videoPic = dyResult.getItem_list().get(0).getVideo().getDynamic_cover().getUrl_list().get(0);
//            dyDto.setVideoPic(videoPic);
//
//            /**
//             * 5、视频文案
//             */
//            String desc = dyResult.getItem_list().get(0).getDesc();
//            dyDto.setDesc(desc);
        }
        return dyDto;
    }

    public static void main(String[] args) {
        String url = "https://v.douyin.com/iFS252pc/";
        try {
            dyParseUrl(url);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
